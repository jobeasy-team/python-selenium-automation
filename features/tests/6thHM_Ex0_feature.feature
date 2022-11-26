# Created by AAA at 11/24/2022
Feature: Expected Condition

  Scenario: user see sign in button
    When open Amazon web page
    Then verify sign in is clickable
    When wait for 5 seconds
    Then verify sign in is clickable
    Then Verify sign in disappears

