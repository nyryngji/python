#네 자리 정수를 입력받은 후 역순으로 출력하시오

n = int(input('네 자리 정수 입력: '))

a = n//1000
b = n % 1000//100
c = n % 1000 % 100//10
d = n % 1000 % 100 % 10

print('{}{}{}{}'.format(d, c, b, a))
