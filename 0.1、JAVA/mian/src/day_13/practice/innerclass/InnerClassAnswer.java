package day_13.practice.innerclass;

public class InnerClassAnswer {
    private String name = "外部类";
    class MemberInner {
        public void print() { System.out.println(name); }
    }
    // Q12 理解题答案：有成员内部类、静态内部类、局部内部类、匿名内部类。成员类用于封装逻辑，匿名类用于回调等。
}
