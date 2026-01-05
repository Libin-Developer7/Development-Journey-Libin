from abc import ABC                  # abstraction is used to hide implementation details
from abc import abstractmethod       # abc is a python module(file), collection of modules is called package 
class Editor(ABC):                   # ABC-abstract base method must be imported and inherited to create abstract class
    @abstractmethod                  # abstractmethod must be called for each method in abstract base class
    def create_module_and_package(self):
        pass
    @abstractmethod                  # decorator used to add extra feature without changing the method
    def edit(self):
        pass
    @abstractmethod   
    def execute(self):
        pass
    @abstractmethod   
    def debug(self):
        pass
class VsCode(Editor):                     # all methods of ABC must be defined in VsCode child class
    def create_module_and_package(self):
        print("vs code create module and package")
    def edit(self):
        print("edit code in vs code")
    def execute(self):
        print("execute code in vs code")
    def debug(self):
        print("debug code in vs code")
vscode_instance=VsCode()
vscode_instance.create_module_and_package()