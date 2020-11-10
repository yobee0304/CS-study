# SpringBoot

## 1. 구조
* 스프링 부트의 프로젝트 구조는 메이븐 기본 프로젝트 구조와 일치하다.
  * 소스 코드
  * 소스 리소스
  * 테스트 코드
  * 테스트 리소스
* @SpringBootApplication이 붙은 클래스를 '메인 애플리케이션'이라고 한다.
  * 사용하고 있는 패키지 중, 최상위 패키지에 메인 애플리케이션을 위치시켜야 한다.
  * @SpringBootApplication은 @ComponentScan을 포함한다.
    * @ComponenteScan은 현재 패키지를 기준으로 모든 하위 패키지를 탐색 범위로 잡고 빈으로 등록하기 때문이다.

## 2. 원리
* <parent> 섹션으로 등록한 상위 dependency에서 의존성을 관리하기 때문에, 사용자가 직접 관리할 부분(ex. 의존성 버전)을 줄여준다. 
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

## 3. 활용
* SpringApplication
  * 기본 로그 : INFO 레벨
  ```
  2020-09-17 17:50:06.865  INFO 38673 --- [  restartedMain] ...
  ```
  * FailureAnalyzer : 에러가 났을때, 에러 메시지를 커스터마이징할 수 있다.
  * Banner
  ```
  # 기본 배너
    .   ____          _            __ _ _
   /\\ / ___'_ __ _ _(_)_ __  __ _ \ \ \ \
  ( ( )\___ | '_ | '_| | '_ \/ _` | \ \ \ \
   \\/  ___)| |_)| | | | | || (_| |  ) ) ) )
    '  |____| .__|_| |_|_| |_\__, | / / / /
   =========|_|==============|___/=/_/_/_/
   :: Spring Boot ::        (v2.3.2.RELEASE)
  ```
    * banner.txt | gif | jpg | png 파일로 새로운 배너 설정 가능
    * ${spring-boot.version(스프링 부트의 버전)}등의 변수를 사용할 수 있다.
    * Banner 클래스를 구현하고 SpringApplication.setBanner()로 설정 가능하다.
    * 배너 끄는 방법
    ```
    app.setBannerMode(Banner.Mode.off);
    ```
  * SpringApplicationBuilder로 빌더 패턴 사용 가능
  ```Java
  new SpringApplicationBuilder()
          .main(SpringinitApplication.class)
          .run(args);
  ```
  * 리스너를 빈으로 등록했더 하더라도, 특정 이벤트가 빈이 등록되기 이전에 발생한다면 실행되지 않는다.
    * 따로 직접 등록 해줘야한다. 
    ```java
    SpringApplication.addListners();
    ```
  * WebApplicationType 설정
    * SERVLET (Spring MVC)
    * REACTIVE (Spring WebFlux)
    * NONE (둘 다 없으면)
    * MVC, WebFlux 둘 다 있으면 "SERVLET"으로 작동 : servlet이 있는지 없는지를 먼저 확인하기 때문에
  ```java
  SpringApplication.setWebApplicationType();
  ```
  * 애플리케이션 아규먼트 사용하기
    * ApplicationArgument를 빈으로 등록해주기 때문에 가져다 쓰면 된다.
  * 애플리케이션 실행한 뒤 실행하고자 할 때
    * ApplicationRunner
    * @Order : 순서 지정 가능
    
### 외부 설정
* 사용할 수 있는 외부 설정
  * properties : key-value 형대로 값을 정의하면 참조해서 사용 가능
    * test 디렉터리에 resources 디렉터리를 생성해서 Test Resources로 지정한 다음, 또 다른 application.properties를 생성하면 테스트용 properties를 사용할 수 있다.
    * 기존의 properties를 테스트용 properties가 오버라이딩 되기 때문에, 기존 properties에 있는 value가 테스트 properties에 없다면 오류가 난다.
  ```
  @Value("${key}")
  private String value;
  ```
  * YAML
  * 환경 변수
  * 커맨드 라인 아규먼트
  
* 프로퍼티 우선 순위
1. 유저 홈 디렉토리에 있는 spring-boot-dev-tools.properties
2. 테스트에 있는 @TestPropertySource
3. @SpringBootTest 에노테이션의 properties 애트리뷰트
4. 커맨드 라인 아규먼트
5. SPRING_APPLICATION_JSON (환경 변수 또는 시스템 프로티)에 들어있는 프로퍼티
6. ServletConfig 파라미터
7. ServletContext 파라미터
8. java:comp/env JNDI 애트리뷰트
9. System.getProperties() 자바 시스템 프로퍼티
10. OS 환경 변수
11. RandomValuePropertySource
12. JAR 밖에 있는 특정 프로파일용 application properties
13. JAR 안에 있는 특정 프로파일용 application properties
14. JAR 밖에 있는 application properties
15. JAR 안에 있는 application properties
16. @PropertySource
17. 기본 프로퍼티 (SpringApplication.setDefaultProperties)

* application.properties 우선 순위 (겹치는게 있으면 높은게 낮은 것을 오버라이딩 한다)
1. file:./config/
2. file:./
3. classpath:/config/
4. classpath:/

* 랜덤값 설정하기 : ${random.'Type'}, Type = int, float, ...
* 플레이스 홀더
  * name = gildong
  * fullName = ${name} hong

* 타임-세이프 프로퍼티 : @ConfigurationProperties
  * 여러 프로퍼티를 묶어서 읽어올 수 있다.
  * 빈으로 등록해서 다른 빈에 주입할 수 있다.
    * @EnableConfigurationProperties
    * @Component
    * @Bean
    
* 융통성 있는 바인딩(Relaxed Binding)
  * context-path(케밥)
  * context_path(언드스코어)
  * contextPath(캐멀)
  * CONTEXTPATH
    * 융통성 있게 모두 같은 걸로 취급하여 매핑한다.
    
* 프로퍼티 타입 컨버전
  * 스프링 부트에서 자체적으로 프로퍼티를 알맞은 타입으로 컨버젼
  * @DurationUnit
    * s, m, d 같이 시간을 나타내는 sufix만 프로퍼티에 잘 붙이면 어노테이션을 사용하지 않아도 컨버젼 된다.

* 프로퍼티 값 검증
  * @Validated
  * JSR-303(@NotNull, @Size, ...)
  
* @Value
  * SpEL(Spring Expression Language) 사용 가능
  * @DurationUnit, @Validated는 사용 불가

* 프로파일(Profile)
  * 선언 : @Profile({profile_name})
  * 프로파일 활성화 : spring.profile.active={profile_name}
  * 프로파일 추가 : spring.profile.inclue={profile_name}
  * 프로파일용 프로퍼티 : spring-{profile_name}.properties
  
* 로깅
  * --debug(일부 핵심 라이브러리만 디버깅 모드로)
  * --trace(정부 다 디버깅으로)
  * 컬러 출력: spring.output.ansi.enabled
  * 파일 출력: logging.file / logging.path
  * 로그 레벨 조정: logging.level.패키지 = 로그 레벨(특정 패키지마다 로그 레벨 설정 가능)

* 커스텀 로그 설정 파일 사용하기
  * Logback: logback-spring.xml(추천)
    * Logback extension (추가 기능 제공)
      * 프로파일 <springProfile name="프로파일">
      * Environment 프로퍼티 <pringProperty>
  * Log4J2: log4j2-spring.xml

### 테스트
- spring-boot-starter-test(test 범위로)를 추가
```
<scope>test</scope>
```
- @SpringBootTest
  - @RunWith(SpringRunner.class)와 같이 사용해야 한다.
  - 빈 설정 파일은 자동으로 찾는다.(@SpringBootApplication)
- webEnvironment
  - @SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.{...})
  - MOCK: mock servlet environment. 내장 톰캣 X
    - @AutoConfigureMockMvc 붙이고 MockMvc 빈을 주입 받아서 사용
  - RANDON_PORT, DEFINED_PORT: 내장 톰캣 O
  - NONE: 서블릿 환경 제공 X
- @MockBean
  - ApplicationContext에 들어있는 빈을 Mock으로 만든 객체로 교체한다.
  - Controller를 원본이 아닌 복사본을 사용하게 된다.
- 슬라이스 테스트
  - @SpringBootTest는 큰 범위의 통합 테스트
  - 통합 테스트를 하지 않고, 레이어 별로 잘라서 테스트하고 싶을 때?
    - @JsonTest, @WebMvcTest, @WebFluxTest, @DataJpaTest
- OutputCaptureRule : 로그를 비롯한 콘솔에 출력되는 모든 사항을 캡쳐

- Spring-Boot-Devtools
  - 의존성으로 추가하여 사용 가능
  - 캐시 설정을 개발 환경에 맞게 변경
  - 클래스패스에 있는 파일이 변경 될 때마다 자동으로 restart
    - 직접 restart하는 것보다 빠르다.
  - 라이브 릴로드 : 리스타트 했을 때 브라우저를 자동으로 refresh하는 기능
  - 글로벌 설정
    - ~/.spring-boot-devtools.properties : 1순위 외부설정 파일

## 4. Spring MVC
### 소개
* 스프링 MVC는 AutoConfiguration에 의해서 자동 설정되므로, 별다른 설정 없이 사용 가능하다.
* 스프링 MVC 기능 확장 : @Configuration + WebMvcConfigurer
* 스프링 MVC 기능 재정의 : @Configuration + @EnableWebMvc
  * 재정의할 경우, 스프링 부트에서 자동으로 제공하는 설정이 모두 리셋 되어 일일히 추가해줘야 하기 때문에 추천하지 않는다!

### HttpMessageConverters
* HTTP 요청 본문을 객체로 변경하거나, 객체를 HTTP 응답 본문으로 변경할 때 사용한다. (@RequestBody, @ResponseBody)
* Default는 Json타입
* 클래스에 @RestConroller 어노테이션이 붙어있따면, @ResponseBody 생략 가능
```Java
@PostMapping("/user")
public @ResponseBody User create(@RequestBody User user){
    return null;
}

