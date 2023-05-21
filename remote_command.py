#coding=utf-8
# 功能：通过python程序 远程执行命令
# 编写者：俺

import paramiko, time

def ssh(hostname, username, password, ):
    command = input('请输入需要执行的命令:')
    # 第一步：通过类SSHClint创建一个SSH_Client客户端对象
    SSH_Client = paramiko.SSHClient()
    # 第二步：自动接收服务器发来的密钥(模拟手工输入的yes)
    SSH_Client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    try:  # 第三步：连接服务器
        SSH_Client.connect(hostname=hostname, username=username, password=password, port=22)
    except paramiko.ssh_exception.AuthenticationException:
        print("服务器账号或密码错误")
        exit(1)
    except Exception as error:
        print(f"服务器连接错误 原因是{error}")
        exit(1)
    xshell = SSH_Client.invoke_shell()  # 第四步：激活终端
    xshell.send(f"{command}\n")  # 第五步：通过激活终端发送(send)指令
    time.sleep(1)
    print(xshell.recv(65535).decode(encoding="utf-8"))  # 第六步：通过激活终端接收（recv）数据
    SSH_Client.close()


def sftp(hostname, username, password):
    # 第一步 新建会话
    src_file = input("请输入源文件的文件路径：")
    dst_file = input("请输入目的的文件路径：")
    try:
        SSH_transport = paramiko.Transport(hostname, 22)
    except Exception as error:
        print(f"服务器连接错误 原因是{error}")
        exit(1)
    # 第二步 通过会话连接
    try:
        SSH_transport.connect(username=username, password=password)
    except paramiko.ssh_exception.AuthenticationException:
        print("服务器账号或密码错误")
        exit(1)
    except Exception as error:
        print(f"服务器连接错误 原因是{error}")
        exit(1)
    # 第三步 创建客户端
    ssh_SFTP = paramiko.SFTPClient.from_transport(SSH_transport)
    # 第四步 上传文件
    #ssh_SFTP.put(src_file, dst_file)
    # 第五步 改名
    #ssh_SFTP.rename(src_file, dst_file)
    # 第六步 下载文件
    #ssh_SFTP.get(dst_file, src_file)
    print("操作成功")
    SSH_transport.close()


if __name__ == '__main__':
    ip = input("请输入需要连接的ip地址:")
    username = input("请输入用户名:")
    password = input("请输入密码:")
    user_input = input("1.ssh连接:\n2.sftp连接:\n")
    if user_input == '1':
        print(f"\n{'*' * 50}")
        ssh(ip, username, password)
    elif user_input == '2':
        print(f"\n{'*' * 50}")
        sftp(ip, username, password)
    else:
        exit(1)