Feature: A User denies a reimbursement request

  Scenario: Ryan denies a reimbursement request
    Given Ryan is on his dashboard
    When Ryan selects Deny on the menu
    When Ryan clicks the Submit button
    Then The form is denied