package day05_teacher_code.src;

public class LoopExercise4 {
    public static void main(String[] args) {
        int line = 15;

        int center = line / 2;
        for(int i=0; i<line; i++){
            //控制打印空格或*
            for(int j=0; j<line; j++){
                //if(|center-i| + |center - j| <=center){
                if(Math.abs(center-i) + Math.abs(center - j) <=center){
                    System.out.print("*");
                }else{
                    System.out.print(" ");
                }
            }

            System.out.println();
        }
    }
}
