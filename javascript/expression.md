### 값
- 값은 식이 평가되어 생성된 결과를 말한다.
- 평가란 식을 해석해서 값을 생성하거나 참조하는 것을 의미한다.
```javascript
// 10 + 20은 평가되어 숫자 값 30을 생성한다.
10 + 20; // 30
```

```javascript
// 변수에는 10 + 20이 평가되어 생성된 숫자 값 30이 할당ㄷ뇐다.
var sum = 10 + 20;
```

### 리터럴
- 리터럴은 사람이 이해할 수 있는 문자 또는 약속된 기호를 사용해 값을 생성하는 표기법을 말한다.

```javascript
// 숫자 리터럴 3
3
```
- 위 예제의 3은 단순한 아라비아 숫자가 아니라 숫자 리터럴이다.
- 사람이 이해할 수 있는 아라비아 숫자를 사용해 숫자 리터럴 3을 코드에 기술하면 자바스크립트
엔진은 이를 평가해 숫자 값 3을 생성한다.

### 표현식
- 표현식은 값으로 평가될 수 있는 문이다. 즉, 
표현식이 평가되면 새로운 값을 생성하거나 기존 값을 참조한다.
- 앞서 살펴본 리터럴은 값으로 평가된다. 따라서 리터럴도 표현식이다.
```javascript
var score = 100;
```
- 위 예제의 100은 리터럴이다. 리터럴 100은 자바스크립트 엔진에 의해 평가되어 값을 생성하므로
리터럴은 그 자체로 표현식이다.
