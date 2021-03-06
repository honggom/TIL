# 교차 출처 리소스 공유 CORS (Cross-Origin Resource Sharing)
다른 도메인으로부터 리소스가 요청될 경우 해당 리소스는 cross-origin HTTP 요청 에 의해 요청된다. 
하지만 대부분의 브라우저들은 보안 상의 이유로 스크립트에서의 cross-origin HTTP 요청을 제한한다. 
이것을 `Same-Origin-Policy(동일 근원 정책)`이라고 한다. 요청을 보내기 위해서는 요청을 보내고자 
하는 대상과 프로토콜도 같아야 하고, 포트도 같아야 함을 의미한다.(이 때, 서브 도메인 네임은 상관없다.)

이러한 문제를 해결하기 위해 과거에는 flash 를 proxy 로 두고 타 도메인간 통신을 했다. 하지만 모바일 운영체제의 등장으로 flash 로는 힘들어졌다. (iOS 는 전혀 플래시를 지원하지 않는다.) 대체제로 나온 기술이 JSONP(JSON-padding)이다. jQuery v.1.2 이상부터 jsonp형태가 지원되 ajax 를 호출할 때 타 도메인간 호출이 가능해졌다. JSONP에는 타 도메인간 자원을 공유할 수 있는 몇 가지 태그가 존재한다. 예를들어 img, iframe, anchor, script, link 등이 존재한다.

여기서 CORS는 타 도메인 간에 자원을 공유할 수 있게 해주는 것이다. Cross-Origin Resource Sharing 표준은 웹 브라우저가 사용하는 정보를 읽을 수 있도록 허가된 출처 집합을 서버에게 알려주도록 허용하는 특정 HTTP 헤더를 추가함으로써 동작한다.