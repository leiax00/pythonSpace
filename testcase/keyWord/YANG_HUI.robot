*** Settings ***
Library           ../../leiax00/basic/datatype/tryGenerator.py

*** Keywords ***
杨辉三角
    [Arguments]    ${lines}
    ${lines}    Convert To Number    ${lines}
    ${result}    yang_hui    ${lines}
    [Return]    ${result}