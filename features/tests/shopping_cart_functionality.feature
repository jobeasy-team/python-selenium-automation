# Created by zzohamadro at 10/20/19
Feature: Test for Amazon Shopping Cart functionality
  # Enter feature description here

  Scenario: User can verify that the shopping cart is empty
    Given Open Amazon page and maximize window
    When Click on Shopping Cart icon
    Then Verify that Your Shopping Cart is empty text is presented

  Scenario: User can add chosen product into the cart
   User goes to Amazon account to purchase product, searches for that product by typing it's title into search field.
   On the next page user chooses one item from the offered variety. Clicks on that particular product,
   gets more familiar with product details, and adds it into shopping cart. User checks the shopping cart
   to make sure the product was successfully added.

     Given Open Amazon page and maximize window
     When Search for cat window perch
     When Open the first product search result
     And Click Add to cart button
     #Then Verify cart has 1 item
     Then Verify 1 item in the cart

   Scenario: User can add another chosen product into the cart

      Given Open Amazon page and maximize window
      When Search for printer paper
      And Open the first product search result
      And Click Add to cart button
      And Close suggestion side section
      Then Verify cart has 1 item


