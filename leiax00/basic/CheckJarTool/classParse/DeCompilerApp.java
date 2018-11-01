package classParse;



public class DeCompilerApp {

    /**
     * @param args 传入两个参数： class的path路径，和转成java文件后的保存路径
     */
    public static void main(String[] args) {
        new DeCompiler().deCompile(args[0], args[1]);
    }

}
