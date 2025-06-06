# Created by mason at 6/6/2025
Feature: Add one product to cart
  # Enter feature description here

  Scenario: Add one product to cart
    Given Open target main page
    When Click add to cart
    Then Click add to cart from popup
    Then Click view cart
    Then Verify product is in cart

