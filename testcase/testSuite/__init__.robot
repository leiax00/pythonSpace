*** Settings ***
Documentation     中文用例名乱码：修改D:\dev\SDK\python373\lib\site-packages
...               obotide\contrib\testrunner\testrunner.py
...                \ def pop(self):
...                \ \ \ \ result = ""
...                \ \ \ try:
...                \ \ \ \ \ \ myqueuerng = xrange(self._queue.qsize())
...                \ except NameError: \ # py3
...                \ \ \ \ myqueuerng = range(self._queue.qsize())
...               for _ in myqueuerng:
...                \ \ try:
...                \ \ \ \ \ # DEBUG result += self._queue.get_nowait()
...                \ \ \ \ # .decode(utils.SYSTEM_ENCODING, 'replace')
...                \ \ \ # .decode('UTF-8','ignore')
...                \ \ result += encoding.console_decode(self._queue.get_nowait(),
...                \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ 'GBK' if IS_WINDOWS
...                \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ else 'UTF-8')
...               # ,'replace') \ # 'latin1' .decode(utils.SYSTEM_ENCODING,
...               # 'replace') \ # .decode('UTF-8','ignore')
...               except Empty:
...               pass
...               return result \ # DEBUG .decode('UTF-8', 'ignore')
...
...               RF命令行执行命令:
...               \ robot --pythonpath E:\work_space\pythonSpace\testcase\Library E:\work_space\pythonSpace\testcase
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
