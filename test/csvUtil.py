import csv


reader = csv.reader(open("F:\\aqidata\Beijing_2008_HourlyPM2.5_created20140325.csv"))

items = [];

date = ""
aqi = 0
high = 0
low = 0
valid = 0
aqisum = []
aqiavg = 0
count = 0
print reader
for title  in reader:
    if reader.line_num < 4 :  
        continue  
    if reader.line_num > 4 and reader.line_num < 190:

        if title[10] == "Valid": #count when aqi value exists
            aqi =  int(title[7])

            # if it's a new date, init data;
            if date != title[2][:8]:
                # if len(aqisum) != 0:
                #     items.append({"sum":sum(aqisum)/len(aqisum)});
                # print items
                print date,aqisum # if its a new date,save aqisum
                date = title[2][:8] #要改成split因为不是定长
           
                aqisum = [aqi]
                high = aqi
                low = aqi
            else:#same date
                aqisum.append(aqi);
                if high < aqi:
                    high = aqi
                if low > aqi:
                    low = aqi 
        
        #print  date, aqi, high, low
        #print title
