import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * @author Youfeng
 */
public class Solution1 {

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        String special = "!,?._'@";

        for (int i = 0; i < special.length(); i++) {
            s = s.replace(special.charAt(i), ' ');
        }

        List<String> array = new ArrayList();

        int loop = 0;
        int j = 0;
        int length = s.length();

        while (loop < length) {

            while (loop < length) {
                if (s.charAt(loop) == ' ') {
                    loop++;
                    continue;
                }
                break;
            }

            int start = loop;
            while (loop < length) {
                if (s.charAt(loop) != ' ') {
                    loop++;
                    continue;
                }
                break;
            }

            if (loop > start) {
                array.add(s.substring(start, loop));
            }
        }

        System.out.println(array.size());
        for (int i = 0; i < array.size(); i++) {
            System.out.println(array.get(i));
        }
    }
}
