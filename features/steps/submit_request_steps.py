from time import sleep

from behave import given, when, then
from selenium.webdriver.chrome.webdriver import WebDriver

from features.pages.trms_home_page import TRMSHomePage


@given(u'The User is on their Dashboard')
def to_dash(context):
    trms_home: TRMSHomePage = context.trms_home_page
    trms_home.url('C:/Users/marcl/PycharmProjects/project1/frontend.html')
    trms_home.navigate_to_dash("marc", "password")
    sleep(4)


@when(u'The User enters the date of training')
def enter_date(context):
    trms_home: TRMSHomePage = context.trms_home_page
    trms_home.date_input_bar().send_keys('05152021')
    sleep(3)


@when(u'The User enters the cost of training')
def enter_cost(context):
    trms_home: TRMSHomePage = context.trms_home_page
    trms_home.cost_input_bar().send_keys('100')
    sleep(3)


@when(u'the User enters the justification for the training')
def enter_justification(context):
    trms_home: TRMSHomePage = context.trms_home_page
    trms_home.justify_input_bar().send_keys('I need to learn new things.')
    sleep(3)

@when(u'The User clicks the form submit button')
def form_submission(context):
    trms_home: TRMSHomePage = context.trms_home_page
    trms_home.form_submit_button().click()
    sleep(3)


@then(u'The form will be submitted for approval')
def step_impl(context):
    trms_home: TRMSHomePage = context.trms_home_page
    message = trms_home.form_submit_button().text
    assert message == "Submitted! Your projected reimbursement amount is $80."

