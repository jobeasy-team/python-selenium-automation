# Created by vsupe at 2/17/2023
Feature: Verify cart is empty
  # Enter feature description here

  Scenario: User sees empty cart
    Given Open amazon page
    When User click on cart icon
    Then Verify that Amazon cart is empty