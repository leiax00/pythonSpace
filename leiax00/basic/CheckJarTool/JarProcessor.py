# __*__ coding: utf-8 __*__
import os
import re
import zipfile

from basic.CheckJarTool.Processor import Processor


class JarProcessor(Processor):
    
    def process(self, file_path):
        temp_path = self.parse_jar(file_path)


    @staticmethod
    def parse_jar(file_path):
        file_name = re.search(r'\\([^\\]*).jar$', file_path).group(1)
        z_file = zipfile.ZipFile(file_path, 'r')
        temp_path = os.path.join(os.getcwd(), 'temp', file_name)
        print(os.getcwd(), temp_path)
        z_file.extractall(path=temp_path)
        z_file.close()
        return temp_path


jarProcessor = JarProcessor()
if __name__ == '__main__':
    jarProcessor.parse_jar(r'F:\work_space\pythonSpace\leiax00\basic\CheckJarTool\resources.jar')

