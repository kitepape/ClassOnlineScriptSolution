import os

class Person:
    def __init__(self, s1=None, s2=None, s3=None, s4=None):
        self.username = s1
        self.account = s2
        self.password = s3
        self.web_address = s4

    # 定义magic function使得类对象返回账号，密码，网站三个变量
    def __getitem__(self, n):
        swith = {"username": self.username, "account": self.account,
                 "password": self.password, "web_address": self.web_address}
        return swith[n]

    # 定义函数save，保存账密
    def save(self):
        if not os.path.exists("./information"):
            os.mkdir("./information")
        if os.path.exists("./information/{}.txt".format(self.username)):
            os.remove("./information/{}.txt".format(self.username))
        with open("./information/{}.txt".format(self.username), "w") as f:
            f.write("username${}\naccount${}\npassword${}\nweb${}".format(
                self.username, self.account, self.password, self.web_address))
        print("保存成功！")

    def change(self, element):
        self.read()
        os.remove("./information/{}.txt".format(self.username))
        if element == "account":
            self.account = input("请输入新的账号：")
            self.save()
        elif element == "password":
            self.password = input("请输入新的密码：")
            self.save()
        elif element == "web":
            self.web_address = input("请输入新的网址：")
            self.save()
        print("修改成功！")


    def read(self):
        with open("./information/{}.txt".format(self.username), "r") as f:
            text = f.read().split("\n")
        for jk in text:
            if "username" in jk:
                self.username = jk.split("$")[1]
            elif "account" in jk:
                self.account = jk.split("$")[1]
            elif "password" in jk:
                self.password = jk.split("$")[1]
            elif "web" in jk:
                self.web_address = jk.split("$")[1]

def login(select):
    p = Person()
    if select == "1":
        p.username = input("请输入用户名：")
        p.account = input("请输入账号：")
        p.password = input("请输入密码：")
        p.web_address = input("请输入网址：")
        p.save()
        print("保存成功!\n如果需要登录请输入1，如果想要退出程序请输入0")
        se = input("请输入：")
        if se == "1":
            pass
        elif se == "0":
            raise SystemExit
    elif select == "2":
        p.username = input("请输入用户名：")
        p.read()
    elif select == "3":
        p.account = input("请输入账号：")
        p.password = input("请输入密码：")
        p.web_address = input("请输入网址：")
    elif select == "4":
        p.username = input("请输入用户名：")
        p.read()
        print("修改账号请输入1，修改密码请输入2，修改网址请输入3")
        select = input("请输入：")
        if select == "1":
            p.change("account")
        elif select == "2":
            p.change("password")
        elif select == "3":
            p.change("web")
    return p
