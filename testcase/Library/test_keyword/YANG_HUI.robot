*** Settings ***
Resource          ../testcase所有依赖集合.robot

*** Keywords ***
杨辉三角
    [Arguments]    ${lines}
    ${lines}    Convert To Number    ${lines}
    ${result}    yang_hui    ${lines}
    [Return]    ${result}
