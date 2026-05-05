package day_17.ArrayListAndVector;

import java.util.Arrays;
import java.util.Objects;
import java.util.StringJoiner;

/*
因为直接跟踪ArrayList和Vector的源码，比较有难度。
为了捋清它的底层思路，我们“模仿”ArrayList写一个简易迷你版的动态数组。

这个思想弄清楚之后，对于ArrayList和Vector，StringBuffer，StringBuilder等的理解都有好处
 */
public class MyArrayList<E> {
    private Object[] elementData = new Object[5];//先初始化为长度5的数组，后续不够了再扩容
    private int size;//记录实际存储的元素的个数  正常来说 size <= elementData.length

   /* public void add(E e){//末尾位置添加
        //选中要抽取到新方法中的代码，然后按Ctrl +Alt + M
        if(size >= elementData.length){//说明数组已满，无法加新元素了
            //扩容
//            elementData = Arrays.copyOf(elementData, elementData.length + (elementData.length>>1));
            elementData = Arrays.copyOf(elementData, elementData.length + elementData.length/2);
            //让elementData指向新数组
        }
        elementData[size++] = e;
    }*/
   public void add(E e){//末尾位置添加
       //检查要不要扩容，如果需要，就进行扩容
       grow();
       elementData[size++] = e;
   }

    private void grow() {
        if(size >= elementData.length){//说明数组已满，无法加新元素了
            //扩容
 //            elementData = Arrays.copyOf(elementData, elementData.length + (elementData.length>>1));
            elementData = Arrays.copyOf(elementData, elementData.length + elementData.length/2);
            //让elementData指向新数组
        }
    }

    public void add(int index, E e){//中间位置插入
        if(index<0 || index>size){
            throw new IndexOutOfBoundsException(index+"越界了");
        }
        //检查要不要扩容，如果需要，就进行扩容
        grow();
        /*
        移动元素,新元素的插入位置是index
        假设 elementData数组的长度为5，size=4， index=1
             需要移动 elementData[1],elementData[2],elementData[3]
             分别移到  elementData[2],elementData[3],elementData[4]
             个数：size-index
         */
        System.arraycopy(elementData,index, elementData, index+1, size-index);
        //把新元素放到[index]位置
        elementData[index] = e;
        //元素个数增加
        size++;
    }

    public void remove(int index){
       if(index<0 || index>=size){
           throw new IndexOutOfBoundsException(index+"越界了");
       }
        /*
        移动元素,删除的位置是index
        假设 elementData数组的长度为5，size=4， index=1
             需要移动 elementData[2],elementData[3]
             分别移到  elementData[1],elementData[2]
             个数：size-index-1
         */
        System.arraycopy(elementData, index+1, elementData, index, size-index-1);
        //把末尾位置置为null，且元素个数减少
        elementData[--size] = null;
    }

    public void remove(Object obj){
       //先找到obj在当前数组的位置
        int index = indexOf(obj);
        if(index==-1){
            return;//提前结束删除过程，不删除了
        }
        remove(index);
    }

    public int indexOf(Object obj){
       //找到了，返回正常的下标
        //思路一：分情况讨论
        /*if(obj == null){
            for (int i = 0; i < size; i++) {
                if (obj == elementData[i]) {
                    return i;
                }
            }
        }else {
            for (int i = 0; i < size; i++) {
                if (obj.equals(elementData[i])) {
                    return i;
                }
            }
        }*/
        //思路二：用Objects工具类的equals方法
        for (int i = 0; i < size; i++) {
            if (Objects.equals(elementData[i],obj)) {
                return i;
            }
        }
       return -1;//代表不存在
    }

    public int lastIndex(Object obj){
        //思路二：用Objects工具类的equals方法
        for (int i = size-1; i >=0; i--) {
            if (Objects.equals(elementData[i],obj)) {
                return i;
            }
        }
        return -1;//代表不存在
    }

    @Override
    public String toString() {
        //return Arrays.toString(elementData);//可以，不够完美，会把null元素也暴露了
        //希望有size个元素，就返回size个元素给对方看
        StringJoiner joiner = new StringJoiner(",","[","]");
        for(int i=0; i<size; i++){
            joiner.add(elementData[i]+"");
        }
        return joiner.toString();
    }
}
