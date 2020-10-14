# data split - 파일 분산 저장 처리 방법 

with open('rowdata.csv','r', encoding="utf8") as f: 
    csvfile = f.readlines()
linesPerFile = 1000
filename = 1 
#del csvfile[0] # header 삭제 

for i in range(0, len(csvfile), linesPerFile):
    with open('logstash_data/'+str(filename) + '.csv', 'w', encoding='utf8') as f:
        if filename > 1: 
            f.write(csvfile[0])
        f.writelines(csvfile[i:i+linesPerFile]) # 가장 중요한 코드 
        # print(str(i) + "," +str(i+linesPerFile))
    filename +=1 
