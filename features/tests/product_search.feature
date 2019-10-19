# Created by zzohamadro at 10/19/19
Feature: Test for Amazon Search functionality
  # Enter feature description here

  Scenario: User can search for a product
    Given Open Amazon page
    When Search for shoes
    Then Search results for shoes is shown