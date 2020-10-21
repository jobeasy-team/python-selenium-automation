# Created by Vallikannu at 10/19/2020
Feature: Test case to add any product to cart
  Check the cart and verify it’s there

  Scenario: Add any product into cart and verify
    Given Open Amazon home page
    When Search for kettle
    Then Click on the search icon
    Then Select first product to cart
    Then Add product in cart
    Then Verify the product in cart