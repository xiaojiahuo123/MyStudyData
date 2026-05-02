package day07_teacher_code.src;

public class TestUnitConverter {
    public static void main(String[] args) {
        //(1)摄氏度转华氏的结果
        double she = 12.0;
        System.out.println("摄氏度转华氏度： " + UnitConverter.celsiusToFahrenheit(she));

        //(2)华氏转摄氏度的结果
        double hua = 100;
        System.out.println("华氏转摄氏度：" + UnitConverter.fahrenheitToCelsius(hua));

        //（3）米转英尺
        int meter = 200;
        System.out.println("米转英尺："  + UnitConverter.metersToFeet(meter));
    }
}
