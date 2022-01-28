from tkinter import *
from utils import Load_Profile_Analyser
from tkinter.ttk import Notebook


root = Tk()
root.title("Load Profile Analysis")


tabControl = Notebook(root)

tab1 = Frame(tabControl)
tab2 = Frame(tabControl)
tab3 = Frame(tabControl)
tab4 = Frame(tabControl)
tab5 = Frame(tabControl)
tab6 = Frame(tabControl)
tab7 = Frame(tabControl)
tab8 = Frame(tabControl)
tab9 = Frame(tabControl)
tab10 = Frame(tabControl)

tabControl.add(tab1, text='Brunei')
tabControl.add(tab2, text="Cambodia")
tabControl.add(tab3, text="Indonesia")
tabControl.add(tab4, text="Laos")
tabControl.add(tab5, text="Malaysia")
tabControl.add(tab6, text="Myanmmar")
tabControl.add(tab7, text="Philippines")
tabControl.add(tab8, text='Singapore')
tabControl.add(tab9, text='France')
tabControl.add(tab10, text='India')


Load_Profile_Analyser(tab1, 'Brunei', 'brunei.csv')
Load_Profile_Analyser(tab2, 'Cambodia', 'cambodia.csv')
Load_Profile_Analyser(tab3, 'Indonesia', 'indonesia.csv')
Load_Profile_Analyser(tab4, 'Laos', 'laos.csv')
Load_Profile_Analyser(tab5, 'Malaysia', 'malaysia.csv')
Load_Profile_Analyser(tab6, 'Myanmmar', 'myanmar.csv')
Load_Profile_Analyser(tab7, 'Philippines', 'philippines.csv')
Load_Profile_Analyser(tab8, 'Singapore', 'singapore.csv')
Load_Profile_Analyser(tab9, 'France', 'france.csv')
Load_Profile_Analyser(tab10, 'India', 'india.csv')

tabControl.pack(expand = 1, fill ="both")


root.mainloop()