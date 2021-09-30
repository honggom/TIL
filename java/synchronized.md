# Synchronized

자바에서 프로그래밍을 한다면 Multi-Thread로 인하여 동기화를 제어해야하는 경우가 생긴다. 
그 때 자바에서 제공하는 키워드인 synchronized 키워드를 사용하게 되는데, Multi-Thread 상태에서 
동일한 자원을 동시에 접근하게 되었을 때 동시 접근을 막게 된다. 

즉 공유 데이터에 lock을 걸어서 먼저 작업 중이던 쓰레드가 작업을 완전히 끝낼 때까지는 다른 
쓰레드에게 제어권이 넘어가더라도 데이터가 변경되지 않도록 보호함으로써 쓰레드의 동기화를 가능하게 한다.

## Synchronized 사용 방법

### 메서드에 synchronized 하기
- 인스턴스 메서드의 동기화는 이 메서드를 가진 인스턴스를 기준으로 이루어진다. 
그러므로 한 클래스에 synchronized를 사용한 메서드를 가진다면, 여기서 동기화는 
인스턴스를 기준으로 이루어진다. 그리고 오직 하나의 Thread 만이 동기화된 인스턴스 
메서드를 실행할 수 있다. 결론은 synchronized를 사용한 메서드가 존재한다면 인스턴스당 
한 개의 Thread만이 접근할 수 있다. 쉽게 생각하면 메서드에 synchronized를 사용하면 
그 함수가 포함된 객체(this)가 lock이 걸린 것이다.

### 블록에 synchronized 하기
- 동기화는 락을 필요로 하며 락은 모든 객체마다 존재한다. 메서드 제어자 뒤에 synchronized 
키워드가 위치한 동기화 메서드는 락 객체를 지정하는 부분이 없다. 동기화 메서드는 내부적으로 자신의 
객체를 락으로 사용한다. 즉, 객체 스스로 메서드 전체를 감시하는 역할을 한다. 이에 반해서 동기화 
블록은 메서드 안의 특정 부분을 동기화할 수 있다. 이런 경우에 락 객체는 자기 자신 객체를 의미하는 
this 키워드를 사용할 수도 있지만 다른 객체를 락으로 사용할 수 있다. 단, 락 객체가 여러 개라면 
우리가 원하는 동기화 작업을 제대로 실행할 수 없다. 그래서 보통은 락 객체를 하나만 사용하는 경우가 많다. 
동기화 블록을 사용하는 경우, 해당 메서드는 여러 스레드가 동시에 점유할 수 있다. 하지만 동기화된 블록에 
이르면 락 객체에 의해서 모든 스레드들은 실행을 중단하고 자신의 차례가 될 때까지 대기한다.