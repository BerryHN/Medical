init -25:
    python:
        
        class Item:
            def __init__(self, name, description, type, image):
                self.name=name
                self.description=description
                self.type=type
                self.image= image
                if type=='symptom':
                    self.icon ='icons/symptom.jpg'
                elif type=='sign':
                    self.icon ='icons/sign.png'
                elif type=='lab':
                    self.icon ='icons/lab.png'
                else:
                    self.icon ='#000'
        Inventory=[Item("Salami", "Delicious", "lab", "")]
        from_inventory=False


screen inventory_button:
    vbox xalign 0 yalign 0:
        textbutton "Inventory" action ui.callsinnewcontext("inventory_label")

label inventory_label:
    image icon =    "icons/lab.png"
    call screen inventory
    return
label item_inventory:
    $ from_inventory=True
    call screen item_inventory
screen item_inventory:
    textbutton "Return" action Return()

    
screen inventory:
    
    frame:
        vbox xalign 0 yalign 0:
            if len(Inventory) > 0:
                python:
                    
                    if from_inventory==False:
                        rows_inventory=len(Inventory)/3
                        remainder=len(Inventory) % 3
                        if remainder !=0:
                            rows_inventory += 1
                            blanks_data=[]
                        for i in range(remainder+1):
                            blanks_data.append(Item(name='',description='',type='', image=""))
                        Inventory.extend(blanks_data)
                
                grid 3 rows_inventory:
                    for i in Inventory:
                        vbox:
                            text "[i.name]"
                            imagebutton:
                                idle i.icon
                                hover i.icon
                                action ui.callsinnewcontext("item_inventory")
                            
                
            else:
                text "The chart is empty!"
            textbutton "Return" action Return()
