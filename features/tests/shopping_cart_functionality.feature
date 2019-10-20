# Created by zzohamadro at 10/20/19
Feature: Test for Amazon Shopping Cart functionality
  # Enter feature description here

  Scenario: User can verify that the shopping cart is empty
    Given Open Amazon page and maximize window
    When Click on Shopping Cart icon
    Then Verify that Your Shopping Cart is empty text is presented

