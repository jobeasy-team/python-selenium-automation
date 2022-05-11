# Created by victorjefferson at 5/9/22
Feature: Test Scenarios for Customer Service Search functionality

  Scenario: Verify that user can use the Customer Service Search bar
    Given Open Amazon Customer Service Page
    When Search for Cancel Order
    Then Verify search results for Cancel Items or Orders

    # Enter steps here