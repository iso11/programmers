public class lessons42577 {
    public static void main(String[] args) throws Exception {
        String[] phone_book = { "119", "97674223", "1195524421" };
        System.out.println(solution(phone_book));
    }

    public static boolean solution(String[] phone_book) {
        boolean answer = true;

        for (String p : phone_book) {
            for (String p2 : phone_book) {
                if(!p.equals(p2) && p2.indexOf(p) == 0) {
                    answer = false;
                    break;
                }
            }
            if (!answer) break;
        }

        return answer;
    }
}
