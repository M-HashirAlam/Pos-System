from tkinter import *

window = Tk()
#icon = PhotoImage(file=r"C:\Users\Waqar Alam\Pictures\Capture.PNG")


class California_Pizza:

    def starting(self):
        canvas=Canvas(window,width=160,height=100)
        #canvas.create_image(0,0,anchor=NW,image=icon)
        canvas.pack()
        window.configure(background="yellow")
        lable = Label(window, text='Welcome to California Pizza', font=("Arial", 50), bg='Black', fg='white').pack()
class Pizza(Menu):
    def pizzas(self):
        global screen1
        screen1 = Toplevel(window)
        screen1.title("Pizzas")

        pizza1 = Label(screen1, text='Fajita', font=("Arial",35),bg='white', fg='black').grid(row=0, column=0)
        pizza2 = Label(screen1, text='Price=1500', font=("Arial", 20), bg='black', fg='white').grid(row=0, column=1)
        pizza3 = Label(screen1, text='Chicken Tikka', font=("Arial", 35),bg='white', fg='black').grid(row=1, column=0)
        pizza4 = Label(screen1, text='Price=1500', font=("Arial", 20), bg='black', fg='white').grid(row=1, column=1)
        pizza5 = Label(screen1, text='Veggie Lover', font=("Arial", 35), bg='white', fg='black').grid(row=2, column=0)
        pizza6 = Label(screen1, text='Price=1200', font=("Arial", 20), bg='black', fg='white').grid(row=2, column=1)
        pizza7 = Label(screen1, text='Sriracha', font=("Arial", 35), bg='white', fg='black').grid(row=3, column=0)
        pizza8 = Label(screen1, text='Price=1200', font=("Arial", 20), bg='black', fg='white').grid(row=3, column=1)
        pizza9 = Label(screen1, text='Cheese Lover', font=("Arial", 35), bg='white', fg='black').grid(row=4, column=0)
        piz = Label(screen1, text='Price=1200', font=("Arial", 20), bg='black', fg='white').grid(row=4, column=1)
        piza9 = Label(screen1, text='Chicken Supreme', font=("Arial", 35), bg='white', fg='black').grid(row=5, column=0)
        piza = Label(screen1, text='Price=1300', font=("Arial", 20), bg='black', fg='white').grid(row=5, column=1)

    def button(self):
        but1 = Button(window, text='Pizzas', font=('Arial', 20), command=self.pizzas).pack()
class deals(Menu):
    def deals(self):
        global screen1
        screen1 = Toplevel(window)
        screen1.title("Deals")
        pizza1 = Label(screen1, text='Kids Deal', font=("Arial",30),bg='black', fg='white').grid(row=0, column=0)
        pizza2 = Label(screen1, text='A Pan Pizza (6 inches) with a Toy and Juice for only 349/- (inclusive of taxes). Pizza Flavors are , Chicken Tikka, Cheese Lover and Veggie Lover.', font=("Arial", 10)).grid(row=1, column=1)
        pizza1 = Label(screen1, text='Value Deal 1', font=("Arial",30),bg='black', fg='white').grid(row=2, column=0)
        pizza2 = Label(screen1, text= "Small + 345 ml Drink for only 349/-(inclusive of taxes).",font=("Arial", 10)).grid(row=3, column=1)
        pizza1 = Label(screen1, text='Value Deal 2', font=("Arial",30),bg='black', fg='white').grid(row=4, column=0)
        pizza2 = Label(screen1, text= "10 inch Regular Pizza + 2 345 ml Drinks for only 1,349/-(inclusive of taxes).",font=("Arial", 10)).grid(row=5, column=1)
        pizza1 = Label(screen1, text='Value Deal 3', font=("Arial",30),bg='black', fg='white').grid(row=6, column=0)
        pizza2 = Label(screen1, text= "16 inch Jumbo Pizza + 1.5 Ltr Drink for only 2,349/-(inclusive of taxes).",font=("Arial", 10)).grid(row=7, column=1)
    def button(self):
        but2 = Button(window, text='Deals', font=('Arial', 20), command=self.deals).pack()

class deserts(Menu):
    def deserts(self):
        global screen1
        screen1 = Toplevel(window)
        screen1.title("Pizzas")

        pizza1 = Label(screen1, text='Brownie Fudge', font=("Arial", 35), bg='yellow', fg='black').grid(row=0, column=0)
        pizza2 = Label(screen1, text='Price=150', font=("Arial", 20), bg='black', fg='white').grid(row=0, column=1)
        pizza3 = Label(screen1, text='IceCreams', font=("Arial", 35), bg='red', fg='black').grid(row=1, column=0)
        pizza4 = Label(screen1, text='Price=1500', font=("Arial", 20), bg='black', fg='white').grid(row=1, column=1)
        pizza5 = Label(screen1, text='Chocolate Heaven Cake', font=("Arial", 35), bg='blue', fg='black').grid(row=2, column=0)
        pizza6 = Label(screen1, text='Price=400', font=("Arial", 20), bg='black', fg='white').grid(row=2, column=1)
    def button(self):
        but3 = Button(window, text='Deserts', font=('Arial', 20), command=self.deserts).pack()
