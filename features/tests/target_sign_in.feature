Feature: Sign in form opens for a signed out user

  Scenario: A user who isn't logged in sees a sign in form
    Given Open target main page
    Then Click sign in on homepage
    Then Click sign in on pop up
    Then Sign in form displays


    Scenario: A user can sign in successfully
      Given Open target main page
      Then Click sign in on homepage
      Then Click sign in on pop up
      Then Sign in form displays
      When Input test@email.com
      When Click continue button
      When Input password
      When Click sign in with password button
      Then User is logged in


  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open sign in page
    When Store original window
    Then Click on Target terms and conditions link
    Then Switch to the newly opened window
    Then Verify Terms and Conditions page is opened
    Then User can close new window and switch back to original

