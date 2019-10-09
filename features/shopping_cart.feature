# Created by vinny at 10/8/2019
Feature: Verify shopping cart is being empty
  # Enter feature description here

  Scenario: Verify shopping cart being empty
    Given Open amazon page
    When Click on shopping cart button
    Then Verify the cart is empty