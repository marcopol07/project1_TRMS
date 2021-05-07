Feature: The User can log in to their Dashboard

  Scenario Outline: The User Inputs their Username
    Given The User is on the HTML WebPage
    When The User enters <username> in the input bar
    When The User clicks the Submit Button
    When The User now enters <password> in the input bar
    When The User clicks the Submit Button again
    Then The title of the page is now <title>

  Examples:
    | username  | password  | title |
    | marc  | password      | Marc Dashboard  |
    | ryan  | 12345 | Ryan Dashboard          |
    | eric  | opensesame  | Eric Dashboard    |
    | darius  | darius123 | Darius Dashboard  |
    | colette | paSswORD  | Colette Dashboard |
    | dan | dangreen  | Dan Dashboard         |
    | frank | tothemoon | Frank Dashboard     |