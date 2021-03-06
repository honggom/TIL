# REST - 네트워크 아키텍쳐
    1. client, server : 클라이언트와 서버가 독립적으로 분리 되어 있어야 한다.
    2. Stateless : 요청에 대해서 클라이언트의 상태를 서버에 저장하지 않는다.
    3. Cache : 클라이언트는 서버의 응답을 Cache(임시저장)할 수 있어야 한다. 이를 통해 서버의 부하는 낮춘다.
    4. 계층화 : 서버와 클라이언트 사이에 방화벽, 게이트웨이, 프록시 등 다양한 계층 형태로 구성이 가능해야 하며, 이를 확장 가능해야 한다.
    5. 인터페이스 일관성 : 인터페이스의 일관성을 지키고, 아키텍처를 단순화시켜 작은 단위로 분리하여, 클라이언트, 서버가 독립적으로 개선 될 수 있어야 한다.
    6. Code on Demand (Optional) : 자바 애플릿, 자바스크립트, 플래시 등 특정한 기능을 서버로부터 클라이언트가 전달받아 코드를 실행 할 수 있어야 한다.
기본적으로 행위는 메서드로, 자원은 URI로 표현한다.

### 1. 자원의 식별
    웹 기반의 REST에서는 리소스 접근을 할 때 URI를 사용한다.
    https://foo.co.kr/user/100
    리소스 : user
    식별자 : 100

### 2. 메시지를 통한 리소스 조작
    web에서는 다양한 방식으로 데이터를 전달 할 수 있다.
    ex) HTML, XML, JSON, TEXT
    이 중에서 어떠한 타입의 데이터인지 알려주기 위해 HTTP Header 부분 content-type을 통해 데이터 타입을 지정한다.

### 3. 자기 서술적 메시지
    요청하는 데이터가 어떻게 처리 되어져야 하는지 충분한 데이터를 포함 할 수 있어야 한다.
    GET   : https://foo.co.kr/user/100 , 사용자의 정보 요청
    POST  : https://foo.co.kr/user     , 사용자 정보 생성
    PUT   : https://foo.co.kr/user     , 사용자 정보 생성 및 수정
    DELETE: https://foo.co.kr/user/100 , 사용자 정보 삭제
    그 외에 담지 못한 정보들은 URI의 메시지를 통하여 표현 한다.

### 4. Application 상태에 대한 엔진으로써 하이퍼미디어
    REST API를 개발할 때 단순히 Client 요청에 대한 데이터만 응답 해주는 것이 아닌 관련된 리소스에 대한
    Link 정보까지 포함 되어져야 한다.
    이러한 조건들을 잘 갖춘 경우 REST Ful 하다고 표현하고, 이를 REST API라고 부른다.