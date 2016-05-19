init -25:
    class Item:
        def __init__(self,name, description, type, image='')
            self.name=name
            self.description=description
            self.type=type
            if type=='symptom':
                self.icon=='icons/symptom.png'
            elif type=='sign':
                self.icon=='icons/sign.png'
            if type=='lab':
                self.icon=='icons/lab.png'
screen inventory:
    pass