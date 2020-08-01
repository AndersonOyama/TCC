package fuzzyLogic;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.*;

import fuzzyLogic.Text;

import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

import antlr.collections.List;
import net.sourceforge.*;
import net.sourceforge.jFuzzyLogic.FIS;
import net.sourceforge.jFuzzyLogic.FunctionBlock;
import net.sourceforge.jFuzzyLogic.Gpr;
import net.sourceforge.jFuzzyLogic.rule.Rule;
import net.sourceforge.jFuzzyLogic.plot.JFuzzyChart;
import net.sourceforge.jFuzzyLogic.rule.Variable;
import sun.security.util.Length;
import net.sourceforge.jFuzzyLogic.fcl.FclObject;

public class main {

	public static void main(String[] args) throws IOException {
		System.out.println(new java.io.File("").getAbsolutePath());
		File fileXLSX = new File("D:\\Users\\ander\\Documents\\GitHub\\TCC\\resultados.xlsx");
		FileInputStream fis = new FileInputStream(fileXLSX);

		XSSFWorkbook workbook = new XSSFWorkbook(fis);

		XSSFSheet sheet = workbook.getSheetAt(0);

		String FCLfile = "D:\\Users\\ander\\Documents\\GitHub\\TCC\\fuzzyLogic\\fuzzyLogic\\rulesFakeNews.fcl";
		FIS fisFCL = FIS.load(FCLfile, true);

		if (fisFCL == null) {
			System.out.println("Arquivo FCL não encontrado");
			System.exit(0);
		}

		FunctionBlock functionBlock = fisFCL.getFunctionBlock(null);

		JFuzzyChart.get().chart(functionBlock);

		Iterator<Row> rowIt = sheet.iterator();

		ArrayList<Text> textList = new ArrayList<Text>();

		int rowCounter = 0;
		
		boolean first = true;
		
		while (rowIt.hasNext()) {
			Row row = rowIt.next();
			if(first == false) {
				Row rowPos = sheet.getRow(rowCounter);
				Cell text = rowPos.getCell(0);
				Cell porc_error = rowPos.getCell(2);
				Cell share = rowPos.getCell(6);
				Cell sen = rowPos.getCell(8);
				
//				System.out.println("Texto: " + text.getStringCellValue() + ". Erro: " + porc_error.getNumericCellValue()*100 + "%. Comp: " + share.getNumericCellValue() + " Sensa: " + sen.getNumericCellValue() + " .");
				
				fisFCL.setVariable("percentual_erro_gramatical", 100*(porc_error.getNumericCellValue()));
				fisFCL.setVariable("compartilhamento", share.getNumericCellValue());
				fisFCL.setVariable("sensacionalismo", sen.getNumericCellValue());
				
				fisFCL.evaluate();
				Variable result = functionBlock.getVariable("fake");
				functionBlock.getVariable("fake").defuzzify();
//				JFuzzyChart.get().chart(result, result.getDefuzzifier(), true);
//				System.out.println("Fake: " + functionBlock.getVariable("fake").getValue() + "Result: " + result);
				System.out.println(formatador(result.toString()));
				

				try{System.in.read();}
				catch(Exception e){}
				
			}
			System.out.println(rowCounter);
			rowCounter++;
			first = false;
		}

		workbook.close();
		fis.close();

	}
	
	private static String formatador(String result) {
		String[] temp = result.toString().split("Term:");
		String[] verdadeira = temp[1].split("Sigmoidal :");
		String[] inconclusivo = temp[2].split("Gaussian :");
		String[] falsa = temp[3].split("Sigmoidal :");
		
		verdadeira = verdadeira[0].split("	");
		inconclusivo = inconclusivo[0].split("	");
		falsa = falsa[0].split("	");
//		
//		for(String element: verdadeira) {
//			System.out.println(element);
//		}
		
		if( (Float.compare(Float.parseFloat(verdadeira[1]), Float.parseFloat(inconclusivo[1])) > 0) && (Float.compare(Float.parseFloat(verdadeira[1]), Float.parseFloat(falsa[1])) > 0) ) {
			return verdadeira[0];
		} else if ( (Float.compare(Float.parseFloat(inconclusivo[1]), Float.parseFloat(verdadeira[1])) > 0) && (Float.compare(Float.parseFloat(inconclusivo[1]), Float.parseFloat(falsa[1])) > 0) ) {
			return inconclusivo[0];
		} else {
			return falsa[0];
		}

	}
	

}