import Tkinter
from Tkconstants import *
import re

tk = Tkinter.Tk()
frame = Tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
label = Tkinter.Label(frame, text="Hello, World")
label.pack(fill=X, expand=1)

text = Tkinter.Text(frame)
text.pack(side=TOP)

def formatsql():
    subject = text.get('0.0','100.100')
    regex = ['(\W+inner\W+join\W+)',\
            '(\W+left\W+join\W+)',\
            '(\W+left\W+outer\W+join\W+)',\
            '(\W+where\W+)',\
            '(\W+union\W+)',\
            '(\W+union\W+all\W+)',\
            '(\W+case\W+when\W+)',\
            '(\W+order\W+by\W+)',\
            '(\W+group\W+by\W+)']
    newstr = ['\n inner join ',\
            '\n left join ',\
            '\n left outer join ',\
            '\n where ',\
            '\n union ',\
            '\n union all ',\
            '\n case when ',\
            '\n group by ']

    result=subject
    number=0
    for i in range(len(regex)):
        result, number = re.subn(regex[i], newstr[i], result)
    #print subject
    text.delete('0.0','100.100')
    text.insert(END, result)

button = Tkinter.Button(frame,text="Format SQL",command=formatsql)
button.pack(side=BOTTOM)
tk.mainloop()

