import java.util.*;
import java.io.*;

public class day24{

	static ArrayList<Integer> lst = new ArrayList<Integer>();
	static int upto;
	static int t_sum;
	static int min_loads=100;
	static long min_qe = 100000;
	static int l;

	public static void main(String[] args) {
		try{
			FileReader file = new FileReader(new File("day24.txt"));
			BufferedReader br = new BufferedReader(file);
			String line;

			while((line=br.readLine())!=null){
				int x= Integer.parseInt(line);
				lst.add(x);
				t_sum+=x;

			}

			l=lst.size();
			upto=2*lst.size()/3;
			// part 1-------------
			// t_sum/=3;
			// part 2-------------
			t_sum/=4;
			System.out.println(t_sum+" : "+upto);

			recur(0,1,0,true,l-1);
			System.out.println(min_loads+" : "+min_qe);

		}catch (Exception e) {
			System.out.println(e);
		}
	}

	public	static void recur(int p_sum,long qe,int loads,boolean notbelowthis,int i){
		if(p_sum>t_sum || loads>min_loads)return;

		if(p_sum==t_sum){
			if(min_loads>loads || (min_loads==loads && min_qe>qe)){
				min_loads=loads;
				min_qe=qe;
			}
		}

		for(;i>=0;i--){
			if(i<upto && notbelowthis)
				return;
			recur(p_sum+lst.get(i),qe*lst.get(i),loads+1,false,i-1);
		}

	}

}