package com.lsw.tool;

import java.util.List;

import com.db4o.Db4oEmbedded;
import com.db4o.ObjectContainer;
import com.db4o.ObjectSet;
import com.lsw.bean.InstantNoodles;
import com.lsw.util.Constants;
import com.lsw.tool.DBQuery;

public class DBUpdate {
    /**
     * ���ºͼ������붼�ȰѶ����������Ȼ����в���
     * @param db
     */
    public static void update(ObjectContainer db, int id, String sampleId, String name, String specification , String manufacturer) {
        List<InstantNoodles> result = db.queryByExample(new InstantNoodles(id));
        InstantNoodles istn; // �������ID���������һ�����
        if (result != null && result.size() > 0) {// �м������
        	istn = result.get(0);
            System.out.println("����ǰ��ֵ��" + istn);
            // ����������¼
            if(sampleId != null){
            	istn.setSampleId(sampleId);
            }
            if(name != null){
            	istn.setName(name);
            }
            if(specification != null){
            	istn.setSpecification(specification);
            }
            if(manufacturer != null){
            	istn.setManufacturer(manufacturer);
            }
            db.store(istn);
//            DBQuery.queryAll(db);
        } else {
            System.out.println("û�м������κμ�¼.");
        }

    }

    public static void main(String[] args) {
        ObjectContainer db = Db4oEmbedded.openFile(Constants.DB4O_FILENAME);
        int n = 1008;
        String sampleId = null;
        String name = null;
        String specification = null;
        String manufacturer = "ͳһ";
        ObjectSet<InstantNoodles> set = db.queryByExample(new InstantNoodles(n));
        DBQuery.listResult(set);
        update(db,n,sampleId, name, specification , manufacturer);
        DBQuery.listResult(set);
        db.close();
    }
}