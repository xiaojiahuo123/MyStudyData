package day06_teacher_code.src;

public class Exam1{
    public static void main(String[] args){
        // char[] letters = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
        char[] letters = new char[26];
        for(int i=0; i<letters.length; i++){
            letters[i] = (char)('A'+ i);
            System.out.print("'" + letters[i] +"',");
        }
    }
}