#include <iostream>
#include <deque>
using namespace std;

int N, K, A;
deque<int> upper_belt, lower_belt;
deque<bool> box_location;

void do_cycle(){
    upper_belt.push_front(lower_belt.front());
    lower_belt.pop_front();
    lower_belt.push_back(upper_belt.back());
    upper_belt.pop_back();
    box_location.pop_back();
    box_location.push_front(false);
}

int main(){
    
    cin >> N >> K;
    upper_belt.resize(N);
    lower_belt.resize(N);
    box_location.resize(N);
    
    for(int i = 0;i < N;i++){
        cin >> A;
        upper_belt[i] = A;
    }
    for(int i=N-1;i>=0;i--){
        cin >> A;
        lower_belt[i] = A;
    }
    
    int zero_cnt = 0;
    int time = 1;
    
    while(1){
        // 1. 벨트가 한 칸 회전
        do_cycle();
        // 회전한 뒤, 내려가는 칸에 로봇이 존재하는 지 확인
        if(box_location[N-1] == true)
            box_location[N-1] = false;
        
        // 2. 로봇을 먼저 들어온 순서대로 한 칸씩 전진
        for(int i = N-2; i >= 0;i--){
            if(box_location[i] == true && box_location[i+1] == false && upper_belt[i+1] > 0){
                swap(box_location[i], box_location[i+1]);
                upper_belt[i+1]--;
                
                if(upper_belt[i+1] == 0)
                    zero_cnt++;
            }
        }
        
        // 전진한 뒤, 내려가는 칸에 로봇이 존재하는 지 확인
        if(box_location[N-1] == true)
            box_location[N-1] = false;
        
        // 3. 올라가는 칸에 로봇을 하나 올림
        if(box_location[0] == false && upper_belt[0] > 0){
            box_location[0] = true;
            upper_belt[0]--;
            
            if(upper_belt[0] == 0)
                zero_cnt++;
        }
        
        if(zero_cnt >= K)
            break;
        
        time++;
    }
    
    cout << time << endl;
    
    return 0;
}
