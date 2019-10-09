# Created by vinny at 10/9/2019
Feature: Test scenario to verify the added item in a cart exists
  # Enter feature description here

  Scenario: User can see the added item in cart
    Given Open amazon page
    When Input Dress into search field
    When Click on search icon
    Then Product result for Dress is shown
    When Click on Dress
    Then Click on add in cart
    When Click on cart icon
    Then Verify the item is in cart