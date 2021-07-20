# Created by bkarp0518 at 7/17/21
Feature: Language selection tests
  # Enter feature description here

  Scenario: User can see Spanish language
    Given Open Amazon page
    When move mouse over flag icon
    Then Spanish language selection is visible

