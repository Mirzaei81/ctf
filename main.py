indecies = [0,
29,
4 ,
2 ,
23,
3 ,
17,
1 ,
7 ,
10,
5 ,
9 ,
11,
15,
8 ,
12,
20,
14,
6 ,
24,
18,
13,
19,
21,
16,
27,
30,
25,
22,
28,
26,
31,
]
map = {
0:  'd',
29: '9',
4 : 'r',
2 : '5',
23: 'r',
3 : 'c',
17: '4',
1 : '3',
7 : 'b',
10: '_',
5 : '4',
9 : '3',
11: 't',
15: 'c',
8 : 'l',
12: 'H',
20: 'c',
14: '_',
6 : 'm',
24: '5',
18: 'r',
13: '3',
19: '4',
21: 'T',
16: 'H',
27: '5',
30: '2',
25: '_',
22: '3',
28: '0',
26: '7',
31: 'e',
}
sortedMap = sorted(map.items(),key= lambda x:x[0])
password = ""
for i in sortedMap:
    password += i[1]
print(password)
    


