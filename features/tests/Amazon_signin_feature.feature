# Created by Steve at 2/23/2023
Feature: Test to get to Amazon's sign in page


  Scenario: User can get to amazon sign in page
    Given Open Amazon page
    When Click on orders
    Then Verify that text Sign in is shown

