*** Settings ***
Documentation     RF命令行执行命令:
...                \ robot --pythonpath E:\work_space\pythonSpace\testcase\Library E:\work_space\pythonSpace\testcase
...
...               robot
...               --pythonpath E:\work_space\pythonSpace\testcase\Library
...               --argumentfile C:\Users\leiax\AppData\Local\Temp\RIDEvpyrn74j.d\argfile.txt
...               E:\work_space\pythonSpace\testcase
...
...               argfile.txt :
...               --outputdir
...               C:\Users\leiax\AppData\Local\Temp\RIDEvpyrn74j.d
...               -C
...               off
...               -W
...               107
...               --suite
...               Testcase.testSuite.测试用.测试的用例集合
...               --test
...               Testcase.testSuite.测试用.测试的用例集合.测试分步调用python脚本
...               robot --pythonpath E:\work_space\pythonSpace\testcase\Library --outputdir ./log --suite Testcase.testSuite E:\work_space\pythonSpace\testcase
