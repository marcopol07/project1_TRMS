Feature: Multiple Users Approve a Request

  Scenario: Ryan, a Department Head, accepts a Reimbursement Request
    Given Ryan is on his dashboard
    When Ryan selects Approve on the menu
    When Ryan clicks the Submit button
    Then The form is approved
