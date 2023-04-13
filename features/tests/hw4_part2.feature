# Created by Steve at 2/26/2023
Feature: Test to verify amazon cart


  Scenario: User can see the amount added to cart
    Given Open Amazon page
    When  Input socks into search field
    And Click on search icon
    And Click on first product
    And Click add to cart
    And Click on cart
    Then Verify that text Shopping Cart is shown

    Scenario: User can select and search in a department
    Given Open Amazon page
    When  Select department books
    When Input text Faust
    When Click on serach button
    Then Verify books department is selected