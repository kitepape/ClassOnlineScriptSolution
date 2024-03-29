import tkinter
import tkinter as tk
from person import Person
from tkinter import messagebox

class App():
    def __init__(self):
        self.p = Person()
        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.root.title("用户登录界面")

        # 创建一个标签
        self.label = tk.Label(self.root, text="请选择操作:",font="Verdana 20 underline")
        self.label.pack()

        # 创建按钮 - 保存账号密码以及课程网站
        self.save_button = tk.Button(self.root, text="保存账号密码以及课程网站",
                                     font="Verdana 20 underline",command=self.save)
        self.save_button.pack()

        # 创建按钮 - 账户登录
        self.login_button = tk.Button(self.root, text="账户登录",
                                      font="Verdana 20 underline", command=self.user_login)
        self.login_button.pack()

        # 创建按钮 - 直接登录
        self.direct_login_button = tk.Button(self.root, text="直接登录",
                                             font="Verdana 20 underline",command=self.direct_login)
        self.direct_login_button.pack()

        # 创建按钮 - 修改账号
        self.modify_button = tk.Button(self.root, text="修改账号",
                                       font="Verdana 20 underline", command=self.change)
        self.modify_button.pack()
        self.root.mainloop()
    def save(self):
        # 在这里调用 login 函数的适当部分，根据用户选择的操作执行相应的代码
        self.root.destroy()
        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.root.title("保存账号密码以及课程网站")
        self.label = tk.Label(self.root, text="请输入账号密码以及课程网站:",
                              font = "Verdana 20 underline")
        self.label.pack()

        self.frame0 = tk.Frame(self.root, width=800, height=100, relief="sunken",
                               borderwidth=2)
        self.frame0.pack()
        self.label00 = tk.Label(self.frame0, text="用户:", font="Verdana 16 underline")
        self.label00.pack(padx=5, pady=40,side=tk.LEFT)
        self.entry0 = tk.Entry(self.frame0, width=40, font="Verdana 16 underline")
        self.entry0.insert(0, "username")
        self.entry0.pack(padx=5, pady=40)

        self.frame1 = tk.Frame(self.root, width=800, height=100, relief="sunken",
                               borderwidth=2)
        self.frame1.pack()
        self.label01 = tk.Label(self.frame1, text="账号:", font="Verdana 16 underline")
        self.label01.pack(padx=5, pady=40, side=tk.LEFT)
        self.entry1 = tk.Entry(self.frame1, width=40, font="Verdana 16 underline")
        self.entry1.insert(0, "account")
        self.entry1.pack(padx=5, pady=40)

        self.frame2 = tk.Frame(self.root, width=800, height=100, relief="sunken",
                               borderwidth=2)
        self.frame2.pack()
        self.label02 = tk.Label(self.frame2, text="密码:", font="Verdana 16 underline")
        self.label02.pack(padx=5, pady=40, side=tk.LEFT)
        self.entry2 = tk.Entry(self.frame2, width=40, font="Verdana 16 underline")
        self.entry2.insert(0, "password")
        self.entry2.pack(padx=5, pady=40)

        self.frame3 = tk.Frame(self.root, width=800, height=100, relief="sunken",
                                 borderwidth=2)
        self.frame3.pack()
        self.label03 = tk.Label(self.frame3, text="网站:", font="Verdana 16 underline")
        self.label03.pack(padx=5, pady=40, side=tk.LEFT)
        self.entry3 = tk.Entry(self.frame3, width=40, font="Verdana 16 underline")
        self.entry3.insert(0, "web_address")
        self.entry3.pack(padx=5, pady=40)

        self.button1 = tk.Button(self.root, text="提交",width=20, font="Verdana 16 underline",
                                bd=4, bg="light blue", command=self.get_it_save)
        self.button1.pack(padx=20)
        self.button2 = tk.Button(self.root, text="返回", width=20, font="Verdana 16 underline",
                                bd=4, bg="light blue", command=self.first_return)
        self.button2.pack(padx=20)
        self.root.mainloop()

    def first_return(self):
        self.root.destroy()
        self.__init__()

    def get_it_save(self):
        if self.entry0.get() == "username" or self.entry1.get() == "account" \
                or self.entry2.get() == "password" or self.entry3.get() == "web_address":
            messagebox.showinfo("提示", "请填写完整")
            return
        self.p.username = str(self.entry0.get())
        self.p.account = str(self.entry1.get())
        self.p.password = str(self.entry2.get())
        self.p.web_address = str(self.entry3.get())
        self.p.save()

        self.root.destroy()
        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.root.title("用户登录界面")
        self.btn1 = tk.Button(self.root, text="继续登录",
                              font="Verdana 20 underline",command=self.goin)
        self.btn2 = tk.Button(self.root, text="退出",
                                font="Verdana 20 underline",command=self.exit_app)

        self.btn1.pack()
        self.btn2.pack()

        self.root.mainloop()

    def user_login(self):
        # 在这里调用 login 函数的适当部分，根据用户选择的操作执行相应的代码
        self.root.destroy()
        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.root.title("用户登录界面")

        self.frame = tk.Frame(self.root, width=800, height=100, relief="sunken",
                                borderwidth=2)
        self.frame.pack()
        self.label = tk.Label(self.frame, text="请输入用户名:", font="Verdana 20 underline")
        self.label.pack(padx=5, pady=40, side=tk.LEFT)
        self.l_entry = tk.Entry(self.frame, width=40, font="Verdana 16 underline")
        self.l_entry.insert(0, "username")
        self.l_entry.pack(padx=5, pady=40)

        self.l_button1 = tk.Button(self.root, text="登录", width=20, font="Verdana 16 underline",
                                bd=4, bg="light blue", command=self.get_it_login)
        self.l_button1.pack()

        self.l_button2 = tk.Button(self.root, text="返回", width=20, font="Verdana 16 underline",
                                bd=4, bg="light blue", command=self.first_return)
        self.l_button2.pack()
        self.root.mainloop()

    def get_it_login(self):
        if self.l_entry.get() == "username":
            messagebox.showinfo("提示", "请填写完整")
            return
        self.p.username = self.l_entry.get()
        self.p.read()
        self.root.destroy()
        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.root.title("用户登录界面")

        self.btn1 = tk.Button(self.root, text="继续登录",
                              font="Verdana 20 underline",command=self.goin)
        self.btn2 = tk.Button(self.root, text="退出",
                                font="Verdana 20 underline",command=self.exit_app)

        self.btn1.pack()
        self.btn2.pack()

        self.root.mainloop()
    def direct_login(self):
        # 在这里调用 login 函数的适当部分，根据用户选择的操作执行相应的代码
        self.root.destroy()
        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.root.title("直接登录")
        self.label = tk.Label(self.root, text="请输入账号密码以及课程网站:")
        self.label.pack()

        self.frame1 = tk.Frame(self.root, width=800, height=100, relief="sunken",
                                borderwidth=2)
        self.frame1.pack()
        self.label01 = tk.Label(self.frame1, text="账号:", font="Verdana 16 underline")
        self.label01.pack(padx=5, pady=40, side=tk.LEFT)
        self.entry1 = tk.Entry(self.frame1, width=40, font="Verdana 16 underline")
        self.entry1.insert(0, "account")
        self.entry1.pack(padx=5, pady=40)

        self.frame2 = tk.Frame(self.root, width=800, height=100, relief="sunken",
                                borderwidth=2)
        self.frame2.pack()
        self.label02 = tk.Label(self.frame2, text="密码:", font="Verdana 16 underline")
        self.label02.pack(padx=5, pady=40, side=tk.LEFT)
        self.entry2 = tk.Entry(self.frame2, width=40, font="Verdana 16 underline")
        self.entry2.insert(0, "password")
        self.entry2.pack(padx=5, pady=40)

        self.frame3 = tk.Frame(self.root, width=800, height=100, relief="sunken",
                                borderwidth=2)
        self.frame3.pack()
        self.label03 = tk.Label(self.frame3, text="网站:", font="Verdana 16 underline")
        self.label03.pack(padx=5, pady=40, side=tk.LEFT)
        self.entry3 = tk.Entry(self.frame3, width=40, font="Verdana 16 underline")
        self.entry3.insert(0, "web_address")
        self.entry3.pack(padx=5, pady=40)

        self.button = tk.Button(self.root, text="提交", width=20, font="Verdana 16 underline",
                                bd=4, bg="light blue", command=self.get_it_direct)
        self.button.pack()

        self.buttonp = tk.Button(self.root, text="返回", width=20, font="Verdana 16 underline",
                                bd=4, bg="light blue", command=self.first_return)
        self.buttonp.pack()
        self.root.mainloop()

    def get_it_direct(self):
        if self.entry1.get() == "account":
            messagebox.showinfo("提示", "请将账号填写完整")
            return
        elif self.entry2.get() == "password":
            messagebox.showinfo("提示", "请将密码填写完整")
            return
        elif self.entry3.get() == "web_address":
            messagebox.showinfo("提示", "请将网址填写完整")
            return
        self.p.account = str(self.entry1.get())
        self.p.password = str(self.entry2.get())
        self.p.web_address = str(self.entry3.get())

        self.root.destroy()
        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.root.title("用户登录界面")
        self.btn1 = tk.Button(self.root, text="继续登录",
                              font="Verdana 20 underline",command=self.goin)
        self.btn2 = tk.Button(self.root, text="退出",
                                font="Verdana 20 underline",command=self.exit_app)

        self.btn1.pack()
        self.btn2.pack()

        self.root.mainloop()

    def change(self):
        # 在这里调用 login 函数的适当部分，根据用户选择的操作执行相应的代码
        self.root.destroy()
        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.root.title("修改账号密码")

        self.frame0 = tk.Frame(self.root, width=800, relief="sunken",
                                borderwidth=2)
        self.frame0.pack()
        self.label0 = tk.Label(self.frame0, text="请输入用户:", font="Verdana 16 underline")
        self.label0.pack(padx=5, pady=20, side=tk.LEFT)
        self.entry0 = tk.Entry(self.frame0, width=40, font="Verdana 16 underline")
        self.entry0.insert(0, "username")
        self.entry0.pack(padx=5, pady=20)

        self.labelk = tk.Label(self.root, text="以下三项，需要修改哪项填写哪项，随后点击按钮：",
                               font="Verdana 16 underline")
        self.labelk.pack(padx=5, pady=20)

        self.frame1 = tk.Frame(self.root, width=800, relief="sunken",
                                borderwidth=2)
        self.frame1.pack()
        self.label1 = tk.Label(self.frame1, text="账号:", font="Verdana 16 underline")
        self.label1.pack(padx=5, pady=5, side=tk.LEFT)
        self.entry1 = tk.Entry(self.frame1, width=40, font="Verdana 16 underline")
        self.entry1.insert(0, "account")
        self.entry1.pack(padx=5, pady=20)

        self.Button1 = tk.Button(self.root, text="修改账号",width=40,
                                 font="Verdana 16 underline",command=self.change_account)
        self.Button1.pack(padx=5, pady=5)

        self.frame2 = tk.Frame(self.root, width=800, relief="sunken",
                                borderwidth=2)
        self.frame2.pack()
        self.label2 = tk.Label(self.frame2, text="密码:", font="Verdana 16 underline")
        self.label2.pack(padx=5, pady=20, side=tk.LEFT)
        self.entry2 = tk.Entry(self.frame2, width=40, font="Verdana 16 underline")
        self.entry2.insert(0, "password")
        self.entry2.pack(padx=5, pady=20)

        self.Button2 = tk.Button(self.root, text="修改密码", width=40,
                                 font="Verdana 16 underline", command=self.change_password)
        self.Button2.pack(padx=5, pady=5)

        self.frame3 = tk.Frame(self.root, width=800, relief="sunken",
                                borderwidth=2)
        self.frame3.pack()
        self.label3 = tk.Label(self.frame3, text="网站:", font="Verdana 16 underline")
        self.label3.pack(padx=5, pady=20, side=tk.LEFT)
        self.entry3 = tk.Entry(self.frame3, width=40, font="Verdana 16 underline")
        self.entry3.insert(0, "web_address")
        self.entry3.pack(padx=5, pady=20)

        self.Button3 = tk.Button(self.root, text="修改网址", width=40,
                                 font="Verdana 16 underline", command=self.change_url)
        self.Button3.pack(padx=5, pady=5)

        self.buttonp = tk.Button(self.root, text="返回", width=20, font="Verdana 16 underline",
                                bd=4, bg="light blue", command=self.first_return)
        self.buttonp.pack()

        self.root.mainloop()

    def change_account(self):
        if self.entry1.get() == "account":
            messagebox.showinfo("提示", "请填写账号")
            return
        elif self.entry0.get() == "username":
            messagebox.showinfo("提示", "请填写用户名")
            return
        self.p.username = str(self.entry0.get())
        self.p.read()
        self.p.account = str(self.entry1.get())
        self.p.save()

        self.root.destroy()
        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.root.title("用户登录界面")

        self.btn1 = tk.Button(self.root, text="继续登录",
                              font="Verdana 20 underline",command=self.goin)
        self.btn2 = tk.Button(self.root, text="退出",
                                font="Verdana 20 underline",command=self.exit_app)

        self.btn1.pack()
        self.btn2.pack()

        self.root.mainloop()

    def change_password(self):
        if self.entry2.get() == "password":
            messagebox.showinfo("提示", "请填写密码")
            return
        elif self.entry0.get() == "username":
            messagebox.showinfo("提示", "请填写用户名")
            return
        self.p.username = str(self.entry0.get())
        self.p.read()
        self.p.password = str(self.entry2.get())
        self.p.save()

        self.root.destroy()
        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.root.title("用户登录界面")

        self.btn1 = tk.Button(self.root, text="继续登录",
                              font="Verdana 20 underline",command=self.goin)
        self.btn2 = tk.Button(self.root, text="退出",
                                font="Verdana 20 underline",command=self.exit_app)

        self.btn1.pack()
        self.btn2.pack()

        self.root.mainloop()

    def change_url(self):
        if self.entry3.get() == "web_address":
            messagebox.showinfo("提示", "请填写网址")
            return
        elif self.entry0.get() == "username":
            messagebox.showinfo("提示", "请填写用户名")
            return
        self.p.username = str(self.entry0.get())
        self.p.read()
        self.p.web_address = str(self.entry3.get())
        self.p.save()

        self.root.destroy()
        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.root.title("用户登录界面")

        self.btn1 = tk.Button(self.root, text="继续登录",
                              font="Verdana 20 underline",command=self.goin)
        self.btn2 = tk.Button(self.root, text="退出",
                                font="Verdana 20 underline",command=self.exit_app)

        self.btn1.pack()
        self.btn2.pack()

        self.root.mainloop()
    def goin(self):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.root.title("用户操作界面")

        self.label = tk.Label(self.root, text="第几节课程开始？", font="Verdana 20 underline")
        self.label.pack(padx=5, pady=20)

        self.entry = tk.Entry(self.root, width=40, font="Verdana 16 underline")
        self.entry.insert(0, "1")
        self.entry.pack(padx=5, pady=5)

        self.var1 = tk.StringVar()
        self.var1.set("还有多少秒，可莉不知道哦~")
        self.var2 = tk.StringVar()
        self.var2.set("现在是第几个视频，可莉不知道哦~")
        self.var3 = tk.StringVar()
        self.var3.set("现在是什么状态，可莉不知道哦~")
        self.label1 = tk.Label(self.root, textvariable=self.var1, font="Verdana 20 underline")
        self.label1.pack(padx=5, pady=5)
        self.label2 = tk.Label(self.root, textvariable=self.var2, font="Verdana 20 underline")
        self.label2.pack(padx=5, pady=5)
        self.label3 = tk.Label(self.root, textvariable=self.var3, font="Verdana 20 underline")
        self.label3.pack(padx=5, pady=5)
        self.btn1 = tk.Button(self.root, text="开始", font="Verdana 20 underline",
                              command=self.thread_execute)
        self.btn1.pack(padx=5, pady=5)

        self.root.mainloop()

    def thread_execute(self):
        import threading
        t = threading.Thread(target=self.execute)
        t.start()
    def execute(self):
        from time import sleep
        from webObject import web
        from selenium.common.exceptions import NoSuchElementException
        wd = web(self.p["account"], self.p["password"], self.p["web_address"])
        wd.confirm()
        video_nums = wd.get_video_num()
        try:
            start_place = int(self.entry.get())
        except ValueError:
            messagebox.showerror("错误", "请输入数字")
            return
        for i in range(start_place - 1, video_nums):
            try:
                self.var2.set("现在是第{}个视频".format(i + 1))
                sleep(1)
                wd.click_video(i)
                sleep(1)
                for k in range(int(wd.wait_video_time())):
                    sleep(1)
                    self.var1.set("\r视频播放中，还剩{}秒".format(
                        int(wd.wait_video_time()) - k - 1))
                self.var3.set("视频播放完毕，准备返回主界面")
                wd.webdriver.switch_to.default_content()
            except NoSuchElementException:
                self.var3.set("章节测验，已跳过")
                wd.webdriver.switch_to.default_content()
                continue
            self.var3.set("已返回主界面，准备播放下一个视频")
        wd.webdriver.quit()
        self.var3.set("所有视频已播放完毕，程序即将退出")
    def exit_app(self):
        if messagebox.askokcancel("退出", "您确定要退出吗?"):
            self.root.destroy()

if __name__ == "__main__":
    app = App()