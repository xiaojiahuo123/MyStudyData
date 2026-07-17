# Day15 知识点总结

## 1. 正则表达式（re 模块）

### 1.1 常用函数

| 函数 | 用途 | 示例 |
|------|------|------|
| `re.match(pattern, string)` | 从**开头**匹配，匹配成功返回 Match 对象，否则返回 None | `re.match(r"^\d+$", "123")` |
| `re.findall(pattern, string)` | 找出**所有**匹配，返回列表 | `re.findall(r"\d+", "a1b2c3")` → `['1', '2', '3']` |
| `re.sub(pattern, repl, string)` | 替换匹配内容 | `re.sub(r"\d", "X", "a1b2")` → `"aXbX"` |

### 1.2 手机号验证

```python
pattern = r"^1[3456789]\d{9}$"
re.match(pattern, "13812345678")  # 匹配成功
```

- `^` 开头，`$` 结尾，确保整个字符串匹配
- `1` 第一位固定是 1
- `[3456789]` 第二位是 3-9 中的一个
- `\d{9}` 后面跟 9 位数字

### 1.3 邮箱验证

```python
pattern = r"[\w!#$%&'*+-/=?^`{|}~.]+@[\w!#$%&'*+-/=?^`{|}~.]+\.[a-zA-Z]{2,}$"
```

- `[\w...]` 用户名和域名部分允许的字符
- `@` @符号分隔
- `\.[a-zA-Z]{2,}$` 顶级域名至少 2 个字母（如 .com, .cn）

### 1.4 IP 地址验证（0-255）

```python
pattern = r"^([1-9]?\d|1\d{2}|2[0-4]\d|25[0-5])$"
```

| 分支 | 匹配范围 | 说明 |
|------|---------|------|
| `[1-9]?\d` | 0-99 | 十位可选，个位 0-9 |
| `1\d{2}` | 100-199 | 百位 1 |
| `2[0-4]\d` | 200-249 | 百位 2，十位 0-4 |
| `25[0-5]` | 250-255 | 百位 2，十位 5，个位 0-5 |

### 1.5 从 HTML 提取链接

```python
test = '<link href="https://example.com">'
pattern = r"href=\"(.+?)\""
re.findall(pattern, test)  # ['https://example.com']
```

- `.+?` 非贪婪匹配，匹配到最近的 `"` 就停
- `()` 捕获组，`findall` 只返回括号内的内容

### 1.6 re.sub + lambda 替换

```python
test = "I have 2 apples and 3 oranges."
num_map = {"1": "one", "2": "two", "3": "three"}

result = re.sub(r"\d", lambda x: num_map[x.group()], test)
# "I have two apples and three oranges."
```

- `re.sub` 的替换参数可以是**函数**
- `lambda x: num_map[x.group()]` 对每个匹配的数字查字典替换

### 1.7 正则语法速查

| 语法 | 含义 | 示例 |
|------|------|------|
| `\d` | 数字 `[0-9]` | `\d+` 匹配一个或多个数字 |
| `\w` | 字母数字下划线 `[a-zA-Z0-9_]` | `\w+` |
| `.` | 任意字符（除换行） | `a.c` 匹配 `abc`, `a1c` |
| `*` | 0 次或多次 | `ab*` 匹配 `a`, `ab`, `abb` |
| `+` | 1 次或多次 | `ab+` 匹配 `ab`, `abb` |
| `?` | 0 次或 1 次（或非贪婪） | `ab?` 匹配 `a`, `ab` |
| `{n}` | 恰好 n 次 | `\d{9}` 匹配 9 位数字 |
| `{n,m}` | n 到 m 次 | `\d{2,4}` 匹配 2-4 位数字 |
| `[]` | 字符集 | `[abc]` 匹配 a/b/c |
| `()` | 捕获组 | `(\d+)` 捕获数字 |
| `\|` | 或 | `a\|b` 匹配 a 或 b |
| `^` | 开头 | `^abc` 以 abc 开头 |
| `$` | 结尾 | `abc$` 以 abc 结尾 |

---

## 2. 客户管理系统（CMS）— OOP 综合应用

### 2.1 项目结构

```
day15/
├── customer.py    # Customer 数据类
├── cms.py         # CMS 管理类（主逻辑）
└── P01_Re.py      # 正则表达式练习
```

### 2.2 Customer 类 — 数据模型

```python
class Customer:
    def __init__(self, c_id, name, age="None", phone="None", email="None"):
        self.c_id = c_id
        self.name = name
        # ...

    def __str__(self):
        return f"Id: {self.c_id:<15}, Name: {self.name:<15}"

    @staticmethod
    def check_phone(phone):
        pattern = r"^1[3456789]\d{9}$"
        return True if re.match(pattern, phone) else False
```

- `__str__` 控制 `print(对象)` 时的输出格式
- `@staticmethod` 静态方法，不依赖实例，用 `类名.方法()` 调用
- 默认参数 `age="None"` 允许选填

### 2.3 CMS 类 — 管理逻辑

```python
class CMS:
    def __init__(self):
        self.customer_id_dict = {}      # {id: Customer} 按 ID 查找
        self.customer_name_dict = {}    # {name: {id: Customer}} 按姓名查找
```

**双字典索引**：同一个 Customer 对象在两个字典中各存一份引用，支持 ID 和姓名两种查找方式。

### 2.4 match-case 语句（Python 3.10+）

```python
match choice:
    case "1":
        self.add_customer()
    case "2":
        self.delete_customer()
    case _:
        print("输入有误")
```

- 类似 switch-case，`_` 是默认分支
- 比 if-elif 更清晰

### 2.5 海象运算符 :=（Python 3.8+）

```python
if not (customer_id := self.set_customer_id()):
    return
```

- `:=` 在表达式内部赋值，同时返回值
- 等价于：
```python
customer_id = self.set_customer_id()
if not customer_id:
    return
```

### 2.6 输入验证 + 重试机制

```python
def set_customer_name(self):
    for i in range(3):
        customer_name = input("请输入客户的名字:")
        if Customer.check_name(customer_name):
            break
        elif i < 2:
            print("输入的名字必须为纯字母，请重新输入")
        else:
            print("3次机会耗尽，退出")
            return False
    return customer_name
```

- 最多重试 3 次
- `Customer.check_name()` 用 `@staticmethod` 验证
- 失败返回 `False`，成功返回输入值

---

## 常见错误总结

| 错误类型 | 示例 | 修复 |
|---------|------|------|
| 正则不加锚点 | `r"\d{9}"` 会匹配 "1234567890" 中的 9 位 | 加 `^...$` 确保全匹配 |
| 贪婪匹配过多 | `.+` 匹配尽可能多的字符 | 改用 `.+?` 非贪婪 |
| `@staticmethod` 忘记装饰 | 验证方法用了 `self` 但不需要 | 加 `@staticmethod`，去掉 `self` |
| 海象运算符版本不够 | `:=` 报 SyntaxError | 确保 Python 3.8+ |
