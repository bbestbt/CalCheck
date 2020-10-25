from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

global totalcd, totalcb, totalcf, totals, totalco, totalcde, totalr
totalcb = 0
totalcd = 0
totalcf = 0
totals = 0
totalco = 0
totalcde = 0
totalr = 0


def allSum():
    allTotal = totalcb + totalcd + totalcde + totalcf + totalco + totalr + totals

    labell = Label(text="Your food calories is :  " + str(allTotal) + "  kcal    ", bg='lightcoral', fg='black',
                   font=('impact', 18)).place(
        x=630, y=490)
    # labell.config( text="Your food calories is : " + str(allTotal))

    # amount.set("your food calories is %d "%amount )


class Food(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        # self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        # PAGE NAME
        for F in (Menu, CalCheck, StartPage, Beverage, Fruit, Dish, Snack, Rice, Dessert, Onedish):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        # self.show_frame("StartPage")
        self.show_frame("Menu")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class Menu(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='mediumpurple')
        self.controller = controller
        image = Image.open('vet.jpg')
        tkimage = ImageTk.PhotoImage(image)
        x1 = Label(self, image=tkimage)
        x1.image = tkimage
        x1.place(x=0, y=0)
        label = Label(self, text="Menu")

        btnMenu1 = Button(self, text="BMI/BMR", bg='dodgerblue', fg='navy', font=('impact', 40),
                          command=lambda: controller.show_frame("CalCheck")).place(x=500, y=200, width=220, height=70,
                                                                                   anchor=CENTER)
        btnMenu2 = Button(self, text="FOOD CALORIES", bg='dodgerblue', fg='navy', font=('impact', 40),
                          command=lambda: controller.show_frame("StartPage")).place(x=500, y=400, width=370, height=70,anchor=CENTER)
        btnMenu3 = Button(self, text="i", bg='lightpink', fg='white', font=('impact', 13),
                          command=Intro).place(x=630, y=220, width=20, height=30,anchor=CENTER)

def Intro():
    text = """\n\n\t“BMI” stands for Body Mass Index.  It is used to determine healthy body weight.By inputting your height and weight,
    your BMI will be shown and to be compared with the appropriate BMI range.Your health risk will then be determined. 
    \t“BMR” stands for Basal Metabolic Rate.  It is the number of calories required to keep your body functioning at rest. 
    BMR is also known as body’s metabolism; therefore, any increase in your metabolic weight,such as exercise, will increase 
    your BMR. To get your BMR, simply input your height, gender, age and weight.Once you’ve determined your BMR, you can 
    begin to monitor how many calories you need per day to maintain or reduce weight.
    """
    window = Tk()
    window.geometry("950x200")
    window.resizable(0,0)
    window.configure(bg='royalblue')
    window.option_add("*Font", "Couriernew 13")
    window.title('information')
    info = Label(window,text= text , bg='royalblue',fg='white',justify = LEFT).grid()

class CalCheck(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='mistyrose')
        self.controller = controller
        # self.headline = Label(self, text="THE GREATEST WEALTH IS HEALTH", fg='mediumorchid', bg='mistyrose',font=('impact', 22)).grid()

        # pic
        image = Image.open('smile.jpg')
        tkimage = ImageTk.PhotoImage(image)
        x1 = Label(self, image=tkimage)
        x1.image = tkimage
        x1.place(x=790, y=350)

        image = Image.open('people.jpg')
        tkimage = ImageTk.PhotoImage(image)
        x2 = Label(self, image=tkimage)
        x2.image = tkimage
        # x2.place(x = 450, y= 360)
        x2.place(x=770, y=100)

        self.headline = Label(self, text="\t\t\t\t\n", fg='mediumorchid', bg='mistyrose', font=('impact', 22)).grid()
        self.headline = Label(self, text="THE GREATEST WEALTH IS HEALTH", fg='mediumorchid', bg='mistyrose',
                              font=('impact', 22)).place(relx=0.29, rely=0.05)

        self.name = StringVar()
        self.username = Label(self, text="Name", bg='mistyrose', fg='navy', font=('impact', 16))
        self.n = Entry(self, textvariable=self.name, font=('impact', 16))
        self.surname = StringVar()
        self.userlast = Label(self, text="Surname", bg='mistyrose', fg='navy', font=('impact', 16))
        self.l = Entry(self, textvariable=self.surname, font=('impact', 16))
        self.age = StringVar()
        self.userage = Label(self, text="Age", bg='mistyrose', fg='navy', font=('impact', 16))
        self.a = Entry(self, textvariable=self.age, font=('impact', 16))
        self.height = StringVar()
        self.userheight = Label(self, text="Height (cm)", bg='mistyrose', fg='navy', font=('impact', 16))
        self.h = Entry(self, textvariable=self.height, font=('impact', 16))
        self.weight = StringVar()
        self.userweight = Label(self, text="Weight (kg)", bg='mistyrose', fg='navy', font=('impact', 16))
        self.w = Entry(self, textvariable=self.weight, font=('impact', 16))
        self.cal = Button(self, text="Calculate BMI", bg='dodgerblue', fg='navy', font=('impact', 16), command=self.BMI)
        self.gender = StringVar()
        self.gen = Label(self, text="Gender", bg='mistyrose', fg='navy', font=('impact', 16)).grid(row=6)
        self.l1 = Listbox(self, height=2, font=('impact', 16))

        self.n.grid(row=1, column=1)
        self.l.grid(row=2, column=1)
        self.a.grid(row=3, column=1)
        self.h.grid(row=4, column=1)
        self.w.grid(row=5, column=1)
        self.cal.grid(row=7)

        self.username.grid(row=1)
        self.userlast.grid(row=2)
        self.userage.grid(row=3)
        self.userheight.grid(row=4)
        self.userweight.grid(row=5)

        self.l1.insert(1, "Male")
        self.l1.insert(2, "Female")

        # self.l1.pack(side = "top")
        button = Button(self, text="Back", font=('Couriernew', 16), relief="solid",
                        command=lambda: controller.show_frame("Menu")).place(x=10, y=450)

        self.l1.grid(row=6, column=1)

        self.bminum = StringVar()
        Label(self, textvariable=self.bminum, bg='mistyrose', fg='darkorange', font=('impact', 16)).grid(row=8)

        self.bmitext = StringVar()
        Label(self, textvariable=self.bmitext, bg='mistyrose', fg='darkorange', font=('impact', 16)).grid(row=9)

        # BMR
        self.BR = Button(self, text="Calculate BMR ", bg='dodgerblue', fg='navy', font=('impact', 16),
                         command=self.BMR).grid(
            row=7, column=1)
        self.enter = 0
        self.value = ""
        self.value1 = ""
        self.bmr = 0
        self.bmrnum = StringVar()
        Label(self, textvariable=self.bmrnum, bg='mistyrose', fg='navy', font=('impact', 16)).grid(row=9, column=1)

    def BMI(self):
        weight = float(self.weight.get())
        height = float(self.height.get())
        bmi = float((weight) / ((height / 100) ** 2))
        self.bminum.set("your bmi is %.2f" % bmi)
        if bmi < 18.5:
            self.bmitext.set("you are underweight")
            self.h1 = Label(self, text="Health risks = Moderate", bg='mistyrose', fg='deepskyblue',
                            font=('impact', 16)).grid(row=10)

        elif bmi <= 24.9:
            self.bmitext.set("you are normal")
            self.h2 = Label(self, text="Health risks = Low", bg='mistyrose', fg='lightseagreen',
                            font=('impact', 16)).grid(row=10)
        elif bmi <= 29.9:
            win = Tk()
            win.configure(bg='gold')
            win.option_add("*Font", "impact 16")
            win.title('risk factors')
            self.bmitext.set("you are overweight")
            self.risk = Label(self,
                              text="Risk Factors\nHigh blood pressure (hypertension)\nHigh LDL cholesterol ('bad' cholesterol) \nLow HDL cholesterol ('good' cholesterol)\n High triglycerides\n High blood glucose (sugar) \nFamily history of premature heart disease\nPhysical inactivity \nCigarette smoking ",
                              bg='gold', fg='red')
            self.risk.grid(win, row=9, column=1)
            self.risk.grid()
            self.h3 = Label(self, text="Health risks = Moderate", bg='mistyrose', fg='deepskyblue',
                            font=('impact', 16)).grid(row=10)
        elif bmi > 30:
            win = Tk()
            win.configure(bg='gold')
            win.option_add("*Font", "impact 16")
            win.title('risk factors')
            self.bmitext.set("you are obese")
            self.risk = Label(win,
                              text="Risk Factors\nHigh blood pressure (hypertension)\nHigh LDL cholesterol ('bad' cholesterol) \nLow HDL cholesterol ('good' cholesterol)\n High triglycerides\n High blood glucose (sugar) \nFamily history of premature heart disease\nPhysical inactivity \nCigarette smoking ",
                              bg='gold', fg='red')
            # self.risk.grid(win,row=9,column=1)
            self.risk.grid()
            self.h4 = Label(self, text="Health risks = High", bg='mistyrose', fg='orangered', font=('impact', 16)).grid(
                row=10)
        # self.mainloop()

    def BMR(self):
        root = Tk()
        root.geometry("550x200")
        root.configure(bg='lightgreen')
        root.option_add("*Font", "Couriernew 13")
        root.title('BMR')
        self.headline2 = Label(root, text="YOUR ACTIVITY", fg='darkgreen', bg='lightgreen').place(x=10)
        self.l2 = Listbox(root, width=55, height=5)
        self.l2.insert(1, "no sport or exercise")
        self.l2.insert(2, "light exercise or sport 1-3 days per week")
        self.l2.insert(3, "moderate exercise or sport 3-5 days per week")
        self.l2.insert(4, "hard exercise or sport or physical job 6-7 days per week")
        self.l2.insert(5, "very hard exercise or sport and a physical job or 2 training")
        self.l2.place(x=30, y=30)
        self.selct = Button(root, text="enter", fg='black', bg='gold', relief="solid", command=self.exercise).place(
            x=250, y=140)

        weight = float(self.weight.get())
        height = float(self.height.get())
        age = int(self.age.get())
        while (True):
            self.value = self.l1.get(ACTIVE)
            #enter =ork
            if (self.enter == 0):
                break
        print(self.value)

        # male

        if (self.value == 'Male'):
            self.bmr = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
            print(self.bmr)
            # return self.bmr
            # self.bmrnum=StringVar()
            # Label(textvariable=self.bmrnum,bg='mistyrose',fg='darkorange').grid()


        # female
        elif (self.value == 'Female'):
            self.bmr = 665 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
            print(self.bmr)

        # self.bmrtext.set("you BMR is %f"%BMR )
        #green page
        self.enter = 1
        return self.bmr

    def exercise(self):
        while (True):
            self.value1 = self.l2.get(ACTIVE)
            #print(self.value1)
            if (self.enter == 1):
                break

        if self.value1 == "no sport or exercise":
            self.bmr = self.bmr * 1.2
        elif self.value1 == "light exercise or sport 1-3 days per week":
            self.bmr = self.bmr * 1.375
        elif self.value1 == "moderate exercise or sport 3-5 days per week":
            self.bmr = self.bmr * 1.55
        elif self.value1 == "hard exercise or sport or physical job 6-7 days per week":
            self.bmr = self.bmr * 1.725
        elif self.value1 == "very hard exercise or sport and a physical job or 2 training":
            self.bmr = self.bmr * 1.9
        print(self.bmr)
        self.bmrnum.set("your bmr is %.2f " % self.bmr)


class StartPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='lightcoral')
        self.controller = controller
        # label = Label(self, text="This is the start page")
        # label.pack(side="top", fill="x", pady=10)

        button1 = Button(self, text="BEVERAGE", bg='peachpuff', fg='darkorange', font=('impact', 40), relief="solid",
                         command=lambda: controller.show_frame("Beverage")).place(x=350, y=100, width=220, height=70,
                                                                                  anchor=CENTER)
        button2 = Button(self, text="Fruit", bg='peachpuff', fg='darkorange', font=('impact', 40), relief="solid",
                         command=lambda: controller.show_frame("Fruit")).place(x=650, y=100, width=220, height=70,
                                                                               anchor=CENTER)
        button3 = Button(self, text="Dish", bg='peachpuff', fg='darkorange', font=('impact', 40), relief="solid",
                         command=lambda: controller.show_frame("Dish")).place(x=350, y=200, width=220, height=70,
                                                                              anchor=CENTER)
        button4 = Button(self, text="Snack", bg='peachpuff', fg='darkorange', font=('impact', 40), relief="solid",
                         command=lambda: controller.show_frame("Snack")).place(x=650, y=200, width=220, height=70,
                                                                               anchor=CENTER)
        button5 = Button(self, text="Rice", bg='peachpuff', fg='darkorange', font=('impact', 40), relief="solid",
                         command=lambda: controller.show_frame("Rice")).place(x=500, y=400, width=220, height=70,
                                                                              anchor=CENTER)
        button6 = Button(self, text="Dessert", bg='peachpuff', fg='darkorange', font=('impact', 40), relief="solid",
                         command=lambda: controller.show_frame("Dessert")).place(x=650, y=300, width=220, height=70,
                                                                                 anchor=CENTER)
        button7 = Button(self, text="Onedish", bg='peachpuff', fg='darkorange', font=('impact', 40), relief="solid",
                         command=lambda: controller.show_frame("Onedish")).place(x=350, y=300, width=220, height=70,
                                                                                 anchor=CENTER)
        button8 = Button(self, text="Total food calories", bg='wheat', fg='tomato', font=('impact', 30), relief="solid",
                         command=allSum).place(x=300, y=500, width=320, height=50, anchor=CENTER)
        button = Button(self, text="Back", font=('Couriernew', 16), relief="solid",
                        command=lambda: controller.show_frame("Menu")).place(x=10, y=480)

        image = Image.open('bev.jpg')
        tkimage = ImageTk.PhotoImage(image)
        x1 = Label(self, image=tkimage)
        x1.image = tkimage
        x1.place(x=800, y=100)

        image = Image.open('des.jpg')
        tkimage = ImageTk.PhotoImage(image)
        x1 = Label(self, image=tkimage)
        x1.image = tkimage
        x1.place(x=800, y=300)

        # button1.pack()
        # button2.pack()
        # button3.pack()
        # button4.pack()
        # button5.pack()
        # button6.pack()
        # button7.pack()


