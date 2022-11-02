import time
from behave import *
from selenium import webdriver


@given(u'user should be login into the application with valid username and password')
def login(context):
    path = r"C:\Users\Nandan K S\PycharmProjects\pythonProject\pythonProject\HTD_facebook\drivers\chromedriver.exe"
    context.driver = webdriver.Chrome(executable_path=path)
    context.driver.maximize_window()
    context.driver.get("https://www.facebook.com/")
    context.driver.implicitly_wait(10)
    context.driver.find_element('id', 'email').send_keys("8660532161")
    context.driver.find_element('id', 'pass').send_keys("#Mn071098")
    context.driver.find_element("name", 'login').click()


@when('user should able to open the messanger')
def open_messanger(context):
    context.driver.find_element("xpath", '//div[@aria-label="Messenger"]').click()
    context.driver.find_element('xpath', '//a[text()="See all in Messenger"]').click()
    context.driver.find_element("xpath", '(//span[text()="moodi"])[1]').click()
    time.sleep(3)


@then('user mute the chat and call for 8 hours')
def mute_chat(context):
    context.driver.find_element('xpath', '//div[@aria-label="Mute notifications"]').click()
    context.driver.find_element('xpath', "//span[contains(text(),'Mute message and call')]").click()
    context.driver.find_element("xpath", "(//span[text()='Next'])[2]").click()
    context.driver.find_element("xpath", "//span[text()='For 8 Hours']").click()
    context.driver.find_element("xpath", "(//span[text()='Mute'])[3]").click()
    time.sleep(3)
    context.driver.find_element('xpath', '//div[@aria-label="Unmute notifications"]').click()
    time.sleep(3)


@then('user logout from the application')
def logout(context):
    context.driver.find_element('xpath', '(//div[@aria-label="Account Controls and Settings"]//div)[1]').click()
    context.driver.find_element('xpath', "//span[text()='Log Out']").click()
    context.driver.quit()


@then('verify send button is displayed')
def verify_send_button(context):
    try:
        send_button = context.driver.find_element('xpath', '//div[@aria-label="Press enter to send"]')
        if send_button.is_displayed():
            print("Fail: Without typing any message Send Button is displayed and verified.")

    except BaseException:
        print("Pass: Without typing any message Send Button is not displayed and verified.")


@then('send a msg to friend as "{message}"')
def send_msg(context, message):
    context.driver.find_element('xpath', '//div[@aria-label="Message"]').send_keys(message)
    context.driver.find_element('xpath', '//div[@aria-label="Press enter to send"]').click()


@then('user change the "{theme}"')
def change_theme(context, theme):
    context.driver.find_element('xpath', "//span[text()='Customize chat']").click()
    context.driver.find_element("xpath", '''//div[@role='button']//span[text()="Change theme"]''').click()
    context.driver.find_element('xpath', f"//div[text()='{theme}']/..").click()
    context.driver.find_element('xpath', "(//span[text()='Save'])[2]").click()


@then('user change the emoji "{emoji}"')
def change_emoji(context, emoji):
    context.driver.find_element('xpath', "//span[text()='Customize chat']").click()
    context.driver.find_element('xpath', "//span[text()='Change emoji']").click()
    context.driver.find_element('xpath', f"(//h3[text()='Smileys & People']/..//img)[{emoji}]").click()