class menu(California_Pizza):
    def __init__(self,fajita,chickentikka,veggielover,sriracha,chesselover,chickensuoreme,kidsdeal,valuedal1,valuedeal2,valuedeal3,browniefudge,icecreams,cake):

        self.Fajita = fajita
        self.chickentikka = chickentikka
        self.VeggieLove =veggielover
        self.Sriracha = sriracha
        self.CheeseLover=chesselover
        self.ChickenSupreme =chickensuoreme
        self.KidsDeal = kidsdeal
        self.ValueDeal1 = valuedal1
        self.ValueDeal2 = valuedeal2
        self.ValueDeal3 = valuedeal3
        self.BrownieFudge = browniefudge
        self.IceCreams = icecreams
        self.Cake = cake
    def order(self):
        global total
        global name
        name=input('Enter your name: ')
        input1 = input('What do you like to have? Deals/Pizzas/Deserts: ')
    
        if input1 != 'Pizzas' or input1 != 'Deals' or input1 != 'Deserts':
             print('please choose a valid option')
        if input1 == 'Pizzas':
            input2 = input('Which Pizza sir? ChickenTikka,Fajita,VeggieLove,Sriracha,CheeseLover,ChickenSupreme: ')
            if input2 == 'ChickenTikka':
                quantity=int(input('Enter Quantity: '))
                total=self.chickentikka*quantity
                print('Your total is: ',total)
            elif input2 == 'Fajita':
                quantity = int(input('Enter Quantity: '))
                total = self.chickentikka * quantity
                print('Your total is: ', total)
            elif input2 == 'VeggieLove':
                quantity = int(input('Enter Quantity: '))
                total = self.VeggieLove * quantity
                print('Your total is: ', total)
            elif input2 == 'Sriracha':
                quantity = int(input('Enter Quantity: '))
                total = self.Sriracha * quantity
                print('Your total is: ', total)
            elif input2 == 'CheeseLover':
                quantity = int(input('Enter Quantity: '))
                total = self.CheeseLover * quantity
                print('Your total is: ', total)
            elif input2 == 'ChickenSupreme':
                quantity = int(input('Enter Quantity: '))
                total = self.ChickenSupreme * quantity
                print('Your total is: ', total)
            else:
                print('Sorry this item is not avilable')
        if input1 == 'Deals':
            input2 = input('Which Deal sir? ValueDeal1/ValueDeal2/ValueDeal3/KidsDeal ')
            if input2 == 'KidsDeal':
                quantity = int(input('Enter Quantity: '))
                total = self.KidsDeal * quantity
                print('Your total is: ', total)
            elif input2 == 'ValueDeal1':
                quantity = int(input('Enter Quantity: '))
                total = self.ValueDeal1 * quantity
                print('Your total is: ', total)
            elif input2 == 'ValueDeal2':
                quantity = int(input('Enter Quantity: '))
                total = self.ValueDeal2 * quantity
                print('Your total is: ', total)
            elif input2 == 'ValueDeal3':
                quantity = int(input('Enter Quantity: '))
                total = self.ValueDeal3 * quantity
                print('Your total is: ', total)

            else:
                print('Sorry this item is not avilable')
        if input1 == 'Deserts':
            input2 = input('Which Desert sir? BrownieFudge/IceCream/Cake ')
            if input2 == 'BrownieFudge':
                quantity = int(input('Enter Quantity: '))
                total = self.BrownieFudge=quantity
                print('Your total is: ', total)
            elif input2 == 'IceCream':
                quantity = int(input('Enter Quantity: '))
                total = self.IceCreams * quantity
                print('Your total is: ', total)
            elif input2 == 'Cake':
                quantity = int(input('Enter Quantity: '))
                total = self.Cake * quantity
                print('Your total is: ', total)
            else:
                print('Sorry this item is not avilable')
        

class Order(menu):
    def place_order(self):
        but1 = Button(window, text='Order', font=('Arial', 20), command=self.order).pack()

class bill(California_Pizza):
    def give(self):
        print('-------------------------------------------------------------------------------------------')

        print('                                                 California Pizza')
        print("Dear: ",name)
        (print('Your total is: ',total))
        print('GST included')
        print('Thanks For Choosing us Hope you Enjoyed the Dinner')
        print('Branch: North Nazmimabad')
        print('-------------------------------------------------------------------------------------------')
    def print_bill(self):
        button2=Button(text='Print Bill',command=self.give,font=('Arial', 20)).pack()




a=California_Pizza()
a.starting()
pizza=Pizza()
pizza.button()
desert=deserts()
desert.button()
deal=deals()
deal.button()
bc = menu(1500,1500,1200,1200,1200,1300,349,349,1349,2349,150,1500,400)

r=Order(1500,1500,1200,1200,1200,1300,349,349,1349,2349,150,1500,400)
r.place_order()
d=bill()
d.print_bill()
window.mainloop()