class Beverage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='skyblue')
        self.controller = controller
        label = Label(self, text="Beverage")

        image = Image.open('bev4.jpg')
        tkimage = ImageTk.PhotoImage(image)
        x1 = Label(self, image=tkimage)
        x1.image = tkimage
        x1.place(x=750, y=270)

        image = Image.open('bev3.jpg')
        tkimage = ImageTk.PhotoImage(image)
        x2 = Label(self, image=tkimage)
        x2.image = tkimage
        x2.place(x=750, y=70)

        image = Image.open('bev2.jpg')
        tkimage = ImageTk.PhotoImage(image)
        x3 = Label(self, image=tkimage)
        x3.image = tkimage
        x3.place(x=350, y=290)

        image = Image.open('bev5.jpg')
        tkimage = ImageTk.PhotoImage(image)
        x4 = Label(self, image=tkimage)
        x4.image = tkimage
        x4.place(x=350, y=70)

        # back button
        button = Button(self, text="Go to the menu page", font=('Couriernew', 16), relief="solid",
                        command=lambda: controller.show_frame("StartPage")).place(x=10, y=450)
        # button.grid(row=13,column=0,sticky=W)

        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()
        self.var4 = IntVar()
        self.var5 = IntVar()
        self.var6 = IntVar()
        self.var7 = IntVar()
        self.var8 = IntVar()
        self.var9 = IntVar()
        self.var10 = IntVar()
        self.var11 = IntVar()
        self.enterr = 0
        Label(self, text="BEVERAGE", bg='skyblue', fg='navy', font=('Couriernew', 20)).grid(row=0, column=0, sticky=W)

        Softdrink = Checkbutton(self, text="Soft drink", font=('Couriernew', 15), bg='skyblue',
                                variable=self.var1).grid(row=1, column=0, sticky=W)

        Lemonade = Checkbutton(self, text="Lemonade", font=('Couriernew', 15), bg='skyblue', variable=self.var2).grid(
            row=2, column=0, sticky=W)
        Coconutjuice = Checkbutton(self, text="Coconut juice", font=('Couriernew', 15), bg='skyblue',
                                   variable=self.var3).grid(row=3, column=0, sticky=W)
        Orangejuice = Checkbutton(self, text="Orange juice", font=('Couriernew', 15), bg='skyblue',
                                  variable=self.var4).grid(row=4, column=0, sticky=W)
        Pineapplejuice = Checkbutton(self, text="Pineapple juice", font=('Couriernew', 15), bg='skyblue',
                                     variable=self.var5).grid(row=5, column=0, sticky=W)
        DarkThaiicetea = Checkbutton(self, text="Dark Thai ice tea", font=('Couriernew', 15), bg='skyblue',
                                     variable=self.var6).grid(row=6, column=0, sticky=W)
        LimeThaitea = Checkbutton(self, text="Lime Thai tea", font=('Couriernew', 15), bg='skyblue',
                                  variable=self.var7).grid(row=7, column=0, sticky=W)
        Icedtea = Checkbutton(self, text="Iced tea", font=('Couriernew', 15), bg='skyblue', variable=self.var8).grid(
            row=8, column=0, sticky=W)
        Hotchocolate = Checkbutton(self, text="Hot chocolate", font=('Couriernew', 15), bg='skyblue',
                                   variable=self.var9).grid(row=9, column=0, sticky=W)
        Guavajuice = Checkbutton(self, text="Guava juice", font=('Couriernew', 15), bg='skyblue',
                                 variable=self.var10).grid(row=10, column=0, sticky=W)
        Pandanjuice = Checkbutton(self, text="Pandan juice", font=('Couriernew', 15), bg='skyblue',
                                  variable=self.var11).grid(row=11, column=0, sticky=W)

        choose1 = Button(self, text="enter", command=self.enter, font=('Couriernew', 16), relief="solid").place(x=10,
                                                                                                                y=500)

        # choose1.bind('<Button-1>',show)
        # choose1.pack()

    def enter(self):
        cb1 = self.var1.get()
        cb2 = self.var2.get()
        cb3 = self.var3.get()
        cb4 = self.var4.get()
        cb5 = self.var5.get()
        cb6 = self.var6.get()
        cb7 = self.var7.get()
        cb8 = self.var8.get()
        cb9 = self.var9.get()
        cb10 = self.var10.get()
        cb11 = self.var11.get()
        global totalcb
        totalcb = (cb1 * 100) + (cb2 * 100) + (cb3 * 120) + (cb4 * 160) + (cb5 * 125) + (cb6 * 110) + (cb7 * 100) + (
                    cb8 * 100) + (cb9 * 120) + (cb10 * 100) + (cb11 * 120)
        print(totalcb)
        messagebox.showinfo("select", "FINISH!!!")


