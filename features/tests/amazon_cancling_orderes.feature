# Created by Yonas at 5/5/2022
Feature: test canceled orders


  Scenario: verify canceling order functions
    Given open amazon page
    When  search for customer service
    Then  search for canceled items
    Then  verify the canceled item or order page comes


  Scenario: user can add a product to cart
    Given open amazon page
    When input "basketball" into search,taps Enter
    Then click on the first price
    Then click to add to cart
    And Open cart page
    Then verify cart has 1 item(s)


  Scenario: user can see all  sections on header of best seller page
    Given  open amazon best sellers page
    Then verify there are 5 links


