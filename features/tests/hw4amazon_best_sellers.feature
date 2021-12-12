# Created by bobo at 11/30/2021
Feature: User can Open bestSellers on Amazon

  Scenario: User can open bestsellers page with 5 links
    # Enter steps here
  Given Open Amazon bestSeller page
    Then  bestseller page is shown
    Then  5 links display on the page


  Scenario: User can add product to cart

    Given Open Amazon page
    When Search for glass
    And Click for search icon
    And Click on the first product
    And Click on Add to cart button
    And Open cart page
    Then Verify cart has 1 item(s)