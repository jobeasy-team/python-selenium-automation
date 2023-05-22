# Created by ekaterinasuvorova at 5/10/23
Feature: Sign in page display for new/logged out user
  #Verify that logged out user sees Sign In when clicking on Returns and Orders

  Scenario:  User can see Sign In page
    Given Open Amazon page
    When Click Returns and Orders
    Then Verify that header Sign in is visible
    Then Verify that Email field is present