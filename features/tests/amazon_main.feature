# Created by svetlanalevinsohn at 10/1/22
Feature: Tests for Amazon main page

  Scenario: Hamburger menu is present
    Given Open amazon page
    Then Verify hamburger menu is present

  Scenario: Footer has correct amount of links
    Given Open amazon page
    Then Verify that footer has 38 links

  Scenario: User can see language options
    Given Open Amazon page
    When Hover over language options
    Then Verify Spanish option present
