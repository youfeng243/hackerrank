import java.util.Scanner;

/**
 * @author Youfeng
 */
public class Solution {

    private static boolean flag = false;
    private static int B = 0;
    private static int H = 0;

    static {
        Scanner sa = new Scanner(System.in);

        B = sa.nextInt();
        H = sa.nextInt();

        if (B <= 0 || H <= 0) {
            System.out.println("java.lang.Exception: Breadth and height must be positive");
        } else {
            flag = true;
        }
    }

    public static void main(String[] args) {
        if (flag) {
            int area = B * H;
            System.out.print(area);
        }

    }//end of main
}
