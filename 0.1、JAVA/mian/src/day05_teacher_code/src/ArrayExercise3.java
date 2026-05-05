package day05_teacher_code.src;

public class ArrayExercise3 {
    public static void main(String[] args) {
        /*
        （1）用一个数组存储26个英文字母的小写形式a-z
        （2）正序遍历输出小写字母
        （3）逆序遍历输出小写字母
         */
        //(1)先声明一个char[]的数组，长度是26
        char[] letters = new char[26];
        //把26个英文字母放到数组中
        for (int i = 0; i < letters.length; i++) {
            letters[i] = (char)('a' + i);
        }

        //(2)正序遍历：下标[0,1,2,3,....,25]
        System.out.println("正序遍历输出小写字母：");
        for (int i = 0; i < letters.length; i++) {
            System.out.print(letters[i]+" ");
        }
        System.out.println();

        //(3)反着遍历数组：下标[25,24,23,....1,0]
        System.out.println("逆序遍历输出小写字母：");
        for(int i=letters.length-1; i>=0; i--){
            System.out.print(letters[i]+" ");
        }
        System.out.println();
    }
}
