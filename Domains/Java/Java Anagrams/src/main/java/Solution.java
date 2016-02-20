
import java.util.Arrays;
import java.util.Scanner;

public class Solution {

    static boolean isAnagram(String A, String B) {

        if (A.length() != B.length()) {
            return false;
        }

        if (A.length() <= 0) {
            return false;
        }

        A = A.toLowerCase();
        B = B.toLowerCase();

        char[] alist = A.toCharArray();
        char[] blist = B.toCharArray();

        Arrays.sort(alist);
        Arrays.sort(blist);

        for (int i = 0; i < A.length(); i++) {
            if (alist[i] != blist[i]) {
                return false;
            }
        }

        return true;
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        String A = sc.next();
        String B = sc.next();
        boolean ret = isAnagram(A, B);
        if (ret) System.out.println("Anagrams");
        else System.out.println("Not Anagrams");
    }
}
