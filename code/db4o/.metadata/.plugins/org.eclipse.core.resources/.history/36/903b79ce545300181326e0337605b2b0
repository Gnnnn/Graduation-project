package com.lsw.tool;

import com.db4o.Db4oEmbedded;
import com.db4o.ObjectContainer;
import com.lsw.bean.People;
import com.lsw.util.Constants;

public class DBInsert {

    public static void main(String[] args) {
        // 打开数据库
        ObjectContainer db = Db4oEmbedded.openFile(Db4oEmbedded.newConfiguration(), Constants.DB4O_FILENAME);
        try {
            // 构造 People 对象
            People peo = new People(1);
            peo.setAddress("成都市");
            peo.setName("张三");
            // 保存对象
            db.store(peo);
            People peo2 = new People();
            peo2.setId(2);
            peo2.setAddress("上海");
            peo2.setName("李斯");
            db.store(peo2);
            People peo3 = new People(3, "小杜甫", "河北");
            db.store(peo3);
        } finally {
            // 关闭连接
            db.close();
        }
    }

}