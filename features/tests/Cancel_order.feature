# Created by bkarp0518 at 5/30/21
Feature: Cancel Order


  Scenario: Verify if user can cancel order by search input
    Given Open Amazon customer page
    When Input Cancel order in search field and press enter to search
    Then Verify Cancel Order text is shown
