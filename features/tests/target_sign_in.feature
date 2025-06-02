Feature: Sign in form opens for a signed out user

  Scenario: A user who isn't logged in sees a sign in form
    Given Open target main page
    Then click "sign in"
    Then From right side navigation menu, click Sign In
    Then Verify sign in form displays