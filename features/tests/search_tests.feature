# Created by svetlanalevinsohn at 3/20/21
Feature: Wiki search

  Scenario Outline: Search returns correct results
    Given Open main page
    When Search for <query_words>
    Then Verify article opens for <query_words>
    Examples:
    |query_words                    |
    |Cat                            |
    |Python (programming language)  |
    |Java (programming language)    |
    |Selenium (software)            |
    |List of HTTP status codes      |

  Scenario: Search can open No Search Results
    Given Open main page
    When Search for ahgsfgaddgast
    Then Verify No Search Results page opens

  Scenario: Article creation can be opened from No Search Results
    Given Open main page
    When Search for ahgsfgaddgast
    Then Verify No Search Results page opens
    When Click to create article
    Then Verify article opens for Wikipedia:Articles for creation
