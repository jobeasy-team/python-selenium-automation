# Created by vinny at 10/7/2019
Feature: Test for Amazon search functionality
  # Enter feature description here

  Scenario: User can search for a product
    Given Open amazon page
    When search for Dress
    Then search result for Dress is shown