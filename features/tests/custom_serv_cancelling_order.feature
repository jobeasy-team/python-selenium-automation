# Created by zzohamadro at 10/20/19
Feature: Test for Amazon Customer Service functionality
  # Enter feature description here

  Scenario: User can search for solutions of Cancelling order on Amazon
    Given Open Amazon page and maximize window
    When Click on Customer Service link
    When Input Cancel order into search box
    And Click Go button
    Then Verify that Cancel Items or Orders text is presented