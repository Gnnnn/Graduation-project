package com.lsw.tool;

import java.util.List;

import com.db4o.Db4oEmbedded;
import com.db4o.ObjectContainer;
import com.db4o.ObjectSet;
import com.lsw.bean.People;
import com.lsw.util.Constants;

public class DBQuery {
    /**
     * ����ȫ�����
     * 
     * @param db
     */
    public static void queryAll(ObjectContainer db) {
        People people = new People();
        ObjectSet<?> result = db.queryByExample(people);
        listResult(result);
    }

    /**
     * ������
     * 
     * @param result
     */
    public static void listResult(List<?> result) {
        System.out.println("�������������" + result.size());
        for (int i = 0; i < result.size(); i++) {
            System.out.println((People) result.get(i));
        }

    }

    public static void main(String[] args) {
        ObjectContainer db = Db4oEmbedded.openFile(Constants.DB4O_FILENAME);
        ObjectSet<People> set = db.queryByExample(new People(1));
        ObjectSet<People> set2 = db.queryByExample(new People(2));
//        ObjectSet<People> set3 = db.queryByExamplenew(People());
//		�������û�ж�
        listResult(set);
        listResult(set2);
        db.close();
    }
}