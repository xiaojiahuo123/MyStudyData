package day05_teacher_code.src;

public class MyLianxi_01 {
        public static void main(String[] args) {
            System.out.println("1000以内的完数有：");

            // 遍历1到1000的每个数
            for (int num = 1; num <= 1000; num++) {
                if (isPerfectNumber(num)) {
                    System.out.print(num + " ");
                }
            }
        }

        /**
         * 判断一个数是否为完数
         * 完数是指一个数恰好等于它的真因子之和（不包括自身的约数）
         */
        public static boolean isPerfectNumber(int num) {
            // 1没有真因子，不是完数
            if (num <= 1) {
                return false;
            }

            int factorSum = 1; // 1是所有大于1的数的真因子

            // 寻找所有真因子并累加
            // 只需检查到num/2即可，因为大于num/2的数不可能是num的因子（除了num本身）
            for (int i = 2; i <= num / 2; i++) {
                if (num % i == 0) {
                    factorSum += i;
                }
            }

            // 如果因子和等于该数，则是完数
            return factorSum == num;
        }


}
