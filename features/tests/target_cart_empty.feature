Feature: “Your cart is empty” message is shown in cart

  Scenario: A user with an empty cart sees a message
    Given Open target main page
    When Click on cart Icon
    Then Verify “Your cart is empty” message is shown

