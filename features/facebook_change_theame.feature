Feature: mute_chats


  Scenario Outline: mute_notification
    Given user should be login into the application with valid username and password
    When user should able to open the messanger
    Then user can change the "<theme>"
    And user logout from the application
    Examples:
      |   theme         |
      |Doctor Strange   |
      |Lavender         |
      |Support          |






