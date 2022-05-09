# Created by Yonas at 5/5/2022
Feature: test canceled orders


  Scenario: verify canceling order functions
    Given open amazon page
    When  search for customer service
    Then  search for canceled items
    Then  verify the canceled item or order page comes