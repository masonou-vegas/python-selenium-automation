Feature: Sign in form opens for a signed out user

  Scenario: A user who isn't logged in sees a sign in form
    Given Open target main home page
    Then Click sign in on homepage
    Then Click sign in on pop up
    Then Sign in form displays