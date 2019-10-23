# Created by zzohamadro at 10/23/19
Feature: Test for hamburger menu functionality
  # Enter feature description here

  Scenario: Amazon Music has 6 links
    Given Open Amazon page and maximize window
    When Click on hamburger menu
    And Click on Amazon Music menu item
    Then 6 menu items are present