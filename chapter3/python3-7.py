# -7에서 0까지 10진수와 2진수, 8진수, 16진수를 다음과 같이 정형화해 출력하는 프로그램을 작성하시오.
for i in range(7,-1,-1):
    mask=0xff
    print('10진수: {:3d} 2진수: {:8b} 8진수: {:5} 16진수: {:2}'.format(~i+1, ~i+1 & mask, oct(~i+1 & mask), hex(~i+1 & mask)))
