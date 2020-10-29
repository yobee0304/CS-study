# 컨베이어 벨트 위의 로봇

## 1. 문제
https://www.acmicpc.net/problem/20055

## 2. 유형
* 시뮬레이션(구현)

## 3. 풀이
* 컨베이어 벨트를 위쪽과 아래쪽을 구분해서 총 2개의 데크로 선언한다.
```c++
deque<int> upper_belt, lower_belt;
```
* 위쪽 벨트에 있는 로봇의 위치를 확인하기 위해 위쪽 벨트와 똑같은 크기의 데크를 1개 더 선언한다.
```c++
deque<bool> box_location;
```
* Why "deque"?

벨트가 회전하면서 아래쪽의 front가 위쪽의 front로 이동하고, 위쪽의 back이 아래쪽의 back으로 이동하여 양쪽에서 push와 pop이 발생하기 때문이다.
  
* 컨베이어 벨트의 작동 순서는 다음과 같다.
  1. 벨트가 한 칸 회전한다.
  ```c++
  // 한 칸 회전 시키는 함수
  void do_cycle(){
    upper_belt.push_front(lower_belt.front());
    lower_belt.pop_front();
    lower_belt.push_back(upper_belt.back());
    upper_belt.pop_back();
    box_location.pop_back();
    box_location.push_front(false);
  }
  ```
  2. 가장 먼저 들어온 로봇을 기준으로, 로봇이 한 칸 앞으로 움직일 수 있다면 움직인다.
  ```c++
  for(int i = N-2; i >= 0;i--){
      if(box_location[i] == true && box_location[i+1] == false && upper_belt[i+1] > 0){
          swap(box_location[i], box_location[i+1]);
          upper_belt[i+1]--;
                
          if(upper_belt[i+1] == 0)
              zero_cnt++;
      }
  }
  ```
  3. 올라가는 칸에 로봇이 올라갈 수 있는지 확인.
  ```c++
  if(box_location[0] == false && upper_belt[0] > 0){
      box_location[0] = true;
      upper_belt[0]--;
            
      if(upper_belt[0] == 0)
          zero_cnt++;
  }
  ```
  4. 내구도가 0인 개수를 확인한다.
    * K개 이상이면 과정을 반복을 종료한다.
    * K개 보다 작다면, 과정을 반복한다.
  ```c++
  if(zero_cnt >= K)
      break;
  ```
    
  * 주의사항
    * 로봇이 움직이는 상황(벨트가 움직이거나, 로봇이 직접 움직이는 경우)에서는 항상 로봇이 내려오는 자리를 확인해줘야 한다.
    * 로봇이 직접 움직여 벨트의 값이 줄어들게 됬을 때, 0이 될때 마다 카운트를 해주어야 나중에 K개와 0의 개수를 비교할 때 다시 한 번 확인 해야하는 번거로움을 없앨 수 있다.

## 4. 후기

컨베이어 벨트가 돌아가는 부분을 구현하는 것이 키 포인트 인 것 같다.

처음에는 2N 크기의 고정된 배열을 가지고 시작과 끝 인덱스를 옮겨가는 식으로 벨트의 회전을 구현해보고자 했으나, 코드가 직관적이지 않아 문제가 생겼던 것 같다.

2개의 데크로 구현한 방법이 내게는 더 직관적으로 머리속에 그려진 것 같다.

하지만 push와 pop이 자주 발생하는 만큼 실행속도를 꽤 잡아먹을 수 도 있으니 원래의 방법으로 다시 시도해봐야겠다.
