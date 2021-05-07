Feature: Submit Reimbursement Request

  Scenario: The User submits a Reimbursement Request
    Given The User is on their Dashboard
    When The User enters the date of training
    When The User enters the cost of training
    When the User enters the justification for the training
    When The User clicks the form submit button
    Then The form will be submitted for approval