// @ResponseBody가 생략된 핸들러
@PostMapping("/user")
public User create(@RequestBody User user){
    return null;
}
```

### ViewResolve
* 들어오는 Accept Header에 알맞는 응답을 제공하는 기능.
  * Accept Header : 어떠한 형식의 응답을 원하는지 서버 사이드에 제공하는 정보
  
### 정적 리소스
* 서버 사이드로 요청이 들어왔을 때, 새로운 뷰를 생성하지 않고 해당하는 리소스가 이미 만들어져 있는 리소스.
* 기본 리소스 위치
  * classpath:/static
  * classpath:/public
  * classpath:/resources/
  * classpath:/META-INF/resources
  * spring.mvc.static-path-pattern : 맵핑 설정 변경 가능
  * spring.mvc.static-locations : 리소스 찾을 위치 변경 가능
* Last-Modified 헤더를 통해 304 응답을 보낸다.
  * 변경 사항이 없으면 캐시에 있는 데이터를 사용하기 때문에 속도가 더 빠르다.
  * 변경 사항이 있으면 200 응답을 보낸다.
* ResourceHttpRequestHandler가 처리한다.
  * WebMvcConfigurer의 addResourceHandlers로 커스터마이징 할 수 있다.
```Java
// path의 마지막이 "/"로 끝나야 맵핑이 잘 된다.
@Override
public void addResourceHandlers(ResourceHandlerRegistry registry){
    registry.addResourceHandler("/m/**")
         .addResourceLocations("classpath:/m/")
         .setCachePeriod(20);
}
```

### 웹JAR
* 스크립트 라이브러리(JQuery, Bootstrap)를 웹JAR파일을 통해 추가 가능
* 웹JAR 맵핑 : "/webjars/**"
* webjars-locator-core 의존성 : 웹JAR 버전 생략 가능

### index 페이지 & 파비콘
* 웰컴페이지
  * 루트로 접근했을 때 확인할 수 있는 페이지
  * index.html -> index.템플릿 순으로 확인하고, 존재하면 웰컴페이지로 사용
  * 둘 다 없으면 에러 발생
* 파비콘
  * favicon.ico
  * 페이지 탭에 표시되는 작은 아이콘

### 템플릿 엔진
* 스프링 부트가 자동 설정을 지원하는 템플릿 엔진
  * Thymeleaf
  * FreeMarker
  * Groovy
  * Mustache
* JSP는 권장하지 않는 이유
  * JAR 패키징 할 때는 동작하지 않고, WAR 패키징을 따로 해야한다
  * Undertow 서블릿 엔진의 경우, JSP를 지원하지 않음
* Thymeleaf
  * 템플릿 엔진이 있더라도, 서블릿 엔진에 의해서 최종적인 템플릿이 완성된다.
  * Thymeleaf는 서블릿 엔진에 독립적으로 동작하는 템플릿 엔진이다.
  
### HtmlUnit
* HtmlUnit : HTML의 단위테스트를 위한 툴
* WebClient를 주입받아 단위테스트에 사용한다.
```xml
        <dependency>
            <groupId>org.seleniumhq.selenium</groupId>
            <artifactId>htmlunit-driver</artifactId>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>net.sourceforge.htmlunit</groupId>
            <artifactId>htmlunit</artifactId>
            <scope>test</scope>
        </dependency>
