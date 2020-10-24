# Created by Vallikannu at 10/23/2020
Feature: Create a test case that will open amazon BestSellers page
  # Enter feature description here

  Scenario: Verify there are 5 links
    Given Open amazon bestsellers
    Then Verify 5 links
