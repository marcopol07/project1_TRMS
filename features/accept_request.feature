Feature: Multiple Users Approve a Request

  Scenario: Ryan, a Department Head, accepts a Reimbursement Request
    Given Ryan is on his dashboard
    When Ryan selects Approve on the menu
    When Ryan clicks the Submit button
    Then The form is approved

  Scenario: Eric, the Benefits Coordinator, requests more information
    Given Eric is on his dashboard
    When Eric enters his query into the search bar
    When Eric clicks the Send button
    Then The query is Sent

  Scenario: Marc looks at the query Eric has sent him
    Given Marc is on his dashboard
    Then Marc can see the query

  Scenario: Eric, the Benefits Coordinator, accepts a Reimbursement Request
    Given Eric is on his dashboard
    When Eric selects Approve on the menu
    When Eric clicks the Submit button
    Then The form is approved