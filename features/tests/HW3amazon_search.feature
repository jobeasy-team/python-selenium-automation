# Created by Adewale at 5/4/2022
Feature: Test for amazon search

  Scenario: Verify User can confirm the cart is empty
    Given open amazon page
    When click cart icon
    Then verify cart is empty


  Scenario: Verify user can search for "cancel order" in amazon
    Given   Open Amazon page
    When   Select customer service
    Then   Verify user can cancel order