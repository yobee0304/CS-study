# 그 밖의 용어 정리

## 1. 바인딩(Binding)
* 프로그램의 기본 단위에 해당 단위가 가질 수 있는 속성 중에서 필요한 속성만을 선택하여 연결해 주는 것을 말한다.
```C++
// 'Yobee_Age'라는 변수는 정수(int)의 속성에 연결되고
// 변수의 자료값으로는 100이 할당된다
// 이 2가지 과정에서 바인딩 개념이 적용된다
int Yobee_Age = 100;
```
* 바인딩이 일어나는 시점(바인딩 타임)에 따라 '정적 바인딩'과 '동적 바인딩'으로 나뉜다.
  * 정적 바인딩 : 실행 시간 이전에 바인딩이 일어나고, 실행 중에는 변하지 않고 유지되는 바인딩.
  * 동적 바인딩 : 실행 시간 중에 일어나거나, 프로그램 실행 과정에서 변경되는 바인딩.