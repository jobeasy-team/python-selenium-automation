# Created by zzohamadro at 10/23/19
Feature: Test for dress  selection
  # Enter feature description here

  Scenario: User can loop through dress colors
    Given Open Amazon product B07K16Z8LH page
    Then Verify User can select through colors

  Scenario: User can navigate through product colors
    Given Open Amazon product B07BKD8JCQ page
    Then Verify User can loop through colors