import tkinter as tk
from PIL import ImageTk, Image
import tkinter.messagebox
from tickets import *
from time import sleep

login_val = 0

def onBtn(a, b, c, d, e, f, g, h, e1, e2, user, root):
    global login_val
    list = []
    if a > 0:
        list.append(1)
    if b > 0:
        list.append(2)
    if c > 0:
        list.append(3)
    if d > 0:
        list.append(4)
    if e > 0:
        list.append(5)
    if f > 0:
        list.append(6)
    if g > 0:
        list.append(7)
    if h > 0:
        list.append(8)

    if list != [] and e1 != '' and e2 != '':
        uname = e1
        pwd = e2
        list1 = map(str, list)
        code = (" ".join(list1))
        result = user.captcha_check(code, uname, pwd)

        if result == 1:
            tkinter.messagebox.showinfo(title='提示', message='登录成功')
            login_val = user
            root.destroy()

        elif result == 0:
            tkinter.messagebox.showerror(title='Error', message='用户名或密码错误')
            root.destroy()
            sleep(0.1)
            YanZheng(user)
        elif result == -1:
            tkinter.messagebox.showerror(title='Error', message='验证码错误')
            root.destroy()
            sleep(0.1)
            YanZheng(user)
    else:
        tkinter.messagebox.showerror(title='Error', message='请输入完整信息')


def login_ret():
    return login_val


def mouseDownEvent(e):
    print("鼠标左键按下, 在:",
          e.x, e.y, e.x_root, e.y_root)


def YanZheng(user=None):
    # 创建用户
    if not user:
        user = Login()
    user.captcha()
    sleep(0.5)

    root = tk.Tk()
    root.title('--用户登陆--')

    # top1 = tk.Frame(root)

    label1 = tk.Label(root, text='用户名:')
    e1 = tk.Entry(root)
    label1.grid(row=0, column=0, pady=10)
    e1.grid(row=0, column=1)

    label2 = tk.Label(root, text='密码:')
    e2 = tk.Entry(root)

    e2['show'] = '*'
    label2.grid(row=1, column=0, pady=10)
    e2.grid(row=1, column=1)

    img_open = Image.open('./Images/captcha_img.png')
    img_png = ImageTk.PhotoImage(img_open)
    label_img = tk.Label(root, image=img_png)
    label_img.grid(row=2, columnspan=2)

    lf = tk.LabelFrame(root, text='请选择所有对应图片')
    lf.grid(row=3, columnspan=2, sticky='we')
    a = tk.IntVar(root, value=0)
    b = tk.IntVar(root, value=0)
    c = tk.IntVar(root, value=0)
    d = tk.IntVar(root, value=0)
    e = tk.IntVar(root, value=0)
    f = tk.IntVar(root, value=0)
    g = tk.IntVar(root, value=0)
    h = tk.IntVar(root, value=0)

    rb1 = tk.Checkbutton(lf, text='图１', variable=a)
    rb1.grid(row=4, column=0, padx=11)
    rb2 = tk.Checkbutton(lf, text='图２', variable=b)
    rb2.grid(row=4, column=1, padx=11)

    rb3 = tk.Checkbutton(lf, text='图３', variable=c)
    rb3.grid(row=4, column=2, padx=11)

    rb4 = tk.Checkbutton(lf, text='图４', variable=d)
    rb4.grid(row=4, column=3, padx=11)

    rb5 = tk.Checkbutton(lf, text='图５', variable=e)
    rb5.grid(row=5, column=0, padx=11)

    rb6 = tk.Checkbutton(lf, text='图６', variable=f)
    rb6.grid(row=5, column=1, padx=11)

    rb7 = tk.Checkbutton(lf, text='图７', variable=g)
    rb7.grid(row=5, column=2, padx=11)

    rb8 = tk.Checkbutton(lf, text='图８', variable=h)
    rb8.grid(row=5, column=3, padx=11)

    btn = tk.Button(root, text="确定",
                    command=lambda: onBtn(a.get(), b.get(), c.get(), d.get(), e.get(), f.get(), g.get(), h.get(), \
                                          e1.get(), e2.get(), user, root))
    btn.grid(row=5, columnspan=4, pady=20)

    # center_window(root, 150, 500)
    # root.maxsize(600, 450)
    # root.minsize(150, 240)

    root.geometry('300x420+800+300')
    root.maxsize(300, 420)
    root.minsize(300, 420)

    # root.bind('<Button-1>', mouseDownEvent)
    root.mainloop()


if __name__ == '__main__':
    YanZheng()
