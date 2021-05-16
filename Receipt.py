from tkinter import *
import random

class Bar_App:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1400x800+0+0")
        self.window.title("Goods Billing Receipt App")
        self.window.config(background='#5cfcff')
        self.window.title("Bar Billing Receipt System")

        self.customer_name = StringVar()
        self.customer_ID = StringVar()

        """random receipt number"""
        receipt_random = random.randint(1, 9999)
        self.customer_receipt_no = StringVar()

        """setting the values to variable"""
        self.customer_receipt_no.set(str(receipt_random))

        self.Jack_Daniels = IntVar()
        self.vice_roy = IntVar()
        self.hennessy = IntVar()
        self.fourth_street = IntVar()
        self.amarula = IntVar()
        self.johnny_walker = IntVar()
        self.white_cap = IntVar()
        self.gilbeys = IntVar()
        self.kenya_cane = IntVar()
        self.chrome = IntVar()
        self.smirnoff = IntVar()
        self.delmonte = IntVar()
        self.mineral_water = IntVar()
        self.guarana = IntVar()
        self.black_label = IntVar()
        self.grants = IntVar()
        self.total_whisky = StringVar()
        self.total_wines_and_brandy = StringVar()
        self.total_spirit_and_others = StringVar()
        self.total_price = StringVar()
        self.tax_cost = StringVar()
        self.whisky_tax = StringVar()
        self.WinesBrandy_tax = StringVar()
        self.spiritOthers_tax = StringVar()

        """design"""
        bg_color ="#5cfcff"
        fg_color = "black"
        lbl_color = "white"

        """Title"""
        heading = Label(self.window,
                    text="Bar Billing Receipt System",
                    bd=12,
                    relief=GROOVE,
                    font=('Constantia', 20, "bold"),
                    fg = fg_color,
                    bg = bg_color,
                    pady=3).pack(fill=X)


        """frame"""
        frame_1 = LabelFrame(text="Customer's Details",
                             bg=bg_color,
                             fg="grey",
                             font=('Constantia', 20, "bold"),
                             relief=GROOVE,
                             bd=10)
        frame_1.place(x=0, y=80, relwidth=1)
        """customer's naming part"""
        customer_name = Label(frame_1, text="Customer's Name", fg="black", bg=bg_color, font=('Constantia', 15, "bold")).grid(row=0, column=0,padx=10, pady=5)
        cus_name_entry = Entry(frame_1, bd=8, relief=GROOVE, textvariable=self.customer_name)
        cus_name_entry.grid(row=0, column=1, ipady=4, ipadx=30, pady=5)

        """customer identification part"""
        cus_id = Label(frame_1, text="Customer's ID Number", font=('Constantia', 15, "bold"),
                       bg=bg_color, fg=fg_color).grid(row = 0,column = 2,padx = 20)

        id_entry = Entry(frame_1, bd=8, relief=GROOVE, textvariable=self.customer_ID)
        id_entry.grid(row=0, column=3, ipady=4, ipadx=30, pady=5)

        """receipt number part"""
        receipt_numbers_label = Label(frame_1, text="Receipt No.", bg=bg_color, font=('Constantia', 15, "bold"), fg=fg_color)
        receipt_numbers_label.grid(row = 0,column = 4,padx = 20)
        receipt_entry = Entry(frame_1, bd=8, relief=GROOVE, textvariable=self.customer_receipt_no)
        receipt_entry.grid(row = 0,column = 5,ipadx = 30,ipady = 4,pady = 5)

        """brews frame"""
        frame_2 = LabelFrame(self.window, text="Whisky", bd=10, relief=GROOVE, bg=bg_color, fg="grey", font=('Constantia', 15, "bold"))
        frame_2.place(x=5, y=180, width=325, height=380)

        """whiskies content"""
        "first brand"
        johnny_lbl = Label(frame_2, font=('Constantia', 15, "bold"), fg=fg_color, bg=bg_color, text="Johnny Walker")
        johnny_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
        johnny_entry = Entry(frame_2, bd=6, relief=GROOVE, textvariable=self.johnny_walker)
        johnny_entry.grid(row = 0,column = 1,ipady = 3,ipadx = 1)

        """second brand"""
        jack_lbl = Label(frame_2, font=('Constantia', 15, "bold"), fg=fg_color, bg=bg_color, text="Jack Daniels")
        jack_lbl.grid(row=1, column=0, padx=10, pady=20)
        jack_entry = Entry(frame_2, bd=6, relief=GROOVE, textvariable=self.Jack_Daniels)
        jack_entry.grid(row=1, column=1, ipady=3, ipadx=1)

        """third brand"""
        hennessy_lbl = Label(frame_2, font=('Constantia', 15, "bold"), fg=fg_color, bg=bg_color, text="Hennessy")
        hennessy_lbl.grid(row=2, column=0, padx=10, pady=20)
        hennessy_entry = Entry(frame_2, bd=6, relief=GROOVE, textvariable=self.hennessy)
        hennessy_entry.grid(row=2, column=1, ipady=3, ipadx=1)

        """fourth brand"""
        black_lbl = Label(frame_2, font=('Constantia', 15, "bold"), fg=fg_color, bg=bg_color, text="Black Label")
        black_lbl.grid(row=3, column=0, padx=10, pady=20)
        black_entry = Entry(frame_2, bd=6, relief=GROOVE, textvariable=self.black_label)
        black_entry.grid(row=3, column=1, ipady=3, ipadx=1)



        """Wines Frame"""
        frame_2 = LabelFrame(self.window, text="Wines & Brandy", bd=10, relief=GROOVE, bg=bg_color, fg="grey", font=('Constantia', 15, "bold"))
        frame_2.place(x=330, y=180, width=325, height=380)

        """Wines content"""
        """first wine"""
        amarula_lbl = Label(frame_2,font=('Constantia', 15, "bold"), fg=fg_color, bg=bg_color, text="Amarula")
        amarula_lbl.grid(row = 0,column = 0,ipadx = 5,pady = 5)
        amarula_entry = Entry(frame_2, bd=6, relief=GROOVE, textvariable=self.amarula)
        amarula_entry.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        """second wine"""
        fourth_lbl = Label(frame_2, font=('Constantia', 15, "bold"), fg=fg_color, bg=bg_color, text="4th Street")
        fourth_lbl.grid(row=1, column=0, ipadx=5, ipady=5)
        fourth_entry = Entry(frame_2, bd=6, relief=GROOVE, textvariable=self.fourth_street)
        fourth_entry.grid(row=1, column=1, ipady = 5,ipadx = 5)

        """first brandy"""
        gilbey_lbl = Label(frame_2, font=('Constantia', 15, "bold"), fg=fg_color, bg=bg_color, text="Gilbey's")
        gilbey_lbl.grid(row=2, column=0, ipadx=5, ipady=5)
        gilbey_entry = Entry(frame_2, bd=6, relief=GROOVE, textvariable=self.gilbeys)
        gilbey_entry.grid(row=2, column=1, ipady=5, ipadx= 5)

        """second brandy"""
        grants_lbl = Label(frame_2, font=('Constantia', 15, "bold"), fg=fg_color, bg=bg_color, text="Grants")
        grants_lbl.grid(row=3, column=0, ipadx=5, ipady=5)
        grants_entry = Entry(frame_2, bd=6, relief=GROOVE, textvariable=self.grants)
        grants_entry.grid(row=3, column=1, ipady=5, ipadx= 5)

        """third brandy"""
        vice_lbl = Label(frame_2, font=('Constantia', 15, "bold"), fg=fg_color, bg=bg_color, text="Vice Roy")
        vice_lbl.grid(row=4, column=0, ipadx=5, ipady=5)
        vice_entry = Entry(frame_2, bd=6, relief=GROOVE, textvariable=self.vice_roy)
        vice_entry.grid(row=4, column=1, ipady=5, ipadx= 5)

        """fourth brandy"""
        white_lbl = Label(frame_2, font=('Constantia', 15, "bold"), fg=fg_color, bg=bg_color, text="White Cap")
        white_lbl.grid(row=5, column=0, ipadx=5, ipady=5)
        white_entry = Entry(frame_2, bd=6, relief=GROOVE, textvariable=self.white_cap)
        white_entry.grid(row=5, column=1, ipady=5, ipadx= 5)



        """Spirit frame"""
        frame_2 = LabelFrame(self.window,text="Spirits & Others", bd=10, relief=GROOVE, bg=bg_color, fg="grey", font=('Constantia', 15, "bold"))
        frame_2.place(x=655, y=180, width=325, height=380)

        """Spirit content"""
        """first spirit"""
        smir_lbl = Label(frame_2, font=('Constantia', 15, "bold"), fg=fg_color, bg=bg_color, text="Smirnoff")
        smir_lbl.grid(row=0, column=0, ipadx=5, pady=5)
        smir_entry = Entry(frame_2, bd=6, relief=GROOVE, textvariable=self.smirnoff)
        smir_entry.grid(row=0, column=1, ipady=5, ipadx=5)

        """second spirit"""
        kenya_lbl = Label(frame_2, font=('Constantia', 15, "bold"), fg=fg_color, bg=bg_color, text="Kenya Cane")
        kenya_lbl.grid(row=1, column=0, ipadx=5, pady=5)
        kenya_entry = Entry(frame_2, bd=6, relief=GROOVE, textvariable=self.kenya_cane)
        kenya_entry.grid(row=1, column=1, ipady=5, ipadx=5)

        """third spirit"""
        chrome_lbl = Label(frame_2, font=('Constantia', 15, "bold"), fg=fg_color, bg=bg_color, text="Chrome")
        chrome_lbl.grid(row=2, column=0, ipadx=5, pady=5)
        chrome_entry = Entry(frame_2, bd=6, relief=GROOVE, textvariable=self.chrome)
        chrome_entry.grid(row=2, column=1, ipady=5, ipadx=5)

        """first others"""
        delmonte_lbl = Label(frame_2, font=('Constantia', 15, "bold"), fg=fg_color, bg=bg_color, text="Delmonte")
        delmonte_lbl.grid(row=3, column=0, ipadx=5, pady=5)
        delmonte_entry = Entry(frame_2, bd=6, relief=GROOVE, textvariable=self.delmonte)
        delmonte_entry.grid(row=3, column=1, ipady=5, ipadx=5)

        """second others"""
        guarana_lbl = Label(frame_2, font=('Constantia', 15, "bold"), fg=fg_color, bg=bg_color, text="Guarana")
        guarana_lbl.grid(row=4, column=0, ipadx=5, pady=5)
        guarana_entry = Entry(frame_2, bd=6, relief=GROOVE, textvariable=self.guarana)
        guarana_entry.grid(row=4, column=1, ipady=5, ipadx=5)

        """third others"""
        mineral_lbl = Label(frame_2, font=('Constantia', 15, "bold"), fg=fg_color, bg=bg_color, text="Mineral Water")
        mineral_lbl.grid(row=5, column=0, ipadx=5, pady=5)
        mineral_entry = Entry(frame_2, bd=6, relief=GROOVE, textvariable=self.mineral_water)
        mineral_entry.grid(row=5, column=1, ipady=5, ipadx=5)


        """receipt area"""
        frame_3 = Label(self.window, bd=10, relief= GROOVE)
        frame_3.place(x=1010, y=180, width=325, height=380)
        """******************"""
        receipt_title = Label(frame_3, text="Receipt Bill", font=("Lucida", 13, "bold"),bd=7, relief=GROOVE)
        receipt_title.pack(fill=X)

        """****************"""
        skrol_y = Scrollbar(frame_3, orient=VERTICAL)
        self.txt = Text(frame_3,yscrollcommand=skrol_y.set)
        skrol_y.pack(side=RIGHT, fill=Y)
        skrol_y.config(command=self.txt.yview)
        self.txt.pack(fill=BOTH, expand = 1)

        """buttons frame"""
        frame_4 = LabelFrame(self.window, text="Bill Menu", bd=10, relief=GROOVE,bg=bg_color, fg="grey", font=('Constantia', 15, "bold"))
        frame_4.place(x=0, y=560, relwidth=1, height=145)

        """*******************"""
        total_whisky = Label(frame_4, font=('Constantia', 10, "bold"), fg=fg_color, bg=bg_color, text="Total Whisky")
        total_whisky.grid(row=0, column=0, padx=10, pady=0)
        total_whisky_entry = Entry(frame_4, bd=8, relief=GROOVE, textvariable=self.total_whisky)
        total_whisky_entry.grid(row=0, column=1, ipady=2, ipadx=5)

        """*******************"""
        total_wines_brandy = Label(frame_4, font=('Constantia', 10, "bold"), fg=fg_color, bg=bg_color, text="Total Wines & Brandy")
        total_wines_brandy.grid(row=1, column=0, padx=10, pady=0)
        total_wines_entry = Entry(frame_4, bd=8, relief=GROOVE, textvariable=self.total_wines_and_brandy)
        total_wines_entry.grid(row=1, column=1, ipady=2, ipadx=5)

        """*******************"""
        total_spirit_others = Label(frame_4, font=('Constantia', 10, "bold"), fg=fg_color, bg=bg_color, text="Total Spirit & Others")
        total_spirit_others.grid(row=2, column=0, padx=10, pady=0)
        total_spirit_entry = Entry(frame_4, bd=8, relief=GROOVE, textvariable=self.total_spirit_and_others)
        total_spirit_entry.grid(row=2, column=1, ipady=2, ipadx=5)

        """**********************"""
        whisky_tax_lbl = Label(frame_4, font=('Constantia', 10, "bold"), fg=fg_color, bg=bg_color, text="Whisky Tax")
        whisky_tax_lbl.grid(row=0, column=2, padx=30, pady=0)
        whisky_tax_entry = Entry(frame_4, bd=8, relief=GROOVE, textvariable=self.whisky_tax)
        whisky_tax_entry.grid(row=0, column=3, ipady=2, ipadx=5)

        """**********************"""
        winesBrandy_tax_lbl = Label(frame_4, font=('Constantia', 10, "bold"), fg=fg_color, bg=bg_color, text="Wines & Brandy Tax")
        winesBrandy_tax_lbl.grid(row=1, column=2, padx=30, pady=0)
        winesBrandy_tax_entry = Entry(frame_4, bd=8, relief=GROOVE, textvariable=self.WinesBrandy_tax)
        winesBrandy_tax_entry.grid(row=1, column=3, ipady=2, ipadx=5)

        """***********************"""
        spiritOthers_tax_lbl = Label(frame_4, font=('Constantia', 10, "bold"), fg=fg_color, bg=bg_color, text="Spirit & Others Tax")
        spiritOthers_tax_lbl.grid(row=2, column=2, padx=30, pady=0)
        spiritOthers_tax_entry = Entry(frame_4, bd=8, relief=GROOVE, textvariable=self.spiritOthers_tax)
        spiritOthers_tax_entry.grid(row=2, column=3, ipady=2, ipadx=5)

        """************************"""
        total_whisky_btn = Button(frame_4, text="Total", bg=bg_color, fg=fg_color, font=("lucida",12,"bold"), bd=7, relief=GROOVE, command=self.total)
        total_whisky_btn.grid(row=1, column=4, ipadx=20, padx=30)

        """*************************"""
        genbill_btn = Button(frame_4, text="Gen. Receipt", bg=bg_color, fg=fg_color, font=("lucida",12,"bold"), bd=7, relief=GROOVE, command=self.receipt_area)
        genbill_btn.grid(row = 1,column = 5,ipadx = 20)

        """****************************"""
        print_btn = Button(frame_4, text="Print", bg=bg_color, fg=fg_color, font=("lucida",12,"bold"), bd=7, relief=GROOVE)
        print_btn.grid(row = 1,column = 6,ipadx = 20, padx=30)

        """****************************"""
        clear_btn = Button(frame_4, text="Clear", bg=bg_color, fg=fg_color, font=("lucida",12,"bold"), bd=7, relief=GROOVE, command=self.clear)
        clear_btn.grid(row=1, column=7, ipadx=20)

        """*********************************"""
        exit_btn = Button(frame_4, text="Exit", bg=bg_color, fg=fg_color, font=("lucida",12,"bold"), bd=7, relief=GROOVE, command=self.exit)
        exit_btn.grid(row = 1,column = 8,ipadx = 20, padx=30)


        """Functions to get total price"""
    def total(self):
        """total brew price"""
        self.total_whisky_price = (
        (self.johnny_walker.get()*1)+
        (self.Jack_Daniels.get()*3)+
        (self.hennessy.get()*8)+
        (self.black_label.get()*7)
        )
        self.total_whisky.set("KES"+str(self.total_whisky_price))
        self.tax_cost.set("KES"+str(round(self.total_whisky_price*0.05)))
        """total whisky&brandy prices"""
        self.total_wines_prices = (
        (self.amarula.get()*1)+
        (self.fourth_street.get()*5)+
        (self.gilbeys.get()*2)+
        (self.grants.get()*4)+
        (self.vice_roy.get()*8)+
        (self.white_cap.get()*3)
        )
        self.total_wines_and_brandy.set("KES"+str(self.total_wines_prices))
        self.WinesBrandy_tax.set("KES"+str(round(self.total_wines_prices*0.05)))

        """total spirit&other prices"""
        self.spirit_others = (
        (self.smirnoff.get()*1)+
        (self.kenya_cane.get()*6)+
        (self.chrome.get()*7)+
        (self.delmonte.get()*4)+
        (self.guarana.get()*3)+
        (self.mineral_water.get()*3)
        )
        self.total_spirit_and_others.set("KES"+str(self.spirit_others))
        self.spiritOthers_tax.set("KES"+str(round(self.spirit_others*0.05)))

    """function for welcome area"""
    def welcome(self):
        self.txt.delete('1.0', END)
        self.txt.insert(END, "         Wines & Spirits Store\n")
        self.txt.insert(END,f"\nReceipt No. : {str(self.customer_receipt_no.get())}")
        self.txt.insert(END,f"\nCustomer's Name : {str(self.customer_name.get())}")
        self.txt.insert(END,f"\nID Number : {str(self.customer_ID.get())}")
        self.txt.insert(END, "\n==================================")
        self.txt.insert(END, "\nProduct          Qty         Price")
        self.txt.insert(END, "\n==================================")


    """function to clear the receipt area"""
    def clear(self):
        self.txt.delete('1.0',END)

    """Add item name, qty and price to receipt area"""
    def receipt_area(self):
        self.welcome()
        if self.Jack_Daniels.get() != 0:
            self.txt.insert(END,f"\nJack Daniels         {self.Jack_Daniels.get()}          {self.Jack_Daniels.get()* 3}")
        if self.johnny_walker.get() != 0:
            self.txt.insert(END,f"\nJohnny Walker        {self.johnny_walker.get()}         {self.johnny_walker.get() * 1}")
        if self.hennessy.get() != 0:
            self.txt.insert(END,f"\nHennessy             {self.hennessy.get()}              {self.hennessy.get() * 8}")
        if self.black_label.get() != 0:
            self.txt.insert(END,f"\nBlack Label          {self.black_label.get()}           {self.black_label.get() * 7}")
        if self.amarula.get() != 0:
            self.txt.insert(END,f"\nAmarula              {self.amarula.get()}               {self.amarula.get() * 1}")
        if self.fourth_street.get() != 0:
            self.txt.insert(END,f"\n4th Street           {self.fourth_street.get()}         {self.fourth_street.get() * 5}")
        if self.gilbeys.get() != 0:
            self.txt.insert(END,f"\nGilbeys              {self.gilbeys.get()}               {self.gilbeys.get() * 2}")
        if self.grants.get() != 0:
            self.txt.insert(END,f"\nGrants               {self.grants.get()}                {self.grants.get() * 4}")
        if self.vice_roy.get() != 0:
            self.txt.insert(END,f"\nVice Roy             {self.vice_roy.get()}              {self.vice_roy.get() * 8}")
        if self.white_cap.get() != 0:
            self.txt.insert(END,f"\nWhite Cap            {self.white_cap.get()}             {self.white_cap.get() * 3}")
        if self.smirnoff.get() != 0:
            self.txt.insert(END,f"\nSmirnoff             {self.smirnoff.get()}              {self.smirnoff.get() * 1}")
        if self.chrome.get() != 0:
            self.txt.insert(END,f"\nChrome               {self.chrome.get()}                {self.chrome.get() * 7}")
        if self.kenya_cane.get() != 0:
            self.txt.insert(END,f"\nKenya Cane           {self.kenya_cane.get()}            {self.kenya_cane.get() * 6}")
        if self.delmonte.get() != 0:
            self.txt.insert(END,f"\nJack Del Monte       {self.delmonte.get()}              {self.delmonte.get() * 4}")
        if self.guarana.get() != 0:
            self.txt.insert(END,f"\nSmirnoff Guarana     {self.guarana.get()}               {self.guarana.get() * 3}")
        if self.mineral_water.get() != 0:
            self.txt.insert(END,f"\nMineral Water        {self.mineral_water.get()}         {self.mineral_water.get() * 3}")
        self.txt.insert(END,"\n==================================")
        self.txt.insert(END,f"\n                    Total: KES{self.total_whisky_price+self.total_wines_prices+self.spirit_others+self.total_whisky_price*0.05+self.total_wines_prices*0.05+self.spirit_others*0.05}")

    def exit(self):
        self.window.destroy()


window = Tk()
object = Bar_App(window)
window.mainloop()