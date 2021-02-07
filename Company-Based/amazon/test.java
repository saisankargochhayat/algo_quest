import java.util.*;
import java.io.*;
import java.lang.*;

public class test {
    
    public static boolean compareProduct(int num) {
        if (num < 10)
            return false;
        int oddProdValue = 1, evenProdValue = 1;

        while(num > 0) {
            int digit = num / 10;
            System.out.println(digit);
            oddProdValue *= digit;
            num = num / 10;
            if(num == 0)
                break;
            System.out.println(digit);
            digit = num / 10;
            evenProdValue *= digit;
            num = num / 10;
        }
        System.out.println(evenProdValue);
        if(evenProdValue == oddProdValue)
            return true;
        return false;
    }

    public static void main(String[] args){
        compareProduct(11);
        System.out.println("Hello World");
        
    }
}