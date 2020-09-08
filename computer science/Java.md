# Java
## 1. 자바의 장단점
- 장점
1) JVM에서 독자적으로 동작하기 때문에, 운영체제로부터 독립적이다.
2) 객체지향 언어이다.
3) 오픈 소스다.
4) 스레드 생성 및 제어와 관련된 라이브러리 API를 제공하고 있기 때문에, 쉽게 멀티 스레드를 구현할 수 있다.
5) 애플리케이션을 실핼될 때 모든 객체가 생성되지 않고, 각 객체가 필요한 시점에 클래스를 동적 로딩해서 생성한다. 또한 유지보수시에는 해당 클래스만 수정하면 되기 때문에 전체 애플리케이션을 다시 컴파일할 필요가 없다. 즉, 유지보수가 편리하다.
6) JVM에서 ‘가비지 컬렉터’라 불리는 데몬 쓰레드에 의해서 자동으로 메모리 관리를 해준다.
	* 가비지 컬렉션(Garbage Collection)
		* 변수에 새로운 값을 선언할 때, 원래 값은 메모리에 유지된 채 새로운 값이 메모리에 생성되고 변수는 가리키기만 한다.
		* 때문에 사용하지 않는 값이 메모리 스택에 존재하게 되고, 이를 메모리 누수(Memory Leak)라고 한다.
		* 이런 사용하지 않는 값들을 메모리 스택에서 지워 메모리 누수를 방지하는 방법을 가비지 콜렉션(Garbage Collection)이라 한다.
		```java
		String url = “https://”     // But 변수 url은 “https”//www.naver.com”만을 가리킨다
		url += “www.naver.com”      // 메모리 스택에는 “https://”와 “https”//www.naver.com”이 존재
		                            // 결과적으로, “https://”는 사용하지 않으므로 메모리 누수가 발생!
		```
	(참고 : https://yaboong.github.io/java/2018/06/09/java-garbage-collection/ )
- 단점
1) 속도가 느리다
	* 한 번의 컴파일링으로 실행 가능한 기계어가 만들어지지 않고, JVM에 의해 기계어로 번역되고 실행하는 과정을 거치기 때문에, C나 C++에 비해 느리다
2) 예외처리가 불편하다
	* 프로그래머 검사가 필요한 예외가 등장한다면 무조건 프로그래머가 선언해줘야 한다.

## 2. 자바 접근 제어자 종류
- public  + : 어떤 클래스의 객체에서도 접근 가능
- private  - : 이 클래스에서 생성된 객체들만 접근 가능
- protected  # : 이 클래스와 동일 패키지에 있거나 상속 관계에 있는 하위 클래스의 객체들만 접근 가능
- package  ~ : 동일 패키지에 있는 클래스의 객체들만 접근 가능

## 3. 자바의 데이터 타입
1) 기본형 데이터 타입
- 정수형(byte, short, int, long)
- 실수형(float, double)
- 논리형(boolean)
- 문자형(char)
2) 참조형 테이터 타입
- 기본형 데이터 타입을 제외한 모든 데이터 타입
- new 키워드를 이용해 객체를 생성하고 데이터가 생성된 주소를 참조하는 타입
- String과 배열 타입은 new없이 생성 가능
- 참조 타입의 데이터의 크기가 가변적, 동적이기 때문에 동적으로 관리되는 Heap 영역에 저장된다.
- 더 이상 참조하는 변수가 없을 때 가비지 컬렉션에 의해 파괴된다.
- 참조 타입은 값이 저장된 곳의 주소를 저장하는 공간으로 객체의 주소를 저장한다. (Call-By-Value)

## 4. OOP의 4가지 특징
1) 추상화
- 구체적인 사물들의 공통적인 특징을 파악해서 이를 하나의 개념(집합)으로 다루는 것
- 추상적인 메소드를 활용하면, 변수의 값이 변하더라도 코드를 변경할 필요가 없다.
2) 캡슐화
- 필요가 없는 정보는 외부에서 접근하지 못하도록 제한하는 것 = 정보 은닉(information hiding)
- 높은 응집도와 낮은 결합도를 유지하여, 한 클래스에서 변경이 발생할 경우 다른 클래스에서도 변경이 일어나는 경우를 줄인다
	- 모듈화 : 기능별로 분리
	- 결합도 : 어떤 모듈이 다른 모듈에 의존하는 정도
	- 응집도 : 하나의 모듈이 하나의 기능을 수행하는 요소들간의 연관성 척도
3) 일반화 관계
- 여러 개체들이 가진 공통된 특성을 부각시켜 하나의 개념이나 법칙으로 성립시키는 과정
- 객체지향 프로그램 관점에서는 '상속'이라고 한다.
	* 상속
		* 부모 객체의 필드와 메소드를 자식 객체에게 물려주는 행위
		* 자식 객체는 추가적으로 확장된 필드와 메소드를 지닐 수 있다.
