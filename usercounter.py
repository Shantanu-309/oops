class user ():

    the_count = 0
    def __init__(self,usern,email):
        self.usern = usern
        self.email  =email
        user.the_count += 1

    def display_user (self):
        return f"name {self.usern} and email {self.email}"


usr1 = user("nick","nikdickbig@gmail.com")
usr2 = user("jik","JIKrick@gmail.com")
usr3 =user("kikri","kikikimaria@gmail.com")

print(usr1.display_user())
print(user.the_count)
