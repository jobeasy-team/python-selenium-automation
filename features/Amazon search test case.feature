# Created by raihanamin at 6/7/21
Feature:Amazon cancelling order test


  Scenario: User can cancel order on Amazon
  Given Open Amazon help page
  When input cancel_order in search help library field
  Then Verify cancel_order worked
