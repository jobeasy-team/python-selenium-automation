
Feature: Test switch window feature

  Scenario: User able to navigate to privacy page from conditions page
  Given Open conditions page
  Given Store original window
  When Click on privacy link
  When Switch to new window
  Then Verify privacy page is open
  Then Close privacy page
  Then Return to original window