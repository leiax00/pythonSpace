*** Settings ***
Resource          ../keyWord/计算器.robot

*** Test Cases ***
加法
    ${result}    加法    1    2
    Should Be Equal As Numbers    ${result}    3
