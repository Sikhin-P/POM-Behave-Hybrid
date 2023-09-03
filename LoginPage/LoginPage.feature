Feature: Login Page
Scenario: Navigate to Login page
  Given Open "https://phptravels.net"
  When Move to login page
  Then Login page should be loaded
Scenario: Login using valid credentials
  Given Wait for login page
  When enter "admin@phptravels.com" and "demoadmin" as credentials
  Then Dashboard should be loaded.
