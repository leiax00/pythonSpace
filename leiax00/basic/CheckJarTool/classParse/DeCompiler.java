package classParse;

import jd.core.loader.Loader;
import jd.core.process.DecompilerImpl;
import org.jd.gui.util.decompiler.GuiPreferences;

import java.io.File;

public class DeCompiler {

    public void deCompile(String srcPath, String dstPath) {
        DecompilerImpl decompiler = new DecompilerImpl();
        Loader loader = new ClazzLoader(srcPath);
        CustomPrinter printer = new CustomPrinter();
        GuiPreferences preferences = new GuiPreferences();
        System.out.println(new File(srcPath).getParent());
        try {
            decompiler.decompile(preferences, loader, printer, new File(srcPath).getParent());
            printer.print2File(dstPath);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}
