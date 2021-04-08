Feature: Login to Trello
  As a user,
  I want to Login
  So that I can use the featurees

  Scenario Outline: Login with wrong credentials
    Given the Tello page is displayed
    When the user wants to login with <attlasian> <login> login and <password> password
    Then login fails

    Examples:
      |   login     |  password   | attlasian |
      | fake_login  | fake_passw  |   False   |
      | fake_login_2| fake_passw_2|   False   |