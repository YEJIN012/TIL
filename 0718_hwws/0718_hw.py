num1 = 0.1 * 3
num2 = 0.3

import math
print(math.isclose(num1,num2))



name = '철수'
print(f'안녕, {name}야')



print(str(1) == '1')
print(int('30') == 30)
print(int(5) == 5)
print(bool('50'))



n = 5
m = 9
s = '* '
b = ' '
print(s * int(n))
print((s + b * int(n+1) + s + '\n' )* int(m), end='')
print(s * int(n))


print('''"파일은 c:|Windows|Users|내문서|python에 저장이 되었습니다."
나는 생각했다. 'cd를 써서 git bash로 들어가 봐야지.' ''')


a=input()
b=input()
c=input()
r1= (-b + (b**2-4*a*c)**0.5)/(2*a)
r2 = (-b - (b**2-4*a*c)**0.5)/(2*a)