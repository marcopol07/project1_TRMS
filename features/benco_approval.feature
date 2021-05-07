Feature: The Benefits Coordinator approves a Reimbursement Request

  Scenario: Eric, the Benefits Coordinator, accepts a Reimbursement Request
    Given Eric is on his dashboard
    When Eric selects Approve on the menu
    When Eric clicks the Submit button
    Then The form is approved