package day_11.homework_01;

public class TestPeople {
    public static void main(String[] args) {
        Person[] arr = new Person[4];
        arr[0] = new Man("张三",23,"Java中级工程师");
        arr[1] = new Man("李四",24,"大数据工程师");
        arr[2] = new Woman("翠花",22,"UI设计师");
        arr[3] = new Woman("如花",23,"前端设计师");

        System.out.println("------------初次见面--------------");
        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
        }

        System.out.println("-------------开始聚餐--------------");
        for (int i = 0; i < arr.length; i++) {
            arr[i].eat();
        }

        System.out.println("---------------饭后休息-------------");
        for (int i = 0; i < arr.length; i++) {
            arr[i].toilet();
            if(arr[i] instanceof Man m){
                m.smoke();
            }else if(arr[i] instanceof Woman w){
                w.makeup();
            }
        }
    }
}
