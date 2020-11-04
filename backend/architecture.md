# 아키텍쳐

## 1. 모놀리식 아키텍쳐 vs MSA
![architecture_versus](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2F49wTn%2FbtqASzgr8wR%2FjLuZ4oQHoMyv4CnkeTxBC0%2Fimg.png)

### 모놀리식 아키텍쳐(Monolithic Architecture)
* 장점
  * 모든 기능의 개발 환경이 같아 개발이 편리하다.
  * E2E(End-to-End: 사용자 입장에서 테스트) 테스트가 용이하다
* 단점
  * 서버의 크기가 커지면 빌드, 배포 시간이 오래 걸린다.
  * 작은 수정사항이라 하더라도, 전체를 빌드하여 배포해야 한다.
  * 일부분의 오류가 서버 전체에 영향을 줄 수 있다.

### MSA(Micro Service Architecture)
* 장점
  * 기능별로 마이크로서비스를 개발하고, 작업 할당을 서비스 단위로 하면 개발자가 이해하기 쉽다.
  * 새로 추가되거나 수정해야하는 경우, 해당 마이크로서비스만 수정하면 되기 때문에 빠르게 수정 및 배포가 가능하다.
  * 각각의 기능에 적합한 언어나 기술을 선택하기 쉽다.
* 단점
  * 작은 서비스가 분산되어 있기 때문에 모니터링이 힘들다.
  * 마이크로 서비스들 간의 통신이 자주 발생하기 때문에, 통신관련 오류가 자주 발생할 가능성이 있다.
  * 테스트를 위해서는 여러 개의 마이크로 서비스를 구동시켜야 하므로, 테스트가 까다롭다.
