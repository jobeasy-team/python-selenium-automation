# Created by Steve at 2/26/2023
Feature: Test to verify amazon cart


  Scenario: User can see the amount added to cart
    Given Open Amazon page
    When  Input socks into search field
    And Click on search icon
    And Click on first product
    And Click add to cart
    And Click on cart
    Then Verify that text Shopping Cart is shown