screen inventario:
    pass
    '''
    if len(inventoryList) > 0:
        vbox xalign 0 yalign0:
            text "The chart is empty"
    else:
        frame:
            for i in inventoryList:
                text
    '''