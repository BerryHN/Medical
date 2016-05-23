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
        Inventory=["Salami", "Delicious", "Pepper", "apple"]


screen inventory_button:
    vbox xalign 0 yalign 0:
        textbutton "Inventory" action ui.callsinnewcontext("inventory_label")

label inventory_label:
    call screen inventory
    return
label item_inventory:
    call screen item_inventory
screen item_inventory:
    pass
    
screen inventory:
    frame:
        vbox xalign 0 yalign 0:
            if len(Inventory) > 0:
                python:
                    rows_inventory=len(Inventory)/3
                    remainder=len(Inventory) % 3
                    if remainder !=0:
                        rows_inventory += 1
                        blanks_data=[]
                    for i in range(remainder+1):
                        blanks_data.append("a")#Item(name='',description='',type=''))
                    Inventory.extend(blanks_data)
                grid 3 rows_inventory:
                    for i in Inventory:
                        vbox:
                            #textbutton "See more" action ui.callsinnewcontext("item_inventory")
                            text " [i] "
                            text " [i] Next line"
                
            else:
                text "The chart is empty!"
            textbutton "Return" action Return()
