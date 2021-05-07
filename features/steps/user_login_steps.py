from time import sleep

from behave import given, when, then
from selenium.webdriver.chrome.webdriver import WebDriver

from features.pages.trms_home_page import TRMSHomePage


@given(u'The User is on the HTML WebPage')
def get_page(context):
    driver: WebDriver = context.driver
    driver.get('C:/Users/marcl/PycharmProjects/project1/frontend.html')
    sleep(1)


@when(u'The User enters {username} in the input bar')
def enter_user(context, username):
    trms_home: TRMSHomePage = context.trms_home_page
    trms_home.credential_input_bar().send_keys(username)
    sleep(1)


@when(u'The User clicks the Submit Button')
def user_submit(context):
    trms_home: TRMSHomePage = context.trms_home_page
    trms_home.credential_submit().click()
    sleep(1)


@when(u'The User now enters {password} in the input bar')
def enter_password(context, password):
    trms_home: TRMSHomePage = context.trms_home_page
    trms_home.credential_input_bar().send_keys(password)
    sleep(1)


@when(u'The User clicks the Submit Button again')
def password_submit(context):
    trms_home: TRMSHomePage = context.trms_home_page
    trms_home.credential_submit().click()
    sleep(1)


@then(u'The title of the page is now {title}')
def verify_title(context, title):
    driver: WebDriver = context.driver
    assert driver.title == title
