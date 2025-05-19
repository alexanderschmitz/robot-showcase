*** Settings ***
Library    OpenCVLibrary.py
Library    AutoItLibrary


*** Test Cases ***
Add 3 And 5 In Calculator
    Run    calc.exe
    Sleep  1s

    Log To Console    Activate calculator window
    Win Wait Active    Calculator

    Log To Console    Send keys: 3 + 5 =
    Send    3
    Send    {+}
    Send    5
    Send    {ENTER}
    Wait For Image    button.png    timeout=5
    Click Image       button.png

    Get Active Window Image    result.png

    # Close calculator
    Win Close    Calculator