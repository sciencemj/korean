def hasJongseong(code):
    if (code-44032)%28 == 0:
        return False
    else:
        return True


input = input("판단할 단어:") #'을/를'을 판단할 단어를 입력 받는다
last_word = input[len(input) - 1] #단어의 마지막 글자를 구한다
utf = ord(last_word) #마지막 글자를 유니코드 코드로 변환한다
hasJong = hasJongseong(utf) # (번호-44032)/4의 나머지로 0일시 종성 없음

if not hasJongseong: #종성이 없으면 '를'
    print(input + '를')
else:                 #종성이 있으면 '을'
    print(input + '을')

#demo