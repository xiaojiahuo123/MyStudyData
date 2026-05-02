package day_11.test_05;

public class TestArray {
    public static void main(String[] args) {
        //需求：存储一组图形的对象，统一管理它们，比如：让它们以面积从小到大排序，暂时先不用Comparable接口
        //多态数组：元素的类型声明为父类类型，元素存储的是子类对象。
        Shape[] arr = new Shape[5];

        //下面这些赋值语句，体现了多态引用
        //arr[下标] 它们声明的类型是Shape类型，父类类型
        //arr[下标] 它们赋值的/存储的是子类对象
        //左边是父类或父接口的类型的变量，右边是子类的对象，这种引用方式就是多态引用。
        arr[0] = new Circle(2.5);
        arr[1] = new Rectangle(4,3);
        arr[2] = new Rectangle(5,2);
        arr[3] = new Triangle(3,4,5);
        arr[4] = new Triangle(6,6,6);

        //当arr[下标]调用方法时，就会遵循编译时看左边，运行时看右边
        for(int i=1; i<arr.length; i++){
            for(int j=0; j<arr.length-i; j++){
                //按照面积比较大小
                //编译时，arr[j]是Shape类型，会看Shape类中有没有area()方法
                //运行时，arr[j]会执行子类中重写的area()方法，具体执行哪个子类的，看arr[j]存的是哪个子类的对象
                //遵循了动态绑定
                if(arr[j].area() > arr[j+1].area()){
                    Shape temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
        }

        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
        }
    }
}
