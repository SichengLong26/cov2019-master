# encoding:utf-8
from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
import string
import time
import utils
from jieba.analyse import extract_tags

app = Flask(__name__)
@app.route('/',methods=['get','post'])
def index():
    return render_template('index.html')

@app.route('/time',methods=['get','post'])
def Etime():
    dt = utils.get_time()
    return dt

@app.route("/c1",methods=['get','post'])
def get_c1():
    data=utils.get_c1_data()
    return jsonify({"confirm":str(data[0]),"suspect":str(data[1]),"heal":str(data[2]),"dead":str(data[3])})

@app.route("/c2",methods=['get','post'])
def get_c2():
    datas=[]
    res = utils.get_c2_data()
    for item in res:
        datas.append({"name":item[0],"value":str(item[1])})
    return jsonify({"data":datas})

@app.route('/l1',methods=['get','post'])
def get_l1():
    res = utils.get_l1_data()
    day,confirm,suspect,heal,dead = [],[],[],[],[]
    for tup in res:
        day.append(tup[0].strftime("%m-%d"))
        confirm.append(tup[1])
        suspect.append(tup[2])
        heal.append(tup[3])
        dead.append(tup[4])
    return jsonify({"day": day, "confirm": confirm, "suspect": suspect, "heal": heal, "dead": dead})

@app.route("/l2",methods=['get','post'])
def get_l2_data():
    data = utils.get_l2_data()
    city = []
    confirm = []
    for k, v in data:
        city.append(k)
        confirm.append(int(v))
    return jsonify({"city": city, "confirm": confirm})


@app.route("/r1",methods=['get','post'])
def get_r1_data():
    data = utils.get_r1_data()
    city = []
    confirm = []
    for k, v in data:
        city.append(k)
        confirm.append(int(v))
    return jsonify({"city": city, "confirm": confirm})


# @app.route("/r2",methods=['get','post'])
# def get_r2_data():
#     data = utils.get_r2_data()  # 格式 (('民警抗疫一线奋战16天牺牲1037364',), ('四川再派两批医疗队1537382',)
#     return data

# 4、启动程序
if __name__ == '__main__':
    # 执行app.run()，就会将Flask程序运行在一个简易的服务器（Flask提供用于测试）
   app.run(host='0.0.0.0', port=5000, debug=True)
