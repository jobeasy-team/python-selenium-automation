# Created by Vallikannu at 11/17/2020
Feature: verify that user can open amazon application
   from Terms of Conditions

  Scenario: User can open and close Amazon Applications
    Given Open Amazon T&C page
    When Click on Amazon applications link and store original window
    When Switch to the newly opened window
    Then Amazon app page is opened
    Then User can close new window and switch back to original