
Feature: Confirming that Selenium is set up correctly

    Scenario: Check that we can confirm the title of the home page
        When I go to the home page
        Then I should see that the title is "Google"