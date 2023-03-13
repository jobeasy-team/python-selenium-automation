# Created by svetlanalevinsohn at 2/11/23
Feature: Amazon search tests

  Scenario Outline: User can search for coffee on Amazon
    Given Open Amazon page
    When Input text <search_word>
    And Click on search button
    Then Verify that text <search_result> is shown
    Examples:
    |search_word  |search_result  |
    |coffee       |"coffee"       |
    |table        |"table"        |
    |mug          |"mug"          |

  Scenario: User can search for a table on Amazon
    Given Open Amazon page
    When Input text table
    When Click on search button
    Then Verify that text "table" is shown
#
#  Scenario: User can search for a mug on Amazon
#    Given Open Amazon page
#    When Input text mug
#    When Click on search button
#    Then Verify that text "mug" is shown

  Scenario: User can add a product to the cart
    Given Open Amazon page
    When Input text Tritan Farm to Table Pitcher
    When Click on search button
    And Click on the first product
    And Click on Add to cart button
    And Open cart page
    Then Verify cart has 1 item(s)

#  Scenario: User can click on a hamburger menu
#    Given Open Amazon page
#    Then Verify hamburger menu icon present
#
#  Scenario: Footer has correct amount of links
#    Given Open amazon page
#    Then Verify that footer has 38 links