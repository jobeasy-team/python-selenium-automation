# Created by Ayaz at 7/15/2022
Feature: Unlogged user navigates to Amazon cart

  Scenario: Unlogged user goes to empty Amazon cart and sees cart is empty
    Given User Opens Amazon page (No Sign In)
    When User clicks on Amazon cart
    Then cart results show empty