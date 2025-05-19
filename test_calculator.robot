*** Settings ***
Library    cv_library/OpenCVLibrary.py
Library    os_library/OSLibrary.py
Library    Screenshot
# Library    OperatingSystem


*** Variables ***
${CALCULATOR_PATH}     C:/Windows/System32/calc.exe
${RESULT_IMAGE}        test_input/calculator/two_plus_three_result.png


*** Test Cases ***
Add Two Numbers In Calculator
    Launch App   ${CALCULATOR_PATH}
    Wait For Window    Calculator

    Click Button    Two
    Click Button    Plus
    Click Button    Three
    Click Button    Equals
    ${result}=    Get Text    CalculatorResults
    Should Contain    ${result}    5

    Take Screenshot    result.png
    Close App



*** Test Cases ***
Add Two Numbers With Image Recognition
    Launch App    ${CALCULATOR_PATH}
    Wait For Image    test_input/calculator/two.png    timeout=5

    Click Image          test_input/calculator/two.png
    Click Image          test_input/calculator/plus.png
    Click Image          test_input/calculator/three.png
    Click Image          test_input/calculator/equals.png

    Wait For Image    ${RESULT_IMAGE}    timeout=3
    Find Image    ${RESULT_IMAGE}

    Take Screenshot       result.png
    Close App