# __*__ coding: utf-8 __*__
import os
import re

# processor = {
#     'jar': JarProcessor(),
#     'class': ClazzProcessor();
#     'java': JavaProcessor();
# }
from basic.CheckJarTool.JarProcessor import jarProcessor


class StartUp:

    def __init__(self, root_path=os.getcwd()):
        self.root_path = root_path

    def process(self):
        file_list = self.__get_sum_file()


    def __get_sum_file(self):
        dst_file_list = []
        file_obj_list = os.walk(self.root_path)
        for file_obj in file_obj_list:
            dir = file_obj[0]
            for file in file_obj[2]:
                file_path = '%s\\%s' % (dir, file)
                result = re.search(r'(\.jar|\.class|\.java)$', file_path)
                if result is not None:
                    dst_file_list.append(file_path)
                    print(file_path)
        return dst_file_list


app = StartUp()
if __name__ == '__main__':
    java_file = r'D:\SDK\jdk8\src\org\xml\sax\helpers\SecuritySupport.java'
    jar_file = r'D:\SDK\jdk8\lib\missioncontrol\plugins\com.jrockit.mc.rjmx_5.5.2.174165\lib\mailapi.jar'
    clazz_file = r'F:\work_space\pythonSpace\leiax00\basic\CheckJarTool\Employee.class'
    app.process();
    # result = re.match(r'.*(\.jar|\.class|\.java)$', java_file)
    # print(result.group(1))
    jarProcessor.process1()
    jarProcessor.process()
