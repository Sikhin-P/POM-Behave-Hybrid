Feature: Login Page
Scenario: Navigate to Login page
  Given Open "https://phptravels.net"
  When Move to login page
  Then Login page should be loaded
Scenario: Login using valid credentials
  Given Wait for login page
  When enter "admin@phptravels.com" and "demoadmin" as credentials
  Then Dashboard should be loaded.
Scenario: Logout
  When Click on Logout option
  Then User should be logged out

Scenario: Invalid Login
  Given Click on login option
  When Enter invalid credentials "example@example" and "password"
  Then Error message should be appeared.