# __*__ coding: utf-8 __*__
import os
import re
import zipfile

TEMP_ROOT = os.path.join(os.getcwd(), 'temp')
TEMP_SRC_ROOT = os.path.join(os.getcwd(), 'temp-src')


class StartUp:
    def __init__(self, root_path=os.getcwd(),
                 decompile_jar_path=os.path.join(os.getcwd(), 'lib', 'clazz-parse-1.0-SNAPSHOT.jar')):
        self.root_path = root_path
        self.decompile_jar_path = decompile_jar_path
        self.jar_file_list = []

    def process(self):
        jar_file_list = self.__get_sum_file()
        for jar_file in jar_file_list:
            jar_unzip_path, jar_src_path = self.__get_temp_path(jar_file)
            clazz_list = self.unzip_jar(jar_file, jar_unzip_path)
            self.de_compile(clazz_list, jar_src_path)
            print('Parse jar: [%s] complete...next..' % jar_file)

    def __get_sum_file(self, path=None, re_str=r'\.jar$'):
        file_list = []
        if path is None:
            path = self.root_path
        file_obj_list = os.walk(path)
        for file_obj in file_obj_list:
            m_dir = file_obj[0]
            for m_file in file_obj[2]:
                file_path = '%s\\%s' % (m_dir, m_file)
                if re.search(re_str, file_path):
                    file_list.append(file_path)
        return file_list

    def unzip_jar(self, jar_file, jar_unzip_path):
        global zip_file
        try:
            zip_file = zipfile.ZipFile(jar_file, 'r')
            zip_file.extractall(path=jar_unzip_path)
            return self.__get_sum_file(jar_unzip_path, r'\.class$')
        finally:
            zip_file.close()

    @staticmethod
    def __get_temp_path(jar_file):
        file_name = re.match(r'.*\\([^\\]*).jar$', jar_file).group(1)
        jar_unzip_path = os.path.join(TEMP_ROOT, file_name)
        jar_src_path = os.path.join(TEMP_SRC_ROOT, file_name)
        return jar_unzip_path, jar_src_path

    def de_compile(self, clazz_list, jar_src_path):
        command = r'java -jar %s' % self.decompile_jar_path
        for clazz in clazz_list:
            cmd = [command, clazz]
            clazz_name = re.match(r'.*\\([^\\]*)', clazz).group(1)
            java_name = re.sub(r'(.*)\.class', r'\1.java', clazz_name)
            cmd.append(os.path.join(jar_src_path, java_name))
            os.system(' '.join(cmd))


app = StartUp()
if __name__ == '__main__':
    app.process()
    # java_file = r'D:\SDK\jdk8\src\org\xml\sax\helpers\SecuritySupport.java'
    # jar_file = r'D:\SDK\jdk8\lib\missioncontrol\plugins\com.jrockit.mc.rjmx_5.5.2.174165\lib\mailapi.jar'
    # clazz_file = r'F:\work_space\pythonSpace\leiax00\basic\CheckJarTool\Employee.class'
    # clazz_name = re.match(r'.*\\([^\\]*)', clazz_file).group(1)
    # java_name = re.sub(r'(.*)\.class', r'\1.java', clazz_name)
    # print(java_name)
    # app.process();
    # result = re.match(r'.*(\.jar|\.class|\.java)$', java_file)
    # print(result.group(1))
    # jarProcessor.process1()
    # jarProcessor.process()
    # jar_path = os.path.join(os.getcwd(), 'clazz-parse-1.0-SNAPSHOT.jar')
    # command = r'java -jar %s' % jar_path
    # cmd = [command]
    # cmd.append(r'F:\work_space\pythonSpace\leiax00\basic\CheckJarTool\Employee.class')
    # cmd.append(r'F:\work_space\pythonSpace\leiax00\basic\CheckJarTool\Employee.java')
    # os.system(' '.join(cmd))
    #  jpype包的用法
    # print(os.path.join(os.path.abspath('.'), r'F:\work_space\pythonSpace\leiax00\basic\CheckJarTool'))
    # jar = os.path.join(os.getcwd(), 'lib', 'clazz-parse-1.0-SNAPSHOT.jar')
    # print(jpype.getDefaultJVMPath())
    # # jpype.startJVM(jpype.getDefaultJVMPath(), '-ea', r"-Djava.class.path=F:\work_space\clazz-parse\target\clazz-parse-1.0-SNAPSHOT.jar")
    # jpype.startJVM(r'D:\SDK\jdk8\jre\bin\server\jvm.dll', '-ea', r"-Djava.class.path=F:\work_space\clazz-parse\target\clazz-parse-1.0-SNAPSHOT.jar")
    # JDClass = JClass("classParse.DeCompiler")
    # jd = JDClass()
    # jd.deCompile(r'F:\work_space\pythonSpace\leiax00\basic\CheckJarTool\Employee.class', r'F:\work_space\pythonSpace\leiax00\basic\CheckJarTool\Employee.java')
    # jpype.shutdownJVM()
