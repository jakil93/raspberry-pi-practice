import pymysql
from flask import Flask, render_template



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
        cur.execute(sql)
        db.commit()
    except all as e:
        print e
        db.rollback()

    dataDisconnect(db, cur)

def dataSelectOne():
    db, cur = dataConnect()

    sql = "select * from mysql_test"

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

app = Flask(__name__)

@app.route('/')
def index():
    rs = dataSelectAll()
    templateData = {'data' : rs}
    return render_template('index.html', **templateData)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8888)

