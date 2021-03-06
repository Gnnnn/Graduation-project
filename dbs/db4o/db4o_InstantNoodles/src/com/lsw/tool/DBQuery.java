package com.lsw.tool;

import java.util.List;

import com.db4o.Db4oEmbedded;
import com.db4o.ObjectContainer;
import com.db4o.ObjectSet;
import com.lsw.bean.InstantNoodles;
import com.lsw.util.Constants;

public class DBQuery {
    /**
     * 检索全部结果
     * 
     * @param db
     */
    public static void queryAll(ObjectContainer db) {
    	InstantNoodles istn = new InstantNoodles();
        ObjectSet<?> result = db.queryByExample(istn);
        listResult(result);
    }

    /**
     * 输出结果
     * 
     * @param result
     */
    public static void listResult(List<?> result) {
        System.out.println("共检索结果数：" + result.size());
        for (int i = 0; i < result.size(); i++) {
            System.out.println((InstantNoodles) result.get(i));
        }

    }

    public static void main(String[] args) {
        ObjectContainer db = Db4oEmbedded.openFile(Constants.DB4O_FILENAME);
        int searchNum = 1001;
        ObjectSet<InstantNoodles> set = db.queryByExample(new InstantNoodles(searchNum));
        ObjectSet<InstantNoodles> setall = db.queryByExample(new InstantNoodles());
        
        System.out.println("全局搜索：");
//        两种方法一样的，二选一
        queryAll(db);
//        listResult(setall);
        
        System.out.println("局部搜索：");
        listResult(set);
        db.close();
    }
}