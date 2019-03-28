*** Settings ***
Resource          ../Library/testcese所有keyword集合.robot

*** Test Cases ***
字典测试
    ${result}    Create Dictionary    a=1    b=2    c=3
    log    ${result}

测试两个list相等
    ${list_1}    create list    a    b    c
    ${list_2}    create list    a    c    b
    should be equal as list    ${list_1}    ${list_2}

测试两个dict相等
    ${dict_1}    create dictionary    a=a    b=b
    ${dict_2}    create dictionary    b=b    a=a
    should be equal as dict    ${dict_1}    ${dict_2}
