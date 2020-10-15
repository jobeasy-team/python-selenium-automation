# Created by Vallikannu at 10/14/2020
Feature:  Test case for support search using BDD
User can search for Cancelling an order on Amazon



  Scenario: User can search for Cancelling an order on Amazon
    Given Open amazon help search page
    When Input cancel order in Search the help library
    Then click enter
    Then Verify Cancel Items or Orders text present