# Created by zzohamadro at 11/6/19
Feature: Best seller page header links functionality

  Scenario: User can navigate through the page header menu
    Given Open Amazon page
    When Clicks on link to proceed to Best Seller page
    Then User can navigate through the header menu links and verify banner is matching link text
