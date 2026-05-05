package day06_teacher_code.src;

public class Exam3{
    public static void main(String[] args){
//        String[] numStrings = {'壹','贰','叁','肆','伍','陆','柒','捌','玖','拾'};

        //Ctrl + F查找，Ctrl + R 替换
        char[] numStrings = {'壹','贰','叁','肆','伍','陆','柒','捌','玖','拾'};
        for(int i=1; i<=10; i++){
            System.out.println(i + "->" + numStrings[i-1]);
        }
    }
}