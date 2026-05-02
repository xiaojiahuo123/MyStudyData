package day_17.迭代器;

import day_17.MyLinkedList.MyLinkedList;

import java.util.Iterator;
import java.util.Objects;
import java.util.StringJoiner;

public class MyLinkedList_Iterator<E> implements Iterable<E>{
    private Node<E> first;//用于记录双向链表的头结点的地址，默认值是null
    private Node<E> last;//用于记录双向链表的尾结点的地址，默认值是null
    private int size;//记录双向链表中结点的数量，同时就是元素个数

    private static class Node<E>{
        MyLinkedList_Iterator.Node<E> previous;//记录前一个结点的地址
        E data;
        MyLinkedList_Iterator.Node<E> next;//记录下一个结点的地址

        Node(MyLinkedList_Iterator.Node<E> previous, E data, MyLinkedList_Iterator.Node<E> next) {
            this.previous = previous;
            this.data = data;
            this.next = next;
        }
    }

/*    public class MyLinkedListIterator<E>  implements Iterator<E>{
        int index;

        @Override
        public boolean hasNext() {
            return index < size;  //链表中还有没有元素存在
        }

        @Override
        public E next() {
            return null;
        }
    }*/

    // 移除内部类的泛型参数（使用外部类的泛型）
    public class MyLinkedListIterator implements Iterator<E> {
        private Node<E> current; // 当前迭代节点
        private int index; // 当前迭代索引

        // 构造方法，从首节点开始迭代
        public MyLinkedListIterator() {
            this.current = first;
            this.index = 0;
        }

        @Override
        public boolean hasNext() {
            return index < size; // 还有元素未遍历
        }

        @Override
        public E next() {
            if (!hasNext()) {
                throw new java.util.NoSuchElementException();
            }
            E data = current.data; // 获取当前节点数据
            current = current.next; // 移动到下一个节点
            index++; // 索引递增
            return data; // 返回当前元素
        }
    }

   public void add(E e){
       MyLinkedList_Iterator.Node<E> newNode = new MyLinkedList_Iterator.Node<>(last,e,null);
       if(first == null){
           first = newNode; //如果原来不存在首节点，那么新增的节点就是链表的首节点，这样直接操作赋值的是地址
       }else{
           last.next = newNode;//添加的方式，尾插的方式就是直接在其last的下一位的地址改为该节点的地址实现添加到链表中
       }
       last = newNode;//新结点成了链表的最后一个结点
       //元素或结点个数+1
       size++;
   }

   public Node<E> findNode(Object o){
       MyLinkedList_Iterator.Node<E> current = first;
       while(current!=null){
           // 处理 null 值的情况
           if (o == null ? current.data == null : Objects.equals(o,current.data)) {
               return current; // 找到节点，返回
           }
           current = current.next; // 移动到下一个节点
       }
       return null;
   }

    public boolean remove(Object o){
        // 找到目标节点
        MyLinkedList_Iterator.Node<E> myNode = findNode(o);
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
    public String toString() {
        //拼接所有结点的data，返回
        StringJoiner joiner = new StringJoiner(",","[","]");
        MyLinkedList_Iterator.Node<E> node = first;
        while(node!= null){
            joiner.add(node.data+"");
            node = node.next;//让node往右移动
        }

        return joiner.toString();
    }

    @Override
    public Iterator<E> iterator() {
        return new MyLinkedListIterator();
    }
}
