import java.util.Scanner;

/**
 * @author Youfeng
 */
public class Solution {
    public static void main(String[] args) {
        Scanner sa = new Scanner(System.in);

        int cnt = 0;
        while (sa.hasNext()) {
            cnt++;
            String str = sa.nextLine();
            System.out.printf("%d %s\n", cnt, str);
        }
    }
}
