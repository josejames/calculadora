Feature: Calculate
	In order to play add two numbers
	As myself
	We'll implement a calculator

Scenario: add of 2 plus 3
	Given I have the number "2" and the number "3"
	When I add them
	Then I see the number "5"

Scenario: add of 4 plus 6
	Given I have the number "4" and the number "6"
	When I add them
	Then I see the number "10"

Scenario: add of 5 plus 6
	Given I have the number "5" and the number "6"
	When I add them
	Then I see the number "11"

Scenario: subtraction of 4 minus 3
	Given I have the number "4" and the number "3"
	When I substrac them
	Then I see the number "1"

Scenario: subtraction of 3 minus 3
	Given I have the number "3" and the number "3"
	When I substrac them
	Then I see the number "0"

Scenario: subtraction of 2 minus 3
	Given I have the number "2" and the number "3"
	When I substrac them
	Then I see the number "-1"

Scenario: multiplication of 2 times 3
	Given I have the number "2" and the number "3"
	When I multiply them
	Then I see the number "6"

Scenario: multiplication of 3 times 3
	Given I have the number "3" and the number "3"
	When I multiply them
	Then I see the number "9"

Scenario: multiplication of 5 times 6
	Given I have the number "5" and the number "6"
	When I multiply them
	Then I see the number "30"