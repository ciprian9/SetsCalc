"""
# Program Name :  Gui Lesson 1          
# Created by Ciprian Anton        
# Date:  21/11/16                       
# OS : Win 10
# V 1.0
"""

import itertools

from tkinter import *
import tkinter.messagebox
a = 1
class Calculator(object):

    def __init__(self, setA=set(), setB=set(), setC=set()):

        self.setA = setA
        self.setB = setB
        self.setC = setC
        self.calc = ''
        self.answer = set()
        self.cartp = set()

        """Creating the window and configuring the main parts. This is only the
               Graphical User Interface that contains no functions yet"""
        self.root = Tk()
        self.root.geometry('470x620')
        menu = Menu(self.root)
        self.root.resizable(0, 0)  # remove the maximise button
        self.root.config(menu=menu, bg='light blue')
        self.root.title('Set Calculator')
        """Create the submenu in order to deploy reset options"""

        submenu = Menu(menu)
        menu.add_cascade(label='Reset', menu=submenu)
        submenu.add_command(label='Restart', command=self.reset)
        submenu.add_command(label='Exit', command=self.exitt)

        """Create frame to set the location of the widgets"""

        entries = Frame(self.root, height=600, width=400, bg='light green')
        entries.pack()

        """Create the labels and entries for the sets and screen. The labels and entries are used
        for the main part of the input by the users."""

        self.screen = Entry(entries, width=73, relief=SUNKEN, bg='light blue')
        self.screen1 = Entry(entries, width=73, relief=SUNKEN, bg='light blue')
        self.screen.grid(row=0, columnspan=4, sticky=NW, ipady=10, padx=15)
        self.screen1.grid(row=1, columnspan=4, sticky=NW, ipady=10, padx=15)

        set_A = Label(entries, text='SET_A', font="Times 12 bold", bg='light green')
        set_B = Label(entries, text='SET_B', font="Times 12 bold", bg='light green')
        set_C = Label(entries, text='SET_C', font="Times 12 bold", bg='light green')

        set_A.grid(row=2, column=0, sticky=W)
        set_B.grid(row=3, column=0, sticky=W)
        set_C.grid(row=4, column=0, sticky=W)

        self.enter_ = Label(entries, bg='light green')
        self.enter_1 = Label(entries, bg='light green')
        self.enter_2 = Label(entries, bg='light green')

        self.enter_.grid(row=2, column=1, sticky=E, pady=4)
        self.enter_1.grid(row=3, column=1, sticky=E, pady=4)
        self.enter_2.grid(row=4, column=1, sticky=E, pady=4)

        self.enter = Entry(entries, width=60, bg='light blue')
        self.enter.grid(row=2, column=1, sticky=E, pady=4)
        self.enter1 = Entry(entries, width=60, bg='light blue')
        self.enter1.grid(row=3, column=1, sticky=E, pady=4)
        self.enter2 = Entry(entries, width=60, bg='light blue')
        self.enter2.grid(row=4, column=1, sticky=E, pady=4)

        """Acceptance of the sets by pressing the button"""

        self.letgo = Button(entries, text="Read in sets", command=self.readset)
        self.letgo.grid(row=5, column=1, sticky=E)

        """Divider to set out a better layout"""

        divider = Label(entries, text='Enter set elements divided by commas', relief=SUNKEN, font='Times 12 italic',
                        bg='light green')

        divider1 = Label(entries, text='One operation at a time', relief=SUNKEN, font='Times 12 italic',
                         bg='light green')
        divider.grid(row=6, columnspan=4, ipadx=112)
        divider1.grid(row=7, columnspan=5, ipadx=112)

        """Create secondary frame for buttons"""

        butt = Frame(self.root, width=400, height=600, bg='light blue')
        butt.pack(side=TOP)

        """Create buttons for the calculator"""

        self.rbrack = Button(butt, text=') ', bd=5, width=9, height=3, command=lambda: self.display(3),
                             bg='light green')
        self.lbrack = Button(butt, text='(', bd=5, width=9, height=3, command=lambda: self.display(0),
                             bg='light green')
        self.A_button = Button(butt, text='A_set', bd=5, width=9, height=3, command=lambda: self.display(1),
                               bg='light green', state=DISABLED)
        self.B_button = Button(butt, text='B_set', bd=5, width=9, height=3, command=lambda: self.display(2),
                               bg='light green', state=DISABLED)
        self.C_button = Button(butt, text='C_set', bd=5, width=9, height=3, command=lambda: self.display(28),
                               bg='light green', state=DISABLED)

        self.lbrack.grid(row=1, column=0, sticky=W)
        self.rbrack.grid(row=1, column=1, sticky=W)
        self.A_button.grid(row=0, column=1, sticky=W)
        self.B_button.grid(row=0, column=2, sticky=W)
        self.C_button.grid(row=0, column=3, sticky=W)

        self.subs = Button(butt, text='Subset', bd=4, width=12, height=3, command=lambda: self.display(4),
                           bg='light green', state=DISABLED)
        self.subs.grid(row=0, column=4, padx=1)

        self.uni = Button(butt, text='Union', bd=4, width=12, height=3, command=lambda: self.display(5),
                          bg='light green', state=DISABLED)
        self.uni.grid(row=1, column=4, padx=1)

        self.inter = Button(butt, text='Intersect', bd=4, width=12, height=3, command=lambda: self.display(6),
                            bg='light green', state=DISABLED)
        self.inter.grid(row=2, column=4, padx=1)

        self.compl = Button(butt, text='Complement', bd=4, width=12, height=3, command=lambda: self.display(8),
                            bg='light green', state=DISABLED)
        self.compl.grid(row=3, column=4, padx=1)

        self.diff = Button(butt, text='Difference', bd=4, width=12, height=3, command=lambda: self.display(7),
                           bg='light green', state=DISABLED)
        self.diff.grid(row=4, column=4, padx=1)

        self.cart = Button(butt, text='Cartisian Product', bd=4, width=12, height=3, command=lambda: self.display(9),
                           bg='light green', state=DISABLED)
        self.cart.grid(row=5, column=4, padx=1)

        num0 = Button(butt, text='0', bd=4, width=9, height=3, command=lambda: self.display(10), bg='light green')
        numdot = Button(butt, text='.', bd=4, width=9, height=3, command=lambda: self.display(11), bg='light green')
        numequal = Button(butt, text='=', bd=4, width=20, height=3, command=lambda: self.display(27), bg='light green')
        num0.grid(row=5, column=0, padx=0, sticky=W)
        numdot.grid(row=5, column=1, padx=0)
        numequal.grid(row=5, columnspan=2, column=2, padx=0, sticky=W)

        num1 = Button(butt, text='1', width=9, height=3, bd=4, command=lambda: self.display(12), bg='light green')
        num2 = Button(butt, text='2', width=9, height=3, bd=4, command=lambda: self.display(13), bg='light green')
        num3 = Button(butt, text='3', width=9, height=3, bd=4, command=lambda: self.display(14), bg='light green')
        num4 = Button(butt, text='4', width=9, height=3, bd=4, command=lambda: self.display(15), bg='light green')
        num5 = Button(butt, text='5', width=9, height=3, bd=4, command=lambda: self.display(16), bg='light green')
        num6 = Button(butt, text='6', width=9, height=3, bd=4, command=lambda: self.display(17), bg='light green')
        num7 = Button(butt, text='7', width=9, height=3, bd=4, command=lambda: self.display(18), bg='light green')
        num8 = Button(butt, text='8', width=9, height=3, bd=4, command=lambda: self.display(19), bg='light green')
        num9 = Button(butt, text='9', width=9, height=3, bd=4, command=lambda: self.display(20), bg='light green')
        numplus = Button(butt, text='+', width=9, height=3, bd=4, command=lambda: self.display(21), bg='light green')
        nummin = Button(butt, text='-', width=9, height=3, bd=4, command=lambda: self.display(22), bg='light green')
        nummul = Button(butt, text='*', width=9, height=3, bd=4, command=lambda: self.display(23), bg='light green')
        numdiv = Button(butt, text='/', width=9, height=3, bd=4, command=lambda: self.display(24), bg='light green')
        numrem = Button(butt, text='%', width=9, height=3, bd=4, command=lambda: self.display(25), bg='light green')
        clear = Button(butt, text='C', width=9, height=3, bd=4, command=lambda: self.display(26), bg='light green')

        num1.grid(row=4, column=0)
        num2.grid(row=4, column=1)
        num3.grid(row=4, column=2)
        numplus.grid(row=4, column=3)

        num4.grid(row=3, column=0)
        num5.grid(row=3, column=1)
        num6.grid(row=3, column=2)
        nummin.grid(row=3, column=3)

        num7.grid(row=2, column=0)
        num8.grid(row=2, column=1)
        num9.grid(row=2, column=2)
        nummul.grid(row=2, column=3)

        clear.grid(row=0, column=0)
        numdiv.grid(row=1, column=2)
        numrem.grid(row=1, column=3)

        self.root.protocol("WM_DELETE_WINDOW", self.exitt)

        self.root.mainloop()

    def readset(self):
        """
        This function reads the entries for the sets and takes the input from the user and turns it into real sets.
        Further it solidifies the fields so they can not be changed before a reset.
        :return:
        """

        self.setA = self.enter.get()
        self.setA = self.setA.split(',')
        self.setA = list(self.setA)

        for i in self.setA:
            if i == "":
                self.setA.pop()


        self.setA = set(self.setA)

        self.setB = self.enter1.get()
        self.setB = self.setB.split(',')
        self.setB = list(self.setB)

        for i in self.setB:
            if i == "":
                self.setB.pop()

        self.setB = set(self.setB)

        self.setC = self.enter2.get()
        self.setC = self.setC.split(',')
        self.setC = list(self.setC)

        for i in self.setC:
            if i == "":
                self.setC.pop()

        self.setC = set(self.setC)

        self.enter.destroy()
        self.enter1.destroy()
        self.enter2.destroy()

        self.enter_.configure(text=self.setA, font="Times 12 bold")
        self.enter_1.configure(text=self.setB, font="Times 12 bold")
        self.enter_2.configure(text=self.setC, font="Times 12 bold")

        self.A_button.configure(state=NORMAL)
        self.B_button.configure(state=NORMAL)
        self.C_button.configure(state=NORMAL)
        self.subs.configure(state=NORMAL)
        self.uni.configure(state=NORMAL)
        self.compl.configure(state=NORMAL)
        self.diff.configure(state=NORMAL)
        self.cart.configure(state=NORMAL)
        self.letgo.configure(state=DISABLED)
        self.inter.configure(state=NORMAL)

    def display(self, seti):
        if seti == 0:
            self.screen.insert(END, '( ')
        elif seti == 1:
            self.screen.insert(END, 'A_set ')
        elif seti == 2:
            self.screen.insert(END, 'B_set ')
        elif seti == 3:
            self.screen.insert(END, ') ')
        elif seti == 4:
            self.screen.insert(END, '<= ')
        elif seti == 5:
            self.screen.insert(END, '| ')
        elif seti == 6:
            self.screen.insert(END, '& ')
        elif seti == 7:
            self.screen.insert(END, '-- ')
        elif seti == 8:
            self.screen.insert(END, '^ ')
        elif seti == 9:
            self.screen.insert(END, 'x ')
        elif seti == 10:
            self.screen.insert(END, '0')
        elif seti == 11:
            self.screen.insert(END, '.')
        elif seti == 12:
            self.screen.insert(END, '1')
        elif seti == 13:
            self.screen.insert(END, '2')
        elif seti == 14:
            self.screen.insert(END, '3')
        elif seti == 15:
            self.screen.insert(END, '4')
        elif seti == 16:
            self.screen.insert(END, '5')
        elif seti == 17:
            self.screen.insert(END, '6')
        elif seti == 18:
            self.screen.insert(END, '7')
        elif seti == 19:
            self.screen.insert(END, '8')
        elif seti == 20:
            self.screen.insert(END, '9')
        elif seti == 21:
            self.screen.insert(END, ' + ')
        elif seti == 22:
            self.screen.insert(END, ' - ')
        elif seti == 23:
            self.screen.insert(END, ' * ')
        elif seti == 24:
            self.screen.insert(END, ' / ')
        elif seti == 25:
            self.screen.insert(END, ' % ')
        elif seti == 26:
            self.screen.delete(0, END)
            self.screen1.delete(0, END)
        elif seti == 27:
            self.calculate_Set()
        elif seti == 28:
            self.screen.insert(END, 'C_set ')

    def subsets(self, choice):

        if choice == 4:
            ans = self.setA <= self.setB
            if ans:
                self.screen1.insert(END, 'True')
            else:
                self.screen1.insert(END, 'False')

        elif choice == 7:
            ans = self.setB <= self.setA
            if ans:
                self.screen1.insert(END, 'True')
            else:
                self.screen1.insert(END, 'False')
        elif choice == 0:
            ans = self.answer <= self.setA
            if ans:
                self.screen1.insert(END, 'True')
            else:
                self.screen1.insert(END, 'False')
        elif choice == 1:
            ans = self.answer <= self.setB
            if ans:
                self.screen1.insert(END, 'True')
            else:
                self.screen1.insert(END, 'False')
        elif choice == 2:
            ans = self.setC <= self.setA
            if ans:
                self.screen1.insert(END, 'True')
            else:
                self.screen1.insert(END, 'False')
        elif choice == 3:
            ans = self.setC <= self.setB
            if ans:
                self.screen1.insert(END, 'True')
            else:
                self.screen1.insert(END, 'False')
        elif choice == 5:
            ans = self.answer <= self.setC
            if ans:
                self.screen1.insert(END, 'True')
            else:
                self.screen1.insert(END, 'False')
        elif choice == 6:
            ans = self.setA <= self.setC
            if ans:
                self.screen1.insert(END, 'True')
            else:
                self.screen1.insert(END, 'False')
        elif choice == 8:
            ans = self.setB <= self.setC
            if ans:
                self.screen1.insert(END, 'True')
            else:
                self.screen1.insert(END, 'False')

    def complement(self, choice):

        if choice == 4:
            self.answer = self.setA - self.setB
            self.screen1.insert(END, self.answer)
        elif choice == 7:
            self.answer = self.setB - self.setA
            self.screen1.insert(END, self.answer)
        elif choice == 0:
            self.answer -= self.setA
            self.screen1.insert(END, self.answer)
        elif choice == 1:
            self.answer -= self.setB
            self.screen1.insert(END, self.answer)
        elif choice == 2:
            self.answer = self.setC - self.setA
            self.screen1.insert(END, self.answer)
        elif choice == 3:
            self.answer = self.setC - self.setB
            self.screen1.insert(END, self.answer)
        elif choice == 5:
            self.answer -= self.setC
            self.screen1.insert(END, self.answer)
        elif choice == 6:
            self.answer = self.setA - self.setC
            self.screen1.insert(END, self.answer)
        elif choice == 8:
            self.answer = self.setB - self.setC
            self.screen1.insert(END, self.answer)

    def difference(self, choice):

        if choice == 4:
            self.answer = self.setA ^ self.setB
            self.screen1.insert(END, self.answer)
        elif choice == 7:
            self.answer = self.setB ^ self.setA
            self.screen1.insert(END, self.answer)
        elif choice == 0:
            self.answer ^= self.setA
            self.screen1.insert(END, self.answer)
        elif choice == 1:
            self.answer ^= self.setB
            self.screen1.insert(END, self.answer)
        elif choice == 2:
            self.answer = self.setC ^ self.setA
            self.screen1.insert(END, self.answer)
        elif choice == 3:
            self.answer = self.setC ^ self.setB
            self.screen1.insert(END, self.answer)
        elif choice == 5:
            self.answer ^= self.setC
            self.screen1.insert(END, self.answer)
        elif choice == 6:
            self.answer = self.setA ^ self.setC
            self.screen1.insert(END, self.answer)
        elif choice == 8:
            self.answer = self.setB ^ self.setC
            self.screen1.insert(END, self.answer)

    def union(self, choice):
        if choice == 4:
            self.answer = self.setA | self.setB
            self.screen1.insert(END, self.answer)
        elif choice == 7:
            self.answer = self.setB | self.setA
            self.screen1.insert(END, self.answer)
        elif choice == 0:
            self.answer |= self.setA
            self.screen1.insert(END, self.answer)
        elif choice == 1:
            self.answer |= self.setB
            self.screen1.insert(END, self.answer)
        elif choice == 2:
            self.answer = self.setC | self.setA
            self.screen1.insert(END, self.answer)
        elif choice == 3:
            self.answer = self.setC | self.setB
            self.screen1.insert(END, self.answer)
        elif choice == 5:
            self.answer |= self.setC
            self.screen1.insert(END, self.answer)
        elif choice == 6:
            self.answer = self.setA | self.setC
            self.screen1.insert(END, self.answer)
        elif choice == 8:
            self.answer = self.setB | self.setC
            self.screen1.insert(END, self.answer)

    def inters(self, choice):

        if choice == 4:
            self.answer = self.setA & self.setB
            self.screen1.insert(END, self.answer)
        elif choice == 7:
            self.answer = self.setB & self.setA
            self.screen1.insert(END, self.answer)
        elif choice == 0:
            self.answer &= self.setA
            self.screen1.insert(END, self.answer)
        elif choice == 1:
            self.answer &= self.setB
            self.screen1.insert(END, self.answer)
        elif choice == 2:
            self.answer = self.setC & self.setA
            self.screen1.insert(END, self.answer)
        elif choice == 3:
            self.answer = self.setC & self.setB
            self.screen1.insert(END, self.answer)
        elif choice == 5:
            self.answer &= self.setC
            self.screen1.insert(END, self.answer)
        elif choice == 6:
            self.answer = self.setA & self.setC
            self.screen1.insert(END, self.answer)
        elif choice == 8:
            self.answer = self.setB & self.setC
            self.screen1.insert(END, self.answer)

    def cartesian_product(self, choice):

        if choice == 4:
            for i in itertools.product(self.setA, self.setB):
                print(i)
                self.answer.add(i)
            self.screen1.insert(END, self.answer)
        elif choice == 7:
            for i in itertools.product(self.setB, self.setA):
                print(i)
                self.answer.add(i)
            self.screen1.insert(END, self.answer)
        elif choice == 0:
            for i in itertools.product(self.answer, self.setA):
                print(i)
                self.answer.add(i)
            self.screen1.insert(END, self.answer)
        elif choice == 1:
            for i in itertools.product(self.answer, self.setB):
                print(i)
                self.answer.add(i)
            self.screen1.insert(END, self.answer)
        elif choice == 2:
            for i in itertools.product(self.setC, self.setA):
                print(i)
                self.answer.add(i)
            self.screen1.insert(END, self.answer)
        elif choice == 3:
            for i in itertools.product(self.setC, self.setB):
                print(i)
                self.answer.add(i)
            self.screen1.insert(END, self.answer)
        elif choice == 5:
            for i in itertools.product(self.answer, self.setC):
                print(i)
                self.answer.add(i)
            self.screen1.insert(END, self.answer)
        elif choice == 6:
            for i in itertools.product(self.setA, self.setC):
                print(i)
                self.answer.add(i)
            self.screen1.insert(END, self.answer)
        elif choice == 8:
            for i in itertools.product(self.setB, self.setC):
                print(i)
                self.answer.add(i)
            self.screen1.insert(END, self.answer)

    def calculate_Set(self):

        self.calc = self.screen.get()
        self.calc = self.calc.split()
        self.screen.delete(0, END)
        self.screen1.delete(0, END)
        self.screen.insert(0, 'ANS ')
        if len(self.calc) == 3:

            if self.calc[1] == '+':
                self.add()

            elif self.calc[1] == '-':
                self.minus()

            elif self.calc[1] == '*':
                self.multiply()

            elif self.calc[1] == '/':
                self.divide()

            elif self.calc[1] == '<=':

                if self.calc[0] == 'ANS' and self.calc[2] == 'A_set':
                    self.subsets(0)
                elif self.calc[0] == 'ANS' and self.calc[2] == 'B_set':
                    self.subsets(1)
                elif self.calc[0] == 'C_set' and self.calc[2] == 'A_set':
                    self.subsets(2)
                elif self.calc[0] == 'C_set' and self.calc[2] == 'B_set':
                    self.subsets(3)
                elif self.calc[0] == 'A_set' and self.calc[2] == 'B_set':
                    self.subsets(4)
                elif self.calc[0] == 'ANS' and self.calc[2] == 'C_set':
                    self.subsets(5)
                elif self.calc[0] == 'A_set' and self.calc[2] == 'C_set':
                    self.subsets(6)
                elif self.calc[0] == 'B_set' and self.calc[2] == 'A_set':
                    self.subsets(7)
                elif self.calc[0] == 'B_set' and self.calc[2] == 'C_set':
                    self.subsets(8)

            elif self.calc[1] == '|':

                if self.calc[0] == 'ANS' and self.calc[2] == 'A_set':
                    self.union(0)
                elif self.calc[0] == 'ANS' and self.calc[2] == 'B_set':
                    self.union(1)
                elif self.calc[0] == 'C_set' and self.calc[2] == 'A_set':
                    self.union(2)
                elif self.calc[0] == 'C_set' and self.calc[2] == 'B_set':
                    self.union(3)
                elif self.calc[0] == 'A_set' and self.calc[2] == 'B_set':
                    self.union(4)
                elif self.calc[0] == 'ANS' and self.calc[2] == 'C_set':
                    self.union(5)
                elif self.calc[0] == 'A_set' and self.calc[2] == 'C_set':
                    self.union(6)
                elif self.calc[0] == 'B_set' and self.calc[2] == 'A_set':
                    self.union(7)
                elif self.calc[0] == 'B_set' and self.calc[2] == 'C_set':
                    self.union(8)

            elif self.calc[1] == '&':

                if self.calc[0] == 'ANS' and self.calc[2] == 'A_set':
                    self.inters(0)
                elif self.calc[0] == 'ANS' and self.calc[2] == 'B_set':
                    self.inters(1)
                elif self.calc[0] == 'C_set' and self.calc[2] == 'A_set':
                    self.inters(2)
                elif self.calc[0] == 'C_set' and self.calc[2] == 'B_set':
                    self.inters(3)
                elif self.calc[0] == 'A_set' and self.calc[2] == 'B_set':
                        self.inters(4)
                elif self.calc[0] == 'ANS' and self.calc[2] == 'C_set':
                    self.inters(5)
                elif self.calc[0] == 'A_set' and self.calc[2] == 'C_set':
                    self.inters(6)
                elif self.calc[0] == 'B_set' and self.calc[2] == 'A_set':
                    self.inters(7)
                elif self.calc[0] == 'B_set' and self.calc[2] == 'C_set':
                    self.inters(8)

            elif self.calc[1] == '^':

                if self.calc[0] == 'ANS' and self.calc[2] == 'A_set':
                    self.complement(0)
                elif self.calc[0] == 'ANS' and self.calc[2] == 'B_set':
                    self.complement(1)
                elif self.calc[0] == 'C_set' and self.calc[2] == 'A_set':
                    self.complement(2)
                elif self.calc[0] == 'C_set' and self.calc[2] == 'B_set':
                    self.complement(3)
                elif self.calc[0] == 'A_set' and self.calc[2] == 'B_set':
                    self.complement(4)
                elif self.calc[0] == 'ANS' and self.calc[2] == 'C_set':
                    self.complement(5)
                elif self.calc[0] == 'A_set' and self.calc[2] == 'C_set':
                    self.complement(6)
                elif self.calc[0] == 'B_set' and self.calc[2] == 'A_set':
                    self.complement(7)
                elif self.calc[0] == 'B_set' and self.calc[2] == 'C_set':
                    self.complement(8)

            elif self.calc[1] == '--':

                if self.calc[0] == 'ANS' and self.calc[2] == 'A_set':
                    self.difference(0)
                elif self.calc[0] == 'ANS' and self.calc[2] == 'B_set':
                    self.difference(1)
                elif self.calc[0] == 'C_set' and self.calc[2] == 'A_set':
                    self.difference(2)
                elif self.calc[0] == 'C_set' and self.calc[2] == 'B_set':
                    self.difference(3)
                elif self.calc[0] == 'A_set' and self.calc[2] == 'B_set':
                    self.difference(4)
                elif self.calc[0] == 'ANS' and self.calc[2] == 'C_set':
                    self.difference(5)
                elif self.calc[0] == 'A_set' and self.calc[2] == 'C_set':
                    self.difference(6)
                elif self.calc[0] == 'B_set' and self.calc[2] == 'A_set':
                    self.difference(7)
                elif self.calc[0] == 'B_set' and self.calc[2] == 'C_set':
                    self.difference(8)

            elif self.calc[1] == 'x':

                if self.calc[0] == 'ANS' and self.calc[2] == 'A_set':
                    self.cartesian_product(0)
                elif self.calc[0] == 'ANS' and self.calc[2] == 'B_set':
                    self.cartesian_product(1)
                elif self.calc[0] == 'C_set' and self.calc[2] == 'A_set':
                    self.cartesian_product(2)
                elif self.calc[0] == 'C_set' and self.calc[2] == 'B_set':
                    self.cartesian_product(3)
                elif self.calc[0] == 'A_set' and self.calc[2] == 'B_set':
                    self.cartesian_product(4)
                elif self.calc[0] == 'ANS' and self.calc[2] == 'C_set':
                    self.cartesian_product(5)
                elif self.calc[0] == 'A_set' and self.calc[2] == 'C_set':
                    self.cartesian_product(6)
                elif self.calc[0] == 'B_set' and self.calc[2] == 'A_set':
                    self.cartesian_product(7)
                elif self.calc[0] == 'B_set' and self.calc[2] == 'C_set':
                    self.cartesian_product(8)

        else:
            tkinter.messagebox.showerror(title='Too many Arguments', message="Please do one sum at a time")
            self.screen1.delete(0, END)
            self.screen.delete(0, END)

    def add(self):
        if self.calc[0] == 'ANS':
            self.answer += float(self.calc[2])
            self.screen1.insert(END, self.answer)
        else:
            self.answer = float(self.calc[0]) + float(self.calc[2])
            self.screen1.insert(END, self.answer)


    def multiply(self):
        if self.calc[0] == 'ANS':
            self.answer *= float(self.calc[2])
            self.screen1.insert(END, self.answer)
        else:
            self.answer = float(self.calc[0]) * float(self.calc[2])
            self.screen1.insert(END, self.answer)

    def divide(self):
        if self.calc[0] == 'ANS':
            self.answer /= float(self.calc[2])
            self.screen1.insert(END, self.answer)
        else:
            self.answer = float(self.calc[0]) / float(self.calc[2])
            self.screen1.insert(END, self.answer)

    def minus(self):
        if self.calc[0] == 'ANS':
            self.answer -= float(self.calc[2])
            self.screen1.insert(END, self.answer)
        else:
            self.answer = float(self.calc[0]) - float(self.calc[2])
            self.screen1.insert(END, self.answer)

    def reset(self):

        self.root.destroy()

    def exitt(self):
        global a
        a=0
        self.root.destroy()



def main():
    while a == 1:
        Calculator()

if __name__ == "__main__":
    main()
