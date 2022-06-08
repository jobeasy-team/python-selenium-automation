# Created by victorjefferson at 5/9/22
Feature: Test scenarios for cart status
  # Enter feature description here

  Scenario: Verify user can check for items in their cart
    Given Open Amazon Main page
    When Click on the cart icon
    Then Verify Your Amazon Cart is empty

  Scenario: Verify links on BestSellers Page
    Given Open Amazon BestSellers Page
    Then Verify there are 5 link

  Scenario: Verify that user can use the Customer Service Search bar
    Given Open Amazon Customer Service Page
    When Search for Cancel Order
    Then Verify search results for Cancel Items or Orders

    #Rewritten for page object
  Scenario: Verify that user can add items to cart
    Given Open Amazon Main page
    When Search for a ginkgo biloba product
    Then Click on Amazon's Choice
    Then Add item to cart
    Then Verify Added to Cart text is present

    #lesson 5
  Scenario: User can search colors
    Given Open Amazon B07RGZ5NKS product page
    Then Verify user can click through colors

    #lesson 6
  Scenario: User can open and close Amazon Privacy Notice
    Given Open Amazon T&C page
    When Store original windows
    And Click on Amazon Privacy Notice link
    And Switch to the newly opened window
    Then Verify Amazon Privacy Notice page is opened
    And User can close new window
    And switch back to original

  Scenario Outline: Verify that user can search for a product
    Given Open Amazon Main page
    When Search for a <search_word> product
    Then Verify search results for <search_result>
    Examples:
      | search_word  | search_result   |
      | Creatine     | "Creatine"      |
      | Whey protein | "Whey protein"  |

  #Lesson 7
  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon Main page
    When Click Amazon Orders link
    Then Verify Sign-In page is opened

  Scenario: 'Your Shopping Cart is empty' shown if no product added
    Given Open Amazon Main page
    When Click on the cart icon
    Then Verify Your Amazon Cart is empty text is present


