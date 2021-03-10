#Welcome.py
#First screen to inform users about the programme
#P.Patchigalla Feb 21

#Import took kit interface (tkinter) modules
from tkinter import*
from tkinter import ttk

#Parent class
class MathQuiz:
  def __init__(self,parent):

    '''Widgets for Welcome Frame'''

    self.Welcome = Frame(parent)
    self.Welcome.grid(row=0, column=0)

    self.TitleLabel = Label(self.Welcome, text = "Welcome to Maths Quiz",
                            bg = "black", fg = "white", width = 20, padx = 30, pady = 10,
                            font = ("Time", '14', "bold italic"))
    self.TitleLabel.grid(columnspan = 2) #Lable spans over two columns

    self.NextButton = ttk.Button(self.Welcome, text = 'Next') #ttk prefit gives modern Button
    self.NextButton.grid(row = 8, column = 1)

    

#Main routine
if __name__ == "__main__": #checks if condition - name of Parent class is main module
  root =Tk()
  frames = MathQuiz(root)
  root.title("Quiz")
  root.mainloop() #binds the above commands togeter
