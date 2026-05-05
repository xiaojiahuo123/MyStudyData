package day_12.homework2;

public class ShapTest {
    public static void main(String[] args) {
        // 获取圆形对象并调用draw方法
        Shape circle = ShapeFactory.getShape("circle");
        if (circle != null) {
            circle.draw();  // 输出：绘制圆形
        }
        
        // 获取正方形对象并调用draw方法
        Shape square = ShapeFactory.getShape("square");
        if (square != null) {
            square.draw();  // 输出：绘制正方形
        }
        
        // 获取三角形对象并调用draw方法
        Shape triangle = ShapeFactory.getShape("triangle");
        if (triangle != null) {
            triangle.draw();  // 输出：绘制三角形
        }
    }
}
