package day07_teacher_code.src;

public class UnitConverter {//比喻：外包公司
//    - celsiusToFahrenheit(double celsius): 将摄氏温度转换为华氏温度。华氏温度 = 摄氏温度 *1.8+32
    public static double celsiusToFahrenheit(double celsius){
        return celsius * 1.8 + 32;
    }
//            - fahrenheitToCelsius(double fahrenheit): 将华氏温度转换为摄氏温度。
    public static double fahrenheitToCelsius(double fahrenheit){
        return (fahrenheit - 32)/1.8;
    }
//            - metersToFeet(double meters): 将米转换为英尺。1米= 3.2808英尺
    public static double metersToFeet(double meters){
        return meters * 3.2808;
    }

}
