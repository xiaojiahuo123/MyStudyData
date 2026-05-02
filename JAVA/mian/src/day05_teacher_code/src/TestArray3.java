package day05_teacher_code.src;

public class TestArray3 {
    public static void main(String[] args) {
        //用数组存储26个小写字母，然后遍历显示它们
//        char[] letters = {'a','b','c','d'};//需要写26个，可以做，但是麻烦
        char[] letters = new char[26];
        /*for (int i = 0; i < letters.length; i++) {
            System.out.println(letters[i]);
        }

        int[] nums = new int[5];
        for (int i = 0; i < nums.length; i++) {
            System.out.println(nums[i]);
        }

        String[] strings = new String[5];
        for (int i = 0; i < strings.length; i++) {
            System.out.println(strings[i]);
        }*/

       /* letters[0] = 'a';
        letters[1] = 'b';
        letters[2] = 'c';*/
        for (int i = 0; i < letters.length; i++) {
            letters[i] = (char)('a'+i);
            System.out.println(letters[i]);
        }
    }
}
