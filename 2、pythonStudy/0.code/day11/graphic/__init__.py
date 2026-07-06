from . import circle
# __all__ 只是告诉 Python "当 from graphic import * 时，应该导出哪些名字"，但它 本身并不会导入任何东西 。
# Python 在 graphic 的命名空间里找不到 circle 这个名字，就会报 ImportError
__all__ = ["circle"]