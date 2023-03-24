Feature: Tests for bestsellers functionality

  @smoke @negative
  Scenario: Bestsellers links can be opened
    Given Open Amazon Bestsellers
    Then User can click through top links and verify correct page opens