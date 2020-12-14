# Created by Vallikannu at 12/13/2020
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: Your Shopping Cart is empty' shown if no product added
    Given Open Amazon page shopping
    When Click on cart icon shopping
    Then Verify Your Shopping Cart is empty text present shopping