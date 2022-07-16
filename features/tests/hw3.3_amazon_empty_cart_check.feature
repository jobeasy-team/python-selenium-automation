# Created by tosha at 7/11/2022
Feature: Amazon empty cart test

  Scenario: User can verify empty cart
    Given  user opens Amazon page
    When user clicks on cart icon
    Then user sees empty cart message