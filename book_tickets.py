from tkinter import *
from tkinter import ttk
from tickets import *
import tkinter.messagebox
from login import *
from urllib import parse


class QueryPage(object):
    def __init__(self, master=None, query_list=[], user=None):
        self.user = user
        self.query_list = query_list
        self.root = master  # 定义内部变量root

        self.frame_left_top = Frame(width=650, height=145)
        self.frame_right_top = Frame(width=100, height=100)
        self.frame_center = Frame(width=900, height=400)
        self.frame_bottom = Frame(width=900, height=5)
        self.menu_bar()
        self.left_top_page()
        self.right_top_page()
        self.center_page()
        self.layout_frame()

    def parse_train_data(self, data_list):
        return {
            "station_train_code": data_list[3],
            "from_to_station_name": self.get_from_to_station_name(data_list),
            "start_arrive_time": self.get_start_arrive_time(data_list),
            "lishi": data_list[10],
            "business_class_seat": data_list[32] or '--',
            "first_class_seat": data_list[31] or '--',
            "second_class_seat": data_list[30] or '--',
            "super_soft_sleep": data_list[21] or '--',
            "soft_sleep": data_list[23] or '--',
            "dong_sleep": data_list[33] or '--',
            "hard_sleep": data_list[28] or '--',
            "soft_seat": data_list[24] or '--',
            "hard_seat": data_list[29] or '--',
            "no_seat": data_list[26] or '--',
            "other": data_list[22] or '--'
        }

    def get_from_to_station_name(self, data_list):
        from_station_telecode = data_list[6]
        to_station_telecode = data_list[7]
        return "\n".join([stations.get_name(from_station_telecode), stations.get_name(to_station_telecode)])

    def get_start_arrive_time(self, data_list):
        return '\n'.join([data_list[8], data_list[9]])

    def left_top_page(self):
        # 定义左上方区域
        self.var_date = StringVar()
        self.numb = datetime.date.today()
        self.str1 = str(self.numb.year) + '-' + str('%02d' % self.numb.month) + '-' + str('%02d' % self.numb.day)
        self.var_date.set(self.str1)
        self.left_top_frame = Frame(self.frame_left_top)
        self.left_top_frame1 = Label(self.frame_left_top, text="出发站")
        # self.left_e1 = Entry(self.frame_left_top,textvariable=self.sta_station)
        # 创建一个下拉列表
        self.placename1 = StringVar()
        self.placename_Chosen1 = ttk.Combobox(self.frame_left_top, textvariable=self.placename1)
        self.placename_Chosen1['values'] = ('北京', '上海', '天津', '重庆', '深圳', '广州', '杭州', '福州', '长沙', '济南', '长春',
                                            '昆明', '海口', '石家庄', '南京', '沈阳', '成都', '哈尔滨', '南昌', '合肥', '呼和浩特',
                                            '武汉', '南宁', '郑州', '乌鲁木齐', '兰州', '西安', '太原', '贵阳', '银川', '西宁')  # 设置下拉列表的值
        # self.placename_Chosen1.current(0)  # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值
        self.left_top_frame2 = Label(self.frame_left_top, text="到达站")
        # self.left_e2 = Entry(self.frame_left_top,textvariable=self.des_station)
        self.placename2 = StringVar()
        self.placename_Chosen2 = ttk.Combobox(self.frame_left_top, textvariable=self.placename2)
        self.placename_Chosen2['values'] = ('北京', '上海', '天津', '重庆', '深圳', '广州', '杭州', '福州', '长沙', '济南', '长春',
                                            '昆明', '海口', '石家庄', '南京', '沈阳', '成都', '哈尔滨', '南昌', '合肥', '呼和浩特',
                                            '武汉', '南宁', '郑州', '乌鲁木齐', '兰州', '西安', '太原', '贵阳', '银川', '西宁')
        # self.placename_Chosen2.current(0)
        self.left_top_frame3 = Label(self.frame_left_top, text="日期")
        self.left_e3 = Entry(self.frame_left_top, textvariable=self.var_date)
        # self.left_e3 = Entry(self.frame_left_top,self.date_station)
        # 多选类型，火车类型选择# -d动车 -g高铁 -k快速 -t特快 -z直达
        self.left_top_frame4 = LabelFrame(self.frame_left_top, text="车次类型")
        # 创建一个IntVar类型的变量，让如下Checkbutton关联在同一个变量
        self.d = IntVar(self.frame_left_top, value=1)
        self.g = IntVar(self.frame_left_top, value=1)
        self.k = IntVar(self.frame_left_top, value=1)
        self.t = IntVar(self.frame_left_top, value=1)
        self.z = IntVar(self.frame_left_top, value=1)

        self.left_top_button1 = Checkbutton(self.left_top_frame4, text='G-高铁', variable=self.g)
        self.left_top_button2 = Checkbutton(self.left_top_frame4, text='D-动车', variable=self.d)
        self.left_top_button3 = Checkbutton(self.left_top_frame4, text='Z-直达', variable=self.z)
        self.left_top_button4 = Checkbutton(self.left_top_frame4, text='T-特快', variable=self.t)
        self.left_top_button5 = Checkbutton(self.left_top_frame4, text='K-快速', variable=self.k)

        self.left_top_frame1.grid(row=2, column=0, padx=10)
        # self.left_e1.grid(row=2, column=1)
        self.placename_Chosen1.grid(row=2, column=1)
        self.left_top_frame2.grid(row=2, column=2, padx=5)
        # self.left_e2.grid(row=2, column=3)
        self.placename_Chosen2.grid(row=2, column=3)
        self.left_top_frame3.grid(row=2, column=4, padx=5)
        self.left_e3.grid(row=2, column=5)
        self.left_top_frame4.grid(row=3, column=0, columnspan=6)
        self.left_top_button1.grid(row=3, column=1, padx=15)
        self.left_top_button2.grid(row=3, column=2, padx=15)
        self.left_top_button3.grid(row=3, column=3, padx=15)
        self.left_top_button4.grid(row=3, column=4, padx=15)
        self.left_top_button5.grid(row=3, column=5, padx=15)

        self.left_top_frame5 = Label(self.frame_left_top, text="双击车票信息查看票价,显示如下：", fg="blue")
        self.left_top_frame6 = Listbox(self.frame_left_top, width=100)

        self.left_top_frame5.grid(row=4, column=0, columnspan=3)
        self.left_top_frame6.grid(row=5, column=0, columnspan=10)

    def right_top_page(self):
        # 定义右上方区域

        self.right_top_button3 = Button(self.frame_right_top, text="查询余票", command=self.get_tree, font=6)
        self.right_top_button2 = Button(self.frame_right_top, text="购买余票",
                                        command=lambda: self.buy_tickets(user=self.user), font=6)

        self.right_top_button3.grid(row=1, column=1, padx=20)
        self.right_top_button2.grid(row=2, column=1, padx=20, pady=20)

    def center_page(self):
        # 定义中心列表区域
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18,
                                 columns=("a", "b", "c", "d", "e", 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'))
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 表格的标题
        self.tree.column("a", width=45, anchor="center")
        self.tree.column("b", width=120, anchor="center")
        self.tree.column("c", width=120, anchor="center")
        self.tree.column("d", width=40, anchor="center")
        self.tree.column("e", width=60, anchor="center")
        self.tree.column("f", width=60, anchor="center")
        self.tree.column("g", width=60, anchor="center")
        self.tree.column("h", width=60, anchor="center")
        self.tree.column("i", width=45, anchor="center")
        self.tree.column("j", width=45, anchor="center")
        self.tree.column("k", width=45, anchor="center")
        self.tree.column("l", width=45, anchor="center")
        self.tree.column("m", width=45, anchor="center")
        self.tree.column("n", width=45, anchor="center")
        self.tree.column("o", width=45, anchor="center")
        self.tree.heading("a", text="车次")
        self.tree.heading("b", text="出发站->到达站")
        self.tree.heading("c", text="出发时间->到达时间")
        self.tree.heading("d", text="历时")
        self.tree.heading("e", text="商务座")
        self.tree.heading("f", text="一等座")
        self.tree.heading("g", text="二等座")
        self.tree.heading("h", text="高级软卧")
        self.tree.heading("i", text="软卧")
        self.tree.heading("j", text="动卧")
        self.tree.heading("k", text="硬卧")
        self.tree.heading("l", text="软座")
        self.tree.heading("m", text="硬座")
        self.tree.heading("n", text="无座")
        self.tree.heading("o", text="其他")

        # 调用方法获取表格内容插入
        self.get_tree()
        # self.tree.grid(row=0, column=0, sticky=N+EW)
        # self.vbar.grid(row=0, column=1, sticky=NS)
        self.tree.grid(sticky=EW)
        self.vbar.grid(row=0, column=1, sticky=NS)
        self.tree.bind('<Double-1>', self.handlerAdaptor(self.onDBClick))
        # self.tree.bind('<Double-2>',self.get_tree())

    def layout_frame(self):
        # 整体区域定位布局
        self.frame_left_top.grid(row=0, column=0, padx=4, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=10, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)
        self.menu_bar()
        self.root.mainloop()

    def menu_bar(self):
        menubar = Menu(self.root)
        menubar.add_command(label='欢迎您进入火车票查询系统')

        self.root['menu'] = menubar  # 设置菜单栏

    def get_tree(self):
        if self.placename_Chosen1.get() != self.placename_Chosen2.get() and self.left_e3.get() != '':
            from_station = self.placename_Chosen1.get()
            to_station = self.placename_Chosen2.get()
            date = self.left_e3.get()
            self.date = date
            try:
                s = Search(from_station, to_station, date,
                           options={'-d': self.d.get(), '-g': self.g.get(), '-k': self.k.get(),
                                    '-t': self.t.get(), '-z': self.z.get()})
                trains = s.run()
                global train_info
                train_info = trains

            except Exception:
                tkinter.messagebox.showerror(title='Error', message='请输入有效信息')

            result_list = []
            for i in trains:
                m = self.parse_train_data(i)
                result_list.append([
                    m["station_train_code"],
                    m["from_to_station_name"],
                    m["start_arrive_time"],
                    m["lishi"],
                    m["business_class_seat"],
                    m["first_class_seat"],
                    m["second_class_seat"],
                    m["super_soft_sleep"],
                    m["soft_sleep"],
                    m["dong_sleep"],
                    m["hard_sleep"],
                    m["soft_seat"],
                    m["hard_seat"],
                    m["no_seat"],
                    m["other"]
                ])

            # 删除原节点
            for i in result_list:
                for j in i:
                    if '\n' in j:
                        index_num = i.index(j)
                        i[index_num] = j.replace('\n', ' -> ')
            for _ in map(self.tree.delete, self.tree.get_children("")):
                pass
            # 更新插入新节点
            for item in result_list:
                item1 = tuple(item)
                self.tree.insert('', "end", values=item1)
            # self.tree.after(500, self.get_tree)

    def buy_tickets(self, user):
        trains_info = self.trains_info
        order_sec = parse.unquote(trains_info[0])
        from_name = stations.get_name(trains_info[6])
        to_name = stations.get_name(trains_info[7])
        date = trains_info[13]
        timeArray = time.strptime(date, "%Y%m%d")
        date = time.strftime("%Y-%m-%d", timeArray)
        # 预订请求
        sb_res = user.submit(from_name, to_name, order_sec, date)
        if sb_res == -1:
            tkinter.messagebox.showerror(title='Error', message='预订失败，请完成已有订单或重新预订')
        elif sb_res == -2:
            tkinter.messagebox.showerror(title='Error', message='登录超时，请重新登录')

        else:
            self.query_list.extend(sb_res)
            self.root.destroy()

    def handle_price(self, tic_price):
        L = []
        if 'P' in tic_price:
            L.append('特等座：' + '%s' % tic_price['P'] + ' ')

        if 'A9' in tic_price:
            L.append('商务座：' + '%s' % tic_price['A9'] + ' ')

        if 'M' in tic_price:
            L.append('一等座：' + '%s' % tic_price['M'] + ' ')

        if 'O' in tic_price:
            L.append('二等座：' + '%s' % tic_price['O'] + ' ')

        if 'A4' in tic_price:
            L.append('软卧：' + '%s' % tic_price['A4'] + ' ')

        if 'A3' in tic_price:
            L.append('硬卧：' + '%s' % tic_price['A3'] + ' ')

        if 'A1' in tic_price:
            L.append('硬座:' + '%s' % tic_price['A1'] + ' ')

        if 'WZ' in tic_price:
            L.append('无座：' + '%s' % tic_price['WZ'] + ' ')
        self.left_top_frame6.delete(0, END)

        L = '  '.join(L)
        self.left_top_frame6.insert(0, L)

    def handlerAdaptor(self, fun, **kwds):
        return lambda event, fun=fun, kwds=kwds: fun(event, **kwds)

    def onDBClick(self, event):

        item = self.tree.selection()[0]
        v = self.tree.item(item, 'values')
        s = v[0]
        for list1 in train_info:
            if s in list1:
                self.trains_info = list1

        tic_price = TrainCollection.get_price(self, self.trains_info, self.date)
        self.handle_price(tic_price)


def bookWindow(user):
    query_list = []
    root = Tk()
    root.title("火车票查询系统")
    root.geometry('+250+50')
    QueryPage(root, query_list, user)
    root.mainloop()
    return query_list


if __name__ == '__main__':
    bookWindow()
