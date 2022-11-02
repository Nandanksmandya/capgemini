import datetime

import pytest

from Library.configure import Configuration
from Library.read_exel import ReadExcel

from POM.facebook_change_emoji import Fbemoji


class TestFbemoji:

    td = ReadExcel()
    data = td.login_details()

    @pytest.mark.parametrize("u_name, pswd, theme, msg_, eid", data)
    def test_real(self, u_name, pswd, theme, msg_, eid, init_driver):
        driver = init_driver
        try:
            n = Fbemoji(init_driver)
            n.enter_username(u_name)
            n.enter_pswd(pswd)
            n.click_on_longin()
            n.click_on_msg_icon()
            n.click_on_anychat()
            n.click_on_customize()
            n.click_on_change_emoji()
            n.select_emoji(eid)
            n.log_out()

        except BaseException as msg:
            td = datetime.datetime.now()
            name = f"screenshot_{td.date()}_{td.hour}_{td.minute}_{td.second}.png"
            driver.save_screenshot(Configuration.SCREENSHOT_PATH+name)
            raise msg