class Fruit(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='skyblue')
        self.controller = controller
        label = Label(self, text="Fruit")

        # back button
        button = Button(self, text="Go to the menu page", font=('Couriernew', 16), relief="solid",
                        command=lambda: controller.show_frame("StartPage")).place(x=10, y=470)
        # button.grid(row=13,column=0,sticky=W)

        image = Image.open('fruit1.jpg')
        tkimage = ImageTk.PhotoImage(image)
        x1 = Label(self, image=tkimage)
        x1.image = tkimage
        x1.place(x=730, y=300)

        image = Image.open('fruit2.jpg')
        tkimage = ImageTk.PhotoImage(image)
        x2 = Label(self, image=tkimage)
        x2.image = tkimage
        x2.place(x=750, y=70)

        image = Image.open('fruit4.jpg')
        tkimage = ImageTk.PhotoImage(image)
        x3 = Label(self, image=tkimage)
        x3.image = tkimage
        x3.place(x=350, y=290)

        image = Image.open('fruit3.jpg')
        tkimage = ImageTk.PhotoImage(image)
        x4 = Label(self, image=tkimage)
        x4.image = tkimage
        x4.place(x=350, y=70)

        self.var12 = IntVar()
        self.var13 = IntVar()
        self.var14 = IntVar()
        self.var15 = IntVar()
        self.var16 = IntVar()
        self.var17 = IntVar()
        self.var18 = IntVar()
        self.var19 = IntVar()
        self.var20 = IntVar()
        self.var21 = IntVar()
        self.var22 = IntVar()
        self.var23 = IntVar()

        Label(self, text="FRUITS", bg='skyblue', fg='navy', font=('Couriernew', 20)).grid(row=0, column=0, sticky=W)

        Cantaloupe = Checkbutton(self, text="Cantaloupe", font=('Couriernew', 15), bg='skyblue',
                                 variable=self.var12).grid(row=1, column=0, sticky=W)
        Roseapple = Checkbutton(self, text="Rose apple", font=('Couriernew', 15), bg='skyblue',
                                variable=self.var13).grid(row=2, column=0, sticky=W)
        Watermelon = Checkbutton(self, text="Water melon", font=('Couriernew', 15), bg='skyblue',
                                 variable=self.var14).grid(row=3, column=0, sticky=W)
        Guava = Checkbutton(self, text="Guava", font=('Couriernew', 15), bg='skyblue', variable=self.var15).grid(row=4,
                                                                                                                 column=0,
                                                                                                                 sticky=W)
        Papaya = Checkbutton(self, text="Papaya", font=('Couriernew', 15), bg='skyblue', variable=self.var16).grid(
            row=5, column=0, sticky=W)
        Mangosteen = Checkbutton(self, text="Mangosteen", font=('Couriernew', 15), bg='skyblue',
                                 variable=self.var17).grid(row=6, column=0, sticky=W)
        Mandarinorange = Checkbutton(self, text="Mandarin orange", font=('Couriernew', 15), bg='skyblue',
                                     variable=self.var18).grid(row=7, column=0, sticky=W)
        Pomelo = Checkbutton(self, text="Pomelo", font=('Couriernew', 15), bg='skyblue', variable=self.var19).grid(
            row=8, column=0, sticky=W)
        Pineapple = Checkbutton(self, text="Pineapple", font=('Couriernew', 15), bg='skyblue',
                                variable=self.var20).grid(row=9, column=0, sticky=W)
        Grape = Checkbutton(self, text="Grape", font=('Couriernew', 15), bg='skyblue', variable=self.var21).grid(row=10,
                                                                                                                 column=0,
                                                                                                                 sticky=W)
        Apple = Checkbutton(self, text="Apple", font=('Couriernew', 15), bg='skyblue', variable=self.var22).grid(row=11,
                                                                                                                 column=0,
                                                                                                                 sticky=W)
        Dragonfruit = Checkbutton(self, text="Dragon fruit", font=('Couriernew', 15), bg='skyblue',
                                  variable=self.var23).grid(row=12, column=0, sticky=W)

        choose2 = Button(self, text="enter", command=self.enter, font=('Couriernew', 16), relief="solid").place(x=10,
                                                                                                                y=520)

    def enter(self):
        cf1 = self.var12.get()
        cf2 = self.var13.get()
        cf3 = self.var14.get()
        cf4 = self.var15.get()
        cf5 = self.var16.get()
        cf6 = self.var17.get()
        cf7 = self.var18.get()
        cf8 = self.var19.get()
        cf9 = self.var20.get()
        cf10 = self.var21.get()
        cf11 = self.var22.get()
        cf12 = self.var23.get()
        global totalcf
        totalcf = (cf1 * 4) + (cf2 * 16) + (cf3 * 250) + (cf4 * 174) + (cf5 * 8) + (cf6 * 13) + (cf7 * 340) + (
                    cf8 * 60) + (cf9 * 8) + (cf10 * 16) + (cf11 * 42) + (cf12 * 60)
        print(totalcf)
        messagebox.showinfo("select", "FINISH!!!")


