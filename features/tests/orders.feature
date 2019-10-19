# Created by zzohamadro at 10/11/19
Feature: Test for Orders functionality

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click on Orders link
    Then Verify Sign in page opened