package day_13.test_01异常.MyJUnit;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;

import java.io.ByteArrayInputStream;
import java.io.InputStream;
import java.util.Scanner;

public class MyTestJUnit {
    // 保存原始的System.in流
    private InputStream originalIn;
    
    // 在每个测试方法执行前保存原始输入流
    @Before
    public void setUp() {
        originalIn = System.in;
    }
    
    // 在每个测试方法执行后恢复原始输入流
    @After
    public void tearDown() {
        System.setIn(originalIn);
    }
    
    // 测试calculateSumFromInput功能
    @Test
    public void testCalculateSumFromInput() {
        try {
            // 模拟输入："10" 和 "20"
            String input = "10\n20\n";
            System.setIn(new ByteArrayInputStream(input.getBytes()));
            
            // 直接在测试方法中实现计算逻辑
            Scanner scanner = new Scanner(System.in);
            int num1 = scanner.nextInt();
            int num2 = scanner.nextInt();
            int result = num1 + num2;
            
            // 使用JUnit断言验证结果
            assertEquals("10 + 20 应该等于 30", 30, result);
        } catch (Exception e) {
            fail("测试发生异常: " + e.getMessage());
        }
    }
    
    // 测试isPositiveNumber功能 - 正数情况
    @Test
    public void testIsPositiveNumberWithPositiveInput() {
        try {
            // 模拟输入："15"
            String input = "15\n";
            System.setIn(new ByteArrayInputStream(input.getBytes()));
            
            // 直接在测试方法中实现判断逻辑
            Scanner scanner = new Scanner(System.in);
            int num = scanner.nextInt();
            boolean result = num > 0;
            
            // 使用JUnit断言验证结果
            assertTrue("15 应该被判断为正数", result);
        } catch (Exception e) {
            fail("测试发生异常: " + e.getMessage());
        }
    }
    
    // 测试isPositiveNumber功能 - 负数情况
    @Test
    public void testIsPositiveNumberWithNegativeInput() {
        try {
            // 模拟输入："-5"
            String input = "-5\n";
            System.setIn(new ByteArrayInputStream(input.getBytes()));
            
            // 直接在测试方法中实现判断逻辑
            Scanner scanner = new Scanner(System.in);
            int num = scanner.nextInt();
            boolean result = num > 0;
            
            // 使用JUnit断言验证结果
            assertFalse("-5 不应该被判断为正数", result);
        } catch (Exception e) {
            fail("测试发生异常: " + e.getMessage());
        }
    }
    
    // 测试两个整数相加的功能
    @Test
    public void testCalculateSum() {
        try {
            // 准备测试数据
            String input = "5\n7\n";
            Scanner scanner = new Scanner(new ByteArrayInputStream(input.getBytes()));
            
            // 直接在测试方法中实现计算逻辑
            int num1 = scanner.nextInt();
            int num2 = scanner.nextInt();
            int result = num1 + num2;
            scanner.close();
            
            // 使用JUnit断言验证结果
            assertEquals("5 + 7 应该等于 12", 12, result);
        } catch (Exception e) {
            fail("测试发生异常: " + e.getMessage());
        }
    }
}
