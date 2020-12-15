# Created by Vallikannu at 12/14/2020
Feature: Amazon Music has 7 menu items
  # Enter feature description here

  Scenario: Amazon Music has 7 menu items using Page Object pattern
    Given Open Amazon page music
    When Click on hamburger menu
    Then Click on Amazon Music menu item
    Then 9 menu items are present
