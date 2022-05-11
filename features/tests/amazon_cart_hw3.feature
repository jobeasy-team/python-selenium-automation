# Created by victorjefferson at 5/9/22
Feature: Test scenarios for cart status
  # Enter feature description here

  Scenario: Verify user can check for items in their cart
    Given Open Amazon Main page
    When Click on the cart icon
    Then Verify Your Amazon Cart is empty