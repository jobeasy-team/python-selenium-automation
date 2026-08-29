Feature: Cart tests

  Scenario: User can see Empty Cart message after clicking on cart icon
    Given Open main target page
    When Click on cart icon
    Then Verify Cart Empty message is shown

#  Scenario: User can see Empty Cart message when navigating to cart directly
#    Given Open cart page
#    Then Verify Cart Empty message is shown
#
#  Scenario: User can add a product to cart
#    Given Open main target page
#    When Search for mug
#    And Click on Add to Cart button
#    And Store product name
#    And Confirm Add to Cart button from side navigation
#    And Open cart page
#    Then Verify cart has 1 item(s)
#    And Verify product in cart is correct