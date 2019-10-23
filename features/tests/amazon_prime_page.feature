# Created by zzohamadro at 10/23/19
Feature: Amazon Prime page functionality
  # Enter feature description here

  Scenario: Unregistered user opens Amazon Prime page and sees 8 benefit boxes
    Given User opens Amazon Prime page
    Then Verifies 8 benefit boxes are present
