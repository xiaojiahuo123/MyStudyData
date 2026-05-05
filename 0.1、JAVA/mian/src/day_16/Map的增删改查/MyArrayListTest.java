package day_16.Map的增删改查;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Objects;

public class MyArrayListTest<E> {
    private Object[] elementData = new Object[10];
    private int size ;//记录实际存储元素个数，正常size < elementData.lenth

    public void add(E e){//数组添加元素实现
        grow();
        elementData[size++] = e; //添加
    }

    private void grow() {
        if(size >= elementData.length){
            elementData = Arrays.copyOf(elementData, elementData.length + elementData.length/2);//数据扩容
            //复制原数组，并且给出新数组的长度
        }
    }

    @Override
    public String toString() {
        // 处理空数组情况
        if (size == 0) {
            return "[]";
        }
        
        // 构建字符串
        StringBuilder sb = new StringBuilder("[");
        for (int i = 0; i < size; i++) {
            sb.append(elementData[i]);
            // 最后一个元素后不加逗号
            if (i < size - 1) {
                sb.append(", ");
            }
        }
        sb.append("]");
        
        return sb.toString();
    }

    public void add(int index , E e){//中间位置插入元素
        if (index < 0 || index > size) {
            throw new IndexOutOfBoundsException("索引越界！" + index);
        }
        grow();
        System.arraycopy(elementData, index, elementData, index + 1, size - index);
        //把新元素放到[index]位置
        elementData[index] = e;
        //元素个数增加
        size++;
    }

/*    public void remove(int index){
        //根据下标删除元素
        if (index < 0 || index > size -1){
            throw new IndexOutOfBoundsException("输入索引越界!");
        }
*//*      elementData[index] = elementData[index + 1];
        size = size - 1;  存在问题，如果删除的是最后一个元素呢？
       *//*
       if (index + 1 > size){//问题：由于前面已经做了index > size -1抛出异常保证index不会大于size -1 ，所以这里实际不会有作用
           elementData[index] = null;
           size--;
       }else{
           for (int i = index; i < size; i++) {
             elementData[i] = elementData[i + 1];
           }
           size--;
       }
    }*/

    public void remove(int index) {
        // 边界检查
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("输入索引越界! 有效范围: 0-" + (size - 1));
        }

        // 计算需要移动的元素数量
        int numMoved = size - index - 1;
        if (numMoved > 0) {
            // 使用 System.arraycopy 高效移动元素
            System.arraycopy(elementData, index + 1, elementData, index, numMoved);
        }

        // 清空最后一个元素的引用，避免内存泄漏
        elementData[--size] = null;
    }

    public void remove(Object o) {
        //先找到obj在当前数组的位置
        int index = indexOf(o);
        if(index==-1){
            return;//提前结束删除过程，不删除了
        }
        remove(index);
    }

    public int indexOf(Object o) {
        //int indexOf = -1;
        if (o == null) {
            return -1;
        }
//        for (int i = 0; i < size -1 ; i++) {
//            if(elementData[i].equals(o)){
//                indexOf = i;
//            }
//        }
        for (int i = 0; i < size; i++) {
            if (Objects.equals(elementData[i],o)) {
                return i;
            }
        }
        return -1;//代表不存在
    }

    public Object chaxun(E e){
        if (Objects.equals(e,null)){
            throw new IndexOutOfBoundsException("查询为空！");
        }
        for(Object o : elementData ){
            if (o.equals(e)){
                return o;
            }
        }
        return -1;
    }
}
