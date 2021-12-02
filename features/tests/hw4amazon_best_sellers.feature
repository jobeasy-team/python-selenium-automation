# Created by bobo at 11/30/2021
Feature: User can Open bestSellers on Amazon

  Scenario: User can open bestsellers page with 5 links
    # Enter steps here
  Given Open Amazon bestSeller page
    Then  bestseller page is shown
    Then  5 links display on the page