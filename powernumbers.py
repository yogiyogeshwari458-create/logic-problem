import java.util.Scanner;

public class PowerNumber {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int n = sc.nextInt();

        boolean isPower = false;

        for (int base = 2; base <= Math.sqrt(n); base++) {
            long value = base;

            while (value < n) {
                value *= base;
            }

            if (value == n) {
                isPower = true;
                break;
            }
        }

        if (isPower) {
            System.out.println(n + " is a power number.");
        } else {
            System.out.println(n + " is not a power number.");
        }

        sc.close();
    }
}