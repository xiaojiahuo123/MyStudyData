package day_17.MyLinkedList;

import java.util.Objects;
import java.util.StringJoiner;

public class MyLinkedList<E> {
    private Node<E> first;//用于记录双向链表的头结点的地址，默认值是null
    private Node<E> last;//用于记录双向链表的尾结点的地址，默认值是null
    private int size;//记录双向链表中结点的数量，同时就是元素个数

    //添加内部类 ,静态成员内部类，因为在Node内部类中，没有用到外部类MyLinkedList的任何非静态成员
    private static class Node<E>{
        Node<E> previous;//记录前一个结点的地址
        E data;
        Node<E> next;//记录下一个结点的地址

        Node(Node<E> previous, E data, Node<E> next) {
            this.previous = previous;
            this.data = data;
            this.next = next;
        }
    }

    public void add(E e){//新增节点
        //直接从last后面开始新增，不管链表中原本有没有节点，都是可以使用的(原本没有节点的last是null)
        Node<E> newNode = new Node<>(last,e,null);
/*
前向连接 ： newNode.prev = last （在构造函数中完成）
后向连接 ： last.next = newNode （在else分支中完成）
指针更新 ： last = newNode （确保后续添加操作基于新的尾节点）
### 3. 为什么需要双向连接？
如果只设置 newNode.prev = last ，而不设置 last.next = newNode ：

- 新节点知道自己的前一个节点是last ，但
- last不知道自己的后一个节点是newNode
这会导致：

- 从 first 开始遍历链表时，无法到达 newNode （因为 last.next 仍然是 null ）
- 链表结构不完整，新节点实际上 未被整合到链表中
* */
       if(first == null){
           first = newNode; //如果原来不存在首节点，那么新增的节点就是链表的首节点，这样直接操作赋值的是地址
       }else{
           last.next = newNode;//添加的方式，尾插的方式就是直接在其last的下一位的地址改为该节点的地址实现添加到链表中
       }
        last = newNode;//新结点成了链表的最后一个结点
        //元素或结点个数+1
        size++;
    }

/*    public Node<E> findNode(Object o){//查找
    if (o == null) {
        //System.out.println("查询的对象为null");
        return null;
    }else{
        Node<E> myNode =first; //这个时候直接从第一个的地址给创建的新对象，然后按照顺序往后走
        while (myNode.next != null){//链表不是空的或则不是最后一个节点
            if ( !myNode.equals(o)){
            - myNode 是 Node 类型（节点对象）， o 是传入的目标对象。实际比较 ：比较的是 Node 实例和目标对象，而不是 节点中存储的数据 和目标对象。
                myNode = myNode.next;//一个链表中，节点的next就是下一个节点的地址，这里作为一个新对象，也就等于是变为了下一个节点
                break;
            }
        }
        return myNode;//如果没找到,node=null，如果找到了，node是目标结点的地址
    }
### 空值处理错误
- 错误原因 ：当 o == null 时直接返回 null ，但实际上应该允许查找 null 元素。
- 正确做法 ：当 o == null 时，比较 myNode.data == null
}*/

    public Node<E> findNode(Object o){
        Node<E> current = first;
        while (current != null) {
            // 处理 null 值的情况
            if (o == null ? current.data == null : Objects.equals(o,current.data)) {
                return current; // 找到节点，返回
            }
            current = current.next; // 移动到下一个节点
        }
        return null; // 遍历完整个链表，未找到节点
    }

/*    public void remove(Object o){ //自己写的方法
        if(o == null){
            System.out.println("输入错误");
            return;  //直接结束方法
        }else{
            Node<E> myNode = findNode(o);
            //删除一个节点，将该节点对应的上一个节点的next改为下一个节点的地址，将该节点下一个节点的previous改为此节点上一个节点的地址即可
            myNode.previous.next = myNode.next;
            myNode.next.previous = myNode.previous;
            //直接这样做的不足之处在于，只是从这个链表中删除了节点，但对于链表原本的完整没有做检查和维护
        }
        //元素个数减少
        size--;

### 空指针异常风险
- 问题 ：当删除的是 头节点 时， myNode.previous 为 null ，执行 myNode.previous.next 会抛出 NullPointerException
- 问题 ：当删除的是 尾节点 时， myNode.next 为 null ，执行 myNode.next.previous 会抛出 NullPointerException
- 问题 ：当 findNode(o) 返回 null （未找到节点）时，执行 myNode.previous 会抛出 NullPointerException
- 问题 ：删除头节点后， first 指针仍指向被删除的节点
- 问题 ：删除尾节点后， last 指针仍指向被删除的节点
- 影响 ：后续操作（如遍历、添加新节点）会出错
- 问题 ：当 o == null 时直接返回，不符合Java集合的惯例（ LinkedList 允许删除 null 元素）
- 问题 ：未找到节点时没有任何提示或处理
### 内存泄漏风险
- 问题 ：被删除节点的 prev 和 next 引用未置为 null ，可能导致垃圾回收延迟
    }*/

    public boolean remove(Object o){
        // 找到目标节点
        Node<E> myNode = findNode(o);
        // 未找到节点，返回false
        if (myNode == null) {
            return false;
        }
        // 处理头节点删除
        if (myNode == first) {
            first = myNode.next;
            // 如果删除后链表不为空，更新新头节点的prev为null
            if (first != null) {
                first.previous = null;
            }
        } else {
            // 非头节点，更新前一个节点的next
            myNode.previous.next = myNode.next;
        }
        // 处理尾节点删除
        if (myNode == last) {
            last = myNode.previous;
            // 如果删除后链表不为空，更新新尾节点的next为null
            if (last != null) {
                last.next = null;
            }
        } else {
            // 非尾节点，更新后一个节点的prev
            if (myNode.next != null) {
                myNode.next.previous = myNode.previous;
            }
        }
        // 清空被删除节点的引用，避免内存泄漏
        myNode.previous = null;
        myNode.next = null;
        // 元素个数减少
        size--;
        return true;
    }

    @Override
    public String toString(){
        //拼接所有结点的data，返回
        StringJoiner joiner = new StringJoiner(",","[","]");
        Node<E> node = first;
        while(node!= null){
            joiner.add(node.data+"");
            node = node.next;//让node往右移动
        }

        return joiner.toString();
    }
}
