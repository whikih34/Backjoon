import java.util.Scanner;

public class Number10950 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int count = sc.nextInt();
    int[] arr = new int[count];

    for (int i = 0; i < count; i++) {
      int num1 = sc.nextInt();
      int num2 = sc.nextInt();

      if (num1 > 0 && num1 < 10 && num2 > 0 && num2 < 10) {
        arr[i] = num1 + num2;
      } else {
        System.out.println("1부터 9까지의 숫자 중에서 입력하세요");
        return;
      }
    }

    for (int i = 0; i < count; i++) {
      System.out.println(arr[i]);
    }

  }
}