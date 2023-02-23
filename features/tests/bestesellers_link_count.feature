# Created by vsupe at 2/20/2023
Feature:  BestSeller's page


  Scenario: Count number of link in the BestSeller's page
    Given Open amazon page
    When click on Best Sellers tab
    Then Verify the number of links are 5