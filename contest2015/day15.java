import java.util.*;
import java.io.*;

// Not optimised yet is fast enough

public class day15{
	public static void main(String[] args) {
		int max_score=0;
		for(int a=0;a<=100;a++){
			for(int b=0;b<=100-a;b++){
				for(int c=0;c<=100-a-b;c++){
						int d=100-a-b-c;
						int cap = a*2;
						int dur = (5*b-d>0)?(5*b-d):0;
						int fla = (-2*a-3*b+5*c>0)?(-2*a-3*b+5*c):0;
						int tex = (5*d-c>0)?(5*d-c):0;
						int total = cap*dur*fla*tex;
						int cal = 3*(a+b)+8*(c+d);
						if(total>max_score)max_score=total;
				}
			}
		}

		System.out.println(max_score);
	}
}