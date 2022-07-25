# npm
> NPM(Node Package Manager)은 자바스크립트 언어를 위한 패키지 관리자로, 
Node.js의 기본 패키지 관리자이다. 전세계적으로 가장 많이 사용하고 
있는 패키지 관리 툴이다. 이러한 관리 툴을 이용하여 Node.js로 만들어진 모듈을 
웹에서 받아서 쉽게 설치하고 관리해주는 프로그램으로 개발자 입장에서는 단 몇 줄의 
command로 기존 공개된 모듈들을 설치하고 활용할 수 있다. 
또한 그렇게 설치된 모듈들이 업데이트되었는지를 체크해주는 등 JavaScript로 진행하는 
프로젝트를 편하게 진행할 수 있도록 도움을 준다. command-line client인 npm과 
온라인 데이터베이스인 npm registry로 이루어져 있으며, 일반적으로 command-line client를 
npm이라고 생각하는데, 실제로 npm에는 npm registry까지 포함되어 있다.

# yarn
> yarn은 페이스북에서 만든 자바스크립트 패키지 매니저이다.
npm과 같은 기능을 수행한다. 그렇지만 사실 npm과 yarn에 대해 공부해보지 
않아도 어느정도 프로젝트 경험이 있으면 yarn이 조금 더 가볍다는 느낌을 
받아 봤을거라 생각한다. 그 이유는 yarn의 탄생 배경에 있다. yarn은 기본적으로 
npm의 단점을 느꼈기에 이를 향상시키기 위해 만들어진 매니저 툴인데, 여기서 말하는 
npm의 단점으로는 속도(performance), 안정성(stability), 보안성(security) 등이 있다.

## 속도
yarn은 다운받은 패키지 데이터를 캐시(cache)에 저장하여, 중복된 데이터는 다운로드하지않고, 
캐시에 저장된 파일을 활용함으로써 이론적으로 npm에 비해 패키지 설치속도가 매우 빠르다. 또한 여러개의 
패키지를 설치할 때 병렬로 처리하기 때문에 performance와 speed가 증가 된다. (npm은 순차적)

## 안정성/보안성
npm은 패키지가 설치될 때 자동으로 코드와 의존성을 실행할 수 있도록 허용했다. 
이 특징은 편리한 기능이지만 안정성을 위협할 수 있다. 특히나 보장된 정책 없이 
등록한 패키지가 존재할 수 있다는 점에서 더욱 위험도가 높다.
반면 yarn은 yarn.lock이나 package.json으로 부터 설치만 하며, yarn.lock은 
모든 디바이스에 같은 패키지를 설치하는 것을 보장하기 때문에 버전의 차이로 인해 생기는 버그를 방지해줄 수 있다.

## npm? yarn? 무엇을 사용할까?
> 결론은, 무엇이든 편한 것 `하나`를 사용하면 된다.

2016,2017년 이때 기준으로는 yarn이 가시적으로 npm보다 속도나 안정성이 뛰어났다. 
그렇지만 npm 또한 몇년간 발전을 거듭하며 단점을 많이 보완했기 때문에 현재 npm/yarn의 
performance와 stability 차이는 그리 크지 않다고 봐도 무방하다.

## 단, 하나만 사용하자.
> npm, yarn을 둘 다 사용하면 package-lock.json / yarn.lock 2개의 기준이 생겨버린다.

예를 들어, 개발자A는 yarn으로 init한 뒤 개발을 진행하고, 이후 새로 입사한
개발자B는 npm으로 install하게되면

개발자B는 최초에 세팅된 패키지들의 버전 정보가 담긴 yarn.lock 파일을 사용하지 않으면서
package.json에 명시된 ^ 규칙에 따라 버전업이 된 패키지들로
package-lock.json 파일을 다시 생성하게 된다.

결과적으로 npm, yarn을 동시에 사용하게 되면 의존성의 버전이 서로 불일치 하는 경우가 생길 수 있으므로
하나만 선택하여 사용하도록 하자.