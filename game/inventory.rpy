init -25:
    python:
        class Item:
            def __init__(names, description, type, image):
                self.name=name
                self.description=description
                self.type=type
                self.image= image
                if type=='symptom':
                    self.icon=='icons/symptom.jpg'
                elif type=='sign':
                    self.icon=='icons/sign.png'
                elif type=='lab':
                    self.icon=='icons/lab.png'
                else:
                    self.icon==''


#screen inventory:
 #  python:
  #    rows_inventory=len(inventory)/3
   #   remainder=len(inventory) % 3
    #  if remainder !=0:
      #     rows_inventory += 1
     #      blanks_data=[]
       #    for i in range(remainder):
        #       blanks.append(Item(name='',description='',type=''))
