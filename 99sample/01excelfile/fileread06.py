# 파일 읽기 
# 예제 6 

print("-----------file open") 

with open('resource/review.txt','r') as file_tmp: 
    content = file_tmp.readlines()      ## readlines는 줄바꿈의 형태까지 리스트로. 
    print(content)                      ## 줄바꿈의 형태까지 리스트로 가질 수 있음 
    
    for c in content: 
        print(c , end=' **** ')         ## \n을 **** 으로 출력