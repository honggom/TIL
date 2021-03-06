# Base64
- 글자 그대로 직역하면 64진법이라는 뜻.
- 컴퓨터 분야에서 쓰이는 Base 64(베이스 육십사)란 8비트 이진 데이터(예를 들어 실행 파일이나, ZIP 파일 등)를 
문자 코드에 영향을 받지 않는 공통 ASCII 영역의 문자들로만 이루어진 일련의 문자열로 바꾸는 인코딩 방식을 가리키는 개념이다.

## 인코딩 과정
1. 24bit의 buffer를 생성하여 위쪽(MSB)부터 바이트 데이터를 넣은 뒤,
2. 버퍼의 위쪽부터 6bit 단위로 잘라 Base64 테이블의 ASCII 문자로 변환한다. 
- 원본 문자열 > ASCII binary > 6bit로 cut > base64 encodeing 순서가 된다.

## 사용 이유
위의 과정대로 Base64로 인코딩을 하게 되면  6bit당 2bit의 Overhead가 발생하여
전송해야 될 데이터의 크기가 약 33% 정도 늘어난다.   
33%나 데이터의 크기가 증가하고, 인코딩과 디코딩의 추가 연산까지 필요한데
Base64 인코딩을 사용하는 이유는 무엇일까?

- 통신과정에서 바이너리 데이터의 손실을 막기 위해 사용된다.
  - 플랫폼 독립적으로 Binary Data(이미지나 오디오)를 전송할 필요가 있을 때, 
  ASCII로 Encoding 하여 전송하게 되면 여러 가지 문제가 발생할 수 있다.

### 대표적인 문제
- ASCII는 7 bits Encoding인데 나머지 1bit를 처리하는 방식이 시스템 별로 상이하다.
- 일부 제어 문자 (e.g. Line ending)의 경우 시스템 별로 다른 코드값을 가진다.

위와 같은 문제로 ASCII는 시스템 간 데이터를 전달하기에 안전하지 않다. 

Base64는 ASCII 중 제어 문자와 일부 특수문자를 제외한 64개의 안전한 출력 문자만 사용한다.
(* 안전한 출력 문자란 문자 코드에 영향을 받지 않는 공통 ASCII를 의미)

즉, Base64는 HTML 또는 Email과 같이 문자를 위한 Media에 Binary Data를 포함해야 
될 필요가 있을 때, 포함된 Binary Data가 시스템 독립적으로 동일하게 전송 또는 저장되는 걸 보장하기 위해 사용한다.


출처: https://devuna.tistory.com/41 [튜나 개발일기]