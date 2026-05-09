Feature: Tests for header

  @smoke
  Scenario: Verify user sees header links
    Given Open Target main page
    Then Verify header link container is shown
    Then Verify 6 links are shown