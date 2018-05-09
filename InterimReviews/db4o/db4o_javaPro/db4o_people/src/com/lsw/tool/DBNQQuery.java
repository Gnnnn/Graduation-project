package com.lsw.tool;

import java.util.List;

import com.db4o.Db4oEmbedded;
import com.db4o.ObjectContainer;
import com.db4o.ObjectSet;
import com.db4o.query.Predicate;
import com.db4o.query.Query;
import com.lsw.bean.People;
import com.lsw.util.Constants;

public class DBNQQuery {
    /**
     * ʹ��SODA��ʽ���в�ѯ
     * 
     * @param db
     */
    public static void testSODAQuery(ObjectContainer db) {
        Query query = db.query();
        query.constrain(People.class);
        Query idQuery = query.descend("id");
        query.descend("name").constrain("�Ÿ�").or(idQuery.constrain(2).greater().and(idQuery.constrain(4).smaller()));
        ObjectSet<People> result = query.execute();
        DBQuery.listResult(result);
    }

    /**
     * ʹ��NQ��ʽ���в�ѯ
     * 
     * @param db
     */
    public static void testNQQuery(ObjectContainer db) {
        List<People> result = db.query(new Predicate<People>() {
            public boolean match(People people) {
                return people.getId() > 2 && people.getId() < 4 || people.getName().equals("�Ÿ�");
            }
        });
        DBQuery.listResult(result);
    }

    /**
     * ʹ��NQ��ʽ���в�ѯ
     * 
     * @param db
     */
    public static void testNQQuery2(ObjectContainer db) {
        final int[] points = { 1, 2, 5, 6 };
        List<People> result = db.query(new Predicate<People>() {
            public boolean match(People people) {
                for (int point : points) {
                    if (people.getId() == point) {
                        return true;
                    }
                }
                return people.getName().startsWith("��");
            }
        });
        DBQuery.listResult(result);
    }

    public static void main(String[] args) {
        ObjectContainer db = Db4oEmbedded.openFile(Constants.DB4O_FILENAME);
//        People p1 = new People(4, "����", "�Ϻ�");
//        People p2 = new People(5, "�Ÿ�", "����");
//        People p3 = new People(6, "����", "�Ͼ�");
//        db.store(p1);
//        db.store(p2);
//        db.store(p3);
        System.out.println("���ݿ��е�ȫ��ʵ����");
        DBQuery.queryAll(db);
        System.out.println("��ѯ������ʵ����");
        testNQQuery(db);
        testNQQuery2(db);
        db.close();
    }
}