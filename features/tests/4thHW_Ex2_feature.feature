# Created by AAA at 10/27/2022
Feature: add a product into the cart, and make sure it’s there.

  Scenario: user sees one item in cart
    Given open Amazon web page
    When search for item
    When select Item
    When add to the cart
    Then verify there is one item