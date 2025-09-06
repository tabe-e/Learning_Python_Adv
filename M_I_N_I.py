#-----MINI PROJECT-----GROCERY---STORE---BILL------#
#user enter catogery of an item--> display item's with price
#user add multiple item's in cart with quantity---> display cart{}
#user can remove item from cart and choose final bill---> display final bill 



#-----------store's item listed in nested dict
stock = {
    "Vegetables": {
        1: {"name": "Tomato", "unit": "kg", "price": 2},
        2: {"name": "Potato", "unit": "kg", "price": 1},
        3: {"name": "Onion", "unit": "kg", "price": 1.5},
        4: {"name": "Carrot", "unit": "kg", "price": 2.5},
        5: {"name": "Spinach", "unit": "bunch", "price": 1}
    },
    "Fruits": {
        1: {"name": "Apple", "unit": "kg", "price": 3},
        2: {"name": "Banana", "unit": "dozen", "price": 1.5},
        3: {"name": "Orange", "unit": "kg", "price": 2.5},
        4: {"name": "Grapes", "unit": "kg", "price": 3},
        5: {"name": "Mango", "unit": "kg", "price": 4}
    },
    "Grains": {
        1: {"name": "Rice", "unit": "kg", "price": 2},
        2: {"name": "Wheat Flour", "unit": "kg", "price": 1.8},
        3: {"name": "Lentils", "unit": "kg", "price": 2.2},
        4: {"name": "Chickpeas", "unit": "kg", "price": 2},
        5: {"name": "Oats", "unit": "kg", "price": 3}
    },
    "Dairy": {
        1: {"name": "Milk", "unit": "liter", "price": 1},
        2: {"name": "Cheese", "unit": "kg", "price": 5},
        3: {"name": "Yogurt", "unit": "kg", "price": 2},
        4: {"name": "Butter", "unit": "kg", "price": 4},
        5: {"name": "Paneer", "unit": "kg", "price": 4.5}
    }
}
#---------------creating dict for decoding category name
decoder_cat = {}
for item in stock:
    first_letter = item[0]  
    decoder_cat.setdefault(first_letter, []).append(item)

#---------------creating dict for decoding item name
decoder_itm = {}
for ind, details in stock.items():
   for index,name in details.items():
        name = name["name"]
        first_letter = name[0]
        decoder_itm.setdefault(first_letter, []).append(name)

#----------------storing item
cart = {}

#-----------------remove function
def remove_():
        while True:
                if not cart:
                        print("Cart is empty!")
                        break
                else:
                        print("------------------------------Your  Cart--------------------------------")
                        sn = "S.No."
                        q = "Quantity"
                        c = "Item Code"
                        i = "Item"
                        p = "Price"
                        print(f"{sn:<15}{c:<15}{i:<15}{q:<15}{p:<15}")

                        #----------printing every item store in cart
                        i = 1
                        for categ, index_0 in cart.items():
                                for index_1, details in index_0.items():
                                        
                                        #----------storing details in variable
                                        sn = i
                                        price = details['price']
                                        unit = details["unit"]
                                        quant = details["quantity"]
                                        code = details["code"]
                                        
                                        #----------formatting display values
                                        name_d = details["name"]
                                        price_d = f"${price}/{unit}"
                                        quant_d = f"{quant}{unit}"
                                        
                                        #-----------printing pre_bill
                                        print(  f"{sn:<15}"
                                                f"{code:<15}"
                                                f"{name_d:<15}"                        
                                                f"{quant_d:<15}"
                                                f"{price_d:<15}"
                                        )
                                        i += 1
                                print("------------------------------------------------------------------------")
                        #---------asking user to remove item
                        rem = input("Enter Item code from Your Cart to  remove OR enter 'back' to Category: ")
                        if rem == 'back':
                                break
                

                        else:
                                #--------decoding code of item
                                cat_d = rem[0]   
                                name_first = rem[1]
                                name_last = rem[2]   
                                ind_d = int(rem[3:]) 
                                for cat in decoder_cat[cat_d]:
                                        for nam in decoder_itm[name_first]:
                                                length = len(nam)
                                                length -= 1
                                                nam_ = nam[length] 
                                                nam_ = nam_.upper()
                                                if nam_ == name_last:
                                                   if stock[cat][ind_d]["name"] == nam:
                                                        print(f"\n\n---------------{cart[cat][ind_d]['name']} is removed from Your Cart----------------\n\n")
                                                        del cart[cat][ind_d]
                                                        break
