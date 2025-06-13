Feature: Tests for Target Search

  Scenario: User can search for tea
    Given Open target main page
    When Search for tea
    Then Verify search worked for tea

#  Scenario: User can search for a mug on Target
#    Given Open target main page
#    When Search for mug
#    Then Verify search worked for mug
#
#  Scenario: User can search for a coffee on Target
#    Given Open target main page
#    When Search for coffee
#    Then Verify search worked for coffee

  Scenario Outline: User can search for a product
    Given Open target main page
    When Search for <search_word>
    Then Verify search worked for <search_word>
    Examples:
    |search_word  |
    |tea          |
    |mug          |
    |coffee       |

  Scenario: Verify that user can see product names and images
    Given Open target main page
    When Search for AirPods
    Then Verify that every product has a name and an image
