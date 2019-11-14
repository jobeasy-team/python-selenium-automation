# Created by zzohamadro at 11/6/19
Feature: Multiple product search
  # Enter feature description here

  Scenario Outline: User can search for multiple products
    Examples:
    |keyword|expected_result|
    |dress  | dress         |
    |shoes  | shoes         |
    |toys   | toys          |
    Given Open Amazon page
    When Search for <keyword>
    Then Search results for <expected_result> is shown