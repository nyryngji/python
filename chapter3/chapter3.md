## 3. 문자열과 논리 연산

> **문자열**

- 문자열(= text sequence) : 문자의 나열
- len(문자열) : 문자열의 길이 출력
- 문자열 슬라이싱 : 문자열에서 일부 참조
1. str[start : end] : start 첨자에서 end-1첨자까지의 문자열 반환
2. str[-start : -end] : 양수와 같이 start 첨자에서 end-1첨자까지의 문자열 반환
3. str[ : ] : 전체 문자열 반환
4. str[start : end : step] : 문자 사이 간격을 조정 (만약 step이 음수일 경우 문자열을 역순으로 출력)

- ord() : 유니코드 번호 추출
- chr() : 유니코드 번호로 호출 시 문자 반환
<br>

> **문자열 관련 메소드**

- replace(a,b) : 문자열에 있는 a를 b로 바꿈
>
      str = 'hello friend'
      print(str.replace('friend','family'))   -> hello family
 
- count('부분 문자열') : 문자열 내에서 부분 문자열의 출현 횟수 반환
>
      str = 'hello hi hi hi'
      print(str.count('hi'))    -> 3
 
- join(문자열 이름) : 문자와 문자 사이에 원하는 문자열 삽입
>
      str = '12345'
      print('*'.join(str))    -> 1*2*3*4*5
 
- find(sub), index(sub) : 부분 문자열 sub가 맨 처음에 위치한 첨자를 반환 (sub가 없을 경우 find는 -1 반환, index는 ValueError를 반환) 
>
      str = 'hello friend'
      print(str.find('friend'))   ->6

- split() : 문자열을 공백, tab, enter 등을 기준으로 여러 문자열로 나눔
>
      m, n = '100 200'.split()
      print(m, n)    -> 100 200
 
- center() : 폭을 지정하고 중앙에 문자열 배치
>
      print('hello'.center(11,'*'))   -> ***hello***
 
- ljust(),rjust() : 폭을 지정하고 왼쪽, 오른쪽으로 정렬
>
      print('hello'.ljust(11,'*'))    -> hello******
      print('hello'.rjust(11,'*'))    -> ******hello
 
- strip() : 문자열 앞뒤의 특정 문자들을 제거 

> 
      print('***hello---'.strip('* -'))   -> hello
      
- zfill() : 문자열의 지정 폭 앞에 0 채워넣기

>
      print('234'.zfill(5))   -> 00234
      
- format() : 출력을 정형화
<br>

> **논리 자료와 다양한 연산**

- bool : 파이썬은 논리 값으로 True, False를 제공하는데 이러한 논리 값의 자료형
- bool(인자) : 변수나 상수의 논리 값을 알 수 있음
- 논리곱 **and, &** : 두 항이 모두 참이어야 True
- 논리합 **or, |** : 두 항이 모두 거짓이어야 False
- 배타적 논리합 **not, ^** : 두 항이 다르면 True, 같으면 False
- **논리 연산 우선순위 : not -> and -> or**

- in : 멤버의 소속을 알 수 있는 멤버십 연산 
1. x in str : 문자열 str에 부분 문자열 x가 있으면 True, 없으면 False 반환
2. x not in str : 문자열 str에 부분 문자열 x가 있으면 False, 없으면 True 반환

> **비트 연산**

- 비트 논리합 | : 비트가 하나라도 1이면 1
- 비트 논리곱 & : 비트가 모두 1이면 1<br>
- 비트 배타적 논리합 ^ : 두 비트가 다르면 1, 같으면 0
- 비트 이동 연산 >> : 수행 1회마다 2로 나눈 효과
- 비트 이동 연산 << : 수행 1회마다 2를  효과
