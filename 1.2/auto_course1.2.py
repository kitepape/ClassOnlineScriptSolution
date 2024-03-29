from time import sleep
from webObject import web
from selenium.common.exceptions import NoSuchElementException
from person import login
def execute(user):
    wd = web(user["account"], user["password"], user["web_address"])
    wd.confirm()
    video_nums = wd.get_video_num()
    start_place = int(input("从第几个视频开始？请输入序列号："))
    for i in range(start_place - 1, video_nums):
        try:
            sleep(1)
            wd.click_video(i)
            sleep(1)
            for k in range(int(wd.wait_video_time())):
                sleep(1)
                print("\r视频播放中，还剩{}秒".format(
                    int(wd.wait_video_time()) - k - 1), end="")

            wd.webdriver.switch_to.default_content()
        except NoSuchElementException:
            print("章节测验，已跳过")
            wd.webdriver.switch_to.default_content()
            continue
        print("\n已返回主界面，准备播放下一个视频")
    wd.webdriver.quit()
if __name__ == '__main__':
    user = login()
    execute(user)