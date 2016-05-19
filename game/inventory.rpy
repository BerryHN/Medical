init -25:
    class Item:
        def __init__(self,name, description, type, image='')
            self.name=name
            self.description=description
            self.type=type
            if type=='symptom':
                self.icon=='icons/symptom.jpg'
            elif type=='sign':
                self.icon=='icons/sign.png'
            elif type=='lab':
                self.icon=='icons/lab.png'
            else:
                self.icon==''

'''
screen inventory:
    python:
        rows_inventory=len(inventory)/3
        remainder=len(inventory) % 3
        if remainder !=0:
            rows_inventory += 1
            blanks_data=[]
            for i in range(remainder):
                blanks.append(Item(name='',description='',type=''))
        
            
        
    frame:
        xpos=1
        ypos=0
        grid 3 rows_inventory:
            for j in inventory:
                
'''