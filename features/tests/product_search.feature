Feature: Test cases for Product Search on Target

  Scenario: User can search for a product "tea" on Target
    Given Open Target main page
    When Search for tea
    Then Verify search results for tea shown
    And Verify URL has searchTerm=tea

  Scenario: User can search for a product "coffee" on Target
    Given Open Target main page
    When Search for coffee
    Then Verify search results for coffee shown

  Scenario Outline: User can search for products
    Given Open Target main page
    When Search for <search_query>
    Then Verify search results for <product> shown
    Examples:
    |search_query   |product      |
    |Coffee         |Coffee       |
    |coffee cup     |coffee cup   |
    |sugar          |sugar        |

  Scenario: Verify that user can see product names and images
    Given Open Target main page
    When Search for AirPods
    Then Verify that every product has a name and an image

  Scenario: User can see favorites tooltip for search results
    Given Open Target main page
    When Search for tea
    And Hover favorites icon
    Then Favorites tooltip is shown
