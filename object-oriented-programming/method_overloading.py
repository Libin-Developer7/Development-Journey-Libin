class Calculator:
    def add(self,num1,num2):
        print(num1+num2)
    def add(self,num1,num2,num3):
        print(num1+num2+num3)
cal_instance=Calculator()
cal_instance.add(1,2,3)
"""
method overloading - same method name, different number of parameters. 
python only considers the last method defined, therefore method overloading is not supported.
"""