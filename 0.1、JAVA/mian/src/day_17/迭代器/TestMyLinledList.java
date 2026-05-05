package day_17.迭代器;

import org.junit.Test;

public class TestMyLinledList {

    @Test
    public void test1() {
        MyLinkedList_Iterator<String> myLinkedListIterator = new MyLinkedList_Iterator<>();
        myLinkedListIterator.add("1 - 1");
        myLinkedListIterator.add("1 - 2");
        myLinkedListIterator.add("1 - 3");
        myLinkedListIterator.add("1 - 4");
        myLinkedListIterator.add("1 - 5");

        for (String str : myLinkedListIterator) {
            //str = str.trim();
            System.out.print(str);
        }
    }
}
