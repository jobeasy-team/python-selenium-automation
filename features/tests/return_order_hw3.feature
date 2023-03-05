Feature: Test scenario for Returns & Orders
  Scenario: logged out User can see sign in page on clicking Returns & Orders
    Given open amazon home page
    When user is logged out
    When click Returns & Orders link css
    Then Sign in page appears css
