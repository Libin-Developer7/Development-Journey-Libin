class Framework:
    name:str
    language:str
    architecture:str
    def set_framework(self,name,language,architecture):
        self.name=name
        self.language=language
        self.architecture=architecture
    def display(self):
        print(self.name,self.language,self.architecture)
django=Framework()
django.set_framework("django","python","mvt")
django.display()
angular=Framework()
angular.set_framework("angular","typescript","mvt")
angular.display()