# 데이터 베이스

## 1. RDB & NoSQL
* 관계형 데이터베이스(Relational Database)
  * 테이블(table)로 이루어져 있으며, 이 테이블은 키(Key)와 값(Value)의 관계를 나타낸다.  
  * 데이터의 종속성을 관계(relationship)로 표현한다.
  * 테이블마다 특정한 이름을 가지고, 행(row)과 열(column)에 대응하는 특정한 값을 가진다.
  * 관계형 데이터베이스의 특징
    * 데이터의 분류, 정렬, 탐색 속도가 빠르다.
    * 오랫동안 사용된 만큼 신뢰성이 높고, 어떤 상황에서도 데이터의 무결성을 보장해 준다.
    * 기존에 작성된 스키마를 수정하기가 어렵다.
    * 데이터베이스의 부하를 분석하는 것이 어렵다.
* NoSQL
  * Not only SQL의 약자
  * 관계형 데이터베이스의 한계를 극복하기 위해 만들어진 새로운 데이터 저장소
    * 고정된 규격이 존재하지 않아, 스키마 변경이 쉽다.
    * 관계형 데이터베이스보다 분산처리가 쉽다.
  * Why NoSQL?
    * 초당 데이터가 수십만개씩 쌓이는 서비스(SNS, 온라인 서비스)가 많아지면서, 관계형 데이터베이스의 한계로 인해 NoSQL을 도입하는 경우가 늘어나고 있다.
  * NoSQL 데이터베이스는 각 데이터베이스마다 기반으로 하는 데이터 모델이 다르다.
    1. Key-Value Stores (ex. Redis, Riak)
    * Hash Table과 유사한 구조
    * Key/value 모델은 매우 구현하기 쉽고, 간단하다.
    * value의 일부분을 읽거나 업데이트 한다면 매우 비효율적이다.
      
    2. Column family store (ex. Cassandra, HBase)
    * 여러 서버에 분산된 수많은 데이터를 저장, 처리하기 위한 목적.
    * 여전히 key를 사용하지만, key는 여러 개의 컬럼을 가리키고 있다. 
    * 컬럼은 컬럼 패밀리에 따라 정렬되어 진다.
    
    3. Document DB (ex. CouchDB, MongoDB)
    * 기본적으로 key-value store와 비슷하지만, 많은 key-value collection들의 collection인 document로 구성.
    * 반 정형화된 document들이 JSON과 같은 포맷으로 저장되어진다.
    * Document DB는 기본적으로 key-value DB의 차세대 버전이다.
    * 각 key마다 nested value를 허락한다. Document DB는 좀 더 효율적으로 조회를 지원한다.
  
## 2. Redis
* 메모리 기방 "Key-Value" 구조 데이터 관리 시스템
* 모든 데이터를 메모리에 저장하고 조회하기에 빠른 Read, Write 속도를 보장하는 비 관계형 데이터베이스이다.
* Redis의 특징
  * 영속성을 지원하는 인메모리 데이터 저장소.
  * 읽기 성능 증대를 위한 서버 측 복제를 지원한다.
  * 쓰기 성능 증대를 위한 클라이언트 측 '샤딩'을 지원한다.
    * 샤딩(Sharding) : 같은 테이블 스키마를 가진 데이터를 다수의 데이터베이스에 분산하여 저장하는 방법
  * [ String, Set, Sorted Set, Hash, List ] 의 데이터 형식을 지원한다.
* Why Redis?
  * 리스트, 배열과 같은 데이터를 처리하는데 유용하다.
  * 리스트형 데이터 입력과 삭제가 MySQL에 비해서 10배정도 빠르다고 한다.
  * 메모리를 활용하면서 영속적으로 데이터 보존를 보존할 수 있다.
  * Redis Server는 1개의 싱글 쓰레드로 수행되며, 따라서 서버 하나에 여러개의 서버를 띄우는 것이 가능하다.

