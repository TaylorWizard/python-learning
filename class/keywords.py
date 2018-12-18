class User():
    def __init__(self, frist_name, last_name, others):
        self.frist_name = frist_name
        self.last_name = last_name
        self.others = others

    def describe_user(self):
        messagge = {}
        messagge['frist_name'] = self.frist_name
        messagge['last_name'] = self.last_name
        for key in self.others.keys():
            messagge[key] = self.others[key]
        print('用户信息为：', messagge)

    def greet_name(self):
        print(self.frist_name + self.last_name + '欢迎你！')

class Privileges():
    def __init__(self,*privileges):
        self.privileges=privileges
    def show_privileges(self):
        for x in self.privileges:
            print(x)
class Admin1(User):
    def __init__(self,frist_name,last_name,**others):
        super().__init__(frist_name,last_name, others)
        self.privileges=Privileges('can add post','can delete post')

admin=Admin1('huang','jing',age=23)
admin.privileges.show_privileges()
