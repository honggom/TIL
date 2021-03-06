##### 프록시
> 지연 로딩을 사용하려면 실제 엔티티 객체 대신에 데이터베이스 조회를 지연할 수 있는 가짜 객체가 필요한데 이것을 프록시 객체라 한다.

##### 프록시의 특징
> 프록시 클래스는 실제 클래스를 상속 받아서 만들어지므로 실제 클래스와 겉 모양이 같다. 따라서 사용하는 입장에서는 이것이 진짜 객체인지
> 프록시 객체인지 구분하지 않고 사용하면 된다.
> > 프록시 객체의 초기화 : 프록시 객체는 member.getName() 처럼 실제 사용될 때 데이터베이스를 조회해서 실제 엔티티 객체를 생성하는데 이것을
> 프록시 객체의 초기화라 한다.

##### 즉시 로딩
> 엔티티를 조회할 때 연관된 엔티티도 함께 조회한다.

> 연관된 데이터를 즉시 조회한다. 하이버네이트는 가능하면 SQL 조인을 사용해서 한 번에 조회한다.

##### 지연 로딩
> 연관된 엔티티를 실제 사용할 때 조회한다.

> 연관된 엔티티를 프록시로 조회한다. 프록시를 실제 사용할 때 초기화하면서 데이터베이스를 조회한다.

##### JPA 기본 페치 전략
> 추천하는 방법은 모든 연관관계에 지연 로딩을 사용하는 것이다. 그리고 애플리케이션 개발이 어느 정도 완료단계에 왔을 때 실제 사용하는 상황을
> 보고 꼭 필요한 곳에만 즉시 로딩을 사용하도록 최적화하면 된다.