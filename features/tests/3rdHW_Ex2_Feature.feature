# Created by AAA at 10/4/2022
Feature: user should sign in before seeing the orders

  Scenario: Sign in appears by clicking order button
    Given user opens the website
    When user click on Orders
    Then user face with sign in page