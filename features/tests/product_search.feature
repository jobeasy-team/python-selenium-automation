# Created by zzohamadro at 10/19/19
Feature: Test for Amazon Search functionality
  # Enter feature description here

  Scenario: User can search for a product
    Given Open Amazon page
    When Search for shoes
    Then Search result for shoes is shown

  Scenario: User can open and close Today's deals under $25
    Given Open Amazon page
    When Store original windows
    When Click to open deals under 25 dollars
    And Switch to the newly opened window
    Then Explore deals are shown
    And User can close new window and switch back to the original window


  Scenario: User can open and close Today's deals under $25, add product into cart,
  refresh main page and verify product is in the cart
    Given Open Amazon page
    When Store original windows
    And Click to open deals under 25 dollars
    And Switch to the newly opened window
    Then Explore deals are shown
    When Select chosen gift and add to cart
    And User can close new window and switch back to original and refresh main page
    Then Verify cart contains 1 item

