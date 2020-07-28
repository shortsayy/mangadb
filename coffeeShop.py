from tkinter import *

#Define functions
#Create frames
#Pack frames
#Create things for drop down menu
#Create widgets
#Pack widgets
#End program


# Define Funtions
window = Tk()
window.title("Coffee Shop")
window.geometry('400x400+100+20') # Starting size/position: width x hight + leftDistance + topDistance
window.minsize(200,200) #Minimum size: width, height


# Define functions
def calc():
		price = 0.0
		try:
			price = float(entCoffee.get()) *3
		except ValueError:
			print("Invalid coffee.")
		try:
			price += float(entCake.get()) *4.5
		except ValueError:
			print("Invalid cake.")
		if takeaway.get() == "Yes":
			price = price + 0.5
		lblPrice.configure(text="$%.2f" % price)
		
#Define functions 
def getTakeaway(selection):
	takeaway = selection		
	
# Create Frames
frmHeader = Frame(window, bg="black")
frmBody = Frame(window)
frmFooter = Frame(window, bg="black")

#Pack frames
frmHeader.pack(fill=X)
frmBody.pack(fill=BOTH, expand=TRUE)
frmFooter.pack(fill=X)

#Create things for drop down menu
takeaway = StringVar(window) # Stores the slectred text from the drop down menu
choices = ["","Yes","No"] # List of choices
takeaway.set('') # Defult value (blank)
mnuTakeaway = OptionMenu(frmBody, takeaway, *choices, command=getTakeaway)

#Create Widgets
lblTitle = Label(frmHeader, text="My Coffee Shop", bg="black", fg="white", font=("Arial", 24))

lblCoffee = Label(frmBody, text="\nNumber of coffees ($3 each):")
entCoffee = Entry(frmBody)
lblCake = Label(frmBody, text="\nNumber of cake ($4.50 each):")
entCake = Entry(frmBody)
lblTakeaway = Label(frmBody, text="\nTake away? ($0.50 surcharge)")
btnCalc = Button(frmBody, text="Calculate Price", command=calc)
lblPrice = Label(frmBody, text="", fg="red", font=("Arial", 20))

btnExit = Button(frmFooter, text="Exit", bg="red", command=exit)


# Pack widgets
lblTitle.pack()

lblCoffee.pack()
entCoffee.pack()
lblCake.pack()
entCake.pack()
lblTakeaway.pack()
mnuTakeaway.pack()
btnCalc.pack()
lblPrice.pack()

btnExit.pack(side=RIGHT)

	
# End program
window.mainloop()



