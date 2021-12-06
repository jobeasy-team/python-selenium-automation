# Created by Ayaz
Feature: Searching on Amazon help library

  Scenario: User can search for "cancel order" on Amazon help library
    Given open Amazon help page
    When input cancel order into search library
    And begin search
    Then results for cancel order are shown

