# Created by bkarp0518 at 7/11/21
Feature: Item is shown
  # Enter feature description here

  Scenario: Verify if Cologne is shown
    Given Open Amazon page
    When Search for Cologne
    When Click on first product
    When Click on add to cart btn
    Then Verify that cologne in your cart