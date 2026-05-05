package day05_teacher_code.src;

public class TestArrayMemory {
    public static void main(String[] args) {
        int[] arr = {10, 20, 30};
        System.out.println(arr);//[I@776ec8df
        //[I@776ec8df ≈  内存地址，因为JVM不会暴露真实的内存地址，这是为了安全考虑
        //初学者，就理解为内存地址
    }
}
