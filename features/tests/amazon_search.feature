 # Created by bkarp0518 at 5/30/21
Feature: Test Amazon search


  Scenario: User can search for a product
    Given Open Amazon page
    When Input Table in search field
    When Click on Amazon search icon
    Then Verify search worked