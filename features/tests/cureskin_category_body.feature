Feature: Cureskin Shop by category test

    Scenario: Verify user can shop by category 'Body'
        Given Open cureskin main page
        When Click on 'Shop by category'
        And Click on Body
        Then Verify 'Body' is in url

