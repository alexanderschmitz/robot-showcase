*** Settings ***
Library           FlaUILibrary
Library    AutoItLibrary


*** Test Cases ***
Add Two Numbers In Calculator
    Launch Application    calc.exe
    Sleep  1s
    ${windows}=    List Open Windows
    FOR    ${window}    IN    @{windows}
        Run Keyword If    'Calc' in '${window}'    Attach Application By Name    ${window}
        Exit For Loop If    'Calc' in '${window}'
    END

    
    Click    Name:Two
    Click    Name:Plus
    Click    Name:Three
    Click    Name:Equals

    ${result}=    Get Text From Textbox    AutomationId:CalculatorResults
    Should Contain    ${result}    Display is 5

    Close Application    ${pid}
