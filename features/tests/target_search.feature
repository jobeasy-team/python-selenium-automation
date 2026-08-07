# Created by lana at 8/6/26
Feature: Test cases for Target Search

  Scenario: User can search for a product
    Given Open main target page
    When Search for tea
    Then Verify search results are shown for tea

#  Scenario: User can see Empty Cart message
#    Given Open main target page
#    When Click on cart icon
#    Then Verify Cart Empty message is shown
