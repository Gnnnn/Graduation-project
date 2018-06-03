package com.lsw.tool;

import com.db4o.Db4oEmbedded;
import com.db4o.ObjectContainer;
import com.lsw.bean.InstantNoodles;
import com.lsw.util.Constants;

public class DBInsert {

    public static void main(String[] args) {
        // �����ݿ�
        ObjectContainer db = Db4oEmbedded.openFile(Db4oEmbedded.newConfiguration(), Constants.DB4O_FILENAME);
        try {
            // ���� People ����
        	InstantNoodles istn1 = new InstantNoodles(1001);
        	istn1.setSampleId("20070528761");
        	istn1.setName("�Ҷ�ʱ��");
        	istn1.setSpecification("��װ75g");
        	istn1.setManufacturer("��ȵ���");
            db.store(istn1);
            InstantNoodles istn2 = new InstantNoodles(1002, "20070810671", "������ţ��", "��װ75g", "��ȵ���");
            db.store(istn2);
            InstantNoodles istn3 = new InstantNoodles(1003, "BJ20071025262", "�����Ź�", "��װ75g", "��ȵ���");
            db.store(istn3);
            InstantNoodles istn4 = new InstantNoodles(1004, "2007100312", "�Ҷ�ʱ��", "��װ75g", "��ȵ���");
            db.store(istn4);
            InstantNoodles istn5 = new InstantNoodles(1005, "20070917561", "���ʰ���", "��װ75g", "��ȵ���");
            db.store(istn5);
            InstantNoodles istn6 = new InstantNoodles(1006, "20070810671", "������ţ��", "��װ75g", "��ȵ���");
            db.store(istn6);
            InstantNoodles istn7 = new InstantNoodles(1007, "2007092612", "����ԭ֭ţ��", "��װ75g", "��ȵ���");
            db.store(istn7);
            InstantNoodles istn8 = new InstantNoodles(1008, "200706201035", "�Ĵ�����ţ��ζ", "��װ75g", "������");
            db.store(istn8);
            System.out.println("������ɡ�");
            
        } finally {
            // �ر�����
            db.close();
        }
    }

}