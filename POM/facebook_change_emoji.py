from Library.read_exel import ReadExcel


class Fbemoji:
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

    def click_on_change_emoji(self):
        locator = self.lo["change_emoji"]
        self.driver.find_element(*locator).click()

    def select_emoji(self, emoji_id):
        if isinstance(emoji_id, float):
            emoji_id = (int(emoji_id))

        locator_name, locator_value = self.lo["select_emoji"]
        self.driver.find_element(locator_name, locator_value.format(emoji_id)).click()

    def log_out(self):
        locator = self.lo["a/control"]
        self.driver.find_element(*locator).click()
        locator1 = self.lo["logout"]
        self.driver.find_element(*locator1).click()
