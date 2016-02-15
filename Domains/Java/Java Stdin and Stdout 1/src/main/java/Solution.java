import java.util.Scanner;

/**
 * @author Youfeng
 */
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = 0;

        while( true ){

            try {
                a = sc.nextInt();
            }
            catch (Exception e){
                break;
            }
            System.out.println(a);
        }

        /*
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        System.out.println(a);
        System.out.println(b);
        System.out.println(c);
        */
    }
}