- 자식 클래스를 외부로부터 은닉하는 캡슐화의 일종
4) 다형성
- 서로 다른 클래스의 객체가 같은 메시지를 받았을 때 각자의 방식으로 동작하는 능력

(참고 : https://gmlwjd9405.github.io/2018/07/05/oop-features.html )

## 5. OOP의 5대 원칙 (SOLID)
1) S(단일 책임 원칙 SRP, Single Responsibility Principle)
- 객체는 단 하나의 책임을 가져야 한다 
- 변경 사유가 될만한 것도 하나가 되기 때문에, 응집도를 높일 수 있다
2) O(개반-폐쇄 원칙 OCP, Open Closed Priciple)
- 기존의 코드를 	변경하지 않으면서 추가할 수 있도록 설계되어야 한다
- 변해야 하는 것은 쉽게 변하게 해야 하고, 변하지 말아야 하는 것은 영향을 받지 않게 해야 한다.
3) L(리스코프 치환 원칙 LSP, Liskov Substitution Principle)
- 일반화 관계에 대한 이야기며, 자식 클래스는 최소한 자신의 부모 클래스에서 가능한 행위는 수행할 수 있어야 한다
- LSP를 만족하면 부모 클래스의 인터페이스 대신에 자식 클래스의 인터페이스로 대체해도 프로그램의 의미는 변화되지 않는다.
- LSP를 만족시키기 위해서는 재정의하지 않는다(오버라이드).
4) I(인터페이스 분리 원칙 ISP, Interface Segregation Principle)
- 인터페이스를 클라이언트에 특화되도록 분리시키라는 설계 원칙이다
- 클라이언트는 자신이 사용하지 않는 메서드에 생긴 변화로 인한 영향을 받지 않는다.
- ISP를 만족하면 SRP를 만족한다!
5) D(의존 역전 원칙 DIP, Dependency Inversion Principle)
- 의존 관계를 맺을 때, 변화하기 쉬운 것 또는 자주 변화하는 것보다는 변화하기 어려운 것, 거의 변화가 없는 것에 의존해야한다

( 참고 : https://gmlwjd9405.github.io/2018/07/05/oop-solid.html )

## 6. 객체지향 & 절차지향 프로그래밍
* 절차지향 프로그래밍
	* 실행하고자 하는 절차를 정하고, 이 절차대로 프로그래밍하는 방법
	* 목적을 달성하기 위한 일의 흐름에 중점을 둔다.
* 객체지향 프로그래밍
	* 컴퓨터 프로그램을 객체들의 모임으로 파악하고자 하는 프로그래밍 방법
	* 각 객체들은 서로 메시지를 주고 받을 수 있으며 데이터를 처리할 수 있다.
	* 객체지향 프로그래밍의 장점
		* 프로그램을 유연하고 변경이 용이하게 만든다.
		* 프로그램의 개발과 보수를 간편하게 만든다.
		* 직관적인 코드 분석을 가능하게 한다.
		
( 참고 : https://velog.io/@cyranocoding/%EA%B0%9D%EC%B2%B4-%EC%A7%80%ED%96%A5-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8DOOP-Object-Oriented-Programming-%EA%B0%9C%EB%85%90-%EB%B0%8F-%ED%99%9C%EC%9A%A9-%EC%A0%95%EB%A6%AC-igjyooyc6c)

## 7. OOP의 기본 구성 요소
```java
public class person{
	private int age;
	private String name;
	private String home;
	
	... (생성자 생략)
	
	public void introduce(){
		System.out.println("저는 " + Integer.toString(age) + "살 " + home + "에 사는 " + name + "입니다.");
	}
}

... (메인 생략)

person Charlie = new person(23, "김찰리", "서울시 마포구");
Charlie.introduce();

...
```

1) 클래스(Class)
* 같은 종류의 집단에 속하는 속성과 행위를 정의한 것. 
* 다른 클래스와 독립적으로 디자인해야 한다.
* 위에서는 사람들의 속성을 담고 있는 "person"이 클래스가 된다.
2) 객체(Object)
* 클래스의 인스턴스(Instance). 
* 상위 클래스의 속성을 가지고 있으면서 개별적인 특성과 행위(메소드, Method) 또한 가지고 있다.
* 위에서는 클래스 "person"에 개별적 특성을 부여받은 "Charlie"가 객체가 된다.
3) 메서드(Method)
* 클래스로부터 생성된 객체를 사용하는 방법.
* 객체의 속성을 조작하는 데 사용된다.
* 위에서는 객체 "Charlie"에서 부여받은 속성들을 활용해 자기소개를 출력하는 "introduce"가 메소드가 된다.
	
