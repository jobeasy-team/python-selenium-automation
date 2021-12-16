# Created by Ayaz
Feature: 5 links of Amazon Bestseller page

  Scenario: User can see 5 links in Amazon Bestseller page
    Given Open Amazon website (No Sign In)
    When Click on Bestsellers
    Then Verify 5 links
    