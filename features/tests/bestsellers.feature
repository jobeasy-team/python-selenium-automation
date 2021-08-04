# Created by Owner at 6/17/2021
Feature: Verify Best Sellers links
  # 1. Create a test case that will open amazon BestSellers page:
  # https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers
  #And verify there are 5 links:

  Scenario: Verify Bestseller page links
    Given Open Amazon Best Sellers page
    Then Verify there are 5 links


  Scenario: Bestsellers links can be opened
    Given Open Amazon Best Sellers page
    Then User can click through top links and verify correct page opens
