package day_12.test_06枚举;

public enum Week {
        MONDAY("星期一"),
        TUESDAY("星期二"),
        WEDNESDAY("星期三"),
        THURSDAY("星期四"),
        FRIDAY("星期五"),
        SATURDAY("星期六"),
        SUNDAY("星期日");


        private final String description;//建议实例变量加final

        //private在这里完全可以省略，因为枚举类中的构造器一定是私有的
/*    private Week(){//构造器私有化

    }*/
        private Week(String description) {//构造器私有化
            this.description = description;
        }

        //可以再次重写toString

        @Override
        public String toString() {
            return "Week{" +
                    "name = " + name() +
                    "，description='" + description + '\'' +
                    '}';
        }
}
