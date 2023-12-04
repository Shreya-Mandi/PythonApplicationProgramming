# ADAPTER PATTERN
# The Adapter pattern allows the interface of an existing class to be used as another interface. It is often used to make existing classes work with others without modifying their source code.

class adaptee:
    def specific_request(self):
        return "Adaptee's request"

class target:
    def request(self):
        return "Target's request"

class adapter(target):
    def __init__(self,adaptee):
        self.adaptee=adaptee

    def request(self):
        print(f"Adapter:{self.adaptee.specific_request()}")

adaptee_Ob=adaptee()
adapter=adapter(adaptee_Ob)

adapter.request()