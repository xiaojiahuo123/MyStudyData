package day_15.泛型.有名字的类实现泛型接口;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class Rectangle implements Comparable<Rectangle>{

    private double length;
    private double width;

    public double area(){
        return length * width;
    }

    public double perimeter(){
        return 2 * (length + width);
    }


    @Override
    public int compareTo(Rectangle o) {
        return Double.compare(this.area() , o.area());
    }

/*
*  public static int compare(double d1, double d2) {
if (d1 < d2)
return -1;           // Neither val is NaN, thisVal is smaller
if (d1 > d2)
return 1;
* */
}
