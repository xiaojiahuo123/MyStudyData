package day_09.test_01.test_04;

public class TestRectangle {
    public static void main(String[] args) {
        //创建5个矩形对象，放到数组中统一管理
//        int[] arr = {1,2,3,4,5};
/*        int[] nums = new int[5];
        for (int i = 0; i < nums.length; i++) {
            System.out.println(nums[i]);
        }*/

//        Rectangle[] arr = {new Rectangle(5,3),new Rectangle(6,1)};

        Rectangle[] arr = new Rectangle[5];
        //此时我创建了一个数组，准备放5个矩形对象
        //此时arr数组的元素是什么值？5个null
        arr[0] = new Rectangle(5,3);
        arr[1] = new Rectangle(6,1);
        arr[2] = new Rectangle(4,2);
        arr[3] = new Rectangle(7,4);
        arr[4] = new Rectangle(6,2);

        //此时arr数组的元素是什么值？
        //如果重写了toString方法，打印元素看到的是5个矩形对象的信息
        //如果没有重写toString方法，打印元素看到的是5个地址值
        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
            //打印元素，会自动调用对象的toString()
        }

        System.out.println("排序：");
        //按照矩形对象的面积从小到大排序
        for(int i=1; i<arr.length; i++){
            for(int j=0; j<arr.length-i; j++){
                // if(arr[j] > arr[j+1]){//此时arr[j]是对象，arr[j]里面存储的是地址值，地址值是无法比较大小的
                if(arr[j].area() > arr[j+1].area()){
                    Rectangle  temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
        }

        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
            //打印元素，会自动调用对象的toString()
        }

    }
}
