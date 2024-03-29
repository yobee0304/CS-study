# Python

## 1. 얕은 복사 & 깊은 복사
* 얕은 복사(shallow copy)
  ```python
  a = [1, 2, 3, 4, 5, 6, 7]
  b = a[:3]
  # 4414427616 4414430176
  print(id(a), id(b))
  ```
  * list의 슬라이싱을 통해 새로운 리스트를 생성한 경우, 새로 생성된 리스트에는 새로운 id를 부여되며 서로 영향을 주지 않습니다.
  * 하지만 리스트안에 값들은 서로 같은 id를 가리키고 있습니다.
  ```python
  # 4413336480 4413336480
  print(id(a[0]), id(b[0]))
  ```
  * 얕은 복사 상태에서, 리스트안에 리스트 mutable객체 안에 mutable객체인 경우 문제가 발생합니다.
  ```python
  import copy
  
  a = [[1,2], ['a','b']]
  # copy 모듈의 copy 메소드가 얕은 복사에 해당한다.
  b = copy.copy(a)

  # b[0]값을 변경하면 a[0]값도 동시에 변경
  b[0].append(3)
  # a: [[1, 2, 3], ['a', 'b']] / b: [[1, 2, 3], ['a', 'b']]

  # 재할당하는 경우는 문제가 되지 않습니다 (재할당과 동시에 메모리 주소도 변경)
  b[1] = ['c', 'd']
  # a: [[1, 2, 3], ['a', 'b']] / b: [[1, 2, 3], ['c', 'd']]
  ```
  
* 깊은 복사(deep copy)
  * 내부에 있는 객체들까지도 새롭게 복사하는 것
  ```python
  import copy
  
  a = [[1,2], ['a','b']]
  # copy 모듈의 deepcopy 메소드가 얕은 복사에 해당한다.
  b = copy.deepcopy(a)

  # 내부 객체의 id 또한 서로 다르다
  # 4422545488 4422858144
  print(id(a[0]), id(b[0]))

  # b[0]값을 변경하여도 a[0]값은 변하지 않는다.
  b[0].append(3)
  # a: [[1, 2], ['a', 'b']] / b: [[1, 2, 3], ['a', 'b']]
  ```
  
(참고 : https://wikidocs.net/16038)
