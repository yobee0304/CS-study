# SpringBoot

## 0. SpringBoot

### 0-1. 구조
* 스프링 부트의 프로젝트 구조는 메이븐 기본 프로젝트 구조와 일치하다.
  * 소스 코드
  * 소스 리소스
  * 테스트 코드
  * 테스트 리소스
* @SpringBootApplication이 붙은 클래스를 '메인 애플리케이션'이라고 한다.
  * 사용하고 있는 패키지 중, 최상위 패키지에 메인 애플리케이션을 위치시켜야 한다.
  * @SpringBootApplication은 @ComponentScan을 포함한다.
  * 또한, @ComponenteScan은 현재 패키지를 기준으로 모든 하위 패키지를 탐색 범위로 잡고 빈으로 등록하기 때문이다.

### 0-2. 원리
* <parent> 섹션으로 등록한 상위 dependency에서 의존성을 관리하기 때문에, 사용자가 직접 관리할 부분을 줄여준다. (ex. 의존성 버전)
  ```xml
  <!-- pom.xml -->
  <parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.3.2.RELEASE</version>
    <relativePath/>
  </parent>
  ```
  * 상위 dependency에서 관리하지 않는 의존성은 따로 버전을 명시해 주어야 한다.
  * 관리하는 의존성이라도, 특정 버전을 명시하면 오버라이딩되어 실행된다.
    * 버전이 명시되지 않은 의존성을 사용하면, 어떤 버전의 의존성을 사용할지 보장하지 못하기 때문이다.
  * parent를 사용하지 않고, <dependencyManagement> 섹션을 사용해서 직접 의존성을 관리할 수 있다.
    * 하지만, parent를 사용하면 의존성 이외에도 소스인코딩, 자바 버전 등등 다양한 기본 설정들을 함께 관리할 수 있기 때문에 더 유리하다.
  
* 스프링 부트가 관리하는 의존성 변경
  * 자신의 프로젝트에 있는 pom.xml의 properties 섹션에서 오버라이딩
  
* 자동 설정
  * @SpringBootApplication은 아래 3개의 어노테이션을 합한 것과 같은 동작을 한다.
    * @SpringBootConfiguration
    * @ComponentScan
    * @EnableAutoConfiguration
  * @SpringBootApplication은 총 2번 클래스를 빈으로 등록한다.
    * @ComponentScan
      * @Component을 가진 클래스를 빈으로 등록한다.
      * 범위는 @ComponentScan이 붙은 클래스의 패키지를 포함하여 하위 패키지까지이다.
      * @Configuration, @Repository, @Service, @Controller, @RestController는 @Component를 포함하고 있으므로 탐색 범위에 포함한다.
    * @EnableAutoConfiguration
      * 여러 자동 설정들이 포함되어 있다.
      * 결과적으로 Configuration(자바 설정) 파일인 셈이다.
      * 조건에 따라 빈으로 등록하기도 하고 안하기도 함. (@ConditionalOn~~~)
      * @EnableAutoConfiguration을 사용하지 않더라도 실행은 가능하다. (단, 웹서버 관련 설정이 사라지기 때문에 웹서버로 동작하지는 않음)
      * 결과적으로 Configuration(자바 설정) 파일인 셈이다.
  * 설정 파일 등록하는 법
    1. @Configuration 파일 작성
    2. src/main/resource/META-INF에 spring.factories 파일 만들기
    3. spring.factories 안에 자동 설정 파일 추가
    4. mvn install (다른 프로젝트에서도 사용할 수 있도록 로컬 메이븐 저장소에 저장)
    
* 빈의 재정의
  * 1단계(@ComponentScan)에서 등록한 빈을 2단계(@EnableAutoConfiguration)에서 다시 등록하는 경우, 2단계에서 가져온 빈의 설정을 따른다
  * 재정의 방지 방법
    1. @ConditionalOnMissingBean : 2단계에서 덮어쓰는 것을 방지
    2. @ConfigurationProperties("holoman") : application.properties에 있는 값으로 정의
    3. @EnableConfiguration(HolomanProperties)
    
* 내장 웹 서버
  * 스프링 부트 자체는 웹 서버가 아니다!
  * 웹 서버의 실행 과정
    * 톰캣 객체 생성 - 포트 설정 - 톰캣에 컨텍스트 추가 - 서블릿 만들기 - 톰캣에 서블릿 추가 - 컨텍스트에 서블릿 매핑 - 톰캣 실행 및 대기
    * 이 모든 과정을 보다 상세하고 유연하게 실행해 주는게 바로 스프링 부트의 자동설정이다. (AutoConfiguration)
    * ServletWebServerFactoryAutoConfiguration : 서블릿 웹 서버 생성
    * DispatcherServletAutoConfiguration : 서블릿을 만들고 서블릿 컨테이너에 등록
      * AutoConfiguration이 둘로 분리 되어있는 이유는? : 서블릿 컨테이너는 설정(pom.xml)에 따라 변할 수 있지만, 서블릿은 변하지 않기 때문이다.
  * 컨테이너와 포트
    * 컨테이너
      * 스프링 부트의 자동설정으로 인해 기본 컨테이너는 '톰캣(Tomcat)'
      * 톰캣이 아닌 다른 컨테이너를 사용하고 싶다면?
        * <exclusions> 섹션을 사용해서 톰캣 의존성을 제외하고 새로운 의존성 추가
        ```xml
        <exclusions>
            <exclusion>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-starter-tomcat</artifactId>
            </exclusion>
        </exclusions>
        ```
     * 포트
       * application.properties 설정으로 웹서버 제어 가능
         ```
         # 웹서버 사용하지 않기
         spring.main.web-application-type=none

         # 웹서버 포트를 7070으로 변경
         server.port=7070

         # 웹서버 포트를 사용할 수 있는 랜덤 포트로 변경
         server.port=0
         ```
  * HTTPS와 HTTP2
    * HTTPS 설정하기
      * keytool -genkey : 키스토어 만들기
      ```
      # application.properties
      server.ssl.key-store: keystore.p12
      server.ssl.key-store-password: 123456
      server.ssl.keyStoreType: PKCS12
      server.ssl.keyAlias: spring
      ```
      * 커넥터는 하나이기 때문에, https 설정 후에는 http를 동시에 사용할 수 없다.
    * HTTP2 설정하기
      ```
      # application.properties
      server.http2.enabled=true
      ```
  * JAR 파일
    * mvn package를 하면 실행 가능한 JAR 파일 하나가 생성된다.
    * spring-maven-plugin이 해주는 일 : "패키징"
    * JAR 파일 하나에 필요한 라이브러리 JAR파일들이 모두 들어있다.
    * 기본적으로 자바는 JAR파일 안에 있는 JAR 파일들을 로딩하는 표준적인 방법이 없다.
      * 스프링 부트의 전략 = JAR파일 하나로 앱을 실행시키는 전략
        * 애플리케이션 클래스와 라이브러리 위치 구분
        * org.springframework.boot.loader.jar.JarFile을 사용해서 내장 JAR를 읽는다. 
        * org.springframework.boot.loader.Launcher를 사용해서 실행한다.
