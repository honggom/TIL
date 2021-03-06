## Index
- DB 데이터를 빠르게 조회하기 위한 추가적인 저장 공간(자료구조)을 활용한 기술
- 책의 목차(색인)이라고 생각하면 편하다.

기본적으로 인덱스를 사용하면 조회(select) 성능이 향상된다. 추가로 update나 delete도   
성능이 향상된다. 그 이유는 해당 연산을 수행하려면 우선 조회가 필요하기 때문이다.   
만약 인덱스를 사용하지 않은 컬럼을 조회하면 풀스캔을 통해 검색을 해야되기 때문에 최대 행의 개수만큼
연산을 해야된다.

### Index 오버헤드
dbms는 인덱스를 항상 최신의 정렬 상태로 유지해야 원하는 값을 빠르게 탐색이 가능하다.
- Insert : 새로운 데이터에 대한 인덱스를 추가한다.
- Delete : 삭제된 데이터에 대한 인덱스에 마킹을 한다.
  (삭제된 데이터에 대한 인덱스를 삭제하는 것이 아닌, 더이상 사용되지 않는다는 마킹을 하게 된다.)
- Update : 기존의 인덱스를 사용하지 않는다는 마킹을 하고, 갱신된 데이터에 대한 인덱스를 추가한다.

### Index의 장단점
- 장점 :
    - 조회속도가 빨라진다.
    - 전반적인 시스템 부하를 줄일 수 있다.
- 단점 :
    - 인덱스를 관리하기 위해 추가적인 저장공간이 필요하다.
    - 인덱스를 관리하기 위한 추가작업(오버헤드)가 필요하다.
    - 잘못 사용할 경우 성능 악화가 될 수 있다.

### Index 내부 구조
- B+Tree 형태의 자료구조로 인덱스가 이루어져 있다.
- B+Tree의 탐색 시간복잡도는 O(log n)이다.

### Index가 B+Tree 구조인 이유
1. 해쉬테이블이 탐색 시간복잡도가 O(1)이니 인덱스 구조로 해쉬테이블을 사용하면 안 될까? 라고 생각할 수 있지만, 해쉬테이블은
단 하나의 데이터를 탐색하는 시간만 O(1)이다. 이게 왜 해쉬테이블을 인덱스로 사용하면 안 되는 이유나면,
디비에서는 부등호(<, >) 연산을 사용할 수 있다. 하지만 해쉬테이블은 특정 기준보다 크거나 작은 값을 통해 데이터를 찾을 수 없다.
따라서 부등호 연산에 대해서는 해쉬테이블이 무용지물이기때문에 인덱스 구조에 적합하지 않다.
2. B+Tree는 데이터들을 항상 정렬된 상태로 가지고 있다. 따라서 탐색에 대한 시간복잡도가 `O(log N)`으로 준수하다.
3. 탐색뿐만 아니라, 저장, 수정, 삭제도 같은 맥락으로 시간복잡도가 `O(log N)`으로 준수하다.

### 카디널리티 (Cardinality)
- 한 컬럼에 대하여 그 컬럼이 가지는 데이터의 중복 정도가 높을 수록 카디널리티가 낮다.
- 한 컬럼에 대하여 그 컬럼이 가지는 데이터의 중복 정도가 낮을 수록 카디널리티가 높다.
    - ex) 두 컬럼이 있고 각각 컬럼은 성별과, 주민번호 데이터를 저장한다고 가정하면
      성별은 생물학적으로 두 가지밖에 없기 때문에 중복 정도가 높을 수밖에 없다. 그렇기 때문에
      카디널리티가 낮다. 반대로 주민번호는 성별과 비교하여 카디널리티가 높다.
- 인덱스를 2개 이상 설정할 경우에는 카디널리티가 높은 것 부터 설정하는 것이 좋다.
    - 카디널리티가 높아야 인덱스가 많이 생성이 되고, 인덱스는 B트리로 이루어져 있기 때문에 조회속도가 빠르다.
      그렇기 때문에 카디널리티가 높은 것이 인덱스로 설정이 되어야 조회 속도가 빠르다.
        - 대부분의 상황에서는 카디널리티가 높은 것(또는 Where 조건 절에 많이 사용되는 값)하나를 인덱스로 사용하면 좋다.
