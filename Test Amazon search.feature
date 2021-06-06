# Created by raihanamin at 5/30/21
Feature: Test Amazon Search
  # Enter feature description here

  Scenario: User can search for a product

    Given open Amazon search page
    When Input watch in search field
    And Click on Amazon search
    Then verify search worked

