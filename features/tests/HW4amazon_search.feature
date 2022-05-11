# Created by Adewale at 5/4/2022
Feature: Test for amazon search

  Scenario: Verify User can add to cart
    Given open amazon page
    When customer searches for marcy multi-purpose adjustable workout utility weight bench
    Then lamp is added to cart
    Then verify cart has 1 item added

