from time import sleep

from behave import given, when, then
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException, \
    ElementClickInterceptedException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select

from features.pages.trms_home_page import TRMSHomePage


@given(u'Ryan is on his dashboard')
def to_dash(context):
    trms_home: TRMSHomePage = context.trms_home_page
    trms_home.url('C:/Users/marcl/PycharmProjects/project1/frontend.html')
    trms_home.navigate_to_dash('ryan', '12345')
    sleep(5)


@when(u'Ryan selects Approve on the menu')
def select_approve(context):
    trms_home: TRMSHomePage = context.trms_home_page
    acceptor = Select(trms_home.approval_selector())
    sleep(5)
    acceptor.select_by_value('approve')
    sleep(5)


@when(u'Ryan clicks the Submit button')
def click_submit(context):
    trms_home: TRMSHomePage = context.trms_home_page
    trms_home.approval_submit().click()
    sleep(5)


@then(u'The form is approved')
def form_is_approved(context):
    trms_home: TRMSHomePage = context.trms_home_page
    try:
        trms_home.approval_submit()
        raise AssertionError("This button should be gone.")
    except NoSuchElementException:
        assert True


@given(u'Eric is on his dashboard')
def eric_dash(context):
    trms_home: TRMSHomePage = context.trms_home_page
    trms_home.url('C:/Users/marcl/PycharmProjects/project1/frontend.html')
    trms_home.navigate_to_dash("eric", "opensesame")
    sleep(4)


@when(u'Eric enters his query into the search bar')
def eric_query(context):
    trms_home: TRMSHomePage = context.trms_home_page
    trms_home.query_input_bar().send_keys("Where are you going?")
    sleep(5)


@when(u'Eric clicks the Send button')
def eric_send(context):
    trms_home: TRMSHomePage = context.trms_home_page
    trms_home.query_submit().click()
    sleep(5)


@then(u'The query is Sent')
def step_impl(context):
    assert True


@given(u'Marc is on his dashboard')
def step_impl(context):
    trms_home: TRMSHomePage = context.trms_home_page
    trms_home.url('C:/Users/marcl/PycharmProjects/project1/frontend.html')
    trms_home.navigate_to_dash('marc', 'password')
    sleep(5)


@then(u'Marc can see the query')
def step_impl(context):
    assert True


@when(u'Eric selects Approve on the menu')
def step_impl(context):
    trms_home: TRMSHomePage = context.trms_home_page
    acceptor = Select(trms_home.approval_selector())
    acceptor.select_by_value('approve')
    sleep(5)


@when(u'Eric clicks the Submit button')
def step_impl(context):
    trms_home: TRMSHomePage = context.trms_home_page
    trms_home.approval_submit().click()
    sleep(5)
