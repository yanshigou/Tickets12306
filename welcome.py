from login import *

#账号
def r1(root):
    global choice
    choice = 1
    root.destroy()

# 游客
def r0(root):
    global choice
    choice = -1
    root.destroy()

choice = 0
def DengLu():
    root = tk.Tk()
    root.title('欢迎使用12306查询购票系统3.0')

    img_open = Image.open('./Images/12306.png')
    img_png = ImageTk.PhotoImage(img_open)

    label_img = tk.Label(root, image = img_png)
    label_img.pack(side=tk.TOP)

    yonghu=tk.Button(root,text="登  录",font=5,bg='CornflowerBlue',fg='White',command=lambda :r1(root))
    yonghu.pack(padx=85, side=tk.LEFT)

    huanyin=tk.Label

    youke=tk.Button(root,text="游客登录",font=5,bg='DimGray',fg='White',command=lambda :r0(root))
    youke.pack(padx=85, side=tk.RIGHT)
    # center_window(root, 300, 80)

    root.geometry('469x223+700+450')

    root.maxsize(469, 223)
    root.minsize(469, 223)

    root.mainloop()
    return choice



# 居中函数

# def get_screen_size(window):
#     return window.winfo_screenwidth(), window.winfo_screenheight()
#
# def center_window(root, ckwidth, ckheight):
#     pmwidth = root.winfo_screenwidth()
#     pmheight = root.winfo_screenheight()
#     size = '%dx%d+%d+%d' % (ckwidth, ckheight, (pmwidth - ckwidth) / 2, (pmheight - ckheight) / 2)
#     root.geometry(size)

