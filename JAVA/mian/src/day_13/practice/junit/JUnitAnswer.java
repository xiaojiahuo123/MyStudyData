package day_13.practice.junit;

import org.junit.Test;

public class JUnitAnswer {
    // Q15 编程题答案：JUnit测试用例
    public int add(int a, int b) { return a + b; }
    @Test
    public void testAdd() {
        assert add(2, 3) == 5;
    }
    // Q16 理解题答案：单元测试能及时发现代码错误，保证代码质量。
}
