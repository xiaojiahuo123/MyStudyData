package day05_teacher_code.src;

public class Exam1{
    public static void main(String[] args){
       /* for(char letter = 'a'; letter<='z'; letter++){
            System.out.println(letter);
        }*/

        System.out.println("====================");
        char c ='a';
        for(int i=0; i<26; i++){
            System.out.println((char)(c + i));
        }
    }
}