hacker_rak=[
    {"name":"abijith","count":4},
    {"name":"adith","count":2},
    {"name":"aadith","count":5},
    {"name":"adwaith","count":4},
    {"name":"amala","count":9},
    {"name":"arun","count":7},
    {"name":"ashiq","count":9},
    {"name":"fayaz","count":0},
    {"name":"felix","count":5},
    {"name":"harshit","count":4},
    {"name":"neenu","count":8},
    {"name":"saniya","count":7},
    {"name":"sarath","count":9},
    {"name":"SIVANANDANA","count":6},
    {"name":"sona","count":7},
    {"name":"vivek","count":2},
    {"name":"vrinda","count":7},
]

# srt with count
srt_count=sorted(hacker_rak,key=lambda dict:dict.get("count"))
print(srt_count)

sttendance=[

    {"name":"abin","attendance_count":28,"count":1},
    {"name":"aadhil","attendance_count":20,"count":2},
    {"name":"adhnan","attendance_count":20,"count":2},
    {"name":"arya","attendance_count":25,"count":5},
    {"name":"clairin","attendance_count":25,"count":4},
    {"name":"joji","attendance_count":26,"count":7},
    {"name":"libin","attendance_count":28,"count":7},
    {"name":"lijo","attendance_count":21,"count":2},
    {"name":"shajeer","attendance_count":27,"count":2},
    {"name":"shafi","attendance_count":28,"count":7},
    {"name":"resin","attendance_count":24,"count":3},
    {"name":"lakshmi","attendance_count":16,"count":6},
    {"name":"thammana","attendance_count":25,"count":1},
    {"name":"VARSHANA","attendance_count":8,"count":0},

]

srt_attendance=sorted(sttendance,key=lambda dict:dict.get("attendance_count"),reverse=True)
print(srt_attendance)
name_attendance=[{st.get("name"):st.get("attendance_count")} for st in srt_attendance]
print(name_attendance)
srt_hacker=sorted(sttendance,key=lambda dict:dict.get("count"),reverse=True)
print(srt_hacker)
name_count=[{c.get("name"):c.get("count")} for c in srt_hacker]
print(name_count)

