Feature: sendButton

  Scenario: Verify send button
    Given user should be login into the application with valid username and password
    When user should able to open the messanger
    Then verify send button is displayed
    And user logout from the application

