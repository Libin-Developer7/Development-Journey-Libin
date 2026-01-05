class Rbi:
    def gold_loan_rate(self):
        print("gold loan rate",8.5)
    def home_loan_rate(self):
        print("home loan rate",9.2)
    def car_loan_rate(self):
        print("car loan rate",8.5)
class Hdfc(Rbi):
    def gold_loan_rate(self):
        print("gold loan",8.2)
    def home_loan_rate(self):
        print("home loan rate",9.0)
    def car_loan_rate(self):
        print("car loan rate",8.0)
hdfc_instance=Hdfc()
hdfc_instance.gold_loan_rate()