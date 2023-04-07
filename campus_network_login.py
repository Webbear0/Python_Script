# coding=utf-8
# 功能：模拟数字校园的‘注册’和‘登录’功能，用数据库存放注册的用户名和密码
# 编写者：俺
# 时间：2023年4月7日

import pymysql

class bank:
    def __init__(self, card_name, card_password, card_money):
        self.db_conn = pymysql.connect(host='', user='',
                                       password="", db="",
                                       charset="utf8", port=3306)
        self.card_name = card_name
        self.card_password = card_password
        self.card_money = card_money

    def create_table(self):
        print("————创建数据表————")
        cr = self.db_conn.cursor()
        try:
            create_table = f"create table {self.card_name}(`card_id` int(8) zerofill not null primary key auto_increment comment '卡号',\
            `card_name` varchar(8) not null unique key comment '持卡人',\
            `card_password` varchar(16) not null default '88888888' comment '卡密码',\
            `card_money` float(32) not null default 0 comment '余额')charset=utf8;"
            cr.execute(create_table)
            # 创建数据表
        except:
            print('输入错误，请重新输入')
            cr.close()
            self.db_conn.close()
            exit(1)
        cr.close()
        self.db_conn.close()
        print("创建成功")

    def create_user(self):
        print("————开户系统————")
        if (len(self.card_name) == 0) or (len(self.card_password) == 0):
            print("输入的值不能为空")
        elif (len(self.card_name) <= 9) or (len(self.card_password) <= 17):
            cr = self.db_conn.cursor()
            try:
                create_sql = f"insert into `bank` (`card_name`,`card_password`,`card_money`) \
                        values ('{self.card_name}','{self.card_password}','{self.card_money}');"
                # 添加数据
                cr.execute(create_sql)
                self.db_conn.commit()
            except:
                print('开户失败，用户已存在')
                cr.close()
                self.db_conn.close()
                exit(1)
            cr.close()
            self.db_conn.close()
        else:
            print('输入的值错误，请重新输入')

    def search_money(self):
        print("————查询系统————")
        cr = self.db_conn.cursor()
        search_sql = f"select card_money from `bank` \
            where card_name='{self.card_name}' and card_password='{self.card_password}';"
        # 查询数据库
        try:
            cr.execute(search_sql)
            result = cr.fetchall()
            print(f"用户 {self.card_name} 的余额为 {result[0]}元")
        except:
            print('查询失败,用户不存在')
            cr.close()
            self.db_conn.close()
            exit(1)
        cr.close()
        self.db_conn.close()


if __name__ == '__main__':
    while True:
        print("\n1.开户\n2.销户\n3.查询\n4.创建数据表\n0.退出\n")
        user_input = input("请选择：")
        if user_input == '1':
            user_name = input('请输入开户用户名:')
            user_password = input('请输入密码:')
            user_info = bank(card_name=user_name, card_password=user_password, card_money=None)
            user_info.create_user()
        elif user_input == '2':
            user_name = input('请输入销户用户名')
            user_password = input('请输入密码')
            user_info = bank(card_name=user_name, card_password=user_password, card_money=None)
            user_info.delete_user()
        elif user_input == 'config':
            user_name = input('请输入创建的用户数据表名:')
            user_info = bank(card_name=user_name, card_password=None, card_money=None)
            user_info.create_table()
        elif user_input == '0':
            print("————欢迎下次使用————")
            break