# Created by vsupe at 2/22/2023
Feature: Customer Service’s page UI


  Scenario: verify Customer Service’s page UI
    Given Open amazon page
    When Click on Customer service tab
    Then Verify Welcome title is present
    And Verify list of services are present
    And Verify Help title is present
    And Verify search field is present
    And "All help topics" title is present
    And List of all help topics is present
