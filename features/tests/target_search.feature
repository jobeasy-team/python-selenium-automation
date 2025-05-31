Feature: Tests for Target Search

  Scenario: User can search for a product on Target
    Given Open target main page
    When Search for tea
    Then Verify search worked

  Scenario: User can search for a coffee on Target
    Given Open target main page
#    When Search for coffee
#    Then Verify search for coffee worked