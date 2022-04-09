import time
import pymysql
from jieba.analyse import extract_tags
import string

def get_time():
    time_str = time.strftime("%Y{}%m{}%d{} %X")
    return time_str.format("年","月","日")

def get_conn():
    """
    :return 连接 游标
    """
    #创建连接
    #建立连接
    conn = pymysql.connect(host='127.0.0.1', port=3306,user='root', password='20011026LSC0535@', db='cov', charset='utf8')
    #创建游标，默认是元组型
    cursor=conn.cursor()
    return conn,cursor

def close_conn(conn,cursor):
    conn,cursor=get_conn()
    if cursor:
        cursor.close()
    if conn:
        conn.close()

def query(sql,*args):
    """
    封装通用查询
    :param sql:
    :param args:
    :return: 返回查询到的结果，((),(),)的形式
    """
    conn, cursor = get_conn()
    cursor.execute(sql,args)
    res = cursor.fetchall()
    close_conn(conn, cursor)
    return res

def get_c1_data():
    """
    :return: 返回大屏div id=c1 的数据
    """
    # 因为会更新多次数据，取时间戳最新的那组数据
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='20011026LSC0535@', db='cov',
                           charset='utf8')
    # 创建游标，默认是元组型
    cursor = conn.cursor()
    sql = "select sum(confirm)," \
          "(select suspect from history order by ds desc limit 1)," \
          "sum(heal)," \
          "sum(dead) " \
          "from details " \
          "where update_time=(select update_time from details order by update_time desc limit 1) "
    res = query(sql)
    return res[0]

#  获取center2的数据
def get_c2_data():
    """
    :return:  返回各省数据
    """
    # 因为会更新多次数据，取时间戳最新的那组数据
    sql = "select province,sum(confirm) from details " \
          "where update_time=(select update_time from details " \
          "order by update_time desc limit 1) " \
          "group by province"
    res = query(sql)
    return res

def get_l1_data():
    sql = "select ds,confirm,suspect,heal,dead from history"
    res = query(sql)
  #  print(res)
    return res

def get_l2_data():
    sql = "select province,sum(confirm_add) from details " \
          "where update_time=(select update_time from details " \
          "order by update_time desc limit 1) " \
          "group by province"
    res = query(sql)
    print(res)
    return res

def get_r1_data():
    """
    :return:  返回非湖北地区城市确诊人数前5名
    """
    sql = 'SELECT province,confirm FROM ' \
          '(select province,confirm from details  ' \
          'where update_time=(select update_time from details order by update_time desc limit 1) ' \
          'and province not in ("湖北","北京","上海","天津","重庆") ' \
          'union all ' \
          'select province as city,sum(confirm) as confirm from details  ' \
          'where update_time=(select update_time from details order by update_time desc limit 1) ' \
          'and province in ("北京","上海","天津","重庆") group by province) as a ' \
          'ORDER BY confirm DESC LIMIT 5'
    res = query(sql)
    print(res)
    return res

def get_r2_data():
    """
    :return:  返回最近的20条热搜
    """
    sql = 'select content from hotsearch order by id asc limit 20'
    res = query(sql) #格式 (('民警抗疫一线奋战16天牺牲1037364',), ('四川再派两批医疗队1537382',)
    #for i in res:

    return res

if __name__ == "__main__":
    data = get_r2_data()
    print(data)
    # city = []
    # confirm = []
    # for k, v in data:
    #     city.append(k)
    #     confirm.append(int(v))
    # print(city,confirm)