```

### ExceptionHandler
* 스프링 MVC 예외 처리 방법
  * @ControllerAdvice
  * @ExchangepHandler
* BasicErrorHandler
  * 스프링 부트가 제공하는 기본 예외 처리기
  * HTML, JSON 응답을 지원한다.
* 커스텀 에러 페이지 : 상태 코드 값에 따라 다른 에러 페이지를 보여준다.
  * 404.html : 상태 코드가 404일때의 에러 페이지
  * 5xx.html : 상태 코드가 500대일때의 에러 페이지
  * ErrorViewResolver 구현
  
### Spring HATEOAS
* **H**ypermedia **A**s **T**he **E**ngine **O**f **A**pplication **S**tate
* 서버: 현재 리소스와 연관된 링크 정보를 클라이언트에게 제공한다.
* 클라이언트: 연관된 링크 정보를 바탕으로 리소스에 접근한다.
* 연관된 링크 정보
  * Relation
  * **H**ypertext **Ref**erence
* spring-boot-starter-hateoas 의존성을 추가하여 사용 가능하다.
* ObjectMapper 제공
  * 객체를 json으로 변환하거나, json을 객체로 변환하기 위해 필요한 맵퍼
  * 커스터마이징
    * spring.jackson.*
    * Jackson2ObjectMapperBuilder

### CORS
* SOP(Single-Origin Policy)
  * 같은 오리진에만 요청을 보낼 수 있다는 규칙
  * 기본적으로 적용되어 있는 규칙
* CORS(Cross-Origin Resource Sharing)
  * 서로 다른 오리진끼리 리소스를 공유할 수 있다
  * SOP를 우회하기 위한 기법
* Origin이란?
  * URI 스키마 (http, https)
  * hostname (whiteship.me, localhost)
  * 포트 (8080, 18080)
  * 스키마, hostname, 포트가 조합되어 하나의 오리진이 된다.
* 스프링 MVC @CrossOrigin
  * @Controller나 @RequestMapping에 추가
  8 WebMvcConfigurer 사용해서 글로벌 설정


## 5. Spring Data
### 인메모리 데이터베이스
* 지원하는 인메모리 데이터베이스  
  * H2 (추천)
  * HSQL
  * Derby
* Spring-JDBC가 클래스패스에 있으면 자동 설정이 필요한 빈을 설정해 준다.
  * DataSource
  * JdbcTemplate
* 인-메모리 데이터베이스 기본 연결 정보 확인하는 방법
  * URL: “testdb”
  * username: “sa”
  * password: “”
* H2 콘솔 사용하는 방법
  * spring-boot-devtools 추가
  * spring.h2.console.enabled=true 추가.
  * /h2-console로 접속 (이 path도 바꿀 수 있음)
  
### MySQL
* 지원하는 DBCP
  * HikariCP (기본)
  * Tomcat CP
  * Commons DBCP2
* DBCP 설정
  * spring.datasource.hikari.*
  * spring.datasource.tomcat.*
  * spring.datasource.dbcp2.*
* MySQL 커넥터 의존성 추가
```
<dependency>
   <groupId>mysql</groupId>
   <artifactId>mysql-connector-java</artifactId>
