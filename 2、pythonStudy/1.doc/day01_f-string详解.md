# Python f-string 详解

## 一、基本概念

f-string 是 Python 3.6+ 引入的**格式化字符串字面量**（Formatted String Literals），以 `f` 或 `F` 开头，字符串内部用 `{表达式}` 的形式嵌入变量或计算结果。

## 二、基本语法

```python
name = "John"
age = 22
weight = 1000.0

# 基本用法：直接嵌入变量
print(f"{name} {age} {weight}")
# 输出: John 22 1000.0
```

## 三、工作原理

1. Python 解释器识别 `f"` 前缀
2. 解析 `{}` 内的变量/表达式
3. 将结果转换为字符串
4. 嵌入到字符串对应位置

## 四、对比传统字符串格式化方式

| 方式 | 代码示例 | 输出结果 |
|------|----------|----------|
| **f-string** | `f"{name} {age} {weight}"` | `John 22 1000.0` |
| **str.format()** | `"{} {} {}".format(name, age, weight)` | `John 22 1000.0` |
| **% 格式化** | `"%s %d %f" % (name, age, weight)` | `John 22 1000.000000` |
| **字符串拼接** | `name + " " + str(age) + " " + str(weight)` | `John 22 1000.0` |

## 五、f-string 的优势

1. **简洁直观**：变量直接嵌入，无需额外操作
2. **可读性强**：格式一目了然
3. **性能优异**：比传统方式更快
4. **功能强大**：支持表达式、函数、格式控制

## 六、高级用法

### 6.1 表达式计算

```python
age = 22
print(f"十年后年龄: {age + 10}")      # 输出: 十年后年龄: 32
print(f"体重减半: {weight / 2}")       # 输出: 体重减半: 500.0
```

### 6.2 函数调用

```python
name = "john"
print(f"姓名大写: {name.upper()}")     # 输出: 姓名大写: JOHN
print(f"姓名长度: {len(name)}")        # 输出: 姓名长度: 4
```

### 6.3 格式控制

```python
pi = 3.1415926

# 保留2位小数
print(f"π = {pi:.2f}")                 # 输出: π = 3.14

# 整数补零到3位
print(f"年龄: {age:03d}")              # 输出: 年龄: 022

# 科学计数法
print(f"科学计数: {weight:e}")         # 输出: 科学计数: 1.000000e+03

# 千位分隔符
print(f"大数字: {1234567:,}")         # 输出: 大数字: 1,234,567
```

### 6.4 对齐与填充

```python
name = "Alice"

# 左对齐，宽度10
print(f"{name:<10}")                   # 输出: "Alice     "

# 右对齐，宽度10，用*填充
print(f"{name:*>10}")                  # 输出: "*****Alice"

# 居中对齐，宽度10，用=填充
print(f"{name:=^10}")                  # 输出: "==Alice==="
```

## 七、注意事项

### 7.1 引号嵌套

```python
# 字符串内使用双引号，外层用单引号
print(f'{name} 说: "Hello"')           # 输出: John 说: "Hello"

# 使用转义字符
print(f"{name} 说: \"Hello\"")         # 输出: John 说: "Hello"
```

### 7.2 大括号转义

```python
# 输出字面量大括号
print(f"{{name}} 的值是 {name}")        # 输出: {name} 的值是 John
```

## 八、实际应用案例

### 示例：生成用户信息报告

```python
user = {
    "name": "张三",
    "age": 28,
    "score": 95.5,
    "level": "优秀"
}

report = f"""
用户报告
========
姓名: {user['name']}
年龄: {user['age']} 岁
成绩: {user['score']:.1f} 分
评级: {user['level']}
"""

print(report)
```

**输出：**
```
用户报告
========
姓名: 张三
年龄: 28 岁
成绩: 95.5 分
评级: 优秀
```

## 九、总结

f-string 是 Python 中最推荐的字符串格式化方式，具有：
- ✅ 语法简洁
- ✅ 可读性强
- ✅ 功能丰富
- ✅ 性能最优

建议在 Python 3.6+ 版本中优先使用 f-string 进行字符串格式化操作。
