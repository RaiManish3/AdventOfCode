import java.util.*;
import java.io.*;

public class day14{
	static int[][] data_in = {{8,0,8,53},{13,0,4,49},{20,0,7,132},{12,0,4,43},{9,0,5,38},{10,0,4,37},{3,0,37,76},{9,0,12,97},{37,0,1,36}};
	static int[] distance = new int[9];
	static int[] points = new int[9];


	public static void main(String[] args) {
		for(int t=1;t<=2503;t++){
			for(int k=0;k<9;k++)
				update_arr(k,t);
			update_points();
		}

		for(int k=0;k<9;k++)
			System.out.println(points[k]);
	}

	public static void update_arr(int index,int time){
		if(time>data_in[index][1] && time<=data_in[index][2])
			distance[index]+=data_in[index][0];
		if(time==data_in[index][2]+data_in[index][3]){
			int tmp = data_in[index][2] -data_in[index][1];
			data_in[index][1]=data_in[index][2]+data_in[index][3];
			data_in[index][2]=data_in[index][1]+tmp;
		}
	}


	public static void update_points(){
		int max=0;
		for(int k=0;k<9;k++)
			if(max<distance[k]){
				max=distance[k];
			}

		for(int k=0;k<9;k++){
			if(distance[k]==max){
				points[k]+=1;
			}
		}
	}
}