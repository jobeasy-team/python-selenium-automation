# Created by Adewale at 6/5/2022
Feature: amazon page test
  Scenario: Verify user can see language options
    Given   Open Amazon page
    When    Hover over language options
   Then    verify Spanish Option present


    Scenario: Verify Users can view the New Arrivals
      Given    Open product page
     When     Hover over new arrivals
      Then     verify new arrivals present


      Scenario: User can select and search in a department
        Given   Open Amazon page
        When    Select baby department
        And     Search for baby wipes
        Then    verify baby department is selected