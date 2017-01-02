import java.util.*;
import java.io.*;

public class test_java{
	public static void main(String[] args) {
		int members = 3012210;
		ArrayList<Integer> lst = new ArrayList<Integer>();
		int index=0;

		for(int i=1;i<=members;i++)
			lst.add(i);

		while(true){
			int l = lst.size();
			if(l==1)break;

			int tmp = lst.get(l-1);
			lst.remove((index+l/2)%l);
			if(index!=lst.size()-1 || tmp!=lst.get(lst.size()-1))
				index=(index+1)%l;
			System.out.println(l);
		}
		System.out.println(lst.get(0));
	}
}