# 파일 읽기 
# 예제 7 

print("") 
print("") 
print("-----------file example") 
with open('resource/score.txt','r') as file_tmp:

    score = [] 
    
    for line in file_tmp: 
        score.append(int(line)) ## 텍트스파일 안에 있는 내용은 문자열로 인식 
    
    print(score) #읽은 파일을 리스트로 넣음 

print("Average : {:6.3}".format(sum(score)/len(score)))