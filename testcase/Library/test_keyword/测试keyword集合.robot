*** Keywords ***
should be equal as list
    [Arguments]    ${list_1}    ${list_2}
    ${result}    is_equal_for_list    ${list_1}    ${list_2}
    should be true    ${result}

should be equal as dict
    [Arguments]    ${dict_1}    ${dict_2}
    ${result}    is_equal_for_dict    ${dict_1}    ${dict_2}
    should be true    ${result}
