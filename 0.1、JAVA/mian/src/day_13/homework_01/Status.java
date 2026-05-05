package day_13.homework_01;

public  enum Status {
    FREE("空闲"),
    USED("在用"),
    SCRAP("报废");

    private final String description;
    private final int value;

    // 私有构造器
    private Status(String description) {
        this.description = description;
        this.value = ordinal();
        //ordinal() 是Java枚举类型内置的方法，它返回枚举常量在声明时的位置序号（从0开始）。
        //由于每个枚举的实例化对象创建的时候都会调用构造器，所以FREE、USED、SCRAP三个实例化对象创建的时候就调用私有化构造器了，而私有化
        //构造器中直接 this.value = ordinal(); 所以这些实例化的枚举对象就根据自身声明时的编号放入了自己的value属性中，也就实现了
        //getByValue(int value)方法中增强for循环的status对象可以直接访问自己的value属性
    }

    // 重写toString方法，返回description值
    @Override
    public String toString() {
        return description;
    }

    // 提供静态方法根据value值获取Status状态对象
    public static Status getByValue(int value) {
        for (Status status : Status.values()) {
            //Status.values() ：这是Java枚举类型自带的静态方法，它返回一个包含所有枚举常量的数组，在这个例子中就是
            // FREE 、 USED 和 SCRAP 这三个枚举实例
            if (status.value == value) {
                /*
在Java中，枚举类型有些特殊。当我们定义一个枚举类型时（如 Status ），编译器会自动为我们创建一些特殊的东西：
枚举常量 ：像 FREE 、 USED 、 SCRAP 这样的常量，它们实际上是 Status 类型的 实例对象 ，而不仅仅是名称。
values()方法 ：这是枚举类自动拥有的静态方法，它返回一个包含所有枚举常量的数组。

也就是说，这里的每一次循环的status，实际上都已经代表着Status.values()方法返回的一个实例对象，所以能够访问自身对应的value                * */
                return status;
            }
        }
        return null;
    }
}
