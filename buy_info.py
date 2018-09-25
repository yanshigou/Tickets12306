import tkinter as tk
import re

test = 0


def confirm_snp(t_file):
    time = t_file[0]
    checi = t_file[1]
    start_station = t_file[2]
    start_time = t_file[3]
    start_time = start_time[:2] + ':' + start_time[2:]
    stop_station = t_file[4]
    stop_time = t_file[5]
    stop_time = stop_time[:2] + ':' + stop_time[2:]
    zuowei = t_file[7]
    user = dict(t_file[6])
    prices = t_file[8]

    checixinxi = [checi, start_station, start_time, stop_station, stop_time]
    root = tk.Tk()
    # root.geometry('830x350+500+200')
    root.title('购票信息')
    root.resizable(width=False, height=False)
    # 列车信息
    # l1 = tk.Label(root, text='列车信息(余票信息仅供参考)')
    # l1.pack(anchor='nw', ipady=20)
    ff = tk.LabelFrame(root, text='列车信息(余票信息仅供参考)')
    ff.pack()
    la1 = tk.Label(ff, text='－－－－－－－车次信息－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－')
    la1.pack(anchor='w', padx=100, pady=10)
    # can1 = tk.Canvas(ff,bg = 'blue')
    # can1.pack()
    # 列车信息显示
    f = tk.Frame(ff)
    f.pack(anchor='w', padx=100, pady=10)

    l2 = tk.Label(f, text=time + ' ')
    l2.pack(side=tk.LEFT)
    l3 = tk.Label(f, text=checi + ' ')
    l3.pack(side=tk.LEFT)

    l4 = tk.Label(f, text=start_station)
    l4.pack(side=tk.LEFT)

    l5 = tk.Label(f, text=start_time + '  --> ')
    l5.pack(side=tk.LEFT)

    l6 = tk.Label(f, text=stop_station)
    l6.pack(side=tk.LEFT)

    l7 = tk.Label(f, text=stop_time)
    l7.pack(side=tk.LEFT)

    la2 = tk.Label(ff, text='－－－－－－－票价信息－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－')
    la2.pack(anchor='w', padx=100, pady=10)
    # 座位信息
    f2 = tk.Frame(ff)
    f2.pack(anchor='w', padx=100, pady=10)
    # "YZ_num": "1",  # 硬座
    # "RZ_num": "2",  # 软座
    # "YW_num": "3",  # 硬卧
    # "RW_num": "4",  # 软卧
    # "GR_num": "6",  # 高级软卧
    # "TZ_num": "P",  # 特等座
    # "WZ_num": "WZ",  # 无座
    # "ZE_num": "O",  # 二等座
    # "ZY_num": "M",  # 一等座
    # "SWZ_num": "9",  # 商务座
    # # zuo_wei = {"YZ_num'": '1',"RZ_num'":'2',"YW_num'":'3',
    # "RW_num'":'4',"GR_num'":'6',"TZ_num'":'P',"WZ_num'":'WZ',"ZE_num'":'O',"ZY_num'":'M',"SWZ_num'":'9'}

    zuo_weidict = {"YZ_num'": "硬座", "RZ_num'": "软座", "YW_num'": "硬卧", "RW_num'": "软卧",
                   "GR_num'": "高级软卧", "TZ_num'": "特等座", "WZ_num'": "无座", "ZE_num'": "二等座",
                   "ZY_num'": "一等座", "SWZ_num'": "商务座"}
    v = tk.IntVar(root)

    la3 = tk.Label(ff, text='－－－－－－－乘客信息－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－')
    la3.pack(anchor='w', padx=100, pady=10)
    for i in range(len(zuowei)):
        s = zuowei[i - 1].split(':')
        p = prices[i - 1].split(':')
        p1 = p[0].split('_')
        s1 = s[0].split('_')
        regex = re.search(r"'0*(\d+)(\d)'$", p[1])
        price1 = regex.group(1) + '.' + regex.group(2)

        if s[0] in zuo_weidict:
            n = zuo_weidict[s[0]]

        rb = tk.Radiobutton(f2, text=n + '(￥' + price1 + ')' + ' ' + '剩余:' + eval(s[1]) + '张', value=i, variable=v)
        rb.pack(side=tk.LEFT)

    # 乘客信息
    f3 = tk.Frame(ff)
    f3.pack(anchor='w', padx=100)
    user1 = list(user.values())
    v2 = tk.IntVar(root)
    for x in range(len(user)):
        userinfo = user1[x - 1]
        rb1 = tk.Radiobutton(f3, text='姓名:' + userinfo[0] + '   性别:' + userinfo[1]
                                      + '   身份证:' + userinfo[2] + '   票种:' + userinfo[3] + '   电话:' + userinfo[4],
                             variable=v2, value=x)
        rb1.pack(anchor='nw', ipady=7)

    # 信息提交
    f4 = tk.Frame(ff)
    f4.pack(anchor='w', pady=20, padx=150)

    btnback = tk.Button(f4, width=15, text='返回', command=lambda: back(root))
    btnback.pack(side=tk.LEFT, padx=50)

    btn = tk.Button(f4, width=15, text='提交',
                    command=lambda: onbtn(zuowei[v.get() - 1], user1[v2.get() - 1], checixinxi, root))
    btn.pack(side=tk.LEFT, padx=50)
    # root.maxsize(830, 350)
    # root.minsize(850, 350)

    root.mainloop()

    return test


def onbtn(a, b, c, root):
    global test
    # 获取用户点选数据
    zuo_wei = {"YZ_num'": '1', "RZ_num'": '2', "YW_num'": '3',
               "RW_num'": '4', "GR_num'": '6', "TZ_num'": 'P', "WZ_num'": 'WZ', "ZE_num'": 'O', "ZY_num'": 'M',
               "SWZ_num'": '9'}
    zuo_weidict = {"YZ_num'": "硬座", "RZ_num'": "软座", "YW_num'": "硬卧", "RW_num'": "软卧",
                   "GR_num'": "高级软卧", "TZ_num'": "特等座", "WZ_num'": "无座", "ZE_num'": "二等座",
                   "ZY_num'": "一等座", "SWZ_num'": "商务座"}
    ticket = a.split(':')
    b.insert(0, zuo_wei[ticket[0]])
    zuoweixinxi = zuo_weidict[ticket[0]]
    yonghuxinxi = '车次:' + c[0] + ' ' + c[1] + ' ' + c[2] + '---' + c[3] + ' ' + c[4] \
                  + '\n姓名:' + b[1] + ' ' + '性别:' + b[2] + ' ' + '\n身份证:' + b[3] + ' ' + '票种:' + b[4] + ' ' + '\n电话:' + \
                  b[5] + ' ' + '\n选座信息:' + zuoweixinxi
    msg = tk.messagebox.askokcancel(title='请确认购票信息', message=yonghuxinxi)
    if msg == True:
        test = b
        msg1 = tk.messagebox.showinfo('成功', '购票成功,请尽快登录官网付款')
        root.destroy()


def back(root):
    global test

    test = 1
    root.destroy()
