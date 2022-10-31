# Created by AAA at 10/5/2022
Feature: Verify cart is empty

  Scenario: user sees 0 items
    Given open Amazon website
    When user click on cart
    Then text to show cart is empty