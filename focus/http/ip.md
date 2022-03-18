##### IP 패킷 정보
- 전송 데이터를 `출발지 IP`, `목적지 IP`, 기타 ...를 포함한 IP 패킷으로 만들어서 클라이언트로 전달한다.
  - 그 과정 중에서는 수많은 노드를 거친다.

##### IP 프로토콜의 한계
- 비연결성
  - 패킷을 받을 대상이 없거나 서비스 불능 상태여도 패킷 전송
- 비신뢰성
  - 중간에 패킷이 사라지면?
  - 패킷이 순서대로 안 오면?
    - ex) 패킷의 용량이 크면 패킷을 여러개로 나눠서 전송함.. 그 과정에서 패킷이 순서대로 도착 안 할 가능성이 있다.
- 프로그램 구분
  - 같은 IP를 사용하는 서버에서 통신하는 애플리케이션이 둘 이상이면?