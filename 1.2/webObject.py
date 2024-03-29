from random import uniform
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


class web:
    def __init__(self, account, password, up_url):
        self.webdriver = webdriver.Chrome()
        self.webdriver.implicitly_wait(2)
        self.webdriver.get(up_url)
        self.webdriver.find_element(By.ID,"phone").send_keys(account)
        self.webdriver.find_element(By.ID,"pwd").send_keys(password)
        self.webdriver.find_element(By.ID,"loginBtn").click()
        sleep(0.5)

    def confirm(self):
        sleep(1)
        self.webdriver.find_element(By.CSS_SELECTOR,"body div div div .backOld").click()
        if "首页" in self.webdriver.title:
            ll = list(self.webdriver.find_elements(By.TAG_NAME, "a"))
            for i in ll:
                if i.get_attribute("href") != None and i.get_attribute("style") == "display: inline-block; width: 562px;":
                    i.click()
                    break
            sleep(0.5)
        else:
            pass

    def get_video_num(self):
        sleep(0.2)
        nd = self.webdriver.find_elements(By.CSS_SELECTOR,".onetoone div .ncells a")
        return len(nd)

    def get_iframes_TAG(self):
        sleep(0.2)
        return self.webdriver.find_elements(By.TAG_NAME, "iframe")

    def get_iframes_ID(self):
        sleep(0.2)
        return self.webdriver.find_elements(By.ID, "iframe")

    def confirm_iframe(self):
        sleep(0.2)
        try: self.webdriver.find_element(By.CSS_SELECTOR, "#video > .vjs-big-play-button")
        except: return False
        return True
    # 播放第i个视频
    def click_video(self, index):
        sleep(0.2)
        # cd为视频列表
        cd = self.webdriver.find_elements(By.CSS_SELECTOR, ".onetoone div .ncells a")
        if cd == []:
            cd = self.webdriver.find_elements(By.CSS_SELECTOR, ".onetoone div .ncells h4")
        cd[index].click()
        Iframes = self.get_iframes_ID()
        for i in range(len(Iframes)):
            self.webdriver.switch_to.frame(self.get_iframes_ID()[i])
            Iframes2 = self.get_iframes_TAG()
            for j in range(len(Iframes2)):
                    self.webdriver.switch_to.frame(self.get_iframes_TAG()[j])
                    if self.confirm_iframe():
                        self.webdriver.find_element(By.CSS_SELECTOR, "#video > .vjs-big-play-button").click()

    def wait_video_time(self):
        sleep(0.2)
        while True:
            fd = self.webdriver.find_element(By.CSS_SELECTOR, ".vjs-duration-display")
            test = fd.get_attribute("textContent")
            test = test.split(":")
            if test[0] != "0" or test[1] !="00":
                break
            else:
                sleep(1)
        video_time = int(test[0]) * 60 + int(test[1])
        return video_time