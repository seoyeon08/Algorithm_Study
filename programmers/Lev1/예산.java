import java.util.*;
class Solution {
    public int solution(int[] d, int budget) {
        int answer = 0;
        int sum = 0;
        // 작은 수 부터 더할 때 result가 가장 커짐
        Arrays.sort(d);
        for(int i = 0; i < d.length; i++){
            // 처음부터 너무 클 때 -> testcase 3번
            if(d[i] > budget){
                answer = -1;
                break;
            }
            // 기본
            if(sum <= budget){
                sum += d[i];
                // 더했더니 budget보다 커졌을 때
                if(sum > budget)
                    break;
                answer = i;     // 이 때의 i값을 answer에 저장
            }
        }
        return answer + 1;
    }
}