package com.lsw.tool;

import java.util.List;

import com.db4o.Db4oEmbedded;
import com.db4o.ObjectContainer;
import com.db4o.ObjectSet;
import com.db4o.query.Predicate;
import com.db4o.query.Query;
import com.lsw.bean.InstantNoodles;
import com.lsw.util.Constants;

public class DBNQQuery {
    /**
     * 使用SODA方式进行查询
     * 
     * @param db
     */
    public static void testSODAQuery(ObjectContainer db) {
        Query query = db.query();
        query.constrain(InstantNoodles.class);
        Query idQuery = query.descend("id");
        query.descend("name").constrain("杜甫").or(idQuery.constrain(2).greater().and(idQuery.constrain(4).smaller()));
        ObjectSet<InstantNoodles> result = query.execute();
        DBQuery.listResult(result);
    }

    /**
     * 使用NQ方式进行查询
     * 
     * @param db
     */
    public static void testNQQuery(ObjectContainer db) {
        List<InstantNoodles> result = db.query(new Predicate<InstantNoodles>() {
            public boolean match(InstantNoodles istn) {
                return istn.getId() > 2 && istn.getId() < 4 || istn.getName().equals("杜甫");
            }
        });
        DBQuery.listResult(result);
    }

    /**
     * 使用NQ方式进行查询
     * 
     * @param db
     */
    public static void testNQQuery2(ObjectContainer db) {
        final int[] points = { 1, 2, 5, 6 };
        List<InstantNoodles> result = db.query(new Predicate<InstantNoodles>() {
            public boolean match(InstantNoodles istn) {
                for (int point : points) {
                    if (istn.getId() == point) {
                        return true;
                    }
                }
                return istn.getName().startsWith("王");
            }
        });
        DBQuery.listResult(result);
    }

    public static void main(String[] args) {
        ObjectContainer db = Db4oEmbedded.openFile(Constants.DB4O_FILENAME);
        System.out.println("数据库中的全部实例：");
        DBQuery.queryAll(db);
        System.out.println("查询出来的实例：");
        testNQQuery(db);
        testNQQuery2(db);
        db.close();
    }
}