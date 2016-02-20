import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        String A = sc.next();
        String B = sc.next();

        int totallength = A.length() + B.length();
        String compare = A.compareTo(B) > 0 ? "Yes" : "No";
        String result = A.substring(0, 1).toUpperCase() + A.substring(1, A.length()) + " " +
                B.substring(0, 1).toUpperCase() + B.substring(1, B.length());

        System.out.println(totallength);
        System.out.println(compare);
        System.out.println(result);
    }
}
