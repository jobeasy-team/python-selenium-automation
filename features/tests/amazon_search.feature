# Created by Owner at 6/3/2021
Feature: Test Amazon Search

  Scenario: User can search for a product
    Given Open Amazon page
    When Input Table in search field
    When Click on Amazon search icon
    Then Verify search worked