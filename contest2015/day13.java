import java.util.*;
import java.io.*;

public class day13 {
	static HashMap<Integer, int[]> pair_dic = new HashMap<Integer, int[]>();
	static int[][] data_in = {{0,54,-81,-42,89,-89,97,-94,0},
								{3,0,-70,-31,72,-25,-95,11,0},
								{-83,8,0,35,10,61,10,29,0},
								{67,25,48,0,-65,8,84,9,0},
								{-51,-39,84,-98,0,-20,-6,60,0},
								{51,79,88,33,43,0,77,-3,0},
								{-14,-12,-52,14,-62,-18,0,-17,0},
								{-36,76,-34,37,40,18,7,0,0},
								{0,0,0,0,0,0,0,0,0}};

	// test case set size =4 too.
	// static int[][] data_in = {{0,54,-79,-2},{83,0,-7,-63},{-62,60,0,55},{46,-7,41,0}};

	static int max_happy=0;
	static int size = 9;

	public static void main(String[] args) {
		for(int i=0;i<size;i++){
				pair_dic.put(i,new int[]{0,-1,-1});
		}

		recur(0,0);
		System.out.println(max_happy);
	}


	public static void recur(int index, int happy){
		
		if(index>=size){
			if(happy>max_happy){
				max_happy=happy;
				System.out.println("-------------------------------------------------------------");
				System.out.println("happy : "+happy);
				for (int x=0;x<size;x++ ) {
					System.out.println(x+" : "+pair_dic.get(x)[1]+" "+pair_dic.get(x)[2]);	
				}
			}
			return;
		}

		int c=pair_dic.get(index)[0];

		if(c==2)
			recur(index+1,happy+data_in[index][pair_dic.get(index)[1]]+data_in[index][pair_dic.get(index)[2]]);

		// if the element is connected to zero other elements
		else if(c==0){
			for(int i=0;i<size;i++){
				for(int j=i+1;j<size;j++){
					// taking the same object
					if(i==index)break;
					if(j==index)continue;
					if(pair_dic.get(j)[0]==2)
						continue;
					if(pair_dic.get(i)[0]==2)
						break;

					// if(search_this(i,j))continue;

					// increasing the pair count
					if(pair_dic.get(i)[0]==0){
						pair_dic.put(i,new int[]{1,index,-1});
					}
					else pair_dic.put(i,new int[]{2,pair_dic.get(i)[1],index});

					if(pair_dic.get(j)[0]==0){
						pair_dic.put(j,new int[]{1,index,-1});
					}
					else pair_dic.put(j,new int[]{2,pair_dic.get(j)[1],index});

					// update the index pair_lst
					pair_dic.put(index,new int[]{2,i,j});
					
					recur(index+1,happy+data_in[index][i]+data_in[index][j]);

					// decreasing to previous value
					if(pair_dic.get(i)[0]==1){
						pair_dic.put(i,new int[]{0,-1,-1});
					}
					else pair_dic.put(i,new int[]{1,pair_dic.get(i)[1],-1});

					if(pair_dic.get(j)[0]==1){
						pair_dic.put(j,new int[]{0,-1,-1});
					}
					else pair_dic.put(j,new int[]{1,pair_dic.get(j)[1],-1});

				}
			}
			// to previous value
			pair_dic.put(index,new int[]{0,-1,-1});
		}

		else if(c==1){
			for(int i=0;i<size;i++){
				if(i==index || pair_dic.get(i)[0]==2)continue;
				// remove duplicate entry for same index
				if(pair_dic.get(index)[1]==i)continue;

				// if(search_this(pair_dic.get(index)[1],i))
				// 	continue;

				if(pair_dic.get(i)[0]==0)
					pair_dic.put(i,new int[]{1,index,-1});
				else pair_dic.put(i,new int[]{2,pair_dic.get(i)[1],index});

				pair_dic.put(index,new int[]{2,pair_dic.get(index)[1],i});

				recur(index+1,happy+data_in[index][i]+data_in[index][pair_dic.get(index)[1]]);
				
				if(pair_dic.get(i)[0]==1)
					pair_dic.put(i,new int[]{0,-1,-1});
				else pair_dic.put(i,new int[]{1,pair_dic.get(i)[1],-1});
			}
			pair_dic.put(index,new int[]{1,pair_dic.get(index)[1],-1});
		}
	}


	public static boolean search_this(int i,int j){
		for(int k=0;k<size;k++){
					if((pair_dic.get(k)[1]==i && pair_dic.get(k)[2]==j) ||(pair_dic.get(k)[1]==j && pair_dic.get(k)[2]==i))
						return true;}
		return false;
	}
}