(참고 : https://medium.com/@jyejye9201/%EB%A0%88%EB%94%94%EC%8A%A4-redis-%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80-2b7af75fa818)

## 3. Transaction & ACID
### 트랜젝션(Transaction)
* 여러 작업을 하나로 묶은 단위 (ex. 읽기 - 쓰기 - 지우기 - 읽기)
* 한 덩어리의 트랜젝션은 모두 실행되거나, 아예 실행되지 않는다. (All or Nothing)
* Why Transaction?
  * 여러 작업이 진행중에 중단되는 것을 방지하여, 데이터의 유효성을 보장하기 위해 필요하다.
  
### ACID
* 데이터의 유효성을 보장하기 위한 트랜젝션의 특징들의 앞글자를 따 놓은 단어
1. Atomicity(원자성)
* 모든 작업이 실행되거나, 그렇지 않은 경우 롤백되는 특징

2. Consistency(일관성)
* 데이터는 미리 결정된 규칙 내에서만 수정이 가능한 특징
* 숫자 컬럼에 문자열 데이터가 저장되지 않도록 보장한다.

3. Isolation(고립성)
* A와 B 두 개의 트랜잭션이 수행 중일 때, A의 작업들에게 보이는 B의 정도를 나타냅니다.
* A와 B의 작업들은 서로의 트랜젝션에 영향을 주어서는 안됩니다. (데이터 유효성 보장)

4. Durability(영속성)
* 한 번 적용된 트랜젝션은 영원히 적용되는 특성

( 참고 : https://medium.com/@chrisjune_13837/db-transaction-%EA%B3%BC-acid%EB%9E%80-45a785403f9e )

## 4.인덱스(Index)
* 테이블에 대한 동작 속도를 높여주는 자료 구조
* MySQL을 첫 번째 열부터 전체 테이블에 걸쳐 연관된 열을 모두 확인하므로, 테이블의 크기가 커질수록 비용이 크게 증가한다.
  * 만약, 테이블이 쿼리의 컬럼에 대한 인덱스를 가지고 있다면, 데이터 중간에서 검색 위치를 빠르게 잡을 수 있다.

1. 기존 테이블에 인덱스 추가하기
```
ALTER TABLE 테이블명 ADD INDEX (필드명(크기));
```
2. 테이블 생성시 인덱스 추가하기
```
CREATE TABLE 테이블명 (
    필드명 데이터타입(크기), INDEX (필드명(크기))
    ...
    ) ENGINE MyISAM;
```

## 5. 파티셔닝(Partitioning)
* 개념
  * 큰 table이나 index를 관리하기 쉽도록 보다 작은 단위인 partition으로 분할하는 것을 말한다.
  * DB에 접근하는 애플리케이션 입장에서는 물리적 데이터 분할을 인식하지 못한다. (여전히 하나의 table로 인식)
* 배경
  * 하나의 DBMS에 크기가 큰 table이 존재하는 경우, 용량과 성능 측면에서 많은 이슈가 발생한다.
  * '파티셔닝'기법을 통해, 소프트웨어적으로 데이터베이스를 분산 처리하여 성능이 저하되는 것을 방지하고 관리를 보다 수월하게 한다.
* 장단점
  * 장점
    * Full Scan에서 Access 범위를 줄여 성능 향상 효과를 기대할 수 있다.
    * 전체 데이터의 훼손 가능성이 줄어들어 데이터 가용성이 향상된다.
    * partition별로 독립적으로 백업 및 복구가 가능하다.
  * 단점
    * table간 JOIN에 대한 비용이 증가한다.
    * table과 index는 무조건 같이 파티셔닝 해야 한다.
* 종류
  * 수평(horizontal) 파티셔닝
![horizontal_partitioning](https://gmlwjd9405.github.io/images/database/horizontal-partitioning.png)
    * 스키마가 같은 데이터를 두 개 이상의 테이블에 나누어 저장하는 것을 말한다.
    * 샤딩(Sharding)과 동일한 개념
    * 하나의 테이블에 저장되어 있는 데이터의 개수가 작아지고 index의 개수 또한 작아지므로, 성능이 향상된다.
    * 데이터를 찾기 위해서 여러 개의 테이블을 확인해야 하므로 latency가 증가한다.
  * 수직(vertical) 파티셔닝
![vertical_partitioning](https://gmlwjd9405.github.io/images/database/vertical-partitioning.png)
    * 모든 컬럼중 특정 컬럼들을 쪼개서 따로 저장하는 방식이다.
    * 이미 정규화 되어있는 테이블을 다시 분리하는 과정
    * 테이블에서 자주 사용되는 특정 컬럼을 분리하여 성능을 향상시킬 수 있다.
  
( 참고 : https://gmlwjd9405.github.io/2018/09/24/db-partitioning.html )
