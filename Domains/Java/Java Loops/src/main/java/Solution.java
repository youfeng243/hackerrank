import java.util.Scanner;

/**
 * @author Youfeng
 */
public class Solution {
    public static void main(String[] args) {
        int times = 0;
        int a = 0;
        int b = 0;
        int n = 0;
        int sum = 0;
        int temp = 0;
        Scanner sa = new Scanner(System.in);
        times = sa.nextInt();

        for (int i = 0; i < times; i++) {
            a = sa.nextInt();
            b = sa.nextInt();
            n = sa.nextInt();

            temp = b;
            sum = a;
            for (int j = 0; j < n; j++) {
                sum += temp;
                temp *= 2;
                System.out.print(sum + " ");
            }
            System.out.println();
        }
    }
}
