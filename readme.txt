��װ������demo��˵��
1.��װ�����Ի���
  1.��װ����Ϊvirtual box 4.2.12 
  2.�����ϵͳΪdebian 7.1 wheely 64bit
  3.���ݿ�ΪPOSTGRESQL 9.1
  4.������ԣ�python 2.7.5 
  5.������������Ŀ⣺
          1.Django-1.6.6
            �ٷ���ַ�� https://www.djangoproject.com
          2.psycopg2-2.5.1
            ������ַ��http://initd.org/psycopg/tarballs/PSYCOPG-2-5/psycopg2-2.5.1.tar.gz
          3.django-rest-framework-2.4.1
            github��ַ��https://github.com/tomchristie/django-rest-framework.git
          
2.��װPOSTGRESQL���ݿ⣬�뿴��postgresql_9.1_install.txt��

3.���г���
   1.ע�⣺
      1.���д�demo����Ҫȷ����Ļ����ϰ�װ��postgresql 9.1�����ݿ�����Ϊtest_db����python���Ժ����������
      2.���δ��װpostgresql���ݿ⣬������sqlite���ݿ⣬���޸�settings.py�ļ�
         ��������δ����޸�Ϊ��Ҫ�����ݿ�
        DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.postgresql_psycopg2',
              'NAME':'test_db',
              'USER':'postgres',
              'PASSWORD':'postgres',
              'HOST':'localhost',
              'PORT':'5432'
          }
        } 
        
    2.��ѹdemo.tar.gz�����Ŀ¼
    3.�޸����ݿ��������ã���ע��2�����еĲ���
    4.�������ݿ���ر�
        1.�л���demo�����Ŀ¼����manage.py��Ŀ¼��
        2.�������ݿ���ر�
        python manage.py syncdb
        3.ע�⣺demo�ı�ṹ�����ܣ��뿴��demo_table_and_sql.txt���ĵ�
    5.���д�demo
    python manage.py runserver
    
4.���Դ�demo�����뿴��test_demo.txt���ĵ�

5.�Ժ��������
    1.������������ַ��Ƿ���ȷ
    2.�����Ƶķ�ʽ���¹�˾����ѯ��˾�����š���˾��Ա
    3.ɾ���ɹ��󣬷�����ʾ��Ϣ
    4.�����ҳ���漰���rest��API��˵���ĵ���
    5.URL��ѯ��ַ����ӷ�ҳ��ѯ����
    6.����