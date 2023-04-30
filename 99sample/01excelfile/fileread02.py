# 파일 읽기 
# 예제 2 
print("-----file open use <with>------------------------------------") 
with open('resource/review.txt','r') as file_tmp: 
    c = file_tmp.read() 
    print(c) 
    print(list(c)) ##c를 list화