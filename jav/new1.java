
import java.util.Random;

public class new1 {
    public static void main(String[] args) {

        Random random = new Random();

        int number1;
        int number2;
        int number3;

        number1 = random.nextInt(1, 20);
        number2 = random.nextInt(1, 20);
        number3 = random.nextInt(1, 20);

        System.out.println(number1 + "/" + number2 + "/" + number3);

    }
}