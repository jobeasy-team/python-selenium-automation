# Created by Owner at 6/3/2021
Feature: Test Amazon Search

  Scenario: User can search for a product
    Given Open Amazon page
    When Search for Table
    When Click on Amazon search icon
    Then Verify search worked


  Scenario: User can search for a product
    Given Open Amazon page
    When Search for Polo Shirt
    When Click on Amazon search icon
    When Click on the first product
    Then Verify user can select colors
