# Created by AAA at 9/30/2022
Feature: Amazon site search test

  Scenario: search for a product
    Given open Amazon web page
    When user insert for shoes
    Then result for shoes are shown