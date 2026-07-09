#!/usr/bin/env python3
"""
多层 Base64 自动解码工具

功能：
1. 自动检测并逐层解码 Base64（标准 / URL安全 / 去除换行符等变体）
2. 支持从文件或命令行参数读取输入
3. 解码过程中显示每一层的结果预览，便于观察
4. 自动识别最终明文（非 Base64 字符出现即停止）

使用示例：
    python base64_decoder.py                          # 交互式输入
    python base64_decoder.py 1.txt                    # 从文件读取
    python base64_decoder.py -s "VmpJd2VFNUhSa2Rp..."  # 直接传入字符串
    python base64_decoder.py 1.txt -m 50              # 限制最多 50 层
    python base64_decoder.py 1.txt -o result.txt      # 结果写入文件
"""

import argparse
import base64
import re
import sys
from pathlib import Path

# Windows 控制台默认 GBK，强制 stdin/stdout/stderr 用 UTF-8，避免中文路径/内容乱码
if sys.platform == 'win32':
    try:
        sys.stdin.reconfigure(encoding='utf-8')
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except AttributeError:
        pass


# Base64 字符集正则（宽松匹配：允许换行、空格、= 填充）
BASE64_PATTERN = re.compile(
    r'^\s*[A-Za-z0-9+/_-]+={0,2}\s*$'
)

# 标准 Base64 字符集（用于判断是标准还是 URL 安全变体）
STD_B64_CHARS = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=')
URLSAFE_B64_CHARS = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_=')


def is_likely_base64(s: str) -> bool:
    """粗略判断字符串是否像 Base64 编码"""
    s = s.strip()
    if len(s) < 4:
        return False
    # 长度必须是 4 的倍数（去除尾部换行后）
    if len(s) % 4 != 0:
        return False
    # 必须全部是 Base64 字符
    chars = set(s) - {'\n', '\r', ' '}
    if not chars:
        return False
    if not chars.issubset(STD_B64_CHARS | URLSAFE_B64_CHARS):
        return False
    # 不能包含 Base64 之外的可见字符
    if not BASE64_PATTERN.match(s):
        return False
    return True


def try_decode_once(s: str) -> str | None:
    """尝试一次 Base64 解码，失败返回 None"""
    s = s.strip().replace('\n', '').replace('\r', '').replace(' ', '')

    # 优先尝试标准 Base64
    try:
        decoded = base64.b64decode(s, validate=True)
        # 只在能解码成 UTF-8 文本时才返回
        return decoded.decode('utf-8')
    except Exception:
        pass

    # 再尝试 URL 安全 Base64
    try:
        decoded = base64.urlsafe_b64decode(s + '=' * (-len(s) % 4))
        return decoded.decode('utf-8')
    except Exception:
        pass

    return None


def decode_recursive(data: str, max_rounds: int = 1000, verbose: bool = True) -> tuple[str, int]:
    """
    递归解码 Base64

    Args:
        data: 待解码字符串
        max_rounds: 最大解码层数（防止死循环）
        verbose: 是否打印每一层的进度

    Returns:
        (最终明文, 解码层数)
    """
    rounds = 0
    current = data

    while rounds < max_rounds:
        if not is_likely_base64(current):
            if verbose:
                print(f'\n[+] 解码完成，共 {rounds} 层，最终内容长度 {len(current)} 字节')
            return current, rounds

        decoded = try_decode_once(current)
        if decoded is None:
            if verbose:
                print(f'\n[+] 解码停止，共 {rounds} 层（第 {rounds+1} 层解码失败，可能已是明文）')
            return current, rounds

        rounds += 1
        current = decoded

        if verbose:
            preview = current[:80].replace('\n', '\\n')
            tail = '...' if len(current) > 80 else ''
            print(f'  [第 {rounds:>3} 层] len={len(current):>6}  {preview}{tail}')

    if verbose:
        print(f'\n[!] 达到最大层数限制 {max_rounds}，可能存在死循环')
    return current, rounds


def read_input(source: str | None, string: str | None) -> str:
    """从文件或字符串读取输入

    优先级：
    1. -s/--string 指定的字符串
    2. 命令行参数指定的文件路径
    3. stdin 读取（按行读取，无需结束 stdin）：
       - 若输入一行是一个存在的文件路径，则读取该文件
       - 否则把输入内容本身当作待解码的字符串（单行 Base64）
    """
    if string is not None:
        return string
    if source is None or source == '-':
        print('请输入待解码内容，或输入文件路径（直接回车确认即可，无需 Ctrl+Z）：', file=sys.stderr)
        line = sys.stdin.readline()
        if not line:
            raise ValueError('输入为空')
        data = line.strip()
        if not data:
            raise ValueError('输入为空')
        # 尝试把输入当作文件路径来读取
        candidate = Path(data.strip().strip('"').strip("'"))
        if candidate.exists() and candidate.is_file():
            print(f'[*] 检测到文件路径，读取文件：{candidate}', file=sys.stderr)
            return candidate.read_text(encoding='utf-8')
        # 否则当作 Base64 字符串本身
        return data
    path = Path(source)
    if not path.exists():
        raise FileNotFoundError(f'文件不存在：{path}')
    return path.read_text(encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(
        description='多层 Base64 自动解码工具',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''示例：
  python base64_decoder.py 1.txt
  python base64_decoder.py -s "VmpJd2VFNUhSa2Rp..."
  python base64_decoder.py 1.txt -m 50 -o out.txt
'''
    )
    parser.add_argument('source', nargs='?', default=None,
                        help='输入文件路径（不指定则从 stdin 读取）')
    parser.add_argument('-s', '--string', default=None,
                        help='直接传入待解码字符串')
    parser.add_argument('-m', '--max-rounds', type=int, default=1000,
                        help='最大解码层数（默认 1000）')
    parser.add_argument('-o', '--output', default=None,
                        help='将最终结果写入指定文件')
    parser.add_argument('-q', '--quiet', action='store_true',
                        help='静默模式，只输出最终结果')

    args = parser.parse_args()

    try:
        data = read_input(args.source, args.string)
    except FileNotFoundError as e:
        print(f'[!] {e}', file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f'[!] 读取输入失败：{e}', file=sys.stderr)
        sys.exit(1)

    if not args.quiet:
        print(f'[*] 输入长度：{len(data)} 字符')
        print(f'[*] 开始解码...\n')

    result, rounds = decode_recursive(data, args.max_rounds, verbose=not args.quiet)

    if args.quiet:
        print(result)
    else:
        print('\n========== 最终结果 ==========')
        print(result)
        print('==============================')
        print(f'[*] 共解码 {rounds} 层')

    if args.output:
        Path(args.output).write_text(result, encoding='utf-8')
        if not args.quiet:
            print(f'[*] 结果已写入：{args.output}')


if __name__ == '__main__':
    main()
