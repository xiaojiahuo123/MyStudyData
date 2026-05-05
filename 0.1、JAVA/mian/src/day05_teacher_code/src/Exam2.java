package day05_teacher_code.src;

public class Exam2 {
    public static void main(String[] args) {
        //使用循环结合if-else或switch-case输出1-12月每一个月的总天数
        //提示：1,3,5,7,8,10,12月是31天，4,6,9,11月是30天，这里因为没有年份信息，所以2月输出28或29天即可
        for(int month = 1; month<=12; month++){
            if(month == 2){
                System.out.println("2月是28或29天");
            }else if(month==4 || month==6 || month==9 || month==11){
                System.out.println(month + "月是30天");
            }else{
                System.out.println(month + "月是31天");
            }
        }

        System.out.println("================");
        for(int month = 1; month<=12; month++){
            switch (month){
                case 1: System.out.println("1月31天");break;
                case 2: System.out.println("2月28或28天");break;
                case 3: System.out.println("3月31天");break;
                case 4: System.out.println("4月30天");break;
                case 5: System.out.println("5月31天");break;
                case 6: System.out.println("6月30天");break;
                case 7: System.out.println("7月31天");break;
                case 8: System.out.println("8月31天");break;
                case 9: System.out.println("9月30天");break;
                case 10: System.out.println("10月31天");break;
                case 11: System.out.println("11月30天");break;
                case 12: System.out.println("12月31天");break;
            }
        }
        System.out.println("================");
        for(int month = 1; month<=12; month++){
            switch (month){
                case 1-> System.out.println("1月31天");
                case 2-> System.out.println("2月28或28天");
                case 3->  System.out.println("3月31天");
                case 4->  System.out.println("4月30天");
                case 5->  System.out.println("5月31天");
                case 6->  System.out.println("6月30天");
                case 7->  System.out.println("7月31天");
                case 8->  System.out.println("8月31天");
                case 9->  System.out.println("9月30天");
                case 10->  System.out.println("10月31天");
                case 11-> System.out.println("11月30天");
                case 12->  System.out.println("12月31天");
            }
        }

        System.out.println("================");
        for(int month = 1; month<=12; month++){
           String str =  switch (month){
                case 1-> "1月31天";
                case 2-> "2月28或28天";
                case 3->  "3月31天";
                case 4->  "4月30天";
                case 5->  "5月31天";
                case 6->  "6月30天";
                case 7->  "7月31天";
                case 8->  "8月31天";
                case 9->  "9月30天";
                case 10->  "10月31天";
                case 11-> "11月30天";
               default->  "12月31天";//default必选
            };
            System.out.println(str);
        }
        System.out.println("================");
        for(int month = 1; month<=12; month++){
            String str =  switch (month){
                case 1,3,5,7,8,10,12 -> "31";
                case 4,6,9,11 -> "30";
                default -> "28或29";
            };//逗号的这种写法只能支持新特性的写法，用:的不可以
            System.out.println(month + "是" + str + "天");
        }
    }
}
