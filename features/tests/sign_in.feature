# Created by svetlanalevinsohn at 7/16/22
Feature: Sign in test cases

  Scenario: Verify that logged out user sees Sign In when clicking on Returns and Orders
    Given Open Amazon page
    When Click Orders
    Then Verify Sign in page opened

  Scenario: Sign In page can be opened from SignIn popup
    Given Open Amazon page
    When Click on button from SignIn popup
    Then Verify Sign in page opened

  Scenario: Amazon users see sign in button
    Given Open Amazon page
    Then Verify Sign In is clickable
    When Wait for 5 sec
    Then Verify Sign In is clickable
    Then Verify Sign In disappears