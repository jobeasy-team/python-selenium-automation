# Created by vsupe at 3/12/2023
Feature: Homework 7 Page Object Model Scenarios
  # Enter feature description here

Scenario: Logged out user sees Sign in page when clicking Orders
 Given Open Amazon page
 When Click Amazon Orders link
 Then Verify Sign In page is opened and text Sign in is displayed

Scenario: 'Your Shopping Cart is empty' shown if no product added
 Given Open Amazon page
 When Click on cart icon
 Then Verify Your Amazon Cart is empty text present


Scenario:“Add a product to cart” scenario using Page Object pattern.
   Given Open amazon page
   When Input text Tritan Farm to Table Pitcher
   And Click on search button
   And Click on the first product
   And Click on Add to cart button
   Then Verify cart has 1 item(s)
