# Created by Ayaz
Feature: Adding item into Amazon cart

  Scenario: User can search for item & add into Amazon cart
    Given Open Amazon website (No Sign In)
    When Search for Kurukahveci Mehmet Efendi Turkish Coffee, 17.6 Ounce (Pack of 1)
    And Select item
    And Add item into cart
    And Click on Amazon cart
    Then Show Kurukahveci Mehmet Efendi Turkish Coffee, 17.6 Ounce (Pack of 1) in cart


