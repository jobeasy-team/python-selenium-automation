# Created by raihanamin at 5/30/21
Feature: Amazon search test
  # Enter feature description here

  Scenario: User can open Amazon page
   Given open Amazon page
    When Click on sign in
    And Click on conditions of use link
    Then verify searched worked