# 파일 읽기 
# 예제 4 
print("-----------file open") 
with open('resource/review.txt','r') as file_tmp: 
    content = file_tmp.read() 
    print(">",content)

    content = file_tmp.read() ### 이 이후에는 파일의 커서가 맨 뒤로 가있기 때문에 
    print(">",content)        ### 읽지 못함(내용이 없음)