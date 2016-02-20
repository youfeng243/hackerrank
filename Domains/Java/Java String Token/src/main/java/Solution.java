import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * @author Youfeng
 */
public class Solution {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();

        String[] arraystr = s.split("[ !,?.\\_'@]+");
        List<String> array = new ArrayList<String>();

        System.out.println(arraystr.length);
        int cnt = 0;
        for (int i = 0; i < arraystr.length; i++) {
            if (arraystr[i].length() > 0) {
                array.add(arraystr[i]);
                cnt++;
            }
            System.out.println(arraystr[i]);
        }

        System.out.println(cnt);
        for (int i = 0; i < array.size(); i++) {
            System.out.println(array.get(i));
        }

    }
}
