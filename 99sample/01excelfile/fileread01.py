# 파일 읽기 
# 예제 1
print("----file open resource/review.txt------")

file = open('resource/review.txt','r') #파일을 열 때에는, open이라는 함수. 
content = file.read() 
print(content) 
file.close()
