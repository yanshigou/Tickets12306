from welcome import *
from query_tickets import *
from buy_info import *
from book_tickets import *


# 985061107@qq.com
# m674930977

def choice_1():
    YanZheng()
    user = login_ret()
    if user == 0:
        return
    while 1:
        sb_res = bookWindow(user)
        date = sb_res[-1]
        station_train_code = sb_res[0]
        from_station_name = sb_res[1]
        start_time = sb_res[2]
        to_station_name = sb_res[3]
        arrive_time = sb_res[4]
        ticket_num = sb_res[5]
        prices = sb_res[6]
        users = sb_res[7]
        tk = sb_res[8]
        leftTicketStr = sb_res[9]
        from_station = sb_res[10]
        to_station = sb_res[11]
        train_location = sb_res[12]
        train_no = sb_res[13]
        key_check_isChange = sb_res[14]
        t_file = [date, station_train_code, from_station_name, start_time, to_station_name, arrive_time, users.items(),
                  ticket_num, prices]
        # 选票界面
        xieqi_res = confirm_snp(t_file)
        if xieqi_res == 0:
            return
        elif xieqi_res == 1:
            continue
        else:
            break
    seat = xieqi_res[0]
    name = xieqi_res[1]
    id_num = xieqi_res[3]
    phone = xieqi_res[5]

    user.checkOrderInfo(seat, name, id_num, phone, tk)
    # 确认订单
    user.getQueueCount(leftTicketStr, station_train_code, from_station, to_station, train_location,
                       train_no, seat, date, tk)

    oldPassengerStr = name + ",1," + id_num + ",1_"
    passengerTicketStr = seat + ",0,1," + name + ",1," + id_num + "," + phone + ",N"
    comfirm_ret = user.confirmSingleForQueue(key_check_isChange, leftTicketStr, oldPassengerStr, passengerTicketStr,
                                             train_location, tk)

    # print(comfirm_ret)


def main():
    choice = DengLu()
    if choice == 1:
        choice_1()

    if choice == -1:
        ret = searchWindow(user=None)
        if ret == 0:
            return
        else:
            choice_1()


if __name__ == '__main__':
    main()
