import datetime

import pytest

from Library.configure import Configuration
from Library.read_exel import ReadExcel

from POM.facebook_msg import Fbmsg


class TestFbmsg:

    td = ReadExcel()
    data = td.login_details()

    @pytest.mark.parametrize("u_name, pswd, theme, msg_, emojiid", data)
    def test_msg(self, u_name, pswd, theme, msg_, emojiid, init_driver):
        driver = init_driver
        try:
            n = Fbmsg(init_driver)
            n.enter_username(u_name)
            n.enter_pswd(pswd)
            n.click_on_longin()
            n.click_on_msg_icon()
            n.click_on_anychat()
            n.send_msg(msg_)
            n.log_out()

        except BaseException as msg:
            td = datetime.datetime.now()
            name = f"screenshot_{td.date()}_{td.hour}_{td.minute}_{td.second}.png"
            driver.save_screenshot(Configuration.SCREENSHOT_PATH+name)
            raise msg
