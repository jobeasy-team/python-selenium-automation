# Created by bobo at 12/14/2021
Feature: Amazon product search
  # Enter feature description here

  Scenario: User can select pullover colors
  Given Open Amazon product B07XG51NZ8 page
  Then Verify user can click through colors

    # Enter steps here
  Scenario: User can see item details on wholefood sales
    Given Open Amazon wholefoodsdeals page
    Then verify every product has a text Regular and product name
