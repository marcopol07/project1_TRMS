Feature: A User sends a request for more information

  Scenario: Eric, the Benefits Coordinator, requests more information
    Given Eric is on his dashboard
    When Eric enters his query into the search bar
    When Eric clicks the Send button
    Then The query is Sent