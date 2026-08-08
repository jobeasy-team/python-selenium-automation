Feature: Tests for Header Links

  Scenario: Navigation Utility Header is shown
    Given Open main target page
    Then Verify Navigation Utility Header is shown

  Scenario: Navigation Utility Header has correct number of links
    Given Open main target page
    Then Verify 6 Navigation Utility Header links are shown
