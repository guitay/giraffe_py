import Tkinter
from Tkconstants import *
import re

tk = Tkinter.Tk()
frame = Tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)

text = Tkinter.Text(frame)
text.pack(side=TOP)

def formatsql():
    subject = text.get('0.0','100.100')
    regex = ['(\s+inner\s+join\s+)',\
            '(\s+left\s+join\s+)',\
            '(\s+left\s+outer\s+join\s+)',\
            '(\s+where\s+)',\
            '(\s+union\s+)',\
            '(\s+union\s+all\s+)',\
            '(\s+case\s+when\s+)',\
            '(\s+order\s+by\s+)',\
            '(\s+group\s+by\s+)']
    newstr = ['\n inner join ',\
            '\n left join ',\
            '\n left outer join ',\
            '\n where ',\
            '\n union ',\
            '\n union all ',\
            '\n case when ',\
            '\n order by ',\
            '\n group by ']

    result=subject
    number=0
    for i in range(len(regex)):
        result, number = re.subn(regex[i], newstr[i], result,flags=re.IGNORECASE)
    #print subject
    text.delete('0.0','100.100')
    text.insert(END, result)

button = Tkinter.Button(frame,text="Format SQL",command=formatsql)
button.pack(side=BOTTOM)
tk.mainloop()

