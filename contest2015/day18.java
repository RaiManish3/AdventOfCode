import java.util.*;
import java.io.*;

public class day18{	
	public static void main(String[] args) {
		try{
			FileReader file = new FileReader(new File("day18.txt"));
			BufferedReader br = new BufferedReader(file);
			ArrayList<List<String>> old_state = new ArrayList<List<String>>();
			// ArrayList<List<String>> new_state = new ArrayList<List<String>>();

			String line;
			int steps = 100;

			while((line=br.readLine())!=null){
				String[] strx = line.split("\\s");
				old_state.add(Arrays.asList(strx));
			}

			ArrayList<List<String>> new_state = new ArrayList<List<String>>(old_state);
			int l = old_state.size();
			String strx="";

			for(int i=0;i<steps;i++){
				// change the state
				for(int j=0;j<l;j++){
					strx="";
					for(int k=0;k<l;k++){
						// part 2
						// also changed the txt file accordingly.
						if((j==0 && k==0)||(j==0 && k==l-1)||(j==l-1 && k==0)||(j==l-1 && k==l-1))
							strx+="#";
						else if(chk_ngbr(j,k,old_state))
							strx+="#";
						else strx+=".";
					}
					new_state.set(j,Arrays.asList(strx));
				}
				old_state = new ArrayList<List<String>>(new_state);
			}

			System.out.println(count_on(new_state));


		}catch (Exception e) {
			System.out.println(e);
		}
	}

	public static void print_state(ArrayList x){
		System.out.println("---------------------------------------------------------------------------------------------------------------------------------------------");
		for(int i=0;i<x.size();i++)
			System.out.println(x.get(i));
		System.out.println("---------------------------------------------------------------------------------------------------------------------------------------------");
	}

	public static int count_on(ArrayList<List<String>> x){
		int count=0;
		for(int i=0;i<x.size();i++)
			for(int j=0;j<x.size();j++)
				if(x.get(i).get(0).charAt(j)=='#')
					count+=1;

		return count;
	}

	public static boolean chk_ngbr(int i,int j,ArrayList<List<String>> x){
		int y = count_ngbr_on(i,j,x);
		if(x.get(i).get(0).charAt(j)=='#'){
			if(y==2 || y==3)
				return true;
			return false;
		}
		else{
			if(y==3)return true;
			return false;
		}

	}

	public static int count_ngbr_on(int i,int j,ArrayList<List<String>> x){
		int on=0;
		if(i-1>=0 && j-1>=0 && x.get(i-1).get(0).charAt(j-1)=='#')
			on+=1;
		if(i-1>=0 && x.get(i-1).get(0).charAt(j)=='#')
			on+=1;
		if(i-1>=0 && j+1<100 && x.get(i-1).get(0).charAt(j+1)=='#')
			on+=1;
		if(j-1>=0 && x.get(i).get(0).charAt(j-1)=='#')
			on+=1;
		if(j+1<100 && x.get(i).get(0).charAt(j+1)=='#')
			on+=1;
		if(i+1<100 && j-1>=0 && x.get(i+1).get(0).charAt(j-1)=='#')
			on+=1;
		if(i+1<100 && x.get(i+1).get(0).charAt(j)=='#')
			on+=1;
		if(i+1<100 && j+1<100 && x.get(i+1).get(0).charAt(j+1)=='#')
			on+=1;

		return on;

	}

}