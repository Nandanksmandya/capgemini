Feature: mute_chats


  Scenario: mute_notification
    Given user should be login into the application with valid username and password
    When user should able to open the messanger
    Then user mute the chat and call for 8 hours
    And user logout from the application




