string = input()
word = string.split(" ")
word = [w for w in word if w != ""] #공백이 아닌 경우에만 word에 넣음
print(len(word))

####

string = input()
if string == " ":
    print(0)
else:
    words = string.split(" ")
    
    while '' in words: #문장 양쪽에 있는 공백이 없어질 때까지 반복
        words.remove('')
    print(len(words))

# https://roseline124.github.io/algorithm/2019/03/29/Altorithm-baekjoon-1152.html