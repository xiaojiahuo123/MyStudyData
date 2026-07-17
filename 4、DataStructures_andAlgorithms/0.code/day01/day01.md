## 1. array.array 访问行为

- `array.array` 内部存储的是原始 C int 数值，紧凑无对象开销
- 但用 Python 访问时（`arr[0]`），Python 自动将原始值包装成 Python int 对象返回
- 小整数（-5 到 256）命中缓存池，所以 `id(arr[0])` 和 `id(1)` 可能相同

| | 存储时（内存布局） | 访问时（Python 代码） |
|---|---|---|
| `array.array` | 原始 C int，紧凑无对象开销 | 自动转成 Python int 对象返回 |
| `list` | Python int 对象的引用/指针 | 直接返回引用指向的对象 |

---

## 2. `[0] * capacity` 预分配数组

```python
self.__capacity = 5
self.__items = [0] * self.__capacity   # [0, 0, 0, 0, 0]
self.__size = 0                        # 实际元素数为 0
```

- `[0] * capacity` 创建一个用 0 填充的固定大小列表，模拟底层数组的内存预分配
- `0` 只是占位符，表示"空槽位"，后续会被真实数据覆盖
- `__size` 记录实际存储的元素数量（从 0 开始增长）
- `__capacity` 是预分配的总容量（固定不变，除非扩容）

```
capacity=5, size=0:  [0, 0, 0, 0, 0]     ← 全是空槽位
capacity=5, size=3:  [1, 2, 3, 0, 0]     ← 前 3 个是真实数据
                     ↑size=3，只看前 3 个
```

---

## 3. `__str__` 方法（Python 版 toString）

```python
def __str__(self):
    return "对象的字符串表示"
```

- 等价于 Java 的 `toString()` 重写
- `print(obj)` 和 `str(obj)` 时**自动调用**，不需要手动调用
- 不重写时，`print(obj)` 输出 `<类名 object at 0x地址>`
