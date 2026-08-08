Feature: Cart tests

  Scenario: User can see Empty Cart message
    Given Open main target page
    When Click on cart icon
    Then Verify Cart Empty message is shown