# Created by zzohamadro at 11/3/19
Feature: Tests for Sign In functionality
  # Enter feature description here

  Scenario: SignIn tooltip appears and disappears
    Given Open Amazon page
    Then Verify SignIn tooltip is present and clickable
    When Wait until SignIn tooltip disappears
    Then Verify SignIn tooltip is NOT clickable