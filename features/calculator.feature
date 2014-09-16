
Feature: Confirming that the tip calculator form works

    Scenario: Check that the form displays
        When I go to the tip calculator page
        Then I will see the calculator form


    Scenario: Check that the form submits successfully
        When I go to the tip calculator page
        And I submit the form with a valid total and tip percentage
        Then I should see the results page