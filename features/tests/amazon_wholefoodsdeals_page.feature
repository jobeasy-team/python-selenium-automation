# Created by zzohamadro at 10/23/19
Feature: Amazon Wholefoodsdeals page functionality
  User opens Amazon Wholefoodsdeals page, scrolls all the way down
  to compare what deal User gets as a Prime member compare to Regular price
  listed under each product name

  Scenario: User opens Amazon wholefoodsdeals page to compare Prime benefits to regular price
  listed under each product name
    Given User opens Amazon wholefoodsdeals page and maximizes window
    Then Verifies every product listed with Prime benefit has product name and Regular price