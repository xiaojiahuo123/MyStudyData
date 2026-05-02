package day_13.practice.collection;

import java.util.*;

public class CollectionAnswer {
    public static void main(String[] args) {
        List<Integer> list = new ArrayList<>();
        list.add(1); list.add(2); list.add(3); list.add(4); list.add(5);
        for (Integer i : list) System.out.println(i);
    }
    // Q10 理解题答案：泛型让集合更安全，避免类型转换错误，提升代码可读性。
}
