# Created by bobo at 12/25/2021
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: User can open and close Amazon Privacy Notice

    Given Open the Amazon gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088 page
 When Store original window
 And Click on Amazon Privacy Notice link
 And Switch to the newly opened window
Then Verify Amazon Privacy Notice page is opened
And User can close new window and switch back to original