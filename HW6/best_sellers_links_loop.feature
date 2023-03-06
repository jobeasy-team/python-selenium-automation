# Created by vsupe at 3/6/2023
Feature: Best sellers tab


  Scenario: Verify if correct page is opened for Best Sellers links
    Given Open amazon page
    When Click on Best Sellers link on the top menu
    Then Clicks on each top link and Verifies that correct page opens
