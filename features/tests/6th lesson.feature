# Created by AAA at 11/10/2022
Feature: sign in test cases

  Scenario: sign in page anc be opened from signUp popup
    When open Amazon web page
    Then verify sign in is clickable
    When wait for 5 seconds
    Then verify sign in is clickable
    Then verify sign in disappears