import java.util.*;
import java.io.*;

public class day12 {

	// file input system i like it
	// cannot read char with Scanner as easily as with this one.

	public static void main(String[] args) {
		try{
			FileInputStream input = new FileInputStream("day12.txt");
			int sum = 0;
			int r;
			char c;

			while((r = input.read())!=-1){
				c=(char) r;

				// check beginning of object
				if(c=='{'){
					c=read_this(input);	
					sum+=recur(c,0,false,input);
				}

				else if(c==',' || c==':' || c=='[' || c==']'){
					continue;
				}

				else if(c=='"'){
					c=read_this(input);
					while(c!='"'){
						c=read_this(input);
					}
					c=read_this(input);
				}

				else{
					// the number management
					String strx="";
					while(c>='0' && c<='9' || c=='-'){
						strx+=c;
						c=read_this(input);
					}
					sum+=Integer.parseInt(strx);
				}
			}

			System.out.println(sum);
			input.close();

		}catch(FileNotFoundException e){
			System.out.println("No Such File Found.");
		}catch(IOException x){
			System.out.println("Error Parsing.");			
		}

	}

	public static char read_this(FileInputStream input){
		try{
		return (char)input.read();
		}catch(IOException x){
			System.out.println("Error Parsing.");
			return 'a';
		}
	}


	public static int recur(char c,int ss,boolean flag,FileInputStream input){
		int lstopen=0;
		while(true){
			if(c=='}'){
				System.out.println("ss = "+ss);
				return (flag)?0:ss;
			}
			else if(c=='{'){
				ss+=recur(read_this(input),0,false,input);
				c=read_this(input);
			}
			else if(c==',' || c==':'){
				c=read_this(input);
				continue;
			}

			// just to remind myself, why i didn't cared the following.
			// below two cases is what that took me a great time to think about.
			else if(c=='['){
				lstopen++;
				c=read_this(input);
			}
			else if(c==']'){
				lstopen--;
				c=read_this(input);
			}

			else if(c=='"'){
				String strx= "";
				c=read_this(input);
				while(c!='"'){
					strx+=c;
					c=read_this(input);
				}

				// the "red" should not be in an array
				if(strx.equals("red") && lstopen==0)
					flag=true;
				c=read_this(input);
			}

			else{
				// the number management
				String strx="";
				while(c>='0' && c<='9' || c=='-'){
					strx+=c;
					c=read_this(input);
				}
				System.out.println(strx);
				ss+=Integer.parseInt(strx);
			}
		}
	}
}