import java.util.*;
import java.io.*;

public class day22{
	static int boss_damage = 9;
	static int min_mana = 100000;

	public static void main(String[] args) {
		Player manish = new Player(50,500);
		recur(58,0,true,manish);
		System.out.println(min_mana);
	}

	public static void check(Player manish){
		if(manish.recharge_time>0){manish.mana+=101;manish.recharge_time-=1;}
		if(manish.shield_time>0){manish.shield_time-=1;}
		if(manish.shield_time==0){manish.shield=0;}
	}


	public static void check_rev(Player manish, boolean prev, boolean prev2){
		if(manish.recharge_time>0 ||(manish.recharge_time==0 && prev2)){manish.mana-=101;manish.recharge_time+=1;}
		if(manish.shield_time>0){manish.shield_time+=1;}
		if(manish.shield_time==0 && prev){manish.shield_time+=1;manish.shield=7;}
	}

	public static void recur(int boss_h,int iter_mana,boolean turn,Player manish){
		// magic effect with timer
		// System.out.println(manish.mana+ " : "+ manish.hit +" : "+boss_h);
		// manish.hit is for the part 2
		// part 2
		manish.hit-=1;
		
		boolean prev_shield = (manish.shield==7);
		boolean prev_rcg = (manish.recharge_time>0);
		boolean prev_poi = (manish.poison_time>0);
		check(manish);
		if(manish.poison_time>0){boss_h-=3;manish.poison_time-=1;}

		if(iter_mana>=min_mana || manish.hit<=0){
			// part2
			manish.hit+=1;
			check_rev(manish,prev_shield,prev_rcg);
			if(manish.poison_time>0 || (manish.poison_time==0 && prev_poi)){manish.poison_time+=1;}
			return;
		}

		if(boss_h<=0 && manish.hit>0){
			min_mana=iter_mana;
			// part2
			manish.hit+=1;
			check_rev(manish,prev_shield,prev_rcg);
			if(manish.poison_time>0 || (manish.poison_time==0 && prev_poi)){manish.poison_time+=1;}
			// System.out.println("****************************");
			return;
		}

		if(turn){
			// System.out.println("player's chance");
			if(manish.magic_missile()!=-1){
				System.out.println("magic_missile");
				recur(boss_h-4,iter_mana+53,false,manish);
				manish.mana+=53;
			}

			if(manish.drain()!=-1){
				// System.out.println("drain");
				recur(boss_h-2,iter_mana+73,false,manish);
				manish.hit-=2;
				manish.mana+=73;
			}

			if(manish.shield_pow()!=-1){
				// System.out.println("shield");
				recur(boss_h,iter_mana+113,false,manish);
				manish.mana+=113;
				manish.shield=0;
				manish.shield_time=0;
			}

			if(manish.poison()!=-1){
				// System.out.println("poison");				
				recur(boss_h,iter_mana+173,false,manish);
				manish.mana+=173;
				manish.poison_time=0;
			}

			if(manish.recharge()!=-1){
				// System.out.println("recharge");
				recur(boss_h,iter_mana+229,false,manish);
				manish.mana+=229;
				manish.recharge_time=0;
			}

		}

		else{
			// System.out.println("devil's chance");
			int dec =(boss_damage-manish.shield);
			manish.hit-=dec;
			recur(boss_h,iter_mana,true,manish);
			manish.hit+=dec;
		}

		// part2
		manish.hit+=1;
		check_rev(manish,prev_shield,prev_rcg);
		if(manish.poison_time>0 || (manish.poison_time==0 && prev_poi)){manish.poison_time+=1;}
	} 

}

class Player{
		// player properties
		int hit;
		int mana;
		int shield =0;
		int shield_time=0;
		int poison_time=0;
		int recharge_time=0;

		public Player(int h,int m){
			this.hit = h;
			this.mana = m;
		}

		// ----------buy magic 
		public int magic_missile(){
			if(this.mana<53)return -1;
			this.mana-=53;
			return 4;
		}

		public int drain(){
			if(this.mana<73)return -1;
			this.mana-=73;
			this.hit+=2;
			return 2;
		}

		public int shield_pow(){
			if(this.mana<113 || this.shield_time>0)return -1;
			this.mana-=113;
			this.shield=7;
			this.shield_time=6;
			return 0;
		}

		public int poison(){
			if(this.mana<173 || this.poison_time>0)return -1;
			this.mana-=173;
			this.poison_time=6;
			return 3;
		}

		public int recharge(){
			if(this.mana<229 || this.recharge_time>0)return -1;
			this.mana-=229;
			this.recharge_time =5;
			return 0;
		}

	}