import java.util.Scanner;

/**
 * @author Youfeng
 */
public class Solution2 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        String special = "!,?._'@";

        if (s.length() <= 0) {
            System.out.println(0);
            return;
        }

        for (int i = 0; i < special.length(); i++) {
            s = s.replace(special.charAt(i), ' ');
        }

        String[] arraystr = s.split("[ ]+");

        System.out.println(arraystr.length);
        for (int i = 0; i < arraystr.length; i++) {
            System.out.println(arraystr[i]);
        }
    }
}
