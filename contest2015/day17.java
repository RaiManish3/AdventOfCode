import java.util.*;
import java.io.*;

public class day17{
	static int[]  containers = {43,3,4,10,21,44,4,6,47,41,34,17,17,44,36,31,46,9,27,38};
	static int vol = 150 ;
	static int ways = 0;
	static int[] used = {-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1};
	static int l = containers.length;

	// part 2
	static int min_containers = 1638;
	static int ways_in_min = 0;

	public static void main(String[] args) {
		recur(0,0,0,0);
		System.out.println("Part 1----------------------");
		System.out.println(ways);
		System.out.println("Part 2----------------------");
		System.out.println(min_containers);
		System.out.println(ways_in_min);
	}

	// third parameter is for avoiding repetition
	public static void recur(int sum,int arr_index,int k,int numCon){
		if(sum==vol){
			ways+=1;
			// number of containers < present minima : resst min_ways
			if(numCon<min_containers){
				min_containers=numCon;
				ways_in_min=0;
			}
			// if they are same increment min_ways
			if(numCon==min_containers)
				ways_in_min++;
			return;
		}
		if(sum>vol)return;

		for(int i=k;i<l;i++){
			if(!contain_this(i)){
				// store the index in used list
				used[arr_index]=i;
				recur(sum+containers[i],arr_index+1,i+1,numCon+1);
				used[arr_index]=-1;
			}
		}
	}


	public static boolean contain_this(int ind){
		for(int i=0;i<used.length;i++)
			if(ind==used[i])return true;
		return false;
	}
}