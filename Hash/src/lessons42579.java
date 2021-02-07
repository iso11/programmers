import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;

public class lessons42579 {
    public static void main(String[] args) throws Exception {

        String[] genres = {"classic", "pop", "classic", "classic", "pop"};
        int[] plays = {500, 600, 150, 800, 2500};

        int[] result = solution(genres, plays);
        for (int i : result) {
            System.out.println(i);
        }
    }

    public static int[] solution(String[] genres, int[] plays) {
        List<Integer> answer = new ArrayList<>();

        //장르별 합 구하고 정렬해서 장르 순서 구하기
        HashMap<String, Integer> total = new HashMap<>();

        for(int i = 0; i < genres.length; i++) {
            total.put(genres[i], total.getOrDefault(genres[i], 0)+plays[i]);
        }
        
        //정렬
		List<String> keySetList = new ArrayList<>(total.keySet());
        Collections.sort(keySetList, (o1, o2) -> (total.get(o2).compareTo(total.get(o1))));
        
        for (String g : keySetList) {
            HashMap<Integer, Integer> genre = new HashMap<>();

            //장르별로 각각 맵 만들기 인덱스 - 횟수
            for (int i =0 ;i < genres.length; i++) {
                if(genres[i].equals(g)) {
                    genre.put(i, plays[i]);
                }
            }
            List<Integer> genreList = new ArrayList<>(genre.keySet());
            Collections.sort(genreList, (o1, o2) -> (genre.get(o2).compareTo(genre.get(o1))));

            int size = genreList.size();
            for (int k=0; k < size && k < 2; k++) {
                answer.add(genreList.get(k));
            }
        }
        int[] array = answer.stream().mapToInt(i->i).toArray();

        return array;
    }
}
