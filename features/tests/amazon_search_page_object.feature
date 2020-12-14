# Created by Vallikannu at 10/7/2020
Feature: Tests for Amazon search
  # Enter feature description here

  Scenario: Amazon search returns correct results
    Given Open Amazon page1
    When Input Dress into Amazon search field1
    And Click on Amazon search icon1
    Then search result Dress is shown1
