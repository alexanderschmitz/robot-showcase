*** Settings ***
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
    Get Active Window Image    result.png

    # Optionally, capture result if visible in UI (hard with AutoIt alone)
    # We will just sleep to allow user to observe
    Sleep   2s

    # Close calculator
    Win Close    Calculator
