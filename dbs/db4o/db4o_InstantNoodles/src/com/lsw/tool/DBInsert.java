package com.lsw.tool;

import com.db4o.Db4oEmbedded;
import com.db4o.ObjectContainer;
import com.lsw.bean.InstantNoodles;
import com.lsw.util.Constants;

public class DBInsert {

    public static void main(String[] args) {
        // 打开数据库
        ObjectContainer db = Db4oEmbedded.openFile(Db4oEmbedded.newConfiguration(), Constants.DB4O_FILENAME);
        try {
            // 构造 People 对象
        	InstantNoodles istn1 = new InstantNoodles(1001);
        	istn1.setSampleId("20070528761");
        	istn1.setName("庖丁时蔬");
        	istn1.setSpecification("袋装75g");
        	istn1.setManufacturer("五谷道场");
            db.store(istn1);
            InstantNoodles istn2 = new InstantNoodles(1002, "20070810671", "西红柿牛腩", "袋装75g", "五谷道场");
            db.store(istn2);
            InstantNoodles istn3 = new InstantNoodles(1003, "BJ20071025262", "酱香排骨", "袋装75g", "五谷道场");
            db.store(istn3);
            InstantNoodles istn4 = new InstantNoodles(1004, "2007100312", "庖丁时蔬", "袋装75g", "五谷道场");
            db.store(istn4);
            InstantNoodles istn5 = new InstantNoodles(1005, "20070917561", "海鲜八珍", "袋装75g", "五谷道场");
            db.store(istn5);
            InstantNoodles istn6 = new InstantNoodles(1006, "20070810671", "西红柿牛腩", "袋装75g", "五谷道场");
            db.store(istn6);
            InstantNoodles istn7 = new InstantNoodles(1007, "2007092612", "香辣原汁牛肉", "袋装75g", "五谷道场");
            db.store(istn7);
            InstantNoodles istn8 = new InstantNoodles(1008, "200706201035", "四川麻辣牛肉味", "袋装75g", "今麦郎");
            db.store(istn8);
            System.out.println("插入完成。");
            
        } finally {
            // 关闭连接
            db.close();
        }
    }

}