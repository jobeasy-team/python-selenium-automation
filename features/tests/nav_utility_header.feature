Feature: Tests for Header Links

  @smoke @header
  Scenario: Navigation Utility Header is shown
    Given Open main target page
    Then Verify Navigation Utility Header is shown

  @P1 @header
  Scenario: Navigation Utility Header has correct number of links
    Given Open main target page
    Then Verify 6 Navigation Utility Header links are shown
