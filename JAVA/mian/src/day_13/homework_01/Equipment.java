package day_13.homework_01;

public class Equipment {
    // 私有属性
    private int id;          // 设备编号
    private String brand;    // 设备品牌
    private double price;    // 价格
    private String name;     // 设备名称
    private Status status;   // 状态

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getBrand() {
        return brand;
    }

    public void setBrand(String brand) {
        this.brand = brand;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Status getStatus() {
        return status;
    }

    public void setStatus(Status status) {
        this.status = status;
    }

    public Equipment(int id, String brand, double price, String name, Status status) {
        this.id = id;
        this.brand = brand;
        this.price = price;
        this.name = name;
        this.status = status;
    }

    public Equipment() {
    }

    @Override
    public String toString() {
        return "设备编号：" + id + 
               "，品牌：" + brand + 
               "，价格：" + price + 
               "，设备名称：" + name + 
               "，状态：" + status;
    }
}
