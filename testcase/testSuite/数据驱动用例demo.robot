*** Settings ***
Test Template     模板keyword

*** Test Cases ***    expression    expected_result
data_table            2*2           4
                      2+6           8
                      6/2           3
                      6%4           2

*** Keywords ***
模板keyword
    [Arguments]    ${expression}    ${expected_result}
    ${result}    Evaluate    ${expression}
    should be equal as integers    ${result}    ${expected_result}
