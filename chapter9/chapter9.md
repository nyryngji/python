## 9. 모듈과 패키지

> **모듈**
- **모듈** : 함수나 변수, 클래스 정의 등의 파이썬 코드가 저장된 소스 파일
- **써드 파티 모듈** : 여러 회사나 전문가가 개발해 배포하는 모듈
- **표준 모듈** : 파이썬에 기본적으로 설치된 모듈
- 모듈은 **import** 구문으로 불러오기 가능
- import 모듈명 as 별칭 : 모듈을 별칭인 다른 이름으로 지정 가능

>
      import math as m
      print(m.pi) -> 3.141592653589793
 
- from 모듈명 import 함수명 : 모듈에서 지정된 이름을 모듈 이름 없이 사용 가능
>
      from math import gcd
      print(gcd(12,16))   -> 4

<br>

> **모듈 math**
- floor() : 버림
- ceil() : 올림
- lcm(a,b) : a와 b의 최소공배수 반환
- gcd(a,b) : a와 b의 최대공약수 반환
<br>

> **모듈 random**
- random() : 0 ~ 1 사이 난수를 반환
- shuffle(list) : list의 순서를 임의로 섞음
- randint(a,b) : a부터 b까지 랜덤으로 정수를 결과로 내보냄
- sample(리스트, 개수) : 리스트 내에서 매개변수를 몇 개 뽑을지 결정
<br> 

> **모듈 turtle**
- shape('turtle') : 거북이를 화면에 소환 (괄호 안에 circle,triangle 등 변환 가능)
- pencolor('color') : 펜 색깔 지정
- speed() : 속도 지정
- width() : 선 굵기 지정
- forward() : 전진    <-> backward() 