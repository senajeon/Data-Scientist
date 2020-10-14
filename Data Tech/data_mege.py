import json.tool
import csv
import datetime
from json import JSONEncoder


class DateTimeEncoder(JSONEncoder):
        # Override the default method
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()

def make_json(file_num):
    with open("split_json/seoul-metro-2019-{}.json".format(file_num), 'w', encoding='utf-8') as outfile:
        # json.dump(logdata, outfile, cls=DateTimeEncoder, ensure_ascii=False)
        outfile.write(
            '[' +
            ',\n'.join(json.dumps(i, cls=DateTimeEncoder, ensure_ascii=False) for i in logdata) +
            ']\n')

    print("split_json/seoul-metro-2019-{}.json".format(file_num))


with open('subway_gpo.json', 'r', encoding='utf-8') as json_file:
    s_meta = json.load(json_file)

f = open('rowdata.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)

line_num_lang = {
    "1호선": "Line 1", "2호선": "Line 2", "3호선": "Line 3", "4호선": "Line 4",
    "5호선": "Line 5", "6호선": "Line 6", "7호선": "Line 7", "8호선": "Line 8"
}

seoul_metro_log = []

for line in rdr:
    seoul_metro_log.append(line)

f.close()

loglen = len(seoul_metro_log)

logdata = []

filename = 1

del seoul_metro_log[0]

for i in range(0, loglen-1, 2):
    dataIn = seoul_metro_log[i]
    dataOut = seoul_metro_log[i+1]

    ldateTemp = dataIn[0].split('-')
    updatemonth = ldateTemp[1]

    if filename != int(updatemonth):
        make_json(filename)
        logdata = []
        filename = filename+1

    #A 문제가 예상된다. 지우면 지운사람 책임.
    if(dataIn[0] == dataOut[0] and dataIn[1] == dataOut[1]
       and dataIn[2] == dataOut[2] and dataIn[3] == dataOut[3]):

        station_name = dataIn[3]

        for h in range(20):
            ldate = datetime.datetime(
                int(ldateTemp[0]), int(ldateTemp[1]), int(ldateTemp[2]), h+4)

            people_in = dataIn[5+h]
            people_in = int(people_in)

            people_out = dataOut[5+h]
            people_out = int(people_out)

            stn_nm_full = station_name
            if(station_name.find("(") > 0):
                station_name = station_name.split("(")[0]

            s_logs = {}
            t_st_nm = station_name

            if(station_name == "총신대입구"):
                t_st_nm = "이수"
                stn_nm_full = "총신대입구(이수)"

            s_logs = {
                "@timestamp": ldate,
                "code": dataIn[2],
                "line_num": dataIn[1],
                "line_num_en": line_num_lang[dataIn[1]],
                "station": {
                    "name": stn_nm_full,
                    "kr": t_st_nm,
                },
                "location": {
                    "lat": s_meta[t_st_nm][0],
                    "lon": s_meta[t_st_nm][1]
                },
                "people": {
                    "in": people_in,
                    "out": people_out,
                    "total": people_in+people_out
                }
            }

            logdata.append(s_logs)

if len(logdata) > 0:
    make_json("last")


print("저장완료")
