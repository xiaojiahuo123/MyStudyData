package day_13.homework_01;

public class TestMyWork {
    public static void main(String[] args) {
        // 创建Equipment数组
        Equipment[] equipments = new Equipment[10];
        
        // 使用Data.EQUIPMENTS数据初始化设备对象
        for (int i = 0; i < Data.EQUIPMENTS.length; i++) {
            String[] data = Data.EQUIPMENTS[i];
            int id = Integer.parseInt(data[0]);
            //将字符串的整数值转为int型整数值
            String brand = data[1];
            double price = Double.parseDouble(data[2]);
            //将字符串类型的小数值转为double型的小数值
            String name = data[3];
            int statusValue = Integer.parseInt(data[4]);
            Status status = Status.getByValue(statusValue);
            
            equipments[i] = new Equipment(id, brand, price, name, status);
        }
        
        // 遍历输出设备信息
        System.out.println("设备信息列表：");
        System.out.println("--------------------------------------------");
        for (Equipment equipment : equipments) {
            System.out.println(equipment);
        }
        System.out.println("--------------------------------------------");
    }
}
