# 파일 읽기 
# 예제 5 
print("-----------file open")

with open('resource/review.txt','r') as file_tmp: 
    line = file_tmp.readline() 
    #print(line) #한줄만 읽어서 가져오기 때문에 반복문이 필요 

    while line: 
        print(line, end = ' ') 
        line = file_tmp.readline()
    
