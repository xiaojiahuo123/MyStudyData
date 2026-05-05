package day_11.test_03;

public class TestEmployee {
    public static void main(String[] args) {
        Employee[] arr = new Employee[3];
        arr[0] = new Employee("小孙",30000);
        arr[1] = new Employee("老马",20000);
        arr[2] = new Employee("老何",30001);

        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
        }

        System.out.println("按照薪资从低到高排序：");
        for(int i=1; i<arr.length; i++){
            for(int j=0; j<arr.length-i; j++){
                //arr[j]和arr[j+1]
                if(arr[j].compareTo(arr[j+1]) > 0){
                    Employee temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
        }

        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
        }
    }
}
