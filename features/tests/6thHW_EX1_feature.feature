Feature: amazon privacy notice

Scenario: user can open and close Amazon Privacy Notice
    Given Open Amazon T&C page
    When store original windows
    And click on Amazon Privacy Notice link
    And switch to the newly opened window
    Then verify Amazon Privacy Notice is opened
    And user can close new window and switch back to original