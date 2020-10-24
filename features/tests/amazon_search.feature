# Created by Vallikannu at 10/7/2020
Feature: Tests for Amazon search
  # Enter feature description here

  Scenario: Amazon search returns correct results
    Given Open JSP page
    When Input Dress into Amazon search field
    And Click on Amazon search icon
    Then search result Dress is shown