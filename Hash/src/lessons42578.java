import java.util.HashMap;

public class lessons42578 {
    public static void main(String[] args) throws Exception {

        String[][] clothes = {{"yellow_hat", "headgear"}, {"blue_sunglasses", "eyewear"}, {"green_turban", "headgear"}};

        System.out.println(solution(clothes));
    }

    public static int solution(String[][] clothes) {
        int answer = 1;

        HashMap<String, Integer> map = new HashMap<String, Integer>();

        // for (String[] t : clothes) {
        //     if (map.containsKey(t[1])) {
        //         map.put(t[1], map.get(t[1]) + 1);
        //     } else {
        //         map.put(t[1], 1);
        //     }
        // }

        for (int i = 0; i < clothes.length; i++) {
            map.put(clothes[i][1], map.getOrDefault(clothes[i][1], 0) + 1);
        }
        
        for (Integer c : map.values()) {
            answer *= (c + 1);
        }

        answer -= 1;

        return answer;
    }
    
}
