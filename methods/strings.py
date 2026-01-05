"""class Bottle:
    def open(self):
        pass         # method - functions in class, to use method need to create class object
    def close()
    def fill()
        
bottle_obj = Bottle()
bottle_obj.open()
bottle_obj.close()

class Fan:
   def on()
   def off()

   fan_obj = Fan()
   fan_obj.on()


"""

company_name = "LUMINAR"
print(company_name.casefold())
print(company_name.capitalize())
print(company_name.isdigit())  

number = "123"
print(number.isalpha())  
num_text ="12rte"
print(num_text.isalnum())

text_1 = "python programming is simple"
print(text_1.index("py"))   # index(substr)-> returns position of first occurence of the substring
print(text_1.index("on"))
print(text_1.find("on"))
print(text_1.find("no"))    # find(substr,start,stop)-> returns -1 if substring does not exist
print(text_1.find("og",5,30)) 
print(text_1.rfind("ing"))    # returns value from right side

word="#theword#"
print(word.strip("#")) 

data="$status code 401"
print(data.lstrip("$"))

word1="status#"
print(word1.rstrip("#"))

text="python is dynamic"
print(text.split(" "))

text11="python.is.dynamic"
print(text11.split("."))
                         

"""text="adbaddbnadnadbnad"
for i in range(0,len(text)):
    print(text[i])
print("========")

for char in text:
    print(char)"""