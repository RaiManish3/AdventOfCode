import java.util.*;
import java.io.*;

/* 
	HOW TO INSERT A LIST WITHIN ANOTHER:
		CREATE AN ARRAYLIST<LIST<TYPE>> 
		AT THE TIME OF ADDING CONVERT THAT INITIAL ARRAY 
		TO A LIST USING ARRAYS.ASLIST

*/

public class day7{

	static HashMap<String,Integer> dic = new HashMap<String, Integer>();
	static ArrayList<String> var_list = new ArrayList<String>();

	public static void main(String[] args) {
		File file_i = new File("day7.txt");
		long startTime = System.currentTimeMillis();

		// LEARN OUTPUTTING---------------------------------------------
		// File file_o = new File("test.txt");
		// try{
		// 	// writing to a file
		// 	PrintWriter output =new PrintWriter(file_o);
		// 	output.println("Manish Rai.");
		// 	output.println(42);
		// 	output.close();
		// }catch(IOException ex){
		// 	System.out.printf("ERROR :  %s\n", ex);
		// }


		// LEARN INPUTTING-----------------------------------------------
		try{

			// Take input--------------------------------------
			Scanner input = new Scanner(file_i);
			String[] line = input.nextLine().trim().split("\\s+");
			ArrayList<List<String>> lst = new ArrayList<List<String>>();	

			int line_size;
			while(input.hasNext()){

				// this is how we implement a multidimensional list
				lst.add(Arrays.asList(line));

				line_size = line.length;
				if(line_size==3)
					assign_val(Arrays.asList(line));

				if(line_size==4)
					not(Arrays.asList(line));

				if(line_size==5){
					if(line[1].length()==6){
						gen2(Arrays.asList(line));
					}
					else gen1(Arrays.asList(line));
				}

				line=input.nextLine().trim().split("\\s+");
			}

			int i=0;
			int mod=lst.size();
			while(var_list.size()>0){
				line_size = lst.get(i).size();
				if(line_size==3){
					assign_val(lst.get(i));
				}

				if(line_size==4)
					not(lst.get(i));

				if(line_size==5){
					if(lst.get(i).get(1).length()==6){
						gen2(lst.get(i));
					}
					else gen1(lst.get(i));
				}

				i=(i+1)%mod;
			}

			System.out.println(dic.get("a"));
			System.out.println(System.currentTimeMillis()-startTime + "ms");


		}catch(IOException ex){
				System.out.printf("ERROR :  %s\n", ex);
			}
	}

	public static void the_else_case(List<String> x,int x1,int x2){
		if(!var_list.contains(x.get(x1)) && !dic.containsKey(x.get(x1)))
			var_list.add(x.get(x1));
		if(!var_list.contains(x.get(x2)) && !dic.containsKey(x.get(x2)))
			var_list.add(x.get(x2));
	}

	public static void the_else_case2(List<String> x,int x1,int x2,int x3){
		the_else_case(x,x1,x2);
		if(!var_list.contains(x.get(x3)) && !dic.containsKey(x.get(x3)))
			var_list.add(x.get(x3));
	}


	public static void assign_val(List<String> x){
		try{
			int k = Integer.parseInt(x.get(0));
			dic.put(x.get(2),k);

			// remove from var_list
			if(var_list.contains(x.get(2)))
				var_list.remove(x.get(2));
		}catch(NumberFormatException e){

			if(dic.containsKey(x.get(0))){
				dic.put(x.get(2),dic.get(x.get(0)));


				if(var_list.contains(x.get(2)))
					var_list.remove(x.get(2));
			}

			else {
				the_else_case(x,0,2);
			}
		}
	}

	public static void not(List<String> x){
		try{
			int k = Integer.parseInt(x.get(1));
			dic.put(x.get(3),65535-k);
			if(var_list.contains(x.get(3))){
				var_list.remove(x.get(3));
			}
		}catch(NumberFormatException e){
			if(dic.containsKey(x.get(1))){
				dic.put(x.get(3),65535-dic.get(x.get(1)));
				if(var_list.contains(x.get(3))){
					var_list.remove(x.get(3));
				}
			}
			else{
				the_else_case(x,1,3);
			}
		}
	}

	public static void and_or(List<String> x,int n1,int n2){
		if(x.get(1).equals("AND"))
				dic.put(x.get(4),n1 & n2);
			else 
				dic.put(x.get(4),n1 | n2);
	}

	public static void gen1(List<String> x){
		try{
			int k1 = Integer.parseInt(x.get(0));
			int k2 = Integer.parseInt(x.get(2));
			and_or(x,k1,k2);

			if(var_list.contains(x.get(4)))
				var_list.remove(x.get(4));

		}catch(NumberFormatException e){
			try{
				int k1 = Integer.parseInt(x.get(0));
				if(dic.containsKey(x.get(2))){
					and_or(x,k1,dic.get(x.get(2)));
					if(var_list.contains(x.get(4)))
						var_list.remove(x.get(4));
				}

				else
					the_else_case(x,2,4);

			}catch(NumberFormatException e1){
					try{
						int k2 = Integer.parseInt(x.get(2));
						if(dic.containsKey(x.get(0))){
							and_or(x,k2,dic.get(x.get(0)));
							if(var_list.contains(x.get(4)))
								var_list.remove(x.get(4));
						}

						else
							the_else_case(x,0,4);
				
					}catch(NumberFormatException e2){
						if(dic.containsKey(x.get(2)) && dic.containsKey(x.get(0))){
							and_or(x,dic.get(x.get(0)),dic.get(x.get(2)));
							if(var_list.contains(x.get(4)))
								var_list.remove(x.get(4));
						}
						else 
							the_else_case2(x,0,2,4);
					}
				}
			}
		}

	public static void gen2(List<String> x){
		if(dic.containsKey(x.get(0))){
			int k = Integer.parseInt(x.get(2));
			if(x.get(1).equals("RSHIFT")){
				dic.put(x.get(4),(dic.get(x.get(0))>>k) & 65535);
			}
			else{
				dic.put(x.get(4),(dic.get(x.get(0))<< k) & 65535);
			}

			if(var_list.contains(x.get(4)))
				var_list.remove(x.get(4));

		}

		else
			the_else_case(x,0,4);
	}

}
