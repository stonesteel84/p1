# 역량평가 파이썬 중급 1번 문제
'''
아래 기준에 따라 비밀번호가 안전한지 판단하세요. 
'''
# 1. 비밀번호의 길이가 8이상이다.
# 2. 영어 대문자와 소문자, 숫자를 각각 최소 하나 이상 포함해야 한다.

# password validate 메소드
# 입력값 : password
# 리턴값 : True(print 'SAFE') or False(print 'NOT SAFE')

import re
def pwd_lencheck(password) :
    password = str(password)
    if len(password) >= 8:
        return True
    return False

def pwd_lowercheck(password) :
    for pwd in password :
        if pwd.isalpha() and pwd.islower() == False:
            return False
    return True
def pwd_uppercheck(password):
    for pwd in password :
        if pwd.isalpha() and pwd.isupper() == False:
            return False
    return True
def pwd_numcheck(password):
    for pwd in password :
        if pwd.isalnum() == False:
            return False
    return True        
def pwd_validate(password):
    print(pwd_lencheck(password))
    print(pwd_lowercheck(password))
    print(pwd_uppercheck(password))
    print(pwd_numcheck(password))
    if (pwd_lencheck(password) and pwd_lowercheck(password) and pwd_uppercheck(password) and pwd_numcheck(password)) == True :
        print('SAFE')
    else :
        print('NOT SAFE')

s1 = ["a1b43cAb","bkm1AB","pwlm1aqzx","mwkiMOPQz1"]
a = '비밀번호를 입력해주세요 :'
for i in s1:
    if __name__ == '__main__':
        print(a)    
        pwd_validate(input(i))
        