class Dish(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='skyblue')
        self.controller = controller
        label = Label(self, text="Dish")

        # back button
        button = Button(self, text="Go to the menu page", font=('Couriernew', 16), relief="solid",
                        command=lambda: controller.show_frame("StartPage")).place(x=800, y=390)
        # button.grid(row=13,column=0,sticky=W)

        image = Image.open('dish1.jpg')
        tkimage = ImageTk.PhotoImage(image)
        x2 = Label(self, image=tkimage)
        x2.image = tkimage
        x2.place(x=800, y=50)

        self.var24 = IntVar()
        self.var25 = IntVar()
        self.var26 = IntVar()
        self.var27 = IntVar()
        self.var28 = IntVar()
        self.var29 = IntVar()
        self.var30 = IntVar()
        self.var31 = IntVar()
        self.var32 = IntVar()
        self.var33 = IntVar()
        self.var34 = IntVar()
        self.var35 = IntVar()
        self.var36 = IntVar()
        self.var37 = IntVar()
        self.var38 = IntVar()
        self.var39 = IntVar()
        self.var40 = IntVar()
        self.var41 = IntVar()
        self.var42 = IntVar()
        self.var43 = IntVar()
        self.var44 = IntVar()
        self.var45 = IntVar()
        self.var46 = IntVar()
        self.var47 = IntVar()
        self.var48 = IntVar()
        self.var49 = IntVar()
        self.var50 = IntVar()
        self.var51 = IntVar()
        self.var52 = IntVar()

        Label(self, text="DISHES", bg='skyblue', fg='navy', font=('Couriernew', 20)).grid(row=0, column=0, sticky=W)
        d1 = Checkbutton(self, text="Stir-fried shrimp with green pepper", font=('Couriernew', 15), bg='skyblue',
                         variable=self.var24).grid(row=1, column=0, sticky=W)
        d2 = Checkbutton(self, text="Batter-fried prawns", font=('Couriernew', 15), bg='skyblue',
                         variable=self.var25).grid(row=2, column=0, sticky=W)
        d3 = Checkbutton(self, text="Baked prawns and Mung Bean noodle", font=('Couriernew', 15), bg='skyblue',
                         variable=self.var26).grid(row=3, column=0, sticky=W)
        d4 = Checkbutton(self, text="Yellow curry pork", font=('Couriernew', 15), bg='skyblue',
                         variable=self.var27).grid(row=4, column=0, sticky=W)
        d5 = Checkbutton(self, text="Curry chicken", font=('Couriernew', 15), bg='skyblue', variable=self.var28).grid(
            row=5, column=0, sticky=W)
        d6 = Checkbutton(self, text="Vegetable gourd soup with minced pork", font=('Couriernew', 15), bg='skyblue',
                         variable=self.var29).grid(row=6, column=0, sticky=W)
        d7 = Checkbutton(self, text="Stuffed bitter gourd with seasonsed minced pork soup", font=('Couriernew', 15),
                         bg='skyblue', variable=self.var30).grid(row=7, column=0, sticky=W)
        d8 = Checkbutton(self, text="Vermicelli soup", font=('Couriernew', 15), bg='skyblue', variable=self.var31).grid(
            row=8, column=0, sticky=W)
        d9 = Checkbutton(self, text="Chicken curry eggplant", font=('Couriernew', 15), bg='skyblue',
                         variable=self.var32).grid(row=9, column=0, sticky=W)
        d10 = Checkbutton(self, text="Roasted duck red curry", font=('Couriernew', 15), bg='skyblue',
                          variable=self.var33).grid(row=10, column=0, sticky=W)
        d11 = Checkbutton(self, text="Chicken massaman curry", font=('Couriernew', 15), bg='skyblue',
                          variable=self.var34).grid(row=11, column=0, sticky=W)
        d12 = Checkbutton(self, text="Spicy mixed vegetables soup", font=('Couriernew', 15), bg='skyblue',
                          variable=self.var35).grid(row=12, column=0, sticky=W)
        d13 = Checkbutton(self, text="Mixed vegetables sour soup", font=('Couriernew', 15), bg='skyblue',
                          variable=self.var36).grid(row=13, column=0, sticky=W)
        d14 = Checkbutton(self, text="Thai pork curry with morning glory", font=('Couriernew', 15), bg='skyblue',
                          variable=self.var37).grid(row=14, column=0, sticky=W)
        d15 = Checkbutton(self, text="Chicken and gourd with preserved lime soup", font=('Couriernew', 15),
                          bg='skyblue', variable=self.var38).grid(row=15, column=0, sticky=W)
        d16 = Checkbutton(self, text="Fried chicken", font=('Couriernew', 15), bg='skyblue', variable=self.var39).grid(
            row=1, column=1, sticky=W)
        d17 = Checkbutton(self, text="Grilled chicken", font=('Couriernew', 15), bg='skyblue',
                          variable=self.var40).grid(row=2, column=1, sticky=W)
        d18 = Checkbutton(self, text="Omelet", font=('Couriernew', 15), bg='skyblue', variable=self.var41).grid(row=3,
                                                                                                                column=1,
                                                                                                                sticky=W)
        d19 = Checkbutton(self, text="Fried egg", font=('Couriernew', 15), bg='skyblue', variable=self.var42).grid(
            row=4, column=1, sticky=W)
        d20 = Checkbutton(self, text="Boiled egg", font=('Couriernew', 15), bg='skyblue', variable=self.var43).grid(
            row=5, column=1, sticky=W)
        d21 = Checkbutton(self, text="Steamed egg", font=('Couriernew', 15), bg='skyblue', variable=self.var44).grid(
            row=6, column=1, sticky=W)
        d22 = Checkbutton(self, text="Boiled egg in sweet brown sauce", font=('Couriernew', 15), bg='skyblue',
                          variable=self.var45).grid(row=7, column=1, sticky=W)
        d23 = Checkbutton(self, text="Stir-fried kale with crispy pork", font=('Couriernew', 15), bg='skyblue',
                          variable=self.var46).grid(row=8, column=1, sticky=W)
        d24 = Checkbutton(self, text="Pork blood soup", font=('Couriernew', 15), bg='skyblue',
                          variable=self.var47).grid(row=9, column=1, sticky=W)
        d25 = Checkbutton(self, text="River prawn spicy soup", font=('Couriernew', 15), bg='skyblue',
                          variable=self.var48).grid(row=10, column=1, sticky=W)
        d26 = Checkbutton(self, text="Spicy chicken soup", font=('Couriernew', 15), bg='skyblue',
                          variable=self.var49).grid(row=11, column=1, sticky=W)
        d27 = Checkbutton(self, text="Hot and sour snapper filet", font=('Couriernew', 15), bg='skyblue',
                          variable=self.var50).grid(row=12, column=1, sticky=W)
        d28 = Checkbutton(self, text="Fresh mushroom soup", font=('Couriernew', 15), bg='skyblue',
                          variable=self.var51).grid(row=13, column=1, sticky=W)
        d29 = Checkbutton(self, text="Deep fried shrimp cake", font=('Couriernew', 15), bg='skyblue',
                          variable=self.var52).grid(row=14, column=1, sticky=W)
        choose3 = Button(self, text="enter", command=self.enter, font=('Couriernew', 16), relief="solid").place(x=850,
                                                                                                                y=450)

    def enter(self):
        cd1 = self.var24.get()
        cd2 = self.var25.get()
        cd3 = self.var26.get()
        cd4 = self.var27.get()
        cd5 = self.var28.get()
        cd6 = self.var29.get()
        cd7 = self.var30.get()
        cd8 = self.var31.get()
        cd9 = self.var32.get()
        cd10 = self.var33.get()
        cd11 = self.var34.get()
        cd12 = self.var35.get()
        cd13 = self.var36.get()
        cd14 = self.var37.get()
        cd15 = self.var38.get()
        cd16 = self.var39.get()
        cd17 = self.var40.get()
        cd18 = self.var41.get()
        cd19 = self.var42.get()
        cd20 = self.var43.get()
        cd21 = self.var44.get()
        cd22 = self.var45.get()
        cd23 = self.var46.get()
        cd24 = self.var47.get()
        cd25 = self.var48.get()
        cd26 = self.var49.get()
        cd27 = self.var50.get()
        cd28 = self.var51.get()
        cd29 = self.var52.get()
        total3 = (cd1 * 235) + (cd2 * 308) + (cd3 * 300) + (cd4 * 325) + (cd5 * 240) + (cd6 * 90) + (cd7 * 90) + (
                    cd8 * 85) + (cd9 * 235) + (cd10 * 240)
        total4 = (cd11 * 325) + (cd12 * 48) + (cd13 * 120) + (cd14 * 300) + (cd15 * 110) + (cd16 * 345) + (
                    cd17 * 165) + (cd18 * 215) + (cd19 * 215) + (cd20 * 73)
        total5 = (cd21 * 75) + (cd22 * 180) + (cd23 * 420) + (cd24 * 120) + (cd25 * 65) + (cd26 * 60) + (cd27 * 80) + (
                    cd28 * 30) + (cd29 * 255)
        global totalcd
        totalcd = total4 + total5 + total3
        print(totalcd)
        messagebox.showinfo("select", "FINISH!!!")


