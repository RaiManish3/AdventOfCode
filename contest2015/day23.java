import java.util.*;
import java.io.*;

public class day23{
	public static void main(String[] args) {
		try{
			FileReader file = new FileReader(new File("day23.txt"));
			BufferedReader br = new BufferedReader(file);
			String line;
			ArrayList<List<String>> input = new ArrayList<List<String>>();
	
			while((line=br.readLine())!=null)
				input.add(Arrays.asList(line.split("\\s")));

			System.out.println(input);
			long a=1,b=0;
			int index=0,l=input.size();

			while(index<l){
				String x1 = input.get(index).get(0);
				String x2 = input.get(index).get(1);

				if(x1.equals("jio")){
					if(a==1)
						index+=Integer.parseInt(input.get(index).get(2));
					else
						index+=1;
				}

				if(x1.equals("jie")){
					if(a%2==0)
						index+=Integer.parseInt(input.get(index).get(2));
					else
						index+=1;
				}

				else if (x1.equals("inc")) {
					if(x2.equals("a"))
						a+=1;
					else b+=1;
					index+=1;
				}

				else if (x1.equals("hlf")){
					if(x2.equals("a"))
						a/=2;
					else b/=2;
					index+=1;
				}

				else if (x1.equals("tpl")){
					if(x2.equals("a"))
						a*=3;
					else b*=3;
					index+=1;
				}

				else if(x1.equals("jmp")){
					index+=Integer.parseInt(x2);
				}

				System.out.println(a+ " :: "+b +" :: "+index);
			}

			System.out.println(a+ " :: "+b);

		}catch (Exception e) {
			System.out.println(e);
		}
	}
}