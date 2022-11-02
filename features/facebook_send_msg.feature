Feature: send_Msg

  Scenario Outline: Send a message to my friend
    Given user should be login into the application with valid username and password
    When user should able to open the messanger
    Then send a msg to friend as "<message>"
    And user logout from the application
    Examples:
      | message          |
      |Good Morning      |
      |What are you doing|
      |Be happy Always   |

