# 예제 3 

print("---file write sample_03---")
print("---file write example with random package -- Lotto number gen.")

from random import randint 

with open('resource/text2.txt','w') as f: 
    for cnt in range(6): 

        RanInt = str(randint(0,50))
        print(RanInt)

        f.write(RanInt) 
        f.write('\n')