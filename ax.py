from tkinter import *
import math, random,os
from tkinter import messagebox


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color = "#074463"
        title = Label(self.root,
                      text="                                                               SAMADHAN GROCERY STORE                                                 ",
                      bd=12, relief=GROOVE, bg=bg_color, fg="white", font=("times new roman", 30, "bold"),
                      pady=2).pack()
        # =========variable=======
        # cosmatic
        self.soap = IntVar()
        self.face_cream = IntVar()
        self.face_wash = IntVar()
        self.spray = IntVar()
        self.gel = IntVar()
        self.lotion = IntVar()
        # grocery
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()
        # cold drink
        self.maza = IntVar()
        self.coke = IntVar()
        self.frooti = IntVar()
        self.thumbsup = IntVar()
        self.sprite = IntVar()
        self.limca = IntVar()

        # price
        self.cosmatic_price = StringVar()
        self.grocery_price = StringVar()
        self.colddrink_price = StringVar()
        # tax
        self.cosmatic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.colddrink_tax = StringVar()
        # customer
        self.c_name = StringVar()
        self.c_phon = StringVar()

        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))

        self.search_bill = StringVar()

        F1 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Customer Details", font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)
        cname_lbl = Label(F1, text="Customer Name", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(
            row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, font="arial 15", bd=7, relief=SUNKEN).grid(row=0,
                                                                                                             column=1,
                                                                                                             pady=5,
                                                                                                             padx=10)

        c_phn_lbl = Label(F1, text="Phone No.", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(
            row=0, column=2, padx=20, pady=5)
        c_phn_txt = Entry(F1, width=15, textvariable=self.c_phon, font="arial 15", bd=7, relief=SUNKEN).grid(row=0,
                                                                                                             column=3,
                                                                                                             pady=5,
                                                                                                             padx=10)

        c_bill_lbl = Label(F1, text="Bill No.", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(
            row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15, textvariable=self.search_bill, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=0, column=5, pady=5, padx=10)

        bill_btn = Button(F1, text="Search", width=10, bd=7, font="arial 12 bold").grid(row=0, column=6, padx=20,
                                                                                        pady=10)
        # ========cosmatic====
        F2 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cosmatics", font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F2.place(x=5, y=180, width=325, height=380)
        bath_lbl = Label(F2, text="Bath Soap", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=0, column=0, padx=10, pady=10, sticky="w")
        bath_txt = Entry(F2, width=10, textvariable=self.soap, font=("times new roman", 16, "bold"), bd=5,
                         relief=SUNKEN).grid(row=0, column=1,
                                             padx=10, pady=10)

        Face_creame = Label(F2, text="Face Cream", font=("times new roman", 16, "bold"), bg=bg_color,
                            fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        Face_creame_txt = Entry(F2, width=10, textvariable=self.face_cream, font=("times new roman", 16, "bold"), bd=5,
                                relief=SUNKEN).grid(row=1,
                                                    column=1,
                                                    padx=10,
                                                    pady=10)

        face_w_lbl = Label(F2, text="Face Wash", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        face_w_txt = Entry(F2, width=10, textvariable=self.face_wash, font=("times new roman", 16, "bold"), bd=5,
                           relief=SUNKEN).grid(row=2,
                                               column=1,
                                               padx=10,
                                               pady=10)

        hair_s_lbl = Label(F2, text="Hair Spray", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        hair_s_txt = Entry(F2, width=10, textvariable=self.spray, font=("times new roman", 16, "bold"), bd=5,
                           relief=SUNKEN).grid(row=3,
                                               column=1,
                                               padx=10,
                                               pady=10)

        hair_g_lbl = Label(F2, text="Hair Gel", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        hair_g_txt = Entry(F2, width=10, textvariable=self.gel, font=("times new roman", 16, "bold"), bd=5,
                           relief=SUNKEN).grid(row=4,
                                               column=1,
                                               padx=10,
                                               pady=10)

        b_l_lbl = Label(F2, text="Body Lotion", font=("times new roman", 16, "bold"), bg=bg_color,
                        fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        b_l_g_txt = Entry(F2, width=10, textvariable=self.lotion, font=("times new roman", 16, "bold"), bd=5,
                          relief=SUNKEN).grid(row=5, column=1,
                                              padx=10,
                                              pady=10)

        # ======GROCERY=====
        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Grocery", font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F3.place(x=340, y=180, width=325, height=380)
        g1_lbl = Label(F3, text="Rice", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0,
                                                                                                                 column=0,
                                                                                                                 padx=10,
                                                                                                                 pady=10,
                                                                                                                 sticky="w")
        g1_txt = Entry(F3, width=10, textvariable=self.rice, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=0, column=1,
                                           padx=10, pady=10)
        g2 = Label(F3, text="Food oil", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=1,
                                                                                                                 column=0,
                                                                                                                 padx=10,
                                                                                                                 pady=10,
                                                                                                                 sticky="w")
        g2 = Entry(F3, width=10, textvariable=self.food_oil, font=("times new roman", 16, "bold"), bd=5,
                   relief=SUNKEN).grid(row=1, column=1,
                                       padx=1, pady=10)

        g3 = Label(F3, text="Daal", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=2,
                                                                                                             column=0,
                                                                                                             padx=10,
                                                                                                             pady=10,
                                                                                                             sticky="w")
        g3 = Entry(F3, width=10, textvariable=self.daal, font=("times new roman", 16, "bold"), bd=5,
                   relief=SUNKEN).grid(row=2, column=1,
                                       padx=10, pady=10)

        g4 = Label(F3, text="Wheat", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=3,
                                                                                                              column=0,
                                                                                                              padx=10,
                                                                                                              pady=10,
                                                                                                              sticky="w")
        g4 = Entry(F3, width=10, textvariable=self.wheat, font=("times new roman", 16, "bold"), bd=5,
                   relief=SUNKEN).grid(row=3, column=1,
                                       padx=10, pady=10)

        g5 = Label(F3, text="Sugar", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=4,
                                                                                                              column=0,
                                                                                                              padx=10,
                                                                                                              pady=10,
                                                                                                              sticky="w")
        g5 = Entry(F3, width=10, textvariable=self.sugar, font=("times new roman", 16, "bold"), bd=5,
                   relief=SUNKEN).grid(row=4, column=1,
                                       padx=10, pady=10)

        g6 = Label(F3, text="Tea bag", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=5,
                                                                                                                column=0,
                                                                                                                padx=10,
                                                                                                                pady=10,
                                                                                                                sticky="w")
        g6 = Entry(F3, width=10, textvariable=self.tea, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(
            row=5, column=1,
            padx=10, pady=10)

        # ======Cold Drink=====
        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cold Drinks", font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F4.place(x=670, y=180, width=325, height=380)
        g11_lbl = Label(F4, text="Mazaa", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=0, column=0, padx=10, pady=10, sticky="w")
        g11_txt = Entry(F4, width=10, textvariable=self.maza, font=("times new roman", 16, "bold"), bd=5,
                        relief=SUNKEN).grid(row=0, column=1,
                                            padx=10, pady=10)
        g21 = Label(F4, text="coke", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=1,
                                                                                                              column=0,
                                                                                                              padx=10,
                                                                                                              pady=10,
                                                                                                              sticky="w")
        g21 = Entry(F4, width=10, textvariable=self.coke, font=("times new roman", 16, "bold"), bd=5,
                    relief=SUNKEN).grid(row=1, column=1,
                                        padx=1, pady=10)

        g31 = Label(F4, text="Frooti", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=2,
                                                                                                                column=0,
                                                                                                                padx=10,
                                                                                                                pady=10,
                                                                                                                sticky="w")
        g31 = Entry(F4, width=10, textvariable=self.frooti, font=("times new roman", 16, "bold"), bd=5,
                    relief=SUNKEN).grid(row=2, column=1,
                                        padx=10, pady=10)

        g41 = Label(F4, text="Thumbs Up", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=3, column=0, padx=10, pady=10, sticky="w")
        g41 = Entry(F4, width=10, textvariable=self.thumbsup, font=("times new roman", 16, "bold"), bd=5,
                    relief=SUNKEN).grid(row=3, column=1,
                                        padx=10, pady=10)

        g51 = Label(F4, text="Sprite", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=4,
                                                                                                                column=0,
                                                                                                                padx=10,
                                                                                                                pady=10,
                                                                                                                sticky="w")
        g51 = Entry(F4, width=10, textvariable=self.sprite, font=("times new roman", 16, "bold"), bd=5,
                    relief=SUNKEN).grid(row=4, column=1,
                                        padx=10, pady=10)

        g61 = Label(F4, text="Limca", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=5,
                                                                                                               column=0,
                                                                                                               padx=10,
                                                                                                               pady=10,
                                                                                                               sticky="w")
        g61 = Entry(F4, width=10, textvariable=self.limca, font=("times new roman", 16, "bold"), bd=5,
                    relief=SUNKEN).grid(row=5, column=1,
                                        padx=10, pady=10)

        # =======Bill Area=============

        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=180, width=520, height=380)
        bill_title = Label(F5, text="Bill Area", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # =====buttom=============================

        F6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu", font=("times new roman", 16, "bold"),
                        fg="gold", bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=230)

        m1_lbl = Label(F6, text="Total Cosmatic Price", bg=bg_color, fg="white",
                       font=("times new roman", 15, "bold")).grid(row=0, column=0, padx=20, pady=2, sticky="w")
        m1_txt = Entry(F6, width=18, textvariable=self.cosmatic_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=0, column=1, padx=10, pady=8)

        m2_lbl = Label(F6, text="Total Grocery Price", bg=bg_color, fg="white",
                       font=("times new roman", 15, "bold")).grid(row=1, column=0, padx=20, pady=2, sticky="w")
        m2_txt = Entry(F6, width=18, textvariable=self.grocery_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=1, column=1, padx=10, pady=8)

        m3_lbl = Label(F6, text="Total ColdDrink Price", bg=bg_color, fg="white",
                       font=("times new roman", 15, "bold")).grid(row=2, column=0, padx=20, pady=2, sticky="w")
        m3_txt = Entry(F6, width=18, textvariable=self.colddrink_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=2, column=1, padx=10, pady=8)

        m4_lbl = Label(F6, text=" Cosmatic Tax", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(
            row=0, column=2, padx=20, pady=2, sticky="w")
        m4_txt = Entry(F6, width=18, textvariable=self.cosmatic_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=0, column=3, padx=10, pady=8)

        m5_lbl = Label(F6, text=" Grocery Tax", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(
            row=1, column=2, padx=20, pady=2, sticky="w")
        m5_txt = Entry(F6, width=18, textvariable=self.grocery_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=1, column=3, padx=10, pady=8)

        m6_lbl = Label(F6, text=" ColdDrink Tax", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(
            row=2, column=2, padx=20, pady=2, sticky="w")
        m6_txt = Entry(F6, width=18, textvariable=self.colddrink_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=2, column=3, padx=10, pady=8)

        btn_F = Frame(F6, bd=7, relief=GROOVE)
        btn_F.place(x=750, width=755, height=137)

        total_btn = Button(btn_F, command=self.total, text="Total", bg="cadetblue", fg="white", pady=15, width=11,
                           bd=5,
                           font="arial 17 bold").grid(row=0, column=0, padx=7, pady=20)
        gbill_btn = Button(btn_F, command=self.bill_area, text="Generate Bill", bg="cadetblue", fg="white", pady=15,
                           width=11, bd=5,
                           font="arial 17 bold").grid(row=0, column=1, padx=7, pady=20)
        clear_btn = Button(btn_F, text="Clear", bg="cadetblue", fg="white", pady=15, width=11, bd=5,
                           font="arial 17 bold").grid(row=0, column=2, padx=7, pady=20)
        exit_btn = Button(btn_F, text="Exit", bg="cadetblue", fg="white", pady=15, width=11, bd=5,
                          font="arial 17 bold").grid(row=0, column=3, padx=7, pady=20)
        self.welcome_bill()

    def total(self):
        self.c1 = self.soap.get() * 40
        self.c2 = self.face_cream.get() * 140
        self.c3 = self.face_wash.get() * 80
        self.c4 = self.spray.get() * 100
        self.c5 = self.gel.get() * 50
        self.c6 = self.lotion.get() * 180

        self.total_cosmatic_price = float(
            self.c1 +
            self.c2 +
            self.c3 +
            self.c4 +
            self.c5 +
            self.c6
        )
        self.cosmatic_price.set("Rs.  " + str(self.total_cosmatic_price))
        self.c_tax = round((self.total_cosmatic_price * 0.05), 2)
        self.cosmatic_tax.set("Rs.  " + str(self.c_tax))

        self.c7 = self.rice.get() * 22
        self.c8 = self.food_oil.get() * 90
        self.c9 = self.daal.get() * 80
        self.c10 = self.wheat.get() * 30
        self.c11 = self.sugar.get() * 40
        self.c12 = self.tea.get() * 22

        self.total_grocery_price = float(
            self.c7 +
            self.c8 +
            self.c9 +
            self.c10 +
            self.c11 +
            self.c12
        )
        self.grocery_price.set("Rs.  " + str(self.total_grocery_price))
        self.g_tax = round((self.total_grocery_price * 0.04), 2)
        self.grocery_tax.set("Rs.  " + str(self.g_tax))

        self.c13 = self.maza.get() * 40
        self.c14 = self.coke.get() * 15
        self.c15 = self.frooti.get() * 12
        self.c16 = self.thumbsup.get() * 30
        self.c17 = self.sprite.get() * 45
        self.c18 = self.limca.get() * 32

        self.total_colddrink_price = float(
            self.c13 +
            self.c14 +
            self.c15 +
            self.c16 +
            self.c17 +
            self.c18
        )
        self.colddrink_price.set("Rs.  " + str(self.total_colddrink_price))
        self.cd_tax = round((self.total_colddrink_price * 0.02), 2)
        self.colddrink_tax.set("Rs.  " + str(self.cd_tax))

    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\t\tWelcome Samadhan Retail\n")
        self.txtarea.insert(END, f"\nBill Number: {self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer Name : {self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone Number : {self.c_phon.get()}")
        self.txtarea.insert(END, f"\n===========================================================")
        self.txtarea.insert(END, f"\n Products \t\t QTY\t\t\t\tPrice")
        self.txtarea.insert(END, f"\n===========================================================")

        '''self.Total_bill = float(
            self.total_cosmatic_price +
            self.total_grocery_price +
            self.total_colddrink_price +
            self.c_tax +
            self.g_tax +
            self.cd_tax)'''

    def bill_area(self):
        if self.c_name.get() == "" or self.c_phon.get() == "":
            messagebox.showerror("Error", "Customer Details are Must")
        elif self.cosmatic_price.get() == "Rs.  0.0" and self.grocery_price.get() == "Rs.  0.0" and self.colddrink_price.get() == "Rs.  0.0":
            messagebox.showerror("Error", "No Product Purchase")

        else:
            self.welcome_bill()
            # ========cosmatic======
            if self.soap.get() != 0:
                self.txtarea.insert(END, f"\n Bath Soap\t\t{self.soap.get()}\t\t\t\t{self.c1}")
            if self.face_cream.get() != 0:
                self.txtarea.insert(END, f"\n Face Cream\t\t{self.face_cream.get()}\t\t\t\t{self.c2}")
            if self.face_wash.get() != 0:
                self.txtarea.insert(END, f"\n Face Wash\t\t{self.face_wash.get()}\t\t\t\t{self.c3}")
            if self.spray.get() != 0:
                self.txtarea.insert(END, f"\n Hair Spray\t\t{self.spray.get()}\t\t\t\t{self.c4}")
            if self.gel.get() != 0:
                self.txtarea.insert(END, f"\n Hair Gel\t\t{self.gel.get()}\t\t\t\t{self.c5}")
            if self.lotion.get() != 0:
                self.txtarea.insert(END, f"\n Body lotion\t\t{self.lotion.get()}\t\t\t\t{self.c6}")

            # ========Grocery======
            if self.rice.get() != 0:
                self.txtarea.insert(END, f"\n Bath Soap\t\t{self.soap.get()}\t\t\t\t{self.c7}")
            if self.food_oil.get() != 0:
                self.txtarea.insert(END, f"\n Food Oil\t\t{self.food_oil.get()}\t\t\t\t{self.c8}")
            if self.daal.get() != 0:
                self.txtarea.insert(END, f"\n Daal\t\t{self.daal.get()}\t\t\t\t{self.c9}")
            if self.wheat.get() != 0:
                self.txtarea.insert(END, f"\n Wheat\t\t{self.wheat.get()}\t\t\t\t{self.c10}")
            if self.sugar.get() != 0:
                self.txtarea.insert(END, f"\n Sugar\t\t{self.sugar.get()}\t\t\t\t{self.c11}")
            if self.tea.get() != 0:
                self.txtarea.insert(END, f"\n Tea\t\t{self.tea.get()}\t\t\t\t{self.c12}")

            # ========Cold Drink======
            if self.maza.get() != 0:
                self.txtarea.insert(END, f"\n MaaZa\t\t{self.maza.get()}\t\t\t\t{self.c13}")
            if self.coke.get() != 0:
                self.txtarea.insert(END, f"\n Coke\t\t{self.coke.get()}\t\t\t\t{self.c14}")
            if self.frooti.get() != 0:
                self.txtarea.insert(END, f"\n Frooti\t\t{self.frooti.get()}\t\t\t\t{self.c15}")
            if self.thumbsup.get() != 0:
                self.txtarea.insert(END, f"\n Thumbs Up\t\t{self.thumbsup.get()}\t\t\t\t{self.c16}")
            if self.sprite.get() != 0:
                self.txtarea.insert(END, f"\n Sprite\t\t{self.sprite.get()}\t\t\t\t{self.c17}")
            if self.limca.get() != 0:
                self.txtarea.insert(END, f"\n Limca\t\t{self.Limca.get()}\t\t\t\t{self.c18}")

            self.txtarea.insert(END, f"\n-----------------------------------------------------------")
            if self.cosmatic_tax.get() != "Rs.  0.0":
                self.txtarea.insert(END, f"\n Cosmatic Tax   \t\t\t\t\t\t{self.cosmatic_tax.get()}")
            if self.grocery_tax.get() != "Rs.  0.0":
                self.txtarea.insert(END, f"\n Grocery Tax   \t\t\t\t\t\t{self.grocery_tax.get()}")
            if self.colddrink_tax.get() != "Rs.  0.0":
                self.txtarea.insert(END, f"\n Cold Drink Tax   \t\t\t\t\t\t{self.colddrink_tax.get()}")

            # self.txtarea.insert(END, f"\n Total Bill:Rs.  \t\t\t\t\t\t{self.Total_bill()}")
            self.txtarea.insert(END, f"\n-----------------------------------------------------------")
            self.save_bill()
    def save_bill(self):
            op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
            if op>0:
                self.bill_data = self.txtarea.get('1.0',END)
                f1=open("bill/"+str(self.bill_no.get()) +".txt","w")
                f1.write(self.bill_data)
                f1.close()
            else:
                return

root = Tk()
obj = Bill_App(root)
root.mainloop()