import java.util.*;
import java.io.*;

// part 2 unsolved
// takes forever to show the result
// forum says randomised algorithm works.

public class day19{

	static HashMap<String,List<String>> dic = new HashMap<String,List<String>>();
	static String molecule = "";

	static int min_steps =1000000;

	public static void main(String[] args) {
		try{
			FileReader file = new FileReader(new File("day19.txt"));
			BufferedReader br = new BufferedReader(file);
			String line;
			int size1=43;
			String[] strx;
			ArrayList<String> ll = new ArrayList<String>();
			String prev="Al";

			// creating the dictionary

			for(int i=0;i<size1;i++){
				line=br.readLine().trim();
				strx=line.split("\\s");

				// search why the follwing doesnot work
				// if(dic.containsKey(strx[0])){
				// 	dic.get(strx[0]).add(strx[2]);
				// 	}			
				// else {
				// dic.put(strx[0],Arrays.asList(new String[]{strx[2]}));
				// }

				if(prev.equals(strx[0])){
					ll.add(strx[2]);
				}
				else{
						dic.put(prev,new ArrayList<String>(ll));
						ll.clear();
						ll.add(strx[2]);
				}
				prev=strx[0];
			}

			dic.put(prev,new ArrayList<String>(ll));
			line=br.readLine();
			molecule = br.readLine().trim();
// ---------------------------------------------------------------------------
			
			// part 1
			// ArrayList<String> distict_molecules = new ArrayList<String>();
			// int l= molecule.length();
			// String new_mol="";
			// molecule+="@";

			// for (int i=0;i<l ;) {
			// 	String s1 =String.valueOf(molecule.charAt(i));
			// 	String s2 =s1+String.valueOf(molecule.charAt(i+1));
				
			// 	if(dic.containsKey(s1)){
			// 		for (int j=0;j<dic.get(s1).size();j++){
			// 			new_mol=molecule.substring(0,i)+dic.get(s1).get(j)+molecule.substring(i+1,l);
			// 			if(!distict_molecules.contains(new_mol))
			// 				distict_molecules.add(new_mol);
			// 		}
			// 		i+=1;
			// 	}

			// 	else if(dic.containsKey(s2)){
			// 		for (int j=0;j<dic.get(s2).size();j++){
			// 			new_mol=molecule.substring(0,i)+dic.get(s2).get(j)+molecule.substring(i+2,l);
			// 			if(!distict_molecules.contains(new_mol))
			// 				distict_molecules.add(new_mol);
			// 		}
			// 		i+=2;
			// 	}

			// 	else i+=1;
			// }

			// System.out.println(distict_molecules.size());
// ---------------------------------------------------------------------------


			// part 2
			String strz="e";
			recur(strz,0,0);
			System.out.println(min_steps);


		}catch (Exception e) {
			System.out.println(e);
		}
	}

	public static boolean match(String x){
		if(dic.containsKey(x))
			return true;
		return false;
	}

	public static void recur(String strx, int index, int step){

		System.out.println(index);
		if(index==30)System.out.println("--------------------------------------------------");

		if(step>min_steps || strx.length()>molecule.length()||index>=molecule.length() || index>=strx.length())return;

		if(strx.equals(molecule)){
			if(step<min_steps)
				min_steps=step;
			return;
		}

		String s1 =String.valueOf(molecule.charAt(index));
		String s2 =String.valueOf(strx.charAt(index));
		String s3;
		if(index+1<strx.length())
			s3 =String.valueOf(strx.charAt(index+1));
		else s3 = "";

		if(!dic.containsKey(s2) && !dic.containsKey(s2+s3) && !s1.equals(s2))
			return;

		if(s1.equals(s2)){
			int tt=0;
			while(strx.charAt(index+tt)==molecule.charAt(index+tt))
				tt+=1;
			recur(strx,index+tt,step);
		}
		
		if(dic.containsKey(s2)){
			for(int i=0;i<dic.get(s2).size(); i++){
				String tmp = strx.substring(0,index)+dic.get(s2).get(i)+strx.substring(index+1,strx.length());
				recur(tmp,index,step+1);
			}
		}

		else if(dic.containsKey(s2+s3)){
			for(int i=0;i<dic.get(s2+s3).size();i++){
				String tmp = strx.substring(0,index)+dic.get(s2+s3).get(i)+strx.substring(index+2,strx.length());
				recur(tmp,index,step+1);
			}
		}
	}

}
