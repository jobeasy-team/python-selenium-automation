# Created by Yonas at 5/18/2022
Feature: Amazon sign in page


  Scenario: sign in page can be opened from signin popup
    Given open amazon page
    When click on button from signin popup
    Then verify sign in page is opened