import java.util.*;
class mobile
{
	int price =100;
	String model="samsungm31";
	int mobile_stock=2;
}
class laptop
 {
 	int price =10000;
	String model="lenevo";
	int laptop_stock=4;
 }
public class Main {
	public static void main(String[] args) {
		ArrayList<String> cart = new ArrayList<String>();
		mobile mob =new mobile();
		laptop lap =new laptop();
		if(mob.mobile_stock > 0)
		{
			cart.add(mob.model);
			mob.mobile_stock=(mob.mobile_stock)-1;
			System.out.println("samsungm31 mobile phone added susceffuly");
		}
	    if(lap.laptop_stock > 0)
		{
			cart.add(lap.model);
			lap.laptop_stock=(lap.laptop_stock)-1;
			System.out.println("lenevo laptop added susceffuly");
		}
		if(mob.mobile_stock > 0)
		{
			cart.add(mob.model);
			mob.mobile_stock=(mob.mobile_stock)-1;
			System.out.println("samsungm31 mobile phone added susceffuly");
		}
	    if(mob.mobile_stock < 0)
		{
			cart.add(mob.model);
			mob.mobile_stock=(mob.mobile_stock)-1;
			System.out.println("samsungm31 mobile phone is out of stock");
		}
		String s1 =cart.remove(2);
		System.out.println(s1 + "removed sucessfully");
	}
}
