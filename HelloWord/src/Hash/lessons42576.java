package Hash;

import java.util.HashMap;

public class lessons42576 {
    public static void main(String[] args) throws Exception {
        String[] participant = { "marina", "josipa", "nikola", "vinko", "filipa" };
        String[] completion = { "marina", "josipa", "nikola", "filipa" };
        System.out.println(solution(participant, completion));
    }

    public static String solution(String[] participant, String[] completion) {
        String answer = "";

        HashMap<String, Integer> map = new HashMap<String, Integer>();

        for (String p : participant) {
            if (map.containsKey(p)) {
                map.put(p, map.get(p) + 1);
            } else {
                map.put(p, 1);
            }
        }

        for (String c : completion) {
            map.put(c, map.get(c) - 1);
        }

        for (String m : map.keySet()) {
            if (map.get(m) > 0) {
                answer = m;
                break;
            }
        }

        return answer;
    }
}
