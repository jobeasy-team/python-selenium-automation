# Created by bkarp0518 at 6/7/21
Feature: Amazon Bestseller
  # Enter feature description here

  Scenario: verify if Amazon Bestseller has 5 links
   Given Open Amazon Bestseller page
    Then Verify if user can see 5 links on the page

    Scenario: Bestseller page links can be opened
   Given Open Amazon Bestseller page
    Then Verify if user can click through headers links