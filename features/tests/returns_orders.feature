# Created by Vallikannu at 12/13/2020
Feature: # Enter feature name here
  # Enter feature description here

  Scenario:  Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page returns order
    When Click Amazon Orders link returns order
    Then Verify Sign text in the opened page returns order