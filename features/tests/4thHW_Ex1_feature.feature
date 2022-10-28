# Created by AAA at 10/17/2022
Feature: verify there are 5 items in Amazon Best Sellers

  Scenario: User see five links in Best Sellers
    Given open Amazon Best Seller webpage
    Then user see 5 tabs
