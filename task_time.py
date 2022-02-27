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

def dates(lst):
    n = len(lst)
    for i in range(n):
        yield lst[i],lst[(i+1)%n]

def valid():
    for i in list(dates(lst))[::2]:
        if i[0]['event']=='start' and i[1]['event']=='stop':
            print('Correct element')
            print(i)
        else:
            print('Incorrect element')
            print(i)








