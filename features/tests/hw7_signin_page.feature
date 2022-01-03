# Created by bobo at 1/1/2022
Feature: # sign in page
  # Enter feature description here

  Scenario: Logged out user sees Sign in page when clicking Orders
 Given Open Amazon page
 When Click Amazon Orders link
 Then Verify Sign In page is opened

    Scenario: 'Your Shopping Cart is empty' shown if no product added
 Given Open Amazon page
 When Click on cart icon
 Then Verify Your Amazon Cart is empty text present