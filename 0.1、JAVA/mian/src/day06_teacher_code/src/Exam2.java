package day06_teacher_code.src;

public class Exam2{
    public static void main(String[] args){
        int[] nums = new int[10];

        for(int i=0; i<nums.length; i++){
            nums[i] = (int)(Math.random() * 100);
            System.out.print(nums[i] +" ");
        }
    }
}