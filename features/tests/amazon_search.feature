# Created by ekaterinasuvorova at 5/5/23
Feature: Amazon search tests

  Scenario Outline: User can search for a product on Amazon
    Given Open Amazon page
    When Input text <search_word>
    When Click on search button
    Then Verify that text <search_result> is shown
    Examples:
    |search_word  |search_result  |
    |coffee       |"coffee"       |
    |table        |"table"        |
    |mug          |"mug"          |

  Scenario: User can add a product to the cart
    Given Open Amazon page
    When Input text Tritan Farm to Table Pitcher
    When Click on search button
    And Click on the first product
    And Click on Add to cart button
    And Open cart page
    Then Verify cart has 1 item(s)




