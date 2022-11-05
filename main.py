import os

import numpy as np
import pandas as pd
from time import sleep


class DFA1:
    word = ''
    initial_state = 0
    current_state = 0
    valid = False

    def _int_(self):
        self.word = ''
        self.initial_state = 0
        self.valid = False

    def constructor(self, w, i, c):
        self.word = w
        self.initial_state = i
        self.current_state = c


    def transition(self, alphabet, state):
        if state == 0:
            if alphabet == 0:
                state = 1
            elif alphabet == 1:
                state = 3
            else:
                print("INVALID CHARACTER: ", alphabet)
        elif state == 1:
            if alphabet == 0:
                state = 0
            elif alphabet == 1:
                state = 2
            else:
                print("INVALID CHARACTER: ", alphabet)
        elif state == 2:
            if alphabet == 0:
                state = 3
            elif alphabet == 1:
                state = 1
            else:
                print("INVALID CHARACTER: ", alphabet)
        elif state == 3:
            if alphabet == 0:
                state = 2
            elif alphabet == 1:
                state = 0
            else:
                print("INVALID CHARACTER: ", alphabet)
        return state

    def DFA_working(self, neword):
        self.word = neword
        for i in self.word:
            self.current_state = self.transition(self,int(i), self.current_state)

        if self.current_state == 0:
            print("VALID STRING: ", neword,"\n")
        else:
            print("INVALID STRING: ", neword,"\n")


class DFA2:
    word=' '
    initial_state=0
    current_state=0

    def __init__(self):
        self.word=' '
        self.initial_state=0
    def constructor(self,w,i,c):
        self.word=w
        self.initial_state=i
        self.current_state = c


    def transitionfunction(self,alphabet,state):
        if state==0:
            if alphabet==0:
                state=3
            elif alphabet==1:
                state=1
            else:
                print("INVALID CHARACTER: ", alphabet)

        elif state==1:
            if alphabet==0:
                state=1
            elif alphabet==1:
                state=2
            else:
                print("INVALID CHARACTER: ", alphabet)

        elif state==2:
            if alphabet == 0:
                state = 2
            elif alphabet == 1:
                state = 2
            else:
                print("INVALID CHARACTER: ", alphabet)

        elif state==3:
            if alphabet == 0:
                state = 4
            elif alphabet == 1:
                state = 3
            else:
                print("INVALID CHARACTER: ", alphabet)

        elif state==4:
            if alphabet == 0:
                state = 4
            elif alphabet == 1:
                state = 4
            else:
                print("INVALID CHARACTER: ", alphabet)

        return state

    def DFA_working(self,neword):
        self.word = neword
        for i in self.word:
            self.current_state = self.transitionfunction(self,int(i), self.current_state)
        if self.current_state ==  2 or self.current_state ==  4:
            print("VALID STRING: ",neword,"\n")
        else:
            print("INVALID STRING: ",neword,"\n")

class DFA3:
    word=' '
    initial_state=0
    final_state=0
    current_state=0

    def __init__(self):
        self.word=' '
        self.initial_state=0
        self.final_state=0
    def constructor(self,w,i,c,f):
        self.word=w
        self.initial_state=i
        self.current_state = c
        self.final_state=f

    def transitionfunction(self,alphabet,state):
        if state==0:
            if alphabet=='a':
                state=2
            elif alphabet=='b':
                state=2
            elif alphabet=='c':
                state=1
            else:
                print("INVALID CHARACTER: ", alphabet)

        elif state==1:
            if alphabet=='a':
                state=3
            elif alphabet=='b':
                state=2
            elif alphabet=='c':
                state=2
            else:
                print("INVALID CHARACTER: ", alphabet)

        elif state==2:
            if alphabet=='a':
                state=3
            elif alphabet=='b':
                state=3
            elif alphabet=='c':
                state=3
            else:
                print("INVALID CHARACTER: ", alphabet)

        elif state==3:
            if alphabet=='a':
                state=3
            elif alphabet=='b':
                state=3
            elif alphabet=='c':
                state=3
            else:
                print("INVALID CHARACTER: ", alphabet)

        return state

    def DFA_working(self,neword):
        self.word = neword
        for i in self.word:
            self.current_state = self.transitionfunction(self,i, self.current_state)
        if self.current_state == self.final_state:
            print("VALID STRING: ", neword,"\n")
        else:
            print("INVALID STRING: ", neword,"\n")


df= pd.read_csv("Book1.csv")
file=pd.DataFrame(df)

DFA1()
DFA2()
DFA3()


while(1):
    sleep(1)
    print("| Enter 1 To CHECK FIRST DFA   |")
    print("| Enter 2 To CHECK SECOND DFA  | ")
    print("| Enter 3 To CHECK THIRD DFA   |")
    print("| Enter 0 To EXIT              |")

    key = int(input("Enter Here: "))

    if(key==1):
        for word in file['DFA1']:
            DFA1.constructor(DFA1,str(word), 0,0)
            DFA1.DFA_working(DFA1,str(word))

    elif(key==2):

        for word in file['DFA2']:
            DFA2.constructor(DFA2,str(word), 0,0)
            DFA2.DFA_working(DFA2, str(word))

    elif (key==3):
        for word in file['DFA3']:
            DFA3.constructor(DFA3,word,0,0,2)
            DFA3.DFA_working(DFA3,word)


    elif(key==0):
        print("EXIT SUCCESSFUL")
        break

    else:
        print("ERROR : INVALID NUMBER ENTERED")


