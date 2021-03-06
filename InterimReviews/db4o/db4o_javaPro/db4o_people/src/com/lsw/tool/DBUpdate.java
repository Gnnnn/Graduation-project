package com.lsw.tool;

import java.util.List;

import com.db4o.Db4oEmbedded;
import com.db4o.ObjectContainer;
import com.lsw.bean.People;
import com.lsw.util.Constants;

public class DBUpdate {
    /**
     * 更新和检索必须都先把对象检索出来然后进行操作
     * @param db
     */
    public static void update(ObjectContainer db) {
        List<People> result = db.queryByExample(new People(1));
        People people; // 这里根据ID检索，最多一条结果
        if (result != null && result.size() > 0) {// 有检索结果
            people = result.get(0);
            System.out.println("更新前的值：" + people);
            // 更新这条记录
            people.setId(4);
            people.setName("张思");
            people.setAddress("弘博");
            db.store(people);
            // 查看更新后的结果
            DBQuery.queryAll(db);
        } else {
            System.out.println("没有检索到任何记录.");
        }

    }

    public static void main(String[] args) {
        ObjectContainer db = Db4oEmbedded.openFile(Constants.DB4O_FILENAME);
        update(db);
        db.close();
    }
}