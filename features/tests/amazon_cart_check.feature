# Created by Owner at 6/7/2021
Feature: Check for Empty Amazon Cart
  # opens amazon.com, clicks on the cart icon and
  # verifies that Your Shopping Cart is empty

  Scenario: Check for Empty Amazon Cart
    Given Open Amazon page
    When Click on cart
    Then Check that cart is Empty


  Scenario: User can add an item to the cart
    Given Open Amazon page
    When Search for coffee mug
    And Click on the first product
    And Click on Add to Cart button
    Then Verify cart has 1 item