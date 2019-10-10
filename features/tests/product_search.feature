# Created by vinny at 10/7/2019
Feature: Test for Amazon search functionality
  # Enter feature description here

  Scenario: User can search for a product
    Given Open amazon page
    When Input Dress into search field
    When Click on search icon
    Then Product result for Dress is shown