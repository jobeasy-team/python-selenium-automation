# Created by Q at 1/8/22
Feature: using a dropdown and search for an item in a different Amazon department.


  Scenario: # Enter scenario name here
    # Enter steps here
  Given Open Amazon page
    When select department by baby
    And Search for diapers
    And Click for search icon
    Then Verify baby department is selected