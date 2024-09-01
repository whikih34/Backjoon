import java.util.Scanner;

public class Number09498 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int score = sc.nextInt();
    String grade = "";
    if (score >= 0 && score <= 100) {
      switch (score / 10) {
        case 10:
        case 9:
          grade = "A";
          break;
        case 8:
          grade = "B";
          break;
        case 7:
          grade = "C";
          break;
        case 6:
          grade = "D";
          break;
        default:
          grade = "F";
          break;
      }
    }

    System.out.println(grade);
  }
}