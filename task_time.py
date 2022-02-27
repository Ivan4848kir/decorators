from datetime import datetime
lst=[
            {
                "dt": "2022-02-23 04:35:27.353366",
                "event": "start"
            },
            {
                "dt": "2022-02-23 04:35:34.654153",
                "event": "stop"
            },
            {
                "dt": "2022-02-23 04:38:34.382548",
                "event": "start"
            },
            {
                "dt": "2022-02-23 04:38:39.637583",
                "event": "stop"
            }
]

list_intervals=[]
incorrect_list=[]

def dates(lst):
    n = len(lst)
    for i in range(n):
        yield lst[i],lst[(i+1)%n]

def valid():
    for i in list(dates(lst))[::2]:
        if i[0]['event']=='start' and i[1]['event']=='stop':
            list_intervals.append(i)
        else:
            incorrect_list.append(i)

def intervals():
    valid()
    list_intervals = list(dates(lst))[::2]
    res=[]
    for i in list_intervals:
        str_date_start=i[0]['dt']
        str_date_stop=i[1]['dt']
        date_format='%Y-%m-%d %H:%M:%S.%f'
        interval=datetime.strptime(str_date_stop, date_format)-datetime.strptime(str_date_start, date_format)
        res.append(interval)
    return res

print(intervals())













