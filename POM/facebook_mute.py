import time

from Library.read_exel import ReadExcel


class Fbmute:
    rd = ReadExcel()
    lo = rd.chage_theme_locators()

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, u_name):
        if isinstance(u_name, float):
            u_name = str(int(u_name))
        locator = self.lo["uname"]
        self.driver.find_element(*locator).send_keys(u_name)

    def enter_pswd(self, pwd):
        if isinstance(pwd, float):
            pwd = (int(pwd))

        locator = self.lo["password"]
        self.driver.find_element(*locator).send_keys(pwd)

    def click_on_longin(self):
        locator = self.lo["login"]
        self.driver.find_element(*locator).click()

    def click_on_msg_icon(self):
        locator = self.lo["msgicon"]
        self.driver.find_element(*locator).click()
        locator1 = self.lo["see_all_msg"]
        self.driver.find_element(*locator1).click()

    def click_on_anychat(self):
        locator = self.lo["anychat"]
        self.driver.find_element(*locator).click()

    def click_on_customize(self):
        locator = self.lo["cutomize"]
        self.driver.find_element(*locator).click()

    def mute_notification(self):
        locator = self.lo["mute_button"]
        self.driver.find_element(*locator).click()
        locator1 = self.lo["msg_call"]
        self.driver.find_element(*locator1).click()
        locator2 = self.lo["next_button"]
        self.driver.find_element(*locator2).click()
        locator3 = self.lo["mute_time"]
        self.driver.find_element(*locator3).click()
        locator4 = self.lo["confirm_mute"]
        self.driver.find_element(*locator4).click()
        locator5 = self.lo["mute_text"]
        mute_button = self.driver.find_element(*locator5)
        text_when_muted = 'Unmute'
        if mute_button.text == text_when_muted:
            print("PASS: Chat is Muted")
        time.sleep(5)

    def unmute_notification(self):
        locator = self.lo["unmute"]
        self.driver.find_element(*locator).click()
        locator1 = self.lo["unmute_text"]
        unmute_button_text = self.driver.find_element(*locator1)
        time.sleep(5)
        text_when_unmuted = unmute_button_text.text
        if unmute_button_text.text == text_when_unmuted:
            print("PASS: Chat is Unmuted")

    def log_out(self):
        locator = self.lo["a/control"]
        self.driver.find_element(*locator).click()
        locator1 = self.lo["logout"]
        self.driver.find_element(*locator1).click()
