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

  Scenario: Verify that user can add items to cart
    Given Open Amazon Main page
    When Search for ginkgo biloba tincture
    Then Click on Amazon's Choice
    Then Add item to cart
    Then Verify Added to Cart

    #lesson 5
  Scenario: User can search colors
    Given Open Amazon B07RGZ5NKS product page
    Then Verify user can click through colors