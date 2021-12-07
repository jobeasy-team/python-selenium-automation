# Created by Ayaz
Feature: Navigating to Amazon cart

  Scenario: User can open empty Amazon cart without Sign-In
    Given Open Amazon website (No Sign In)
    When Click on Amazon cart
    Then results for empty cart is shown