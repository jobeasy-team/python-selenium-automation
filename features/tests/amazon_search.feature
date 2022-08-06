# Created by svetlanalevinsohn at 7/9/22
Feature: Amazon Product Search Tests

  Scenario Outline: User can search for a product
    Given Open Amazon page
    When Search for <product> on amazon
    Then User sees results for <search_result>
   Examples:
    |product      |search_result   |
    |mug          |"mug"           |
    |coffee       |"coffee"        |

  Scenario: User can add a product to the cart
    Given Open Amazon page
    When Search for Tritan Farm to Table Pitcher on amazon
    And Click on the first product
    And Store product name
    And Click on Add to cart button
    And Open cart page
    Then Verify cart has 1 item(s)
    And Verify cart has correct product

  Scenario: Verify that user sees hamburger menu on main page
    Given Open Amazon page
    Then Verify hamburger menu is present

  Scenario: Verify all footer links are shown
    Given Open Amazon page
    Then Verify 38 footer links are shown

  Scenario: Verify that user can see product names and images
    Given Open Amazon page
    When Search for coffee on amazon
    Then Verify that every product has a name and an image