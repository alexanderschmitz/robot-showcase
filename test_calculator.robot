*** Settings ***
Library    cv_library/OpenCVLibrary.py
Library    os_library/OSLibrary.py
Library    Screenshot


*** Test Cases ***
Add Two Numbers In Calculator
    Launch App    C:/Windows/System32/calc.exe
    Wait For Window    Calculator
    Click Button    Two
    Click Button    Plus
    Click Button    Three
    Click Button    Equals
    ${result}=    Get Text    CalculatorResults
    Should Contain    ${result}    Display is 5

    Take Screenshot    result.png

    Close App
