# Created by Ayaz at 6/30/2022
Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Google page
    When Input Watches into search field
    And Click on search icon
    Then Product results for Watches are shown
