# Created by Adewale at 5/31/2022
Feature: A test to verify Amazon page


  Scenario: Logged out user sees Sign in page when clicking Orders
   Given    Open Amazon page
    When   Click Amazon Orders link
    Then   Verify Sign in page is opened


    Scenario: 'Your Shopping Cart is empty' shown if no product added
      Given    Open Amazon page
      When     Click on cart icon
      Then     Verify "Your Shopping Cart is Empty" text is present