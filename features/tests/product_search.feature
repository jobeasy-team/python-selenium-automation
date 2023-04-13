# Created by Svetlana at 4/4/19
Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Google page
    When Input Watches into search field
    When Click on search icon
    Then Product results for Watches are shown

