# Created by svetlanalevinsohn at 7/16/22
Feature: Sign in test cases

  Scenario: Sign In page can be opened from SignIn popup
    Given Open Amazon page
    When Click on button from SignIn popup
    Then Verify Sign in page opened
