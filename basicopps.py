class HOUSE ():
    def __init__(self,typee,color,owner):
        self.type = typee
        self.color = color
        self.owner = owner

class OWNER():
    def __init__(self,name,address,gender,age):
        self.name = name
        self.address = address
        self.gender = gender
        self.age = age
        

owner1 = OWNER("mike","benton_lx","male","30")

owner2 = OWNER("lucy",";ucy_lx","female","29")

house1 = HOUSE("Tuscan","Blue",owner1)

house2 = HOUSE("modern","Grey",owner2)