</dependency>
```
* MySQL 추가 (도커 사용)
  * docker run -p 3306:3306 --name mysql_boot -e MYSQL_ROOT_PASSWORD=1 -e MYSQL_DATABASE=springboot -e MYSQL_USER=keesun -e MYSQL_PASSWORD=pass -d mysql
  * docker exec -i -t mysql_boot bash
  * mysql -u root -p
* MySQL용 Datasource 설정
  * spring.datasource.url=jdbc:mysql://localhost:3306/springboot?useSSL=false
    * useSSL=true로 설정하고, truststore를 제공하여 SSL로 접근할 수 있게 하는 것이 최선!
  * spring.datasource.username={username}
  * spring.datasource.password={password}
  
### postgreSQL
* 의존성 추가
```
<dependency>
   <groupId>org.postgresql</groupId>
   <artifactId>postgresql</artifactId>
</dependency>
```
* PostgreSQL 설치 및 서버 실행 (docker)
```
docker run -p 5432:5432 -e POSTGRES_PASSWORD=pass -e POSTGRES_USER=keesun -e POSTGRES_DB=springboot --name postgres_boot -d postgres

docker exec -i -t postgres_boot bash

su - postgres

psql springboot

데이터베이스 조회
\list

테이블 조회
\dt

쿼리
SELECT * FROM account;
```

### Spring Data JPA
* ORM(Object-Relational Mapping)
  * 객체와 릴레이션을 맵핑할 때 발생하는 개념적 불일치를 해결하는 프레임워크
* JPA(Java Persistence API)
  * ORM을 위한 자바 표준
* 스프링 데이터 JPA
  * Repository 빈 자동 생성
  * 쿼리 메소드 자동 구현
  * @EnableJpaRepositories (스프링 부트가 자동으로 설정)
* 스프링 데이터 JPA 의존성 추가
```
<dependency>
   <groupId>org.springframework.boot</groupId>
   <artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>
