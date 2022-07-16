# Created by ababa at 7/15/2022
Feature: Navigation in Amazon


  Scenario: Unlogged User goes to Sign In page when clicks on Returns & Orders.
    Given User opens Amazon page (No Sign In)
    When User clicks on Returns & Orders
    Then User sees Sign-In page
    And Email input box is visible