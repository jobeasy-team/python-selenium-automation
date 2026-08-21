Feature: Test cases for Target Search

  Scenario: User can search for tea
    Given Open main target page
    When Search for tea
    Then Verify search results are shown for tea
    Then Verify searchTerm=tea is in the URL

#  Scenario: User can search for a mug
#    Given Open main target page
#    When Search for mug
#    Then Verify search results are shown for mug
#
#  Scenario: User can search for coffee
#    Given Open main target page
#    When Search for coffee
#    Then Verify search results are shown for coffee

  Scenario Outline: User can search for a product
    Given Open main target page
    When Search for <product>
    Then Verify search results are shown for <expected_product>
    Examples:
    |product  |expected_product   |
    |coffee   |coffee             |
    |tea      |tea                |
    |mug      |mug                |

  Scenario: Verify that user can see product names and images
    Given Open main target page
    When Search for AirPods
    Then Verify that every product has a name and an image
