# Created by Анна at 5/11/2022
Feature: Test for Amazon help search

  Scenario: Verify that Cancel Items or Orders page is shown
    Given open Amazon help search
    When Input Cancel order
    And click ENTER
    Then Verify that results for "Cancel Items or Orders" are shown