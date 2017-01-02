import java.util.*;
import java.io.*;

public class day20{
	public static void main(String[] args) {
		int[] houses = new int[100000000];
		int divisor_sum = 33100000;

		// this is for part 2
		for (int i=1;;i++) {
			int count =0 ;
			for (int j=i;count<50;j+=i) {
				houses[j]+=i*11;
				count+=1;
				if(houses[i]>=divisor_sum){
					System.out.println(i+" : "+houses[i]);
					return;
				}
			}
		}
	}
}