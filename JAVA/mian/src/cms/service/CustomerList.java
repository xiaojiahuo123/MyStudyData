package cms.service;


import cms.bean.Customer;

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
    //返回客户ID
    public static Customer getCustomerById(int id){
       if (id < 1 || id > count){
           return null;
        }
       return arr[id - 1];
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

    public static boolean replaceCustomer(int id, Customer c){
        if(id < 1 || id > count){
            System.out.println("客户ID无效，找不到该客户");
            return false;
        }
        if (c == null){
            System.out.println("客户信息不能为NULL！");
            return false;
        }
        arr[id - 1] = c;
        return true;
    }
/*删除后面客户的工作原理 ：

假设数组中有n个客户（count = n），要删除第k个客户（k可以是任何位置，包括最后一个）
循环 for(int i = k; i < count; i++) 会从第k个位置开始，将所有后面的元素前移一位
当k等于count（删除最后一个客户）时，循环条件不满足（i = k 不小于 count），循环体不会执行
然后我们将最后一个元素设为null（ arr[count - 1] = null ）
 最后更新count--，表示客户数量减少了一个*/
    public static boolean deleteCustomer(int id){
        if (id < 1 || id > count){
            System.out.println("不存在该用户！");
            return false;
        }
// 将后面的元素前移
    for(int i = id; i < count; i++){
        arr[i - 1] = arr[i];
    }
    // 最后一个元素设为null
    arr[count - 1] = null;
    // 更新客户数量
    count--;
    return true;
    }
}
