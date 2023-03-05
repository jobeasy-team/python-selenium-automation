Feature: Test scenario for Amazon cart
  Scenario: verify that the Amazon order cart is empty
    Given open amazon home page
    When click cart icon
    Then verify that the cart is empty
