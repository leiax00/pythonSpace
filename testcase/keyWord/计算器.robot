*** Settings ***
Library           ../../leiax00/RF/tryyRF.py

*** Keywords ***
加法
    [Arguments]    ${a}    ${b}
    ${a}    Convert To Number    ${a}
    ${b}    Convert To Number    ${b}
    ${result}    add    ${a}    ${b}
    [Teardown]
    [Return]    ${result}
