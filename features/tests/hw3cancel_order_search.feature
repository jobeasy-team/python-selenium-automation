# Created by bobo at 11/30/2021
Feature: User can search on Amazon
  # Enter feature description here

  Scenario: User can search for Cancelling an order on Amazon
    # Enter steps here
  Given Open Amazon Customer help page
    When Input cancel order in search field
    Then Product cancel order is shown on Amazon page
    And Search Result has cancel order in it