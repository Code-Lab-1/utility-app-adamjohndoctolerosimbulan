def vndmchn(): #Defining the function of your project
    
    #Variables
    a = {'product': '1A', 'price': 130}
    b = {'product': '2A', 'price': 178}
    c = {'product': '3A', 'price': 71}
    d = {'product': '4A', 'price': 113}
    e = {'product': '5A', 'price': 215}
    f = {'product': '6A', 'price': 215}
    g = {'product': '7A', 'price': 323}
    h = {'product': '1B', 'price': 500}
    i = {'product': '2B', 'price': 450}
    j = {'product': '3B', 'price': 255}
    k = {'product': '4B', 'price': 120}
    l = {'product': '5B', 'price': 250}
    m = {'product': '6B', 'price': 130}
    n = {'product': '7B', 'price': 300}
    o = {'product': '1C', 'price': 170}
    p = {'product': '2C', 'price': 125}
    q = {'product': '3C', 'price': 230}
    r = {'product': '4C', 'price': 190}
    s = {'product': '5C', 'price': 200}
    t = {'product': '6C', 'price': 175}
    u = {'product': '7C', 'price': 205}
    
    #The name of the list of variables
    products = [a, b, c, d, e, f, g, h, i, g, k, l, m, n, o, p, q, r, s, t, u]
    # The credits in the vending machine
    credits = 0  

    # Printing the input
    print('                                                            __            /  __ ')
    print('                                                       /\  |  \  /\  |\/|   (_  ')
    print('                                                      /--\ |__/ /--\ |  |   __) ')
    print('                                          __       __          __               __              __ ')
    print('                                    \  / |_  |\ | |  \ | |\ | / _    |\/|  /\  /   |__| | |\ | |_  ')
    print('                                     \/  |__ | \| |__/ | | \| \__)   |  | /--\ \__ |  | | | \| |__ \n') 


    # Shows the products and prices
    def show(prodcut):
        print('                                    _        _______      _______  _______  _______ _________ _______ ')
        print('                                   ( \      (  ___  )    (  ____ \(  ___  )(  ____ )\__   __/(  ____ \ ')
        print('                                   | (      | (   ) |    | (    \/| (   ) || (    )|   ) (   | (    \/ ')
        print('                                   | |      | (___) |    | |      | (___) || (____)|   | |   | (__     ')
        print('                                   | |      |  ___  |    | |      |  ___  ||     __)   | |   |  __)     ')
        print('                                   | |      | (   ) |    | |      | (   ) || (\ (      | |   | (         ')
        print('                                   | (____/\| )   ( |    | (____/\| )   ( || ) \ \__   | |   | (____/\    ')
        print('                                   (_______/|/     \|    (_______/|/     \||/   \__/   )_(   (_______/    ')
        print('                   (------------------------------------------------------------------------------------------------)')
        print('                   (         (A) - BITES          |          (B) - DESSERTS         |         (C) - DRINKS          )')
        print('                   (------------------------------------------------------------------------------------------------)')
        print('                   ( 1. Pocky Strawberry   - ¥130 | 1. Japanese Cheesecake  - ¥500 | 1. Ramune               - ¥170 )')
        print('                   ( 2. Yanyan             - ¥178 | 2. Red Velvet cake      - ¥450 | 2. Yakult               - ¥125 )')
        print('                   ( 3. Ali Baba Chips     - ¥71  | 3. Chocolate Mousse     - ¥255 | 3. Milk Tea             - ¥230 )')
        print('                   ( 4. Cheese Ring  Chips - ¥113 | 4. Ice Candy            - ¥120 | 4. Ice Tea              - ¥190 )')
        print('                   ( 5. Cheese Curls Chips - ¥215 | 5. Warabi Mochi         - ¥250 | 5. Aloe Drink           - ¥200 )')
        print('                   ( 6. Takis Chips        - ¥215 | 6. Dango                - ¥130 | 6. Melon Soda           - ¥175 )')
        print('                   ( 7. Pringles Chips     - ¥323 | 7. Castella Cake        - ¥300 | 7. Sake                 - ¥205 )')
        print('                   (================================================================================================)')
        print('                   (                         THIS MACHINE ONLY ACCEPTS (¥100, ¥500, ¥1000)                          )')
        print('                   (                          CHOOSING THE ITEMS EXAMPLE: (1A or 2B or 3C)                          )')
        print('                   (                             *only UPPER case letters are accepted*                             )')
        print('                   (------------------------------------------------------------------------------------------------)') 

    
    # Have the user choose an item
    proceed = True
    while proceed == True:
        show(products)
        userchoice = input('Choose a product: ') #Asking user to input a product
        #Using for loop 
        for product in products:
            #Using if-else function
            if userchoice == product.get('product'): #Using .get() to get the product code
                userchoice = product             
                price = userchoice.get('price')  #Using .get() to get the product price
                while credits < price:
                    #Asking user to enter the required amount of the product
                    credits = credits + float(input('Place Cash ' + str(price - credits) + ': ')) 
                #Prints the selected product
                print('Product Selected: ' + userchoice.get('product'))
                credits -= price
                #Prints the remaining balance 
                print('Remaining Balance: ' + str(credits))
                #Asking the user if they would buy another product from the vending machine
                q = input('Would you like to buy anything else? (y/n): ')
                #If the user picks No or n it ends the transaction
                if (q == 'n' or q =='N'):
                    proceed = False
                    #Prints out the remaining balance after purchasing
                    if credits != 0:
                        print(str(credits) + ' has been conpensated!')
                        credits = 0
                        print('Thank you for your purchase, have a nice day!\n')
                        break                        
                    else:
                        print('Thank you for your purchase, have a nice day!\n')
                        break  
                else:
                    continue
                        
                    
vndmchn()