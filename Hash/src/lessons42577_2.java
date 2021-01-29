import java.util.HashMap;

public class lessons42577_2 {
    public static void main(String[] args) throws Exception {
        String[] phone_book = { "119", "97674223", "1195524421" };
        System.out.println(solution(phone_book));
    }

    public static boolean solution(String[] phone_book) {
        boolean answer = true;
        HashMap<String, Integer> map = new HashMap<String, Integer>();

        for (String p : phone_book) {
            map.put(p, 1);
        }

        for (String p : phone_book) {
            int length = p.length();
            for(int i = 0; i < length; i++) {
                if (map.containsKey(p.substring(0,i))) {
                    answer = false;
                    break;
                }
            }
            if (!answer) break;
        }

        return answer;
    }
}
