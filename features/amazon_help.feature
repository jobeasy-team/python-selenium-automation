# Created by natalia at 10/7/2019
Feature: Cancelling an order on Amazon

  Scenario: User can search for Cancelling an order on Amazon
    Given Open amazon page
    When Click on help button
    Then Find search field
    Then Click go button
    Then Verify cancel items or orders text is present