class Snack(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='skyblue')
        self.controller = controller
        label = Label(self, text="Snack")

        # back button
        button = Button(self, text="Go to the menu page", font=('Couriernew', 16), relief="solid",
                        command=lambda: controller.show_frame("StartPage")).place(x=10, y=270)
        # button.grid(row=13,column=0,sticky=W)

        image = Image.open('snack4.jpg')
        tkimage = ImageTk.PhotoImage(image)
        x1 = Label(self, image=tkimage)
        x1.image = tkimage
        x1.place(x=700, y=290)

        image = Image.open('snack3.jpg')
        tkimage = ImageTk.PhotoImage(image)
        x2 = Label(self, image=tkimage)
        x2.image = tkimage
        x2.place(x=700, y=70)

        image = Image.open('snack2.jpg')
        tkimage = ImageTk.PhotoImage(image)
        x3 = Label(self, image=tkimage)
        x3.image = tkimage
        x3.place(x=350, y=290)

        image = Image.open('snack1.jpg')
        tkimage = ImageTk.PhotoImage(image)
        x4 = Label(self, image=tkimage)
        x4.image = tkimage
        x4.place(x=350, y=70)

        self.var74 = IntVar()
        self.var75 = IntVar()
        self.var76 = IntVar()
        self.var77 = IntVar()
        self.var78 = IntVar()
        self.var79 = IntVar()

        Label(self, text="SNACK", bg='skyblue', fg='navy', font=('Couriernew', 20)).grid(row=0, column=0, sticky=W)
        s1 = Checkbutton(self, text="Pork dumpling (dim sum)", font=('Couriernew', 15), bg='skyblue',
                         variable=self.var74).grid(row=1, column=0, sticky=W)
        s2 = Checkbutton(self, text="Thai steamed rice-skin dumplings", font=('Couriernew', 15), bg='skyblue',
                         variable=self.var75).grid(row=2, column=0, sticky=W)
        s3 = Checkbutton(self, text="Croissant", font=('Couriernew', 15), bg='skyblue', variable=self.var76).grid(row=3,
                                                                                                                  column=0,
                                                                                                                  sticky=W)
        s4 = Checkbutton(self, text="Potato plate", font=('Couriernew', 15), bg='skyblue', variable=self.var77).grid(
            row=4, column=0, sticky=W)
        s5 = Checkbutton(self, text="Meat ball barbecue", font=('Couriernew', 15), bg='skyblue',
                         variable=self.var78).grid(row=5, column=0, sticky=W)
        s6 = Checkbutton(self, text="Crispy wonton", font=('Couriernew', 15), bg='skyblue', variable=self.var79).grid(
            row=6, column=0, sticky=W)
        choose4 = Button(self, text="enter", font=('Couriernew', 16), relief="solid", command=self.enter).place(x=10,
                                                                                                                y=320)

    def enter(self):
        cs1 = self.var74.get()
        cs2 = self.var75.get()
        cs3 = self.var76.get()
        cs4 = self.var77.get()
        cs5 = self.var78.get()
        cs6 = self.var79.get()
        global totals
        totals = (cs1 * 32) + (cs2 * 26) + (cs3 * 235) + (cs4 * 13) + (cs5 * 165) + (cs6 * 78)
        print(totals)
        messagebox.showinfo("select", "FINISH!!!")


