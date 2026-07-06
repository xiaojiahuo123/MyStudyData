def add(a,n):
    print("调用定义的add方法")
    return a+n
def sum(a,b):
    print("此时调用test_my_add定义的sum方法")
    return a+b

num = 100
strqq = "dada"


if __name__ == "__main__":
    # 这里的作用是，只有单独执行此文件的时候才执行这里的代码，单独执行python文件的时候，文件的__name__属性会变为 __main__，而被导入的时候会变为改文件的名字
    print(__name__)
    print("p01中的代码执行返回的结果:", add(10, 20))