#-------final bill generated here
def bill():
        print("------------------------------Your  Bill--------------------------------")
        sn = "S.No."
        q = "Quantity"
        c = "Item Code"
        i = "Item"
        p = "Price"
        t = "Total"
        print(f"{sn:<15}{c:<15}{i:<15}{q:<15}{p:<15}{t:<15}")

        #----------printing every item store in cart
        i = 1
        for categ, index_0 in cart.items():
                for index_1, details in index_0.items():
                        
                        #----------storing details in variable
                        sn = i
                        price = details['price']
                        unit = details["unit"]
                        quant = details["quantity"]
                        code = details["code"]
                        total = quant * price
                        
                        #----------formatting display values
                        name_d = details["name"]
                        price_d = f"${price}/{unit}"
                        quant_d = f"{quant}{unit}"
                        total_d = f"${total}"
                        
                        #-----------printing pre_bill
                        print(  f"{sn:<15}"
                                f"{code:<15}"
                                f"{name_d:<15}"                        
                                f"{quant_d:<15}"
                                f"{price_d:<15}"
                                f"{total_d:<15}"
                        )
                        i += 1
                print("------------------------------------THANK YOU FOR SHOPPING------------------------------------")


                        

#-----------------main loop
def cat(): 
                #----------------Category loop
                while True:
                        #-----display categories
                        print("-------Categories------")
                        a = 1
                        for key in stock:
                                        print(f"{a}. {key}")
                                        a += 1
                        #-------user navigation bw item loop, bill block, remove block, exit loop category loop               
                        category = input("Enter category from above list to exolore item or enter 'exit' to exit or enter 'remove' to remove item from cart or enter 'bill' to checkout: ")
                        if category == 'exit':
                                break
                        if category == 'bill':
                                bill()#------make bill function
                                break
                        if category == 'remove':
                                remove_()
                                continue
                
                        else:           
                                #----------------display item
                                print(f"\n---------------------- {category} ------------------------")
                                sn ,i, p = "S.No.","Item", "Price/Unit"
                                print(f"{sn:<15}{i:<15}{p:<15}")
                                for ind, details in stock[category].items():
                                        sn = f"{ind}."
                                        item = details["name"]
                                        per = f"${details['price']}/{details['unit']}"                  
                                        print(f"{sn:<15}{item:<15}{per:<15}") 
                                print("------------------------------------------------------------")
                        #------index loop
                                while True:
                                                #---asking user to enter item index no.
                                                index = int(input("Enter S.No. of item to add in cart or enter '0' to category: "))
                                                if index == 0:
                                                        break
                                                if index == 0:
                                                        break
                                                #-----asking user to enter quantity of item
                                                quant = float(input(f"Enter quantity of {stock[category][index]["name"]} in {stock[category][index]["unit"]}: "))
                                                #--------genrating code of Item
                                                _1 = category[0]
                                                name1 = stock[category][index]["name"]
                                                _2 = name1[0]
                                                lenf = len(name1) - 1
                                                letter3 = name1[lenf]
                                                _3 = letter3.upper()
                                                _4 = str(index)
                                                code_here = _1 + _2 + _3 + _4

                                                #-----------update user data in cart                                
                                                if category not in cart:
                                                        cart[category] = {} 
                                                        cart[category][index] = stock[category][index]
                                                        cart[category][index]["quantity"] = quant
                                                        cart[category][index]["code"] = code_here
                                                elif category in cart:
                                                        if index not in cart[category]:
                                                                cart[category][index] = stock[category][index]
                                                                cart[category][index]["quantity"] = quant
                                                                cart[category][index]["code"] = code_here
                                                        else:
                                                                cart[category][index]["quantity"] += quant
                                                else:
                                                        print("Invalid Data!")

                                                #----------------printing pre-bill
                                                print("------------------------------Your  Cart--------------------------------")
                                                sn = "S.No."
                                                q = "Quantity"
                                                c = "Item Code"
                                                i = "Item"
                                                print(f"{sn:<15}{c:<15}{i:<15}{q:<15}{p:<15}")

                                                #----------printing every item store in cart
                                                i = 1
                                                for categ, index_0 in cart.items():
                                                        for index_1, details in index_0.items():
                                                                
                                                                #----------storing details in variable
                                                                sn = i
                                                                price = details['price']
                                                                unit = details["unit"]
                                                                quant = details["quantity"]
                                                                code = details["code"]
                                                                
                                                                #----------formatting display values
                                                                name_d = details["name"]
                                                                price_d = f"${price}/{unit}"
                                                                quant_d = f"{quant}{unit}"
                                                                
                                                                #-----------printing pre_bill
                                                                print(  f"{sn:<15}"
                                                                        f"{code:<15}"
                                                                        f"{name_d:<15}"                        
                                                                        f"{quant_d:<15}"
                                                                        f"{price_d:<15}"
                                                                )
                                                                i += 1
                                                print("------------------------------------------------------------------------")
        
cat()
                        























    







   
    










