package day_09.test_01.cms.atguigu.service;


import day_09.test_01.cms.atguigu.bean.Customer;

/*
如何确定数组的长度？
方案一：设置固定的长度，如果数组满了，就不让往里添加（限量）  今天先用这种方案实现一下
方案二：先初始化一个长度，不够了，再扩容
 */
public class CustomerList {
    private static Customer[] arr = new Customer[3];
    //先用3便于测试，等测试通过了，再修改
    private static int count;//默认值是0

    //提供一个方法，可以把一个客户对象放到arr数组中
    public static boolean addNewCustomer(Customer c){
        /*
        方案一：循环，看哪里有空往哪里放  arr[下标] == null表示空
        方案二：使用一个变量来记录现在已经有几个客户对象了，保证数组中是连续存储，空位置永远在最后
                今天选择方案二
         */
        if(count >= arr.length){
            System.out.println("数组已满！");
            return false;//提前结束，返回false表示失败
        }
        arr[count++] = c;
        return true;//返回true表示成功
    }

    //返回所有客户对象
    public static Customer[] getAllCustomers(){
//        return arr;//方案一：直接返回arr数组，不够完美，因为里面有null值

        //方案二：创建一个新数组，里面只存储count个客户对象，返回这count个客户对象
        Customer[] allCustomers = new Customer[count];
        //从arr数组复制到allCustomers数组
        for(int i=0; i<count; i++){
            allCustomers[i] = arr[i];
        }
        return allCustomers;
    }

    //根据编号id，从数组中来删除一个客户对象
    public static boolean removeCustomer(int id){
        if(id<1 || id>count){
            return false;
        }

        //id与下标的关系： 下标 = id-1
        //方案一：把[id-1]位置的元素直接置为null
        //方案二：把[id-1]后面的元素往前移动（根据上面添加的方案二，这里选择它）
        /*
        假设 arr.length = 5，count = 4  ，[0][1][2][3]是有元素的
        id=2，下标[1]要被删除
        移动的元素情况：
        [2] -> [1]
        [3] -> [2]

        按照假设：i=1,2
         */
        for(int i=id-1; i<count-1; i++){
            arr[i] = arr[i+1];
        }

        //客户数量减少
        count--;
        return true;
    }

    //根据编号id，查询旧的客户对象
    public static Customer getCustomerById(int id){
        if(id<1 || id>count){
            return null;
        }

        //id与下标的关系： 下标 = id-1
        return arr[id-1];
    }

    //用新的客户对象替换id对应的旧客户对象
    public static boolean  replaceCustomer(int id, Customer newCustomer){
        if(id<1 || id>count){
            return false;
        }
        arr[id-1] = newCustomer;
        return true;
    }
}
