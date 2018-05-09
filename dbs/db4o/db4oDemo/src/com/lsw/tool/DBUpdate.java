package com.lsw.tool;

import java.util.List;

import com.db4o.Db4oEmbedded;
import com.db4o.ObjectContainer;
import com.lsw.bean.People;
import com.lsw.util.Constants;

public class DBUpdate {
    /**
     * ���ºͼ������붼�ȰѶ����������Ȼ����в���
     * @param db
     */
    public static void update(ObjectContainer db) {
        List<People> result = db.queryByExample(new People(1));
        People people; // �������ID���������һ�����
        if (result != null && result.size() > 0) {// �м������
            people = result.get(0);
            System.out.println("����ǰ��ֵ��" + people);
            // ����������¼
            people.setId(4);
            people.setName("��˼");
            people.setAddress("�벩");
            db.store(people);
            // �鿴���º�Ľ��
            DBQuery.queryAll(db);
        } else {
            System.out.println("û�м������κμ�¼.");
        }

    }

    public static void main(String[] args) {
        ObjectContainer db = Db4oEmbedded.openFile(Constants.DB4O_FILENAME);
        update(db);
        db.close();
    }
}