class Rice(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='skyblue')
        self.controller = controller
        label = Label(self, text="Rice")

        # back button
        button = Button(self, text="Go to the menu page", font=('Couriernew', 16), relief="solid",
                        command=lambda: controller.show_frame("StartPage")).place(x=10, y=120)
        # button.grid(row=13,column=0,sticky=W)

        image = Image.open('rice2.jpg')
        tkimage = ImageTk.PhotoImage(image)
        x1 = Label(self, image=tkimage)
        x1.image = tkimage
        x1.place(x=640, y=250)

        image = Image.open('rice1.jpg')
        tkimage = ImageTk.PhotoImage(image)
        x2 = Label(self, image=tkimage)
        x2.image = tkimage
        x2.place(x=350, y=10)

        self.var80 = IntVar()
        self.var81 = IntVar()
        Label(self, text="RICE", bg='skyblue', fg='navy', font=('Couriernew', 20)).grid(row=0, column=0, sticky=W)
        s1 = Checkbutton(self, text="Steamed rice", font=('Couriernew', 15), bg='skyblue', variable=self.var80).grid(
            row=1, column=0, sticky=W)
        s2 = Checkbutton(self, text="Steamed brown rice", font=('Couriernew', 15), bg='skyblue',
                         variable=self.var81).grid(row=2, column=0, sticky=W)
        choose5 = Button(self, text="enter", command=self.enter, font=('Couriernew', 16), relief="solid").place(x=10,
                                                                                                                y=170)

    def enter(self):
        cr1 = self.var80.get()
        cr2 = self.var81.get()
        global totalr
        totalr = (cr1 * 68) + (cr2 * 80)
        print(totalr)
        messagebox.showinfo("select", "FINISH!!!")


