package com.lsw.tool;

import com.db4o.Db4oEmbedded;
import com.db4o.ObjectContainer;
import com.db4o.ObjectSet;
import com.lsw.bean.People;
import com.lsw.util.Constants;

public class DBDelete {
    public static void delete(ObjectContainer db) {
        System.out.println("ɾ��ǰ��");
        DBQuery.queryAll(db);
        ObjectSet<People> result = db.queryByExample(new People(4));
        People p = result.next();
//        System.out.println(p);
//        why result.next()?
        if (p != null) { // ����ȷ����Ҫɾ���Ķ������
            db.delete(p);
        }
        System.out.println("ɾ����");
        DBQuery.queryAll(db);
    }

    public static void main(String[] args) {
        ObjectContainer db = Db4oEmbedded.openFile(Constants.DB4O_FILENAME);
        delete(db);
        db.close();

    }
}