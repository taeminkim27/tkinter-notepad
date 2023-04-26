# tkinter로 메모장 만들기
from tkinter import *
from tkinter.filedialog import *

def new_file():
    text_area.delete(1.0,END)

def save_file():
    f= asksaveasfile(mode="w",defaultextension=".txt",filetypes=[('Text files','.txt')])
    text_save=str(text_area.get(1.0,END))
    f.write(text_save)
    f.close()

def maker():
    help_view = Toplevel(window)
    help_view.geometry("300x50")
    help_view.title("만든이")
    lb= Label(help_view, text = "메모장입니다.")
    lb.pack()

window = Tk()
window.title("Notepad")
window.geometry("400x400")
window.resizable(False, False)

menu = Menu(window) # 메뉴 위젯을 만드는 클래스
menu_1 = Menu(menu, tearoff=0) #tearoff=0 은 부동객체를 만드는 설정(마우스를 가져다 대면 나오는 표시?)
menu_1.add_command(label="새파일", command= new_file) 
menu_1.add_command(label="저장", command= save_file)
menu_1.add_separator()
menu_1.add_command(label="종료", command=window.destroy)
menu.add_cascade(label="파일", menu=menu_1)

# add_command(): 메뉴 항목 생성. label 매개변수는 항목명을 의미하며,command 매개변수는 클릭시 동작을 지정

menu_2 = Menu(menu, tearoff=0)
menu_2.add_command(label="만든이", command=maker)
menu.add_cascade(label="만든이", menu=menu_2)

text_area = Text(window)
window.grid_rowconfigure(0,weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky =N + E + S + W)

window.config(menu=menu)

window.mainloop()