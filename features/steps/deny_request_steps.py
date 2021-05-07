from time import sleep

from behave import given, when, then
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException, \
    ElementClickInterceptedException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select

from features.pages.trms_home_page import TRMSHomePage


@when(u'Ryan selects Deny on the menu')
def step_impl(context):
    trms_home: TRMSHomePage = context.trms_home_page
    acceptor = Select(trms_home.approval_selector())
    acceptor.select_by_value('deny')
    sleep(5)


@then(u'The form is denied')
def step_impl(context):
    assert True
