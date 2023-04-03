# coding=utf-8
# 功能：实现银行业务开户、销户、存款、取款和查询余额等功能
# 编写者：俺
# 时间：2023年4月2日

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

    def delete_user(self):
        print("————销户系统————")
        cr = self.db_conn.cursor()
        delete_sql = f"delete from `bank` \
            where card_name='{self.card_name}' and card_password='{self.card_password}' and card_money=0;"
        # 删除数据
        result = cr.execute(delete_sql)
        self.db_conn.commit()
        if result == 0:
            print('销户失败,请检查输入')
            cr.close()
            self.db_conn.close()
            exit(1)
        print(f'用户 {self.card_name} 销户成功')

    def save_money(self):
        print("————存款系统————")
        cr = self.db_conn.cursor()
        save_sql = f"update `bank` set card_money=card_money+{self.card_money} \
            where card_name='{self.card_name}' and card_password='{self.card_password}';"
        # 余额加上输入的金额
        result = cr.execute(save_sql)
        self.db_conn.commit()
        if result == 0:
            print('存款失败,请检查输入')
            cr.close()
            self.db_conn.close()
            exit(1)
        print(f'用户{self.card_name}存款 {self.card_money}元 成功')
        cr.close()
        self.db_conn.close()

    def get_money(self):
        print("————取款系统————")
        cr = self.db_conn.cursor()
        get_sql = f"update `bank` set card_money=card_money-{self.card_money} \
            where card_name='{self.card_name}' and card_password='{self.card_password}';"
        # 余额减去输入的金额
        result = cr.execute(get_sql)
        self.db_conn.commit()
        if result == 0:
            print('取款失败,请检查输入')
            cr.close()
            self.db_conn.close()
            exit(1)
        print(f'用户{self.card_name}取款 {self.card_money}元 成功')
        cr.close()
        self.db_conn.close()

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
        print("\n1.开户\n2.销户\n3.存款\n4.取款\n5.查询\n6.创建数据表\n0.退出\n")
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
        elif user_input == '3':
            user_name = input('请输入用户名')
            user_password = input('请输入密码')
            user_money = input('请输入存款金额')
            user_info = bank(card_name=user_name, card_password=user_password, card_money=user_money)
            user_info.save_money()
        elif user_input == '4':
            user_name = input('请输入用户名')
            user_password = input('请输入密码')
            user_money = input('请输入存款金额')
            user_info = bank(card_name=user_name, card_password=user_password, card_money=user_money)
            user_info.get_money()
        elif user_input == '5':
            user_name = input('请输入查询用户名')
            user_password = input('请输入密码')
            user_info = bank(card_name=user_name, card_password=user_password, card_money=None)
            user_info.search_money()
        elif user_input == 'config':
            user_name = input('请输入创建的用户数据表名:')
            user_info = bank(card_name=user_name, card_password=None, card_money=None)
            user_info.create_table()
        elif user_input == '0':
            print("————欢迎下次使用————")
            break