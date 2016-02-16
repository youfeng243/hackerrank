import java.math.BigInteger;
import java.util.Scanner;

/**
 * @author Youfeng
 */
public class Solution {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        BigInteger maxLong = new BigInteger(String.valueOf(Long.MAX_VALUE));
        BigInteger minLong = new BigInteger(String.valueOf(Long.MIN_VALUE));

        BigInteger maxInt = new BigInteger(String.valueOf(Integer.MAX_VALUE));
        BigInteger minInt = new BigInteger(String.valueOf(Integer.MIN_VALUE));

        BigInteger maxShort = new BigInteger(String.valueOf(Short.MAX_VALUE));
        BigInteger minShort = new BigInteger(String.valueOf(Short.MIN_VALUE));

        BigInteger maxByte = new BigInteger(String.valueOf(Byte.MAX_VALUE));
        BigInteger minByte = new BigInteger(String.valueOf(Byte.MIN_VALUE));

        for (int i = 0; i < t; i++) {
            BigInteger num = new BigInteger(sc.next());

            boolean longflag = false;
            boolean intflag = false;
            boolean shortflag = false;
            boolean byteflag = false;

            if (num.compareTo(minByte) >= 0 && num.compareTo(maxByte) <= 0) {
                byteflag = true;
            }

            if (num.compareTo(minShort) >= 0 && num.compareTo(maxShort) <= 0) {
                shortflag = true;
            }

            if (num.compareTo(minInt) >= 0 && num.compareTo(maxInt) <= 0) {
                intflag = true;
            }

            if (num.compareTo(minLong) >= 0 && num.compareTo(maxLong) <= 0) {
                longflag = true;
            }

            if (longflag == false) {
                System.out.println(num + " can't be fitted anywhere.");
                continue;
            }
            System.out.println(num + " can be fitted in:");
            if (byteflag) {
                System.out.println("* byte");
            }
            if (shortflag) {
                System.out.println("* short");
            }
            if (intflag) {
                System.out.println("* int");
            }
            if (longflag) {
                System.out.println("* long");
            }
        }
    }
}