### 8. 오버로딩 & 오버라이딩
* 오버로딩(Overloading)
	* 메서드가 같은 이름을 가지고 있지만, 파라미터의 자료형이나 개수가 다른 경우
	```java
	public void introduce(int age){...}
	public void introduce(String name){...}
	public void introduce(int age, String name){...}
	```
* 오버라이딩(Overriding)
	* 상위 클래스에 존재하는 메소드를 반환값, 이름, 파라미터 등을 동일하게 하여 재정의 하는 것
	* 재정의하는 경우, 기능을 확장시킬 수 도 있다.
	```java
	public class cloth{
		private String name;
		public void introduce(){
			System.out.println(name + "은 옷이야.");
		}
	}
	
	public class prada extends cloth{
		@Override	// 개발자가 실수하지 않도록 @Override 어노테이션 사용을 권장
		public void introduce(){
			System.out.println(name + "은 아주 비싼 옷이야.");
		}
	}
	```
### 9. 추상 클래스 & 인터페이스
* 추상 클래스(Abstract Class)
	* 개념
		* abstract 키워드로 선언된 클래스
			* 클래스가 추상 메서드를 1개 이상 포함한다면, 반드시 추상 클래스로 선언해야 한다.
			* 하지만, 클래스에 추상 메서드가 없는 경우도 추상 클래스로 선언 가능.
			* 추상 매서드(Abstact Method)
				* abstract 키워드와 함께 원형만 선언되고, 코드는 작성되지 않은 메서드
				```java
				public abstract int result();
				public abstract int result(){
					return 100;	// 추상 메서드지만, 코드가 작성되었기 때문에 오류 발생
				}
				```
	* 선언
		* 서브 클래스에서 슈퍼 클래스의 모든 추상 메서드를 오버라이딩하여 실행가능한 코드로 구현한다.
	* 목적
		* 객체를 생성하기 위한 클래스가 아닌, 상속을 위한 부모 클래스로 활용하는 것이 목적이다.
		* 여러 클래스의 공통적인 부분을 추상화하여 자식 클래스에게 메서드 구현을 강제한다.
		* 부모 클래스로부터 메서드에 대한 책임을 위임 받은 자식 클래스는 메서드의 기능을 구현 및 확장하는 것이 주요 목적이다.
		
		```java
		/* 추상 클래스 */
		public abstract class fruit{
			private String name;
			public abstract void printFruit();
		}
		```
		```java
		/* 자식 클래스 */
		public class apple extends fruit{
			/* 추상 메서드의 오버라이딩 */
			public void printFruit(){
				System.out.println("나는 " + this.name + "야!");
			}
		}
		```
* 인터페이스(Interface)
	* 개념
		* 추상 메서드와 상수만을 포함하며, interface 키워드로 선언한다.
		* 모든 메서드는 추상 메서드로서, public abstract 속성이며 생략가능하다.
		* 상수는 public static final 속성이며 생략가능하다.
		* 다른 인터페이스를 상속받아 새로운 인터페이스를 만들 수 있다.
		```java
		interface avante extends car{...}
		```
	* 구현
		* 인터페이스를 상속받고, 추상 메서드를 모두 구현한 클래스를 작성한다.
		* implements 키워드를 사용하여 구현한다.
	* 목적
		* 상속받을 서브 클래스에게 구현할 메서드들의 원형을 모두 알려주어, 클래스가 자신의 목적에 맞게 메서드를 구현하도록 하는 것이다.
		* 구현 객체의 같은 동작을 보장하기 위한 목적이 있다.
	
	```java
	/* 인터페이스 개념 */
	interface rentCar {
		int Day = 10;		// = public static final int Day = 10;
		void printCar();	// = public abstract void printCar();
		void printDay();
	}
	```
	
	```java
	/* 인터페이스 구현 */
	class sonata implements rentCar {
		// 인터페이스에서 선언된 추상 메서드를 모두 오바리이딩해주어야 한다.
		public void printCar(){...}
		public void printDay(){...}
		// 새로운 메서드를 선언하여 기능을 확장할 수도 있다.
		public void introduceCar(){...}
	}
	```
	
	* 추상 클래스와 인터페이스의 공통점 & 차이점
		* 공통점
		1. 객체를 생성할 수 없다.
		2. 선언만 있고 구현 내용이 없다.
		3. 자식 클래스에게 메서드의 구체적인 구현에 대한 책임을 위임한다.
		* 차이점
		
		종류 | 추상 클래스 | 인터페이스
		---- | ---- | ----
		목적 | 상속을 위한 부모 클래스 | 구현 객체들의 같은 동작을 보장
		클래스 | O | X
		상속 | 단일 | 다중
		예시 | “is a kind of” | “can do this”
		
		* "is a kind of" : Sports(Abstract Class) - Soccer, BasketBall...
		* "can do this" : Runable(Interface) - Car, cheetah, man...
