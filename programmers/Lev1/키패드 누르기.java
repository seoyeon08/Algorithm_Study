class Solution {
    public String solution(int[] numbers, String hand) {
        String answer = "";
        int L = 10;  // 왼쪽 엄지손가락 기본 위치
        int R = 12;  // 오른쪽 엄지손가락 기본 위치
        
        for(int i = 0; i < numbers.length; i++){
            if(numbers[i] == 0)
                numbers[i] = 11;    // 0을 11로 바꿔준다
            
            if(numbers[i] % 3 == 1){    // 맨 왼쪽 라인이면
                answer += "L";
                L = numbers[i];
            }
            else if(numbers[i] % 3 == 0){   // 맨 오른쪽 라인이면
                answer += "R";
                R = numbers[i];
            }
            else if(numbers[i] % 3 == 2){   // 가운데 라인이면
                int L1; // L위치 절댓값
                int R1; // R위치 절댓값
                
                // 왼손
                if(numbers[i] > L)
                    L1 = numbers[i] - L;
                else
                    L1 = L - numbers[i];
                
                // 오른손
                if(numbers[i] > R)
                    R1 = numbers[i] - R;
                else
                    R1 = R - numbers[i];

                int L2; // 왼쪽 거리
                int R2; // 오른쪽 거리
                //   세로로 몇칸  가로로 몇칸
                L2 = (L1 % 3) + (L1 / 3);
                R2 = (R1 % 3) + (R1 / 3);
                
                if(L2 > R2){
                    answer += "R";
                    R = numbers[i];
                }
                else if(L2 < R2){
                    answer += "L";
                    L = numbers[i];
                }
                else{
                    if(hand == "right"){
                        answer += "R";
                        R = numbers[i];
                    }
                    else{
                        answer += "L";
                        L = numbers[i];
                    }
                }
            }
        }
        return answer;
    }
}