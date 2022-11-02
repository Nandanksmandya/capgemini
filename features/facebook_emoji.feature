Feature: change_emoji


  Scenario Outline: mute_notification
    Given user should be login into the application with valid username and password
    When user should able to open the messanger
    Then user change the emoji "<emoji>"
    And user logout from the application
    Examples:
      |   emoji |
      |1        |
      |5        |
      |9        |






