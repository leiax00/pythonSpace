# __*__ coding: utf-8 __*__
from basic.CheckJarTool.Processor import Processor


class ClazzProcessor(Processor):
    def process(self, file_path):
        with open (file_path) as topic:
            for line in topic.readlines():
                print line


clazzProcessor = ClazzProcessor()
if __name__ == '__main__':
    clazzProcessor.process(r'F:\work_space\pythonSpace\leiax00\basic\CheckJarTool\Employee.class')
