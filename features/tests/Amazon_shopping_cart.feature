# Created by bkarp0518 at 5/30/21
Feature: Shopping Cart


  Scenario: User can verify shopping cart is empty
    Given Open Amazon homepage
    When Click on Shopping cart icon
    Then Verify Shopping Cart is empty
