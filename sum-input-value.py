import json
# 1.读取文件, 取出名字
# 2.判断名字是否为自己的名字, 是就return 名字, 在greet_user打印名字, 反之就让用户重新输入, 再存入文件
#

def get_stored_name():
    """获取已存储的名字"""
    file_name = 'username.json'
    try:
        with open(file_name) as f_obj:
            user_name=json.load(f_obj)
    except FileNotFoundError:
        get_new_name()
    else:
        print('else: ',user_name)
        a=input('这是你的名字吗？是请按Y,否请按N')
        if a=='Y':
            print('yes: ', user_name)
            return user_name
        else:return get_new_name()
def get_new_name():
    """获取新的用户名"""
    file_name = 'username.json'
    name = input('请输入你的名字：')
    with open(file_name,'w') as fil_obj:
        json.dump(name,fil_obj)
    return get_stored_name()
def greet_user():
    """给用户问好"""
    user_name=get_stored_name()
    print('result: ', user_name)
    print('你好：!')
greet_user()