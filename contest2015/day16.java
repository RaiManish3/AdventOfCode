import java.util.*;
import java.io.*;

public class day16{
	static HashMap<String,Integer> ref = new HashMap<String,Integer>();

	public static void main(String[] args) {
		try{
				FileReader file = new FileReader(new File("day16.txt"));
				BufferedReader br = new BufferedReader(file);
				String line;

				// fill the hashmap ref
				ref.put("children",6);
				ref.put("cats",7);
				ref.put("samoyeds",2);
				ref.put("pomeranians",3);
				ref.put("akitas",0);
				ref.put("vizslas",0);
				ref.put("goldfish",5);
				ref.put("trees",3);
				ref.put("cars",2);
				ref.put("perfumes",1);

				String answer=null;
		
				while((line=br.readLine())!=null){

					String[] str_arr = line.split("\\s");

					String x1 = str_arr[2].substring(0,str_arr[2].length()-1);
					int x2 = Integer.parseInt(str_arr[3].substring(0,str_arr[3].length()-1));
					String x3 = str_arr[4].substring(0,str_arr[4].length()-1);
					int x4 = Integer.parseInt(str_arr[5].substring(0,str_arr[5].length()-1));
					String x5 = str_arr[6].substring(0,str_arr[6].length()-1);
					int x6 = Integer.parseInt(str_arr[7]);

					// --------------part 1
					// if (ref.get(x1)==x2 && ref.get(x3)==x4 && ref.get(x5)==x6) {
					// 	answer=str_arr[1].substring(0,str_arr[1].length()-1);
					// 	break;
					// }

					// --------------part 2
					if(chk_str(x1,x2) && chk_str(x3,x4) && chk_str(x5,x6)){
						answer=str_arr[1].substring(0,str_arr[1].length()-1);
						break;
					}

				}

				System.out.println(answer);

			}catch (Exception e) {
				System.out.println(e);
			}
	}

	public static boolean chk_str(String x,int y){
		if(x.equals("cats") || x.equals("trees")){
			if(y>ref.get(x))
				return true;
		}

		else if(x.equals("pomeranians") || x.equals("goldfish")){
			if(y<ref.get(x))
				return true;
		}

		else if(ref.get(x)==y){
			return true;
		}

		return false;
	}
}