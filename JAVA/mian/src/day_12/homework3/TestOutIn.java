package day_12.homework3;
//变量作用域优先级 ：局部变量 > 内部类成员变量 > 外部类成员变量
public class TestOutIn {
    public static void main(String[] args) {
        Out.In in = new Out().new In();
        in.print();
    }
}
class Out {  // 外部类
    private int a = 12;  // 外部类的成员变量a
    class In {  // 非静态内部类
        private int a = 13;  // 内部类的成员变量a
        public void print() {
            int a = 14;  // 方法内部的局部变量a 
            
            System.out.println(a);        // 输出14
           //这里直接使用变量名 a ，根据Java的作用域规则，会优先访问 方法内部的局部变量
            //所以直接访问 a 时获取的是这个局部变量的值

            System.out.println(this.a);   // 输出13
           //this 关键字在这里代表 内部类 In 的当前实例（In类的对象）
            // this.a 访问的是内部类 In 中定义的成员变量 a ，其值为13

            System.out.println(Out.this.a);  // 输出12
              // Out.this 是一种特殊的语法，表示 外部类 Out 的当前实例
            // 于内部类可以访问外部类的成员变量，通过 Out.this.a 
            // 可以明确访问外部类 Out 中定义的成员变量 a ，其值为12
        }
    }
}