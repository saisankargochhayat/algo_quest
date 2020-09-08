
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/**
 * Given a chessboard in FEN, find all possible paths of a rook
 *
 * More about FEN here
 * https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation
 * @author amitosh
 */
public class ChessRook {

    public static void main(String[] args) throws IOException {
    
        //read FEN
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        char chessboard[][] = new char[8][8];
        
        // turn a FEN to a chessboard
        String line = br.readLine().trim();
        String parts[] = line.split(" ");
        String fen = parts[0];
        String turn = parts[1];
        int rank = 0;
        int index = 0;
        for (int i = 0; i < fen.length(); i++) {
            char c = fen.charAt(i);

            if (Character.isDigit(c)) {
                for (int j = 1; j <= Character.getNumericValue(c); j++) {
                    chessboard[rank][index++] = 0;
                }
            } else if (c == '/') {
                rank++;
                index = 0;
            } else {
                chessboard[rank][index++] = c;
            }

        }

//        code to print generated chessboard
//        for (int i = 0; i < chessboard.length; i++) {
//            char[] cs = chessboard[i];
//
//            for (int j = 0; j < cs.length; j++) {
//                char c = cs[j];
//                System.out.print(c + " ");
//
//            }
//            System.out.println();
//        }
//
//        System.out.println(turn);

        char search = 'r';
        if (turn.charAt(0) == 'w') {
            search = 'R';
        }

        ArrayList<String> moves = new ArrayList<>();

        for (int i = 0; i < 8; i++) {
            char[] cs = chessboard[i];

            for (int j = 0; j < 8; j++) {
                char c = cs[j];

                if (c == search) {
                    for (int k = 0; k < 8; k++) {
                        for (int l = 0; l < 8; l++) {
                            
                            if(( i == k || j == l) && chessboard[k][l] == 0 )
                                moves.add(getString(i,j,k,l));
                            
                        }
                        
                    }
                }

            }
        }

        System.out.print("[");
        for (Iterator<String> i = moves.iterator(); i.hasNext();) {
            String move = i.next();
            System.out.print(move);
            
            if(i.hasNext()) {
                System.out.print(", ");
            }
        }
        System.out.print("]");
    }

    static char columns[] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'};

    private static String getString(int i, int j, int k, int j0) {

        return "" + columns[j] + (8 - i) + columns[j0] + (8 - k);
    }

}
