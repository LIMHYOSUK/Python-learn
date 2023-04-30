# 파일 읽기 
# # 예제 3 
print("---------file open use <with> line") 
with open('resource/review.txt','r') as file_tmp: 
    for c in file_tmp: 
        print(c) ##라인단위로 출력 
        
    for s in file_tmp: 
        print(s.strip())