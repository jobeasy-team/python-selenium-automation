# Created by bkarp0518 at 6/10/21
Feature: Item is presented in your shopping cart
  # Enter feature description here

  Scenario: Verify if user can add and verify for an item
      Given Open Amazon Page
      When Search for Sanitizer
      When Click on first item
      When Click on add to cart button
      Then Verify that sanitizer in your shopping cart
