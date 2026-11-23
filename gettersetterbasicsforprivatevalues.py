from datetime import datetime
class idt():
    def __init__(self,usernm,password,email):
        self.__usernm = usernm
        self.__password = password
        self.__email = email

    @property
    def usernm(self):
        print(f"userename accessed at {datetime.now()}")
        return f"The username is {self.__usernm}"
      
    @property
    def password(self):
        return f"The password is {self.__password}"

    @property
    def email(self):
        return f"the email is {self.__email} "
    
    @email.setter
    def email(self, new_email):
        if "@" in new_email:
            self.__email = new_email
            print(f"the new email is {self.__email}")
        else:
            raise ValueError("Invalid email: missing '@'")

user1 = idt("liltuff",4814998413,"liltuff@gmail.com")

print(user1.usernm)

print(user1.email)
user1.email = "libro@gmail.com"
print(user1.email)
