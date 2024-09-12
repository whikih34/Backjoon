import java.util.Scanner;

public class Number25314 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int nByte = sc.nextInt();

    if (nByte >= 4 && nByte <= 1000) {
      if (nByte % 4 == 0) {
        for (int i = 0; i < nByte; i += 4) {
          System.out.print("long ");
        }
        System.out.println("int");
      } else {
        System.out.println("4의 배수인 정수를 입력하세요");
      }
    } else {
      System.out.println("4부터 1000사이의 정수를 입력하세요");
    }
  }
}