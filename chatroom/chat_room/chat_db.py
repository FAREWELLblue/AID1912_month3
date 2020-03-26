"""
服务端
数据处理部分
"""

import pymysql

class Database:
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 3306
        self.user = 'root'
        self.password = '123456'
        self.charset='utf8'
        self.database = 'chatroom'
        self.connect_database()

    def connect_database(self):
        self.db = pymysql.connect(host = self.host,
                                  port = self.port,
                                  user = self.user,
                                  password =self.password,
                                  database = self.database,
                                  charset = self.charset)
        self.create_cursor()

    def create_cursor(self):
        self.cur = self.db.cursor()

    # 帮 server 处理注册 成功 True 失败返回 False
    def register(self,name,passwd,email=''):
        # 判断这个姓名的用户是否存在
        if passwd=='':
            sql = "select * from user where username = %s;"
            self.cur.execute(sql,[name])
            r = self.cur.fetchone() # 如果查询到了说明该用户已经存在
            print(r)
            if r:
                print(r)
                return False  # 不可注册
            else:
                return True
        else:
            # 插入数据库
            try:
                sql = "insert into user (username,password,email) values (%s,%s,%s);"
                print(name,passwd,email)
                self.cur.execute(sql,[name,passwd,email])
                self.db.commit()
                return True
            except:
                self.db.rollback()
                return False

    # 处理登录
    def login(self,name,passwd):
        sql = "select id from user where username=%s and password=%s;"
        self.cur.execute(sql,[name,passwd])
        r = self.cur.fetchone()
        if r:
            return r
        else:
            return False

    # 查询聊天室列表
    def query_room_list(self):
        sql="flush privileges;"
        self.cur.execute(sql)
        sql = "select r_id,rname,introduce,username from room_list as r, user as u where r.r_owner_id = u.id;"
        self.cur.execute(sql)
        r = self.cur.fetchall()
        if r:
            return r
        else:
            return '当前没有聊天室'

    # 新建聊天室
    def insert_chat_room(self,r_name,r_intro,username):
        sql = "insert into room_list (rname,introduce,r_owner_id) values(%s,%s,(select id from user where username=%s));"

        try:
            self.cur.execute(sql,[r_name,r_intro,username])
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            self.db.rollback()
            return False

    # 聊天记录入库
    def insert_chat_record(self,u_name,mes,time,r_name):
        sql="insert into chat_record (content,time,r_id,u_id) values (%s,%s,(select r_id from room_list where rname= %s ),(select id from user where username=%s));"
        try:
            self.cur.execute(sql,[mes,time,r_name,u_name])
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            self.db.rollback()
            return False