class Dessert(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='skyblue')
        self.controller = controller
        label = Label(self, text="Dessert", bg='skyblue')
        button = Button(self, text="Go to the menu page", font=('Couriernew', 16), relief="solid",
                        command=lambda: controller.show_frame("StartPage")).place(x=350, y=470)

        image = Image.open('des1.jpg')
        tkimage = ImageTk.PhotoImage(image)
        x1 = Label(self, image=tkimage)
        x1.image = tkimage
        x1.place(x=650, y=300)

        image = Image.open('des2.jpg')
        tkimage = ImageTk.PhotoImage(image)
        x2 = Label(self, image=tkimage)
        x2.image = tkimage
        x2.place(x=650, y=50)

        self.var82 = IntVar()
        self.var83 = IntVar()
        self.var84 = IntVar()
        self.var85 = IntVar()
        self.var86 = IntVar()
        self.var87 = IntVar()
        self.var88 = IntVar()
        self.var89 = IntVar()
        self.var90 = IntVar()
        self.var91 = IntVar()
        self.var92 = IntVar()
        self.var93 = IntVar()
        self.var94 = IntVar()
        self.var95 = IntVar()
        self.var96 = IntVar()
        self.var97 = IntVar()
        self.var98 = IntVar()
        self.var99 = IntVar()
        self.var100 = IntVar()
        self.var101 = IntVar()
        self.var102 = IntVar()
        self.var103 = IntVar()
        self.var104 = IntVar()
        self.var105 = IntVar()
        self.var106 = IntVar()
        self.var107 = IntVar()

        Label(self, text="DESSERT", bg='skyblue', fg='navy', font=('Couriernew', 20)).grid(row=0, column=0, sticky=W)
        de1 = Checkbutton(self, text="Steamed chives dumplings", font=('Couriernew', 15), bg='skyblue',
                          variable=self.var82).grid(row=1, column=0, sticky=W)
        de2 = Checkbutton(self, text="Mock Pomegranate in Coconut Syrup", font=('Couriernew', 15), bg='skyblue',
                          variable=self.var83).grid(row=2, column=0, sticky=W)
        de3 = Checkbutton(self, text="Sweet potatoes in heavy syrup", font=('Couriernew', 15), bg='skyblue',
                          variable=self.var84).grid(row=3, column=0, sticky=W)
        de4 = Checkbutton(self, text="Potato in coconut milk", font=('Couriernew', 15), bg='skyblue',
                          variable=self.var85).grid(row=4, column=0, sticky=W)
        de5 = Checkbutton(self, text="Palm fruit with syrup", font=('Couriernew', 15), bg='skyblue',
                          variable=self.var86).grid(row=5, column=0, sticky=W)
        de6 = Checkbutton(self, text="Coconut jelly", font=('Couriernew', 15), bg='skyblue', variable=self.var87).grid(
            row=6, column=0, sticky=W)
        de7 = Checkbutton(self, text="Steamed custard", font=('Couriernew', 15), bg='skyblue',
                          variable=self.var88).grid(row=7, column=0, sticky=W)
        de8 = Checkbutton(self, text="Pumpkin custard", font=('Couriernew', 15), bg='skyblue',
                          variable=self.var89).grid(row=8, column=0, sticky=W)
        de9 = Checkbutton(self, text="Taro custard", font=('Couriernew', 15), bg='skyblue', variable=self.var90).grid(
            row=9, column=0, sticky=W)
        de10 = Checkbutton(self, text="Banana cake", font=('Couriernew', 15), bg='skyblue', variable=self.var91).grid(
            row=10, column=0, sticky=W)
        de11 = Checkbutton(self, text="Chocolate cake", font=('Couriernew', 15), bg='skyblue',
                           variable=self.var92).grid(row=11, column=0, sticky=W)
        de12 = Checkbutton(self, text="Pandan cake", font=('Couriernew', 15), bg='skyblue', variable=self.var93).grid(
            row=12, column=0, sticky=W)
        de13 = Checkbutton(self, text="Ham-and-cheese sandwich", font=('Couriernew', 15), bg='skyblue',
                           variable=self.var94).grid(row=13, column=0, sticky=W)
        de14 = Checkbutton(self, text="Tuna sandwich", font=('Couriernew', 15), bg='skyblue', variable=self.var95).grid(
            row=14, column=0, sticky=W)
        de15 = Checkbutton(self, text="Chicken sandwich", font=('Couriernew', 15), bg='skyblue',
                           variable=self.var96).grid(row=1, column=1, sticky=W)
        de16 = Checkbutton(self, text="Ham rolls", font=('Couriernew', 15), bg='skyblue', variable=self.var97).grid(
            row=2, column=1, sticky=W)
        de17 = Checkbutton(self, text="Chicken with cheese burger", font=('Couriernew', 15), bg='skyblue',
                           variable=self.var98).grid(row=3, column=1, sticky=W)
        de18 = Checkbutton(self, text="Pork burger", font=('Couriernew', 15), bg='skyblue', variable=self.var99).grid(
            row=4, column=1, sticky=W)
        de19 = Checkbutton(self, text="Donut", font=('Couriernew', 15), bg='skyblue', variable=self.var100).grid(row=5,
                                                                                                                 column=1,
                                                                                                                 sticky=W)
        de20 = Checkbutton(self, text="Rosette", font=('Couriernew', 15), bg='skyblue', variable=self.var101).grid(
            row=6, column=1, sticky=W)
        de21 = Checkbutton(self, text="Coconut ice cream", font=('Couriernew', 15), bg='skyblue',
                           variable=self.var102).grid(row=7, column=1, sticky=W)
        de22 = Checkbutton(self, text="Coffee ice cream", font=('Couriernew', 15), bg='skyblue',
                           variable=self.var103).grid(row=8, column=1, sticky=W)
        de23 = Checkbutton(self, text="Chocolate ice cream", font=('Couriernew', 15), bg='skyblue',
                           variable=self.var104).grid(row=9, column=1, sticky=W)
        de24 = Checkbutton(self, text="Vanilla ice cream", font=('Couriernew', 15), bg='skyblue',
                           variable=self.var105).grid(row=10, column=1, sticky=W)
        de25 = Checkbutton(self, text="Strawberry ice cream", font=('Couriernew', 15), bg='skyblue',
                           variable=self.var106).grid(row=11, column=1, sticky=W)
        de26 = Checkbutton(self, text="Rum Raisin ice cream", font=('Couriernew', 15), bg='skyblue',
                           variable=self.var107).grid(row=12, column=1, sticky=W)

        choose6 = Button(self, text="enter", font=('Couriernew', 16), relief="solid", command=self.enter).place(x=350,
                                                                                                                y=520)

    def enter(self):
        cde1 = self.var82.get()
        cde2 = self.var83.get()
        cde3 = self.var84.get()
        cde4 = self.var85.get()
        cde5 = self.var86.get()
        cde6 = self.var87.get()
        cde7 = self.var88.get()
        cde8 = self.var89.get()
        cde9 = self.var90.get()
        cde10 = self.var91.get()
        cde11 = self.var92.get()
        cde12 = self.var93.get()
        cde13 = self.var94.get()
        cde14 = self.var95.get()
        cde15 = self.var96.get()
        cde16 = self.var97.get()
        cde17 = self.var98.get()
        cde18 = self.var99.get()
        cde19 = self.var100.get()
        cde20 = self.var101.get()
        cde21 = self.var102.get()
        cde22 = self.var103.get()
        cde23 = self.var104.get()
        cde24 = self.var105.get()
        cde25 = self.var106.get()
        cde26 = self.var107.get()
        total11 = (cde1 * 53) + (cde2 * 250) + (cde3 * 230) + (cde4 * 184) + (cde5 * 180) + (cde6 * 80) + (
                cde7 * 204) + (cde8 * 288) + (cde9 * 222) + (cde10 * 370)
        total12 = (cde11 * 275) + (cde12 * 250) + (cde13 * 290) + (cde14 * 180) + (cde15 * 240) + (cde16 * 310) + (
                cde17 * 280) + (cde18 * 245) + (cde19 * 270) + (cde20 * 145)
        total13 = (cde21 * 108) + (cde22 * 142) + (cde23 * 110) + (cde24 * 140) + (cde25 * 110) + (cde26 * 264)
        global totalcde
        totalcde = total11 + total12 + total13
        print(totalcde)
        messagebox.showinfo("select", "FINISH!!!")


