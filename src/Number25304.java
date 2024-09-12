import java.util.Scanner;

public class Number25304 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int totalReceipt = sc.nextInt();
    int countReceipt = sc.nextInt();
    int[] thingPrice = new int[countReceipt];
    int thingTotal = 0;

    for (int i = 0; i < countReceipt; i++) {
      int price = sc.nextInt();
      int count = sc.nextInt();
      thingPrice[i] = price * count;
    }

    for (int i = 0; i < countReceipt; i++) {
      thingTotal += thingPrice[i];
    }

    if (totalReceipt == thingTotal) {
      System.out.println("Yes");
    } else {
      System.out.println("No");
    }

  }
}