import datetime

import pytest

from Library.configure import Configuration
from Library.read_exel import ReadExcel

from POM.facebook_mute import Fbmute


class TestFbmute:

    testdata = ReadExcel()
    data = testdata.mute_login_details()

    @pytest.mark.parametrize("u_name, pswd", data)
    def test_msg(self, u_name, pswd, init_driver):
        driver = init_driver
        try:
            n = Fbmute(init_driver)
            n.enter_username(u_name)
            n.enter_pswd(pswd)
            n.click_on_longin()
            n.click_on_msg_icon()
            n.click_on_anychat()
            n.mute_notification()
            n.unmute_notification()
            n.log_out()

        except BaseException as msg:
            td = datetime.datetime.now()
            name = f"screenshot_{td.date()}_{td.hour}_{td.minute}_{td.second}.png"
            driver.save_screenshot(Configuration.SCREENSHOT_PATH+name)
            raise msg
