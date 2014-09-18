
Feature: Confirming that the tip calculator form works

    Scenario: Check that the form displays
        When I go to the tip calculator page
        Then I will see the calculator form


    Scenario: Check that the form submits successfully
        When I go to the tip calculator page
        And I submit the form with a valid total and tip percentage
        Then I should see the results page


    Scenario: Check that the correct tip amount is calculated
        When I enter $50 as the total meal cost
        And I enter 20% as the tip percentage
        And I submit the form
        Then I should see $10 dollars as the tip in the results page