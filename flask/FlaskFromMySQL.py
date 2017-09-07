#coding: utf-8
import pymysql, json
from flask import Flask, render_template, request, jsonify

# DB Functions Start
def dataConnect():
    db = pymysql.connect('192.168.0.101', 'root', 'boxing12', 'raspberry')
    cur = db.cursor()

    return db, cur

def dataDisconnect(db, cur):
    cur.close()
    db.close


def dataInsert(id, name, phone):

    db, cur = dataConnect()
    sql = "insert into mysql_test(id, name, phone) values('"+ id +"', '"+ name +"', '"+ phone +"')"
    try:
        result = cur.execute(sql)
        db.commit()
    except:
        db.rollback()
        result = "-1"

    dataDisconnect(db, cur)
    return result

def dataSelectID(id):
    db, cur = dataConnect()

    sql = "select * from mysql_test WHERE id ='%s'" %id

    cur.execute(sql)
    rs = cur.fetchone()

    dataDisconnect(db, cur)
    return rs

def dataSelectAll():
    db, cur = dataConnect()

    sql = "select * from mysql_test"

    cur.execute(sql)
    rs = cur.fetchall()

    dataDisconnect(db, cur)
    return rs

def dataUpdate(id, name, phone):
    db, cur = dataConnect()
    sql = "update mysql_test set name = '"+ name +"', phone = '"+ phone +"' WHERE id = '"+ id +"'"

    try:
        rs = cur.execute(sql)
        db.commit()
    except:
        rs = -1
        db.rollback()

    dataDisconnect(db, cur)

    return rs

def dataDelete(id):
    db, cur = dataConnect()
    sql = "DELETE FROM mysql_test WHERE id = '"+ id +"'"
    print sql
    try:
        rs = cur.execute(sql)
        db.commit()
    except:
        rs = -1
        db.rollback()

    dataDisconnect(db, cur)

    return rs

# DB Functions End

app = Flask(__name__)

#Restful API 이름 정의 방식
#Create(POST) : INSERT
#Read(GET) : SELECT
#Update(PUT) : UPDATE
#Delete(DELETE) : DELETE


@app.route('/GET/ID', methods=["GET"])
def get_id():

    id = request.args.get('id')
    rs = dataSelectID(id)

    try:
        result = jsonify( {"result" : "success", "id" : rs[0], "name" : rs[1], "phone" : rs[2]} )
    except:
        result = jsonify({"result": "fail"})
    return result

@app.route("/POST/CREATEID", methods=["POST"])
def create_id():
    id = request.form['id']
    name = request.form['name']
    phone = request.form['phone']

    result = dataInsert(id, name, phone)
    return jsonify({"result" : result})

@app.route("/PUT/UPDATEID", methods=["POST"])
def update_id():
    id = request.form['id']
    name = request.form['name']
    phone = request.form['phone']

    result = dataUpdate(id, name, phone)
    return jsonify({"result" : result})

@app.route("/DELETE/DELETEID", methods=["POST"])
def delete_id():
    id = request.form['id']

    result = dataDelete(id)
    return jsonify({"result" : result})

@app.route("/GET/ALLID", methods=["POST"])
def get_allid():
    #result = jsonify( {"result" : "success", "id" : rs[0], "name" : rs[1], "phone" : rs[2]} )

    result = []

    data = dataSelectAll()
    for item in data:
        result.append({"id" : item[0], "name" : item[1], "phone" : item[2]})

    print result

    return jsonify(result)


@app.route('/')
def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8888)
    print "Server shutdown.."