```
* 스프링 데이터 JPA 사용하기
  * @Entity 클래스 만들기
  * Repository 만들기
* 스프링 데이터 리파지토리 테스트 만들기
  * H2 DB를 테스트 의존성에 추가하기
  * @DataJpaTest (슬라이스 테스트) 작성

### 데이터베이스 초기화
* JPA를 사용한 데이터베이스 초기화
  * spring.jpa.hibernate.ddl-auto
    * update : 기존의 데이터를 유지하면서 사용 가능, 객체의 변수명을 변경할 경우 테이블에는 새로운 컬럼이 생성되고 기존의 컬럼은 유지되는 문제가 발생
    * create : 기존의 테이블을 drop후 새로 생성
    * validate : 오브젝트에 릴레이션을 맵핑할 수 있는지 검증
  * spring.jpa.generate-dll=true로 설정 (기본으로는 false로 설정)
* SQL 스크립트를 사용한 데이터베이스 초기화
  * schema.sql 또는 schema-${platform}.sql
  * data.sql 또는 data-${platform}.sql
  * ${platform} 값은 spring.datasource.platform 으로 설정 가능
  
### 데이버베이스 마이그레이션
* 대표적으로 Flyway와 Liquibase가 있다.
* 의존성 추가(Flyway)
  * org.flywaydb:flyway-core
* 마이그레이션 디렉토리
  * db/migration 또는 db/migration/{vendor}
  * spring.flyway.locations로 변경 가능
* 마이그레이션 파일 이름
  * V숫자__이름.sql
  * V는 꼭 대문자로
  * 숫자는 순차적으로 (타임스탬프 권장)
  * 숫자와 이름 사이에 언더바 두 개
  * 이름은 가능한 서술적으로
  
### Redis
* 캐시, 메시지 브로커, 키/밸류 스토어 등으로 사용 가능.
* 의존성 추가
  * spring-boot-starter-data-redis
* Redis 설치 및 실행 (도커)
```
docker run -p 6379:6379 --name redis_boot -d redis
docker exec -i -t redis_boot redis-cli
```
* 스프링 데이터 Redis
  * https://projects.spring.io/spring-data-redis/
  * StringRedisTemplate 또는 RedisTemplate
  * extends CrudRepository
* Redis 주요 커맨드
  *https://redis.io/commands
```
keys *
get {key}
hgetall {key}
hget {key} {column}
```
* 커스터마이징
  * spring.redis.*
  
### MongoDB
* JSON 기반의 도큐먼트 데이터베이스
* 의존성 추가
  * spring-boot-starter-data-mongodb
* MongoDB 설치 및 실행 (도커)
```
docker run -p 27017:27017 --name mongo_boot -d mongo
docker exec -i -t mongo_boot bash
mongo
```
* 스프링 데이터 몽고DB
  * MongoTemplate
  * MongoRepository
  * 내장형 MongoDB (테스트용)
    * 운영용 MongoDB에 영향을 주지 않으면서 테스트 가능
    * de.flapdoodle.embed:de.flapdoodle.embed.mongo
  * @DataMongoTest
