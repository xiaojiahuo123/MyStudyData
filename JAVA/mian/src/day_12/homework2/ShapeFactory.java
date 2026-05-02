package day_12.homework2;

public class ShapeFactory {
     // 圆形内部类
    private static class Circle implements Shape {
        @Override
        public void draw() {
            System.out.println("绘制圆形");
        }
    }
    
    // 正方形内部类
    private static class Square implements Shape {
        @Override
        public void draw() {
            System.out.println("绘制正方形");
        }
    }
    
    // 三角形内部类
    private static class Triangle implements Shape {
        @Override
        public void draw() {
            System.out.println("绘制三角形");
        }
    }
    
    // 静态工厂方法
    public static Shape getShape(String type) {
        if (type == null) {
            return null;
        }
        
        switch (type.toLowerCase()) {
            case "circle":
                return new Circle();
            case "square":
                return new Square();
            case "triangle":
                return new Triangle();
            default:
                return null;
        }
    }
}
