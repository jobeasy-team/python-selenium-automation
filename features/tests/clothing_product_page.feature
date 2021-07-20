# Created by bkarp0518 at 7/19/21
Feature: New Arrivals tab is visible
  # Enter feature description here

  Scenario: Verify if New Arrivals tab is opening
      Given Open Amazon clothing page
      When Move mouser over to New Arrivals tab
      Then Verify if that user can see deals