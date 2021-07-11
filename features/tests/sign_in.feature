# Created by bkarp0518 at 5/30/21
Feature: Tests for sign in page


  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click Orders
    Then Verify Sign in page opened
