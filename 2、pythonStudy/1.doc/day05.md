##### 知识点

```python
# ----- 题8: 字符串统计词频 [必做] -----
# 知识点: split、字典计数、sorted 排序
text = "the quick brown fox jumps over the lazy dog the fox"

# TODO: 统计每个单词出现的次数，按次数从高到低输出
# 提示: split() 分割 → 字典计数 → 排序
list1 = text.split(" ")  # 用 list 作为变量名会覆盖内置函数！
print(list1)
# 2. 统计每个单词出现的次数
word_count = {}  #空字典
for word in list1:
    if word in word_count:  # 最开始不存在字典中的返回flase
        word_count[word] += 1  # 以及存在的key,直接将值更新
    else:
        word_count[word] = 1  #  将列表中的元素添加为key,1作为value
# - 键不存在时， dict[key] = value 会 创建 新的键值对
# - 键存在时， dict[key] = value 会 修改 现有的值
# - dict.get(key, default) 安全获取值，键不存在返回默认值
print(f"统计结果: {word_count}")

# 3. 按次数从高到低排序
#sorted() 开始遍历word_count.items()这个列表，对每个元素调用 key 函数
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)  # reverse=True，降序排列
# 字典的三个常用方法，items()、keys()、values()，keys()返回所有建，values()返回所有值
# items()返回所有键值对
# 普通函数
# def add_one(x):
#     return x + 1
# # lambda 匿名函数（等价）
# lambda x: x + 1
# # 使用
# print(add_one(5))      # 6
# print((lambda x: x + 1)(5))  # 6
print("\n按次数从高到低排序:")
for word, count in sorted_words:
    print(f"  {word}: {count}")
```

字典的三个常用函数返回的是字典的视图对象而不是能够

| dict.keys()   | 获取字典所有的key，返回一个视图对象。字典改变，视图也会跟着变化 |
| ------------- | ------------------------------------------------------------ |
| dict.values() | 获取字典所有的value，返回一个视图对象                        |
| dict.items()  | 获取字典所有的(key,value)，返回一个视图对象                  |

字典推导式

### 一、什么是字典推导式

字典推导式是一种简洁创建字典的方式，通过对可迭代对象进行遍历和转换，一次性生成新字典。

### 二、语法格式

```python
{key_expression: value_expression for item in iterable}
```

### 三、基础示例

#### 示例1：简单转换

```python
# 创建 {1: 1, 2: 4, 3: 9, ..., 10: 100}（数字到平方的映射）
squares = {x: x**2 for x in range(1, 11)}
print(squares)  # {1: 1, 2: 4, 3: 9, ..., 10: 100}
```

#### 示例2：带过滤条件

```python
# 只保留偶数的平方
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(even_squares)  # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
```

#### 示例3：反转键值对

```python
original = {"a": 1, "b": 2, "c": 3}
reversed_dict = {value: key for key, value in original.items()}
print(reversed_dict)  # {1: "a", 2: "b", 3: "c"}
```

### 四、与传统方式对比

#### 传统方式（for循环）

```python
squares = {}
for x in range(1, 6):
    squares[x] = x**2
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

#### 字典推导式（一行搞定）

```python
squares = {x: x**2 for x in range(1, 6)}
```

### 五、实际应用场景

#### 场景1：数据清洗

```python
# 去除无效数据
data = {"name": "张三", "age": "", "score": 85, "address": None}
cleaned = {k: v for k, v in data.items() if v not in ("", None)}
print(cleaned)  # {"name": "张三", "score": 85}
```

#### 场景2：数据转换

```python
# 将成绩字典转换为等级字典
scores = {"语文": 85, "数学": 92, "英语": 78}
grades = {subject: "A" if score >= 90 else "B" if score >= 80 else "C" 
          for subject, score in scores.items()}
print(grades)  # {"语文": "B", "数学": "A", "英语": "C"}
```

#### 场景3：结合zip使用

```python
keys = ["a", "b", "c"]
values = [1, 2, 3]
dictionary = {k: v for k, v in zip(keys, values)}
print(dictionary)  # {"a": 1, "b": 2, "c": 3}
```

### 六、注意事项

1. **键必须唯一**：如果键重复，后面的会覆盖前面的
   ```python
   {x: x**2 for x in [1, 2, 2, 3]}  # {1: 1, 2: 4, 3: 9}
   ```

2. **性能考虑**：对于简单操作，字典推导式比 `dict()` 构造器更高效

3. **可读性**：避免过于复杂的推导式，必要时拆分为多行

### 七、总结

| 特性 | 说明 |
|------|------|
| **语法** | `{key: value for item in iterable}` |
| **优势** | 简洁、高效、可读性强 |
| **适用场景** | 数据转换、过滤、映射创建 |
| **注意点** | 键唯一性、避免过度嵌套 |

比如

```python
# ----- 题12: 字典推导式 [必做] -----
# 知识点: 字典推导式、zip、反转键值对
# TODO: 用字典推导式完成以下任务

# 1. 创建 {1: 1, 2: 4, 3: 9, ..., 10: 100}（数字到平方的映射）
squares = {x: x**2 for x in range(1, 101)}
print(squares)

# 2. 反转字典的键值对 {"a": 1, "b": 2, "c": 3} → {1: "a", 2: "b", 3: "c"}
squares1 = {"a": 1, "b": 2, "c": 3}
reversed_dict = {v: k for k, v in squares1.items()}
print(reversed_dict)

# 3. 从列表 ["a", "b", "a", "c", "b", "a", "d"] 中统计每个元素出现的次数
lst = ["a", "b", "a", "c", "b", "a", "d"]
freq = {x: lst.count(x) for x in lst}
print(freq)
```

### 字符串驻留

```python
# ----- 题13: 字符串驻留（Interning） [选做] -----
# 知识点: 字符串驻留机制、is vs ==
# Python 会缓存一些字符串，使相同内容的字符串指向同一对象
a = "hello"
b = "hello"
print(f"a is b: {a is b}")       # ____true

a = "hello world!"
b = "hello world!"
print(f"a is b: {a is b}")       # ___true_

a = "hello123"
b = "hello123"
print(f"a is b: {a is b}")       # ____true

# 规则: 只包含字母、数字、下划线的字符串会被自动驻留
# 永远用 == 比较字符串值，不要用 is
```

