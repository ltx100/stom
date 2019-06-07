from util import tushare_base
import pymysql

pro = tushare_base.get_pro()
# df = pro.trade_cal(exchange='', start_date='20180901', end_date='20181001', fields='exchange,cal_date,is_open,pretrade_date', is_open='1')
# print(df)
# pro
data = pro.stock_basic(exchange='', list_status='L',
                       fields='ts_code,symbol,name,area,industry,fullname,enname,market,exchange,curr_type,list_status,list_date,delist_date,is_hs')
# 建立数据库连接,剔除已入库的部分
db = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='stock', charset='utf8')
cursor = db.cursor()
c_len = data.shape[0]
for i in range(c_len):
    resu0 = list(data.ix[i])
    print(resu0)
    try:
        sql_insert = "insert into stock_info values ('%s', '%s','%s', '%s','%s', '%s','%s', " \
                     "'%s','%s', '%s','%s', '%s','%s', '%s')" % (
                         str(resu0[0]), str(resu0[1]), str(resu0[2]), str(resu0[3]), str(resu0[4]), str(resu0[5]),
                         str(resu0[6]), str(resu0[7]), str(resu0[8]), str(resu0[9]),
                         str(resu0[10]), str(resu0[11]), str(resu0[12]), str(resu0[13]))
        print(sql_insert)
        # for key in resu0:
        #     print(key)
        #     if key == "None":
        #         sql_insert = sql_insert + "null,"
        #     else:
        #         sql_insert = sql_insert + str(key) + ","
        # print(sql_insert)
        # sql_insert = sql_insert[:-1] + ")"
        # print(sql_insert)
        cursor.execute(sql_insert)
        db.commit()
    except Exception as err:
        print(err)

cursor.close()
db.close()
print('All Finished!')