class Onedish(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='skyblue')
        self.controller = controller
        label = Label(self, text="Onedish")
        button = Button(self, text="Go to the menu page", font=('Couriernew', 16), relief="solid",
                        command=lambda: controller.show_frame("StartPage")).place(x=10, y=440)

        image = Image.open('onedish.jpg')
        tkimage = ImageTk.PhotoImage(image)
        x1 = Label(self, image=tkimage)
        x1.image = tkimage
        x1.place(x=650, y=390)

        self.var108 = IntVar()
        self.var109 = IntVar()
        self.var110 = IntVar()
        self.var111 = IntVar()
        self.var112 = IntVar()
        self.var113 = IntVar()
        self.var114 = IntVar()
        self.var115 = IntVar()
        self.var116 = IntVar()
        self.var117 = IntVar()
        self.var118 = IntVar()
        self.var119 = IntVar()
        self.var120 = IntVar()
        self.var121 = IntVar()
        self.var122 = IntVar()
        self.var123 = IntVar()
        self.var124 = IntVar()
        self.var125 = IntVar()
        self.var126 = IntVar()
        self.var127 = IntVar()
        self.var128 = IntVar()
        self.var129 = IntVar()
        self.var130 = IntVar()
        self.var131 = IntVar()
        self.var132 = IntVar()
        self.var133 = IntVar()
        self.var134 = IntVar()
        self.var135 = IntVar()
        self.var136 = IntVar()
        self.var137 = IntVar()
        self.var138 = IntVar()
        self.var139 = IntVar()
        self.var140 = IntVar()
        self.var141 = IntVar()
        self.var142 = IntVar()
        self.var143 = IntVar()
        self.var144 = IntVar()
        self.var145 = IntVar()
        self.var146 = IntVar()
        self.var147 = IntVar()
        self.var148 = IntVar()
        self.var149 = IntVar()

        Label(self, text="ONE-DISH", bg='skyblue', fg='navy', font=('Couriernew', 20)).grid(row=0, column=1, sticky=W)
        od1 = Checkbutton(self, text="Stir fried flat noodle, egg and pork with preserved soy bean paste",
                          font=('Couriernew', 15), bg='skyblue', variable=self.var108).grid(row=1, column=1, sticky=W)
        od2 = Checkbutton(self, text="Stir fried rice noodle with prawn", font=('Couriernew', 15), bg='skyblue',
                          variable=self.var109).grid(row=2, column=1, sticky=W)
        od3 = Checkbutton(self, text="Crispy noodle with pork", font=('Couriernew', 15), bg='skyblue',
                          variable=self.var110).grid(row=3, column=1, sticky=W)
        od4 = Checkbutton(self, text="Meat ball with clear water soup", font=('Couriernew', 15), bg='skyblue',
                          variable=self.var111).grid(row=4, column=1, sticky=W)
        od5 = Checkbutton(self, text="Wonton soup with shrimp", font=('Couriernew', 15), bg='skyblue',
                          variable=self.var112).grid(row=5, column=1, sticky=W)
        od6 = Checkbutton(self, text="Wonton soup with fish", font=('Couriernew', 15), bg='skyblue',
                          variable=self.var113).grid(row=6, column=1, sticky=W)
        od7 = Checkbutton(self, text="Crispy noodle in thick gravy", font=('Couriernew', 15), bg='skyblue',
                          variable=self.var114).grid(row=7, column=1, sticky=W)
        od8 = Checkbutton(self, text="Rice noodles with chicken green curry", font=('Couriernew', 15), bg='skyblue',
                          variable=self.var115).grid(row=8, column=1, sticky=W)
        od9 = Checkbutton(self, text="Thai rice noodle with pineapple and coconut milk", font=('Couriernew', 15),
                          bg='skyblue', variable=self.var116).grid(row=9, column=1, sticky=W)
        od10 = Checkbutton(self, text="Rice noodles with spicy pork sauce", font=('Couriernew', 15), bg='skyblue',
                           variable=self.var117).grid(row=10, column=1, sticky=W)
        od11 = Checkbutton(self, text="Thai rice noodle with peanut sauce", font=('Couriernew', 15), bg='skyblue',
                           variable=self.var118).grid(row=11, column=1, sticky=W)
        od12 = Checkbutton(self, text="Thai rice noodle with fish curry sauce", font=('Couriernew', 15), bg='skyblue',
                           variable=self.var119).grid(row=1, column=2, sticky=W)
        od13 = Checkbutton(self, text="Rice topped with stir-fried beef and basil", font=('Couriernew', 15),
                           bg='skyblue', variable=self.var120).grid(row=2, column=2, sticky=W)
        od14 = Checkbutton(self, text="Rice topped with shrimp and garlic pepper", font=('Couriernew', 15),
                           bg='skyblue', variable=self.var121).grid(row=3, column=2, sticky=W)
        od15 = Checkbutton(self, text="Rice with yellow chicken curry", font=('Couriernew', 15), bg='skyblue',
                           variable=self.var122).grid(row=4, column=2, sticky=W)
        od16 = Checkbutton(self, text="Rice topped with stewed pork leg", font=('Couriernew', 15), bg='skyblue',
                           variable=self.var123).grid(row=5, column=2, sticky=W)
        od17 = Checkbutton(self, text="Rice mixed with shrimp plate", font=('Couriernew', 15), bg='skyblue',
                           variable=self.var124).grid(row=6, column=2, sticky=W)
        od18 = Checkbutton(self, text="Northern style curried noodle soup with chicken", font=('Couriernew', 15),
                           bg='skyblue', variable=self.var125).grid(row=7, column=2, sticky=W)
        od19 = Checkbutton(self, text="Northern style curried noodle soup with pork", font=('Couriernew', 15),
                           bg='skyblue', variable=self.var126).grid(row=8, column=2, sticky=W)
        od20 = Checkbutton(self, text="Rice topped with stir-fried chicken and basil", font=('Couriernew', 15),
                           bg='skyblue', variable=self.var127).grid(row=9, column=2, sticky=W)
        od21 = Checkbutton(self, text="Rice topped with stir-fried shrimp and basil", font=('Couriernew', 15),
                           bg='skyblue', variable=self.var128).grid(row=10, column=2, sticky=W)

        choose7 = Button(self, text="enter", font=('Couriernew', 16), relief="solid", command=self.enter).place(x=10,
                                                                                                                y=490)

    def enter(self):
        co1 = self.var108.get()
        co2 = self.var109.get()
        co3 = self.var110.get()
        co4 = self.var111.get()
        co5 = self.var112.get()
        co6 = self.var113.get()
        co7 = self.var114.get()
        co8 = self.var115.get()
        co9 = self.var116.get()
        co10 = self.var117.get()
        co11 = self.var118.get()
        co12 = self.var119.get()
        co13 = self.var120.get()
        co14 = self.var121.get()
        co15 = self.var122.get()
        co16 = self.var123.get()
        co17 = self.var124.get()
        co18 = self.var125.get()
        co19 = self.var126.get()
        co20 = self.var127.get()
        co21 = self.var128.get()
        total7 = (co1 * 679) + (co2 * 486) + (co3 * 690) + (co4 * 225) + (co5 * 275) + (co6 * 165) + (co7 * 550) + (
                co8 * 594) + (co9 * 320) + (co10 * 243)
        total8 = (co11 * 228) + (co12 * 332) + (co13 * 622) + (co14 * 495) + (co15 * 389) + (co16 * 690) + (
                co17 * 410) + (co18 * 395) + (co19 * 395) + (co20 * 540) + (co21 * 554)
        global totalco
        totalco = total7 + total8
        print(totalco)
        messagebox.showinfo("select", "FINISH!!!")


best = Food()
best.mainloop()
