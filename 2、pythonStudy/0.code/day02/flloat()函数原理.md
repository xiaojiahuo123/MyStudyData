# Python float() 函数实现原理

## 1. 函数签名

```python
float(x=0.0)
```

## 2. 特殊值处理

### 2.1 无穷大（inf）

```python
float("inf")   # → inf
float("-inf")  # → -inf
float("infinity")   # → inf（不区分大小写）
float("-Infinity")  # → -inf
```

### 2.2 非数字（nan）

```python
float("nan")   # → nan
float("NaN")   # → nan（不区分大小写）
```

### 2.3 正零和负零

```python
float("0.0")   # → 0.0
float("-0.0")  # → -0.0
```

## 3. 浮点数表示

### 3.1 IEEE 754 双精度格式

Python 的 float 类型使用 IEEE 754 双精度（64位）浮点数格式：

```
┌────────────┬──────────────────┬─────────────────────────────────────────────┐
│  符号位(1) │    指数位(11)     │              尾数位(52)                    │
│    sign    │      exp         │               mantissa                    │
├────────────┼──────────────────┼─────────────────────────────────────────────┤
│   0 = 正   │  偏置值 = 1023   │  隐含的 1.xxx... 中的 xxx... 部分          │
│   1 = 负   │                  │                                             │
└────────────┴──────────────────┴─────────────────────────────────────────────┘
```

### 3.2 数值范围

| 特性 | 值 |
|------|-----|
| 最大值 | ≈ 1.7976931348623157 × 10^308 |
| 最小正规数 | ≈ 2.2250738585072014 × 10^-308 |
| 最小非正规数 | ≈ 4.9406564584124654 × 10^-324 |
| 精度 | 约 15-17 位有效数字 |

### 3.3 特殊浮点数的表示

| 值 | 符号位 | 指数位 | 尾数位 |
|----|--------|--------|--------|
| +0.0 | 0 | 0 | 0 |
| -0.0 | 1 | 0 | 0 |
| +inf | 0 | 全1 | 0 |
| -inf | 1 | 全1 | 0 |
| nan | 任意 | 全1 | 非0 |

## 4. 字符串转浮点数流程

### 4.1 解析阶段

1. **识别正负号**：检查字符串开头是否有 `+` 或 `-`
2. **识别整数部分**：读取小数点前的数字
3. **识别小数部分**：读取小数点后的数字
4. **识别科学计数法**：检查是否有 `e` 或 `E`

### 4.2 转换阶段

Python 使用 C 标准库函数 `strtod()` 进行实际的字符串到浮点数转换：

```c
double strtod(const char *nptr, char **endptr);
```

### 4.3 特殊情况处理

| 输入 | 输出 | 说明 |
|------|------|------|
| `""` | 0.0 | 空字符串返回0 |
| `"inf"` | inf | 正无穷大 |
| `"-inf"` | -inf | 负无穷大 |
| `"nan"` | nan | 非数字 |
| `"1e10"` | 10000000000.0 | 科学计数法 |

## 5. 源码关键函数

### 5.1 builtin_float()

入口函数，定义在 `Python/bltinmodule.c` 中。

### 5.2 PyFloat_FromString()

核心转换函数，定义在 `Objects/floatobject.c` 中。

### 5.3 字符串匹配逻辑

```c
// 检查是否是特殊值
if (strcmp(str, "inf") == 0 || strcmp(str, "infinity") == 0) {
    return PyFloat_FromDouble(Py_HUGE_VAL);
}
if (strcmp(str, "-inf") == 0 || strcmp(str, "-infinity") == 0) {
    return PyFloat_FromDouble(-Py_HUGE_VAL);
}
if (strcmp(str, "nan") == 0) {
    return PyFloat_FromDouble(Py_NAN);
}
```

## 6. 常见问题

### 6.1 精度问题

```python
0.1 + 0.2 == 0.3  # False
print(0.1 + 0.2)  # 0.30000000000000004
```

**原因**：二进制无法精确表示 0.1 和 0.2

### 6.2 比较浮点数

推荐使用 `math.isclose()`：

```python
import math

a = 0.1 + 0.2
b = 0.3

print(math.isclose(a, b))  # True
print(abs(a - b) < 1e-9)   # True
```

### 6.3 NaN 的特殊性

```python
nan = float("nan")
print(nan == nan)    # False（NaN不等于任何值，包括自身）
print(math.isnan(nan))  # True（使用math.isnan判断）
```

## 7. 浮点数运算特性

| 特性 | 示例 |
|------|------|
| 任何数 + inf = inf | `5 + inf = inf` |
| 任何数 - inf = -inf | `5 - inf = -inf` |
| 任何数 * inf = inf | `5 * inf = inf` |
| 0 * inf = nan | `0 * inf = nan` |
| inf / inf = nan | `inf / inf = nan` |
| 任何数 / 0 = inf | `5 / 0 = inf` |

## 8. 总结

float() 函数的实现流程：

1. **参数处理**：检查输入类型
2. **特殊值识别**：检查是否是 inf、-inf、nan
3. **字符串解析**：识别正负号、整数部分、小数部分、科学计数法
4. **调用 strtod**：使用 C 标准库进行实际转换
5. **返回结果**：创建并返回 PyFloatObject 对象