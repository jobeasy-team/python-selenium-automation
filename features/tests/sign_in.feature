# Created by Owner at 6/3/2021
Feature: Tests for sign in page

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click Orders
    Then Verify Sign in page opened