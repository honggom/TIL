# 토비의 스프링 정리

### 제어의 역전 (IoC Inversion of Control)
    - 모든 제어 권한을 자신이 아닌 다른 대상에게 위임하는 것
    - ex) : 슈퍼클래스 UserDao를 상속한 서브클래스가 DB 커넥션의 기능을 따로 구현해서 사용 즉, 
            UserDao 입장에서는 서브클래스가 언제 어떻게 사용될지 UserDao는 모름 
            (UserDao의 템플릿 메서드인 add(), get() 등에서 필요할 떄 호출해서 사용)
      
- 빈 (Bean)
  - 스프링에서 제어권을 가지고 직접 만들고 관계를 부여하는 오브젝트
  - 스프링에서 이 빈의 생성과 관계설정 같은 제어를 담당하는 IoC 오브젝트를 <strong>빈 팩토리</strong>라고 부름
  - 빈 팩토리의 확장한 것이 <strong>애플리케이션 컨텍스트</strong>
    
- 어노테이션 (Annotation)
  - @Configuration : 스프링이 빈 팩토리를 위한 오브젝트 설정을 담당하는 클래스라고 인식하게 해줌
  - @Bean : 오브젝트 생성을 담당하는 IoC용 메소드라는 표시
  - 아래 코드는 자바 코드의 탈을 쓰고 있는 XML과 같은 <strong>스프링 전용 설정정보</strong>라고 보면 됨  
    ```java
    @Configuration
    public class DaoFactory{
    
        @Bean
        public UserDao userDao() {
            return new UserDao(connectionMaker());
        }
    
        @Bean
        public ConnectionMaker connectionMaker() {
            return new DConnectionMaker();
        }
    }
    ```
  - DaoFactory를 설정정보로 사용하는 애플리케이션 컨텍스트를 만드는 법
    ```java
    main...
    ApplicationContext context = new AnnotationConfigApplicationContext(DaoFatory.class);
    UserDao dao = context.getBean("userDao", UserDao.class);
     
    ```
  - getBean() 메소드는 ApplicationContext가 관리하는 오브젝트를 요청하는 메소드, getBean()의 파라미터인
  "userDao"는 ApplicationContext에 등록된 빈의 이름 "userDao"의 이름을 가져온다는 것은 DaoFactory의 userDao() 
    메소드를 호출해서 그 결과를 가져온다고 생각하면 된다.
  - getBean() 의 첫번째 파라미터는 메서드의 이름, 두번째는 리턴 타입
  - 기본적으로 애플리케이션 컨텍스트는 싱글톤을 저장하고 관리하는 싱글톤 레지스트리이다.
  
### 의존관계 주입 (DI Dependency Injection)
    ex) A가 B를 의존하고 있다.
        : B가 변하면 A에 영향을 미친다. 반대로 B는 A의 변화에 영향을 받지 않는다.

- 위 코드에서 UserDao는 ConnectionMaker 인터페이스에 의존하고 있다.
- 하지만 ConnectionMaker 인터페이스를 구현하는 클래스, 즉 DConnectionMaker 등이 다른 것으로 바뀌거나
그 내부 메서드가 변경 되어도 UserDao에 영향을 주지 않는다.
```java
public class UserDao {
  private ConnectionMaker connectionMaker;
  
  public UserDao(ConnectionMaker connectionMaker) {
    this.connectionMaker = connectionMaker;
  }
}

```
- 위 코드는 두 개의 오브젝트 간에 런타임 의존관계를 나타낸 것 : 
  - UserDao 오브젝트는 생성자를 통해 주입받은 ConnectionMaker의 구현 클래스를 언제든지 사용하면 된다.