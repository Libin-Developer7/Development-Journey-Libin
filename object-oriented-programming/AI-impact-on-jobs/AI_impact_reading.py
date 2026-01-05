import csv
class AIDataset:
    data:list
    def __init__(self):
        fr_path="object-oriented-programming\\AI-impact-on-jobs\\AI_Impact_on_Jobs_2030.csv"
        fr=open(fr_path,"r",encoding="utf-8")
        reader=csv.DictReader(fr)
        self.data=[row for row in reader]
    def total_records(self):
        print(len(self.data))
    def all_titles(self):
        all_jobs=[jobs.get("Job_Title") for jobs in self.data]
        print(all_jobs)
    def first_record(self):
        frst_rcrd=self.data[0]
        print(frst_rcrd)

data_length=AIDataset()
data_length.total_records()
all_jobs=AIDataset()
all_jobs.all_titles()
frst_rcr=AIDataset()
frst_rcr.first_record()