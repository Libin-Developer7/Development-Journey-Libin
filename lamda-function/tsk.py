taskreport=[

    {"name":"Abin","task_count":14,"mcq_score":19},
    {"name":"Adhil","task_count":13,"mcq_score":16},
    {"name":"Adhnan","task_count":13,"mcq_score":9},
    {"name":"Aryananda","task_count":16,"mcq_score":10},
    {"name":"Clairin","task_count":18,"mcq_score":12},
    {"name":"Joji","task_count":19,"mcq_score":23},
    {"name":"Libin","task_count":17,"mcq_score":20},
    {"name":"Lijo","task_count":15,"mcq_score":13},
    {"name":"shejeer","task_count":8,"mcq_score":11},
    {"name":"shafi","task_count":10,"mcq_score":18},
    {"name":"Resin","task_count":13,"mcq_score":20},
    {"name":"Sreelakshmi","task_count":14,"mcq_score":0},
    {"name":"Thamanna","task_count":1,"mcq_score":20},
    {"name":"Varshana","task_count":1,"mcq_score":11},
    {"name":"Abhijith ","task_count":10,"mcq_score":21},
    {"name":"Adith","task_count":1,"mcq_score":17},
    {"name":"Adithyan","task_count":3,"mcq_score":16},
    {"name":"Adwaid","task_count":3,"mcq_score":8},
    {"name":"Agnes","task_count":4,"mcq_score":19},
    {"name":"Amala","task_count":12,"mcq_score":18},
    {"name":"Arun","task_count":6,"mcq_score":20},
    {"name":"Ashik","task_count":20,"mcq_score":24},
    {"name":"Fayas","task_count":0,"mcq_score":0},
    {"name":"Felix","task_count":4,"mcq_score":15},
    {"name":"Harshithraj","task_count":7,"mcq_score":21},
    {"name":"Neenu","task_count":18,"mcq_score":21},
    {"name":"Saniya","task_count":20,"mcq_score":22},
    {"name":"Sharath","task_count":18,"mcq_score":22},
    {"name":"Sivanandhana","task_count":8,"mcq_score":15},
    {"name":"Sona","task_count":20,"mcq_score":19},
    {"name":"Vivek","task_count":7,"mcq_score":21},
    {"name":"Vrindha","task_count":8,"mcq_score":13},  

]

srt_tskcount= sorted(taskreport, key=lambda dict:dict.get("task_count"))
print(srt_tskcount)
srt_mcqscore=sorted(taskreport,key=lambda dict:dict.get("mcq_score"),reverse=True)
print(srt_mcqscore)