class Calculator:
    def add_num(self,*num):
        print(sum(num))
cal_instance=Calculator()
cal_instance.add_num(2,4,6,8)