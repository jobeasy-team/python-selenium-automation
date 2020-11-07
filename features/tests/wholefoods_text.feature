# Created by Vallikannu at 11/5/2020
Feature: Test case to verify, every product on the page
    has a text ‘Regular’ and a product name


  Scenario: Verify every product has text Regular
    Given Open amazon wholefoods page
    Then Verify the text Regular