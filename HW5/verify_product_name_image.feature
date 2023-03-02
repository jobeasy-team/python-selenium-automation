# Created by vsupe at 3/1/2023
Feature: Verify product


  Scenario: Verify product name and image
    Given Open amazon page
    When Input text coffee
    When Click on search button
    Then Verify product has name and image