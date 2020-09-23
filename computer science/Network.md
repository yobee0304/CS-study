# 네트워크

## 1. HTTP & HTTPS
  1. HTTP
  * "HyperText Transfer Protocol"의 약자
  * 서로 다른 시스템들 사이에서 통신을 주고 받게 해주는 가장 기본적은 프로토콜
  * 서버에서 브라우저로 전송되는 정보가 암호화가 되어있지 않다. (데이터 도난의 위험 존재)
  * 한 Connection당 하나의 응답 요청을 처리할 수 있다.
    * 동시 접속이 불가하다.
    * 요청과 응답이 순차적으로 진행된다.
  
  1-1. HTTP2
  
  2. HTTPS
  * "HyperText Transfer Protocol Secure"의 약자
  * SSL(Secure Socket Layer 보안 소켓 계층)을 사용하여 통신을 주고 받는 프로토콜
  * HTTP와 HTTPS를 구분짓는 가장 큰 차이점은 "SSL 인증서"이다.
  * 사용자가 사이트에 제공하는 정보를 암호화하기 때문에, 중간에서 데이터를 가로챈다 하더라도 해독이 불가능하다.
  
## 2. Proxy Server
  * Proxy란 "대리"라는 의미를 가지고 있다.
  * 주로 보안상의 이유로 인해 통신할 수 없는 두 접점이 서로 통신할 수 있도록 중계 기능을 하는 서버를 "프록시 서버"라고 한다..
  * 서버 입장에서 프록시 서버는 '클라이언트' 역할을, 클라이언트 입장에서는 '서버'역할을 한다.
  * 프록시 서버는 요청된 내용을 캐시에 저장해 두었다가, 캐시 안에 있는 내용이 다시 요청되면 원격 서버에 접근하지 않고 데이터를 사용할 수 있다.
  * 이 때문에 데이터 전송시간을 줄일 수 있고, 외부와의 불필요한 접촉이 줄어들어 네트워크 병목 현상을 방지할 수 있다.

  (참고 : https://juyoung-1008.tistory.com/10)
  
## 3. LAN & WAN
  1. LAN(Local Area Network)
  * 사용자가 포함된 지역 네트워크
  * 공유기나 스위치를 이용하여 1대다 연결
  * 구성할때 드는 비용과 전기세 정도의 낮은 유지보수비
  * 프로토콜은 "이더넷" 사용 
  
  2. WAN(Wide Area Network)
  * LAN과 LAN사이를 광범위한 지역 단위로 구성하는 네트워크
  * 라우터는 서로 다른 네트워크를 연결하며, 로컬 환경에서 리모트 환경으로 원거리 데이터 전송을 담당한다.
  * ISP(Internet Service Provider)로부터 임대회선을 사용하기때문에 네트워크 구축 비용이 감소하지만 통신, 유지보수 비용이 증가한다.
  
  (참고 : https://ironmask.net/357)
  
## 4. Port
  * 어떤 외부 프로그램에 접속할 것인지를 가리키는 번호 (논리적인 접속 장소를 나타내는 이정표)
  * URI 문법에 의해 표기하면, 000.000.000.000:21로 표현할 수 있다.
    * 여기서, 000.000.000.000는 IP, 21은 Port 번호이다.
    * IP주소는 컴퓨터를 찾을 때 필요하며, Port는 컴퓨터 안에서 프로그램을 찾을 때 필요하다.
    
## 5. URI & URL
  1. URI(Uniform Resource Identifier)
  * 우편물 주소같은 개념이다.
  * 정보 리소스를 고유하게 식별하고 위치를 저장할 수 있다.
  * URL과 URN 두 가지 방식이 있다.
  
  2. URL(Uniform Resource Location)
  * 특정 서버의 한 리소스에 대한 구체적인 위치를 나타낸다
  * 리소스가 정확이 어디에 있고, 어떻게 접근하는지를 분명히 나타낸다.
  ```
  http://naver.com - 네이버 사이트의 URL
  http://img.naver.net/static/www/dl_qr_naver.png - 네이버 앱 QR 코드의 이미지에 대한 URL
  ```
  
  3. URN (Uniform Resource Name)
  * 콘텐츠를 이루는 한 리소스에 대해, 그 리소스의 위치에 영향 받지 않는 유일무이한 이름 역할을 한다.
  * 이 위치 독립적인 URN은 리소스를 여기저기로 옮기더라도 문제없이 동작한다.
  * 리소스가 그 이름을 변하지 않게 유지하는 한, 여러 종류의 네트워크 접속 프로토콜로 접근해도 문제없다.
  ```
  urn:ietf:rfc:2141 - 'RFC 2141' 문서
  ```
  
  (참고 : https://mygumi.tistory.com/139)
  
## 6. REST
  * 정의
    * Representational State Transfer의 약자
    * HTTP URI를 통해 자원(Resource)을 명시하고, HTTP Method를 통해 자원에 대한 CRUD Operation을 적용하는 것을 의미한다.
  * 장점
    * HTTP 프로토콜의 인프라를 그대로 사용하기 때문에 REST API를 활용하기 위한 별도의 인프라가 필요 없다.
    * HTTP 표준 프로토콜을 따르는 모든 플랫폼에서 이용 가능하르모, 범용성이 좋다.
    * 서버와 클라이언트의 역할을 명확하게 분리할 수 있다.
  * 단점
    * HTTP Method의 형태가 제한적이기 때문에 사용할 수 있는 메소드가 4가지밖에 없다.
    * 구형 브라우저가 지원하지 못하는 부분이 존재한다.(PUT, DELETE)
  * REST가 필요한 이유
    * 최근의 서버 프로그램은 웹뿐만 아니라 안드로이드, IOS 같은 모바일 디바이스와도 통신이 가능해야한다.
  * REST의 구성 요소
    1. 자원(Resource) : URI
      * 모든 자원에는 고유의 ID가 존재하고, 자원은 서버에 존재한다.
      * 여기서 고유 ID 역할은 URI가 담당한다.
      * 클라이언트는 URI를 통해 자원을 지정하고, 해당 자원에 대한 조작을 서버에게 요청한다.
    2. 행위(Verb) : HTTP Method
      * HTTP Method는 GET, POST, PUT, DELETE 메소드를 제공한다.
    3. 표현(Representation of Resource)
      * 클라이언트가 자원에 대한 조작을 요청하면, 서버는 이에 적절한 응답을 제공한다.
      * 응답은 주로 JSON, XML로 데이터를 주고 받는 것이 일반적이다.
  * RESTful이란?
    * REST를 REST하게 쓰는 방법
    * REST원리를 따르는 시스템은 RESTful하다고 할 수 있다.
    * RESTful하지 못한 경우
      * CRUD를 한 Method만으로 구현한 경우
      * route에 resource,id 외의 정보가 들어가는 
    
(참고 : https://gmlwjd9405.github.io/2018/09/21/rest-and-restful.html)

## 7. HTTP Method
1. GET
* URI가 가진 정보를 검색하기 위해 서버에 검색을 요청하는 메서드

2. POST
* 요청 URI에 폼 입력을 처리하기 위해 구성한 서버 측 스크립트 혹은 CGI 프로그램으로 구성되고 Form Action과 함께 전송된다.
* 이 때, 헤더 정보에 포함되지 않고 데이터 부분에 요청 정보가 들어있다.

3. PUT
* POST와 유사한 구조
* 헤더 이외의 메시지가 함께 전송된다.

4. DELETE
* 웹서버의 파일을 삭제하기 위한 메서드 (PUT과 반대 개념)

5. HEAD
* GET과 유사한 방식
* 서버에서는 헤더 정보 이외에는 어떤 정보도 보내지 않는다.

(참고 : https://gyrfalcon.tistory.com/entry/HTTP-응답-코드-종류-HTTP-메소드-종류)
