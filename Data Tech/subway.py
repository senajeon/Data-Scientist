from openpyxl import load_workbook
import json
import datetime


with open("subway_location.json", "r", encoding="utf-8") as json_open :
    subway_location=json.load(json_open)

# print(subway_location['가락시장'][0])
# print(subway_location['가락시장'][1])



load_wb = load_workbook("subway_log_2019_1.xlsx", data_only=True)
load_ws = load_wb['Sheet1']

# print(load_wb)
# print(load_ws)
# print(load_ws['A3'])
# print(load_ws['A3'].value)

get_rows = load_ws.rows

metro_2019_log = []

for row in get_rows :
    rowinit = []
    for cell in row :
       rowinit.append(cell.value)
    metro_2019_log.append(rowinit)

# print(metro_2019_log)

# print(get_cells[0][0].value)
# for row in get_cells :
#     for cell in row :
#         print(cell.value)

# metro_2019_log[0][3]


# i = 0
# indata = 0
# outdata = 1

# i = 2
# indata = 2  => 2
# outdata = 3 => 3

# i = 4

log_count=len(metro_2019_log)

# 1호선 => Line 1

line_num_lang = {
    "1호선" : "Line 1",
    "2호선" : "Line 2",
    "3호선" : "Line 3",
    "4호선" : "Line 4",
    "5호선" : "Line 5",
    "6호선" : "Line 6",
    "7호선" : "Line 7",
    "8호선" : "Line 8",
}

log_data = []

for i in range(0,log_count,2) :
    indata=metro_2019_log[i]
    outdate=metro_2019_log[i+1]

    if(indata[0]==outdate[0] and indata[1]==outdate[1] and indata[2]==outdate[2]) :
        
        station_name = indata[3]
        dateTemp = indata[0]

        station_name_full = station_name

        # if '(' in station_name :
        if station_name.find("(") > 0 :
            station_name=station_name.split("(")[0]

        if(station_name == "총신대입구") :
          station_name = "이수"; 
          station_name_full = "총신대입구(이수)"

        for h in range(20) :
            rdate=datetime.datetime(dateTemp.year,dateTemp.month,dateTemp.day,h+4)
            people_in = indata[h+5]
            people_out = outdate[h+5]

            # print(rdate)
            # print(people_in)
            # print(people_out)

            # print(station_name)

            log_raw = {}

            log_raw = {
                "@timestamp":rdate,
                "code":indata[2],
                "line_num":indata[1],
                "line_num_en" :line_num_lang[indata[1]],
                "station" : {
                    "name" : station_name_full,
                    "kr" : station_name
                },
                "location" : {
                    "lat" : subway_location[station_name][0],
                    "lon" : subway_location[station_name][1]
                },
                "people" : {
                    "in": people_in,
                    "out": people_out,
                    "totla": people_in+people_out
                }
            }

            log_data.append(log_raw)

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.isoformat()

with open("subway_log_2019_1.json", "w", encoding="utf-8") as fp:
    json.dump(log_data, fp, ensure_ascii=False, indent="\t", cls=MyEncoder)

# log_data Json 파일로 out




print(indata)
print(outdate)


json_data = { 
    "location_name" : metro_2019_log[0][3],
    "location_x" : subway_location[metro_2019_log[0][3]][0],
    "location_y" : subway_location[metro_2019_log[0][3]][1]
}

print(json_data)