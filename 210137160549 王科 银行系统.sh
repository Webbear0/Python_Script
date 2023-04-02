#!/bin/bash
# 功能:实现银行业务开户、销户、存款、取款和查询余额等功能
# 编写日期:2023/4/2
# 编写者:王科

read -p "请输入数据库地址:" host_name
read -p "请输入数据库用户名:" sql_username
read -p "请输入数据库密码:" sql_passwd

while true 
do 
	cat <<EOF
----欢迎使用银行系统----
输入0初始化数据库
输入1开户
输入2销户
输入3存款
输入4取款
输入5查询
EOF
	read -p '请输入序号,取消运行输入其他字符' input
	case $input in
    "0")
        mysql -h${host_name} -u${sql_username} -p${sql_passwd} <<EOF
create database bank;
use bank;
create table bank(
card_id int(8) zerofill not null primary key auto_increment comment '卡号',
card_name varchar(8) not null unique key comment '持卡人',
card_password varchar(16) not null default '88888888' comment '卡密码',
card_money float(32) not null default 0 comment '余额'
)charset=utf8;
EOF
        echo "数据库初始化完成"
        ;;
	"1")
        echo "----开户系统----"
        read -p "请输入开户用户名:" user_name
        read -p "请输入密码:" user_password
        mysql -h${host_name} -u${sql_username} -p${sql_passwd} <<EOF
        use bank;
        insert into bank (card_name,card_password) values ('${user_name}','${user_password}');
EOF
        command=${?}
        if [ ${command} != 0 ];then
			echo "开户失败,请检查输入"
            exit 1
        fi 
        echo "用户 ${user_name} 开户成功"
		;;
	"2")
        echo "----销户系统----"
        read -p "请输入用户名:" user_name
        read -p "请输入密码:" user_password
        mysql -h${host_name} -u${sql_username} -p${sql_passwd} <<EOF
        use bank;
        delete from bank where card_name='${user_name}' and card_password='${user_password}' and card_money=0;
EOF
        command=${?}
        if [ ${command} != 0 ];then
			echo "销户失败,请检查输入"
            exit 1 
        fi
        echo "用户 ${user_name} 销户成功"
		;;
	"3")
        echo "----存款系统----"
        read -p "请输入用户名:" user_name
        read -p "请输入密码:" user_password
        read -p "请输入需要存款的金额" user_money
        mysql -h${host_name} -u${sql_username} -p${sql_passwd} <<EOF
        use bank;
        update bank set card_money=card_money+${user_money} where card_name='${user_name}' and card_password='${user_password}';
EOF
        command=${?}
        if [ ${command} != 0 ];then
			echo "存款失败,请检查输入"
            exit 1 
        fi
        echo "用户 ${user_name} 存款 ${user_money}成功"
        ;;
	"4")
        echo "----取款系统----"
        read -p "请输入用户名:" user_name
        read -p "请输入密码:" user_password
        read -p "请输入需要取款的金额:" user_money
        mysql -h${host_name} -u${sql_username} -p${sql_passwd} <<EOF
        use bank;
        update bank set card_money=card_money-${user_money} where card_name='${user_name}' and card_password='${user_password}';
EOF
        command=${?}
        if [ ${command} != 0 ];then
			echo "取款失败,请检查输入"
            exit 1 
        fi
        echo "用户 ${user_name} 取款 ${user_money}成功"
        ;;
	"5")
        echo "----查询系统----"
        read -p "请输入用户名:" user_name
        read -p "请输入密码:" user_password
        mysql -h${host_name} -u${sql_username} -p${sql_passwd} <<EOF
        use bank;
        select card_money from bank where card_name='${user_name}' and card_password='${user_password}';
EOF
        ;;
    *) 
		echo "输入为其他字符,脚本将自动退出"
		exit 0
		;;
	esac
done