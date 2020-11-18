# 운영체제

## 1. 페이지 교체 알고리즘
1. FIFO (First In First Out)
- 각 페이지가 주기억장치에 적재될 때 마다, 가장 먼저 들어왔던 페이지와 교체한다.
- 프로그래밍 및 설계가 간단하다.
- '벨레이디의 모순'현상이 발생한다.
  - 벨레이디의 모순 : 페이지 프레임 수가 증가하면 일반적으로 페이지 부재(Page Fault)의 수가 감소하지만 반대로 더 많이 발생하는 현상

2. LRU (Least Recently Used)
- 최근에 가장 오랫동안 사용하지 않은 페이지를 교체한다.
- 만약 적재하고자 하는 페이지가 이미 주기억장치에 존재하는 경우, 주기억장치에 있는 페이지의 사용 시간을 초기화한다.
- 최적 알고리즘은 구현이 불가능하므로, LRU를 통해 비슷한 효과를 기대할 수 있다.
- 시간 오버헤드가 크다.

3. LFU (Least Frequently Used)
- 계수 기반(Counting-Based) 페이지 교체 방식이다.
- 사용 빈도가 가장 적은 페이지를 교체한다.
- 교체 대상인 페이지가 여러개인 경우, LRU 방식을 따른다.

4. NUR (Not Used Recently)
- 최근에 사용하지 않은 페이지를 교체한다.
- LRU와 비슷하지만, LRU에서 발생하는 시간 오버헤드를 줄일 수 있다.
- 최근 사용 여부를 확인하기 위해, 각 페이지마다 '참조 비트'와 '변형 비트'를 사용한다.
  - 참조 비트(Reference Bit) : 페이지가 호출되지 않았을 때는 0, 호출되었을 때는 1로 저장된다.
  - 변형 비트(Modified Bit) : 페이지 내용이 변경되지 않았을 때는 0, 변경되었을 때는 1로 지정된다.
  
참조 비트 | 병형 비트 | 교체 순서
--- | --- | ---
0 | 0 | 1
0 | 1 | 2
1 | 0 | 3
1 | 1 | 4

## 2. Process & Thread
1. Mutex & Semaphore
* Critical Section을 보장하기 위해 사용된다.
  * Critical Section(임계구역) : 각 프로세스에서 공유 데이터를 액세스하는 프로그램 코드 부분
  
* Mutex
  * Mutual Exclusion
  * Critical Section을 가진 쓰레드들의 Running Time이 겹치지 않도록 실행시켜주는 기술.
  * 멀티 쓰레드 환경에서 사용
  
* Semaphore
  * 프로세스가 리소스에 접근할 수 있는 상태를 나타내는 카운터
  * 세마포어의 값에 따라 프로세스는 즉시 자원을 사용할 수 있거나, 일정 시간을 기다려야 한다.
  * 멀티 프로세스 환경에서 사용

* Mutex와 Semaphore의 차이점
  * **Mutex는 동기화 대상이 오직 하나지만, Semaphore는 동기화 대상이 하나 이상일 때 사용한다.**
    * Mutex는 상태가 0, 1뿐인 binary semaphore
    * semaphore는 mutex가 될 수 있지만, mutex는 semaphore가 없다!
  * Semaphore는 소유할 수 없는 반면, Mutex는 소유가 가능하며 이에 대한 소유주가 존재합니다.
    * mutex는 상태가 두 개뿐인 lock이므로, lock을 소유할 수 있습니다.
  * Mutex의 경우 Mutex를 보유하고 있는 쓰레드가 Mutex를 해제할 수 없지만, Semahore의 경우 이러한 Semaphore의 경우 이러한 Semaphore를 보유하지 않는 쓰레드가 이 Semaphore를 해제할 수 있습니다.

( 참고 : https://jwprogramming.tistory.com/13 )

2. Lock
