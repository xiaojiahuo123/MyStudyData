package day05_teacher_code.src;

public class ArrayExercise3_2 {
    public static void main(String[] args) {
        /*
        （1）用一个数组存储26个英文字母的小写形式a-z
        （2）正序遍历输出小写字母
        （3）逆序遍历输出小写字母
         */
        //(1)先声明一个char[]的数组，长度是26
        char[] letters = new char[26];
        //把26个英文字母放到数组中
        System.out.println("正序遍历输出小写字母：");
        for (int i = 0; i < letters.length; i++) {
            letters[i] = (char)('a' + i);
            System.out.print(letters[i]+" ");
        }
        System.out.println();

        System.out.println("逆序遍历输出小写字母：");
        for (int i = 0; i < letters.length; i++) {
            letters[i] = (char)('z'- i);
            System.out.print(letters[i]+" ");
        }
        System.out.println();
    }
}
