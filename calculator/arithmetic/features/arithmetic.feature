Feature: Performing basic arithmetic operations

    In order to perform basic arithmetic
    As a person who is bad at maths
    I want to be able to provide 2 numbers and an operator
    and get a result back.
    

Background:
    Given that we will not use numbers greater that 4 digits
       And that we will enter the input in the order number1, number2, operator
    When we send a request to the calculator
    Then the response will start with "Result = "
       And the response will end with a number

        
Scenario: Adding 2 numbers

    Given we use the "add" operator for our operations
        And our first number is <number1>
        And our second number is <number2>
    When we call the calculator with our numbers and operator
    Then the calculator will return the value <result>

        | number1 | number2 | result |

        |    1    |    1    |   2    |
        |    1    |    2    |   3    |
        |    1    |    3    |   4    |
        |    1    |    6    |   4    |


