# Created by ababa at 7/7/2022
Feature: Navigation in Amazon


  Scenario: Non-logged User goes to Sign In page when clicks on Orders.
    Given User opens Amazon(No Sign In)
    When User clicks on Orders
    Then User sees Sign In page
    And email input is visible