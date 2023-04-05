
Feature: Test to select on amazon search


    Scenario: User can select and search in a department
    Given Open Amazon page
    When Select department by alias audible
    When Input text Faust
    When Click on search icon
    Then Verify audible department is selected