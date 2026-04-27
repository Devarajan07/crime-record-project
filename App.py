from flask import Flask, render_template, flash, request, session, send_file
from flask import render_template, redirect, url_for, request
# from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField


import mysql.connector

app = Flask(__name__)
app.config['DEBUG']
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


@app.route("/")
def homepage():
    return render_template('index.html')


@app.route("/AdminLogin")
def AdminLogin():
    return render_template('AdminLogin.html')


@app.route("/NewOfficer")
def NewOfficer():
    return render_template('NewOfficer.html')


@app.route("/OfficerLogin")
def OfficerLogin():
    return render_template('OfficerLogin.html')

@app.route("/CourtLogin")
def CourtLogin():
    return render_template('CourtLogin.html')


@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    error = None
    if request.method == 'POST':
        if request.form['uname'] == 'admin' and request.form['password'] == 'admin':
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1citizenandpolicedb')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb ")
            data = cur.fetchall()
            return render_template('AdminHome.html', data=data)


        else:
            flash("Username Or Password Incorrect!")
            return render_template('AdminLogin.html')


@app.route("/AdminHome")
def AdminHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1citizenandpolicedb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb ")
    data = cur.fetchall()
    return render_template('AdminHome.html', data=data)


@app.route("/FirInfo")
def FirInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1citizenandpolicedb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM firtb ")
    data = cur.fetchall()
    return render_template('AFirInfo.html', data=data)


@app.route("/newofficer", methods=['GET', 'POST'])
def newofficer():
    if request.method == 'POST':
        name1 = request.form['name']
        email = request.form['email']
        pnumber = request.form['phone']
        address = request.form['address']
        des = request.form['des']
        sno = request.form['sno']
        uname = request.form['uname']
        password = request.form['psw']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1citizenandpolicedb')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO regtb VALUES ('','" + name1 + "','" + pnumber + "','" + email + "','" + address + "','" + des + "','" + sno + "','" + uname + "','" + password + "')")
        conn.commit()
        conn.close()
        # return 'file register successfully'
        flash('Office Info Save successfully')

    return render_template('NewOfficer.html')


@app.route("/oflogin", methods=['GET', 'POST'])
def oflogin():
    error = None
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        session['oname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1citizenandpolicedb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where username='" + username + "' and Password='" + password + "'")
        data = cursor.fetchone()
        if data is None:
            flash('Username or Password is wrong')
            return render_template('OfficerLogin.html')
        else:
            session['sno'] = data[6]

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1citizenandpolicedb')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb where username='" + username + "' and Password='" + password + "'")
            data = cur.fetchall()

            return render_template('OfficerHome.html', data=data)


@app.route("/NewFIR")
def NewFIR():
    sno = session['sno']
    return render_template('NewFIR.html', sno=sno)



@app.route("/NewEvidence")
def NewEvidence():
    sno = session['sno']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1citizenandpolicedb')
    cur = conn.cursor()
    cur.execute("SELECT FIRNumber FROM firtb  ")
    data = cur.fetchall()

    return render_template('NewEvidence.html', data=data,sno=sno)


@app.route("/OfficerHome")
def OfficerHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1citizenandpolicedb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb where Username='" + session['oname'] + "' ")
    data = cur.fetchall()
    return render_template('OfficerHome.html', data=data)


import hmac
import hashlib
import binascii


def create_sha256_signature(key, message):
    byte_key = binascii.unhexlify(key)
    message = message.encode()
    return hmac.new(byte_key, message, hashlib.sha256).hexdigest().upper()


@app.route("/newfir", methods=['GET', 'POST'])
def newfir():
    if request.method == 'POST':
        import random
        oname = session['oname']
        sno = session['sno']
        fno = request.form['fno']
        date = request.form['date']
        appli = request.form['appli']
        aadd = request.form['aadd']
        res = request.form['res']
        info = request.form['info']
        section =request.form['section']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1citizenandpolicedb')
        cursor = conn.cursor()
        cursor.execute("SELECT  *  FROM firtb ")
        data = cursor.fetchone()

        if data:

            conn1 = mysql.connector.connect(user='root', password='', host='localhost', database='1citizenandpolicedb')
            cursor1 = conn1.cursor()
            cursor1.execute("select max(id) from firtb")
            da = cursor1.fetchone()
            if da:
                d = da[0]
                print(d)

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1citizenandpolicedb')
            cursor = conn.cursor()
            cursor.execute("SELECT  *  FROM firtb where  id ='" + str(d) + "'   ")
            data = cursor.fetchone()
            if data:
                hash1 = data[11]
                num1 = random.randrange(1111, 9999)
                hash2 = create_sha256_signature("E49756B4C8FAB4E48222A3E7F3B97CC3", str(num1))

                conn = mysql.connector.connect(user='root', password='', host='localhost',
                                               database='1citizenandpolicedb')
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO firtb VALUES ('','" + oname + "','" + sno + "','" + fno + "','" + date + "','" + appli + "','" + aadd + "','" +
                    res + "','" + info + "','" + section + "','" + hash1 + "','" + hash2 + "')")
                conn.commit()
                conn.close()
                # return 'file register successfully'
                flash('FIR Info Save successfully')



        else:

            hash1 = '0'
            num1 = random.randrange(1111, 9999)
            hash2 = create_sha256_signature("E49756B4C8FAB4E48222A3E7F3B97CC3", str(num1))
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1citizenandpolicedb')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO firtb VALUES ('','" + oname + "','" + sno + "','" + fno + "','" + date + "','" + appli + "','" + aadd + "','" +
                res + "','" + info + "','" + section + "','"+ hash1 +"','"+ hash2 +"')")
            conn.commit()
            conn.close()
            # return 'file register successfully'
            flash('FIR Info Save successfully')



    return render_template('NewFIR.html')


@app.route("/newEvidence", methods=['GET', 'POST'])
def newEvidence():
    if request.method == 'POST':
        import random
        file = request.files['file']
        fnew = random.randint(1111, 9999)
        savename = str(fnew) + ".png"
        file.save("static/upload/" + savename)

        oname = session['oname']
        sno = session['sno']
        fir = request.form['fir']
        date = request.form['date']

        ename = request.form['ename']
        location = request.form['location']
        info = request.form['info']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1citizenandpolicedb')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO evidancetb VALUES ('','" + oname + "','" + sno + "','" + fir + "','" + date + "','" + ename + "','" + location + "','" + info + "','"+ savename +"')")
        conn.commit()
        conn.close()
        flash('New Evidence Info Save successfully')

    return render_template('NewEvidence.html')


@app.route("/OFIRInfo")
def OFIRInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1citizenandpolicedb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM firtb where OfficerName='" + session['sno'] + "' ")
    data = cur.fetchall()
    return render_template('OFIRInfo.html', data=data)



@app.route("/ComplaintInfo")
def ComplaintInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1citizenandpolicedb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM crimetb where Status='Waiting' ")
    data = cur.fetchall()
    return render_template('ComplaintInfo.html', data=data)


@app.route("/EvidenceInfo")
def EvidenceInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1citizenandpolicedb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM evidancetb where OfficerName='" + session['oname'] + "' ")
    data = cur.fetchall()
    return render_template('EvidenceInfo.html', data=data)




@app.route("/AEvidenceInfo")
def AEvidenceInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1citizenandpolicedb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM evidancetb ")
    data = cur.fetchall()
    return render_template('AEvidenceInfo.html', data=data)


@app.route("/CaseHistory")
def CaseHistory():

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1citizenandpolicedb')
    cur = conn.cursor()
    cur.execute("SELECT FIRNumber FROM firtb  ")
    data3 = cur.fetchall()

    return render_template('CaseHistory.html', data3=data3)


@app.route("/search", methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        fir = request.form['fir']
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1citizenandpolicedb')
        cur = conn.cursor()
        cur.execute("SELECT * FROM firtb where FIRNumber='" + fir + "' ")
        data = cur.fetchall()

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1citizenandpolicedb')
        cur = conn.cursor()
        cur.execute("SELECT * FROM evidancetb where FIRNumber='" + fir + "' ")
        data1 = cur.fetchall()


        return render_template('CaseHistory.html', data=data,data1=data1)

@app.route("/search1", methods=['GET', 'POST'])
def search1():
    if request.method == 'POST':
        fir = request.form['fir']
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1citizenandpolicedb')
        cur = conn.cursor()
        cur.execute("SELECT * FROM firtb where FIRNumber='" + fir + "' ")
        data = cur.fetchall()

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1citizenandpolicedb')
        cur = conn.cursor()
        cur.execute("SELECT * FROM evidancetb where FIRNumber='" + fir + "' ")
        data1 = cur.fetchall()


        return render_template('CCaseHistory.html', data=data,data1=data1)


@app.route("/NewUser")
def NewUser():
    return render_template('NewUser.html')


@app.route("/UserLogin")
def UserLogin():
    return render_template('UserLogin.html')


@app.route("/newuser", methods=['GET', 'POST'])
def newuser():
    if request.method == 'POST':
        name1 = request.form['name']
        email = request.form['email']
        pnumber = request.form['phone']
        address = request.form['address']
        uname = request.form['uname']
        password = request.form['psw']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1citizenandpolicedb')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO usertb VALUES ('','" + name1 + "','" + pnumber + "','" + email + "','" + address + "','" + uname + "','" + password + "')")
        conn.commit()
        conn.close()
        # return 'file register successfully'
        flash('User Info Save successfully')

    return render_template('NewUser.html')





@app.route("/UserHome")
def UserHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1citizenandpolicedb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM usertb where Username='" + session['uname'] + "' ")
    data = cur.fetchall()
    return render_template('UserHome.html', data=data)



@app.route("/userlogin", methods=['GET', 'POST'])
def userlogin():
    error = None
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        session['uname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1citizenandpolicedb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from usertb where username='" + username + "' and Password='" + password + "'")
        data = cursor.fetchone()
        if data is None:
            flash('Username or Password is wrong')
            return render_template('UserLogin.html')
        else:
            session['sno'] = data[6]

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1citizenandpolicedb')
            cur = conn.cursor()
            cur.execute("SELECT * FROM usertb where username='" + username + "' and Password='" + password + "'")
            data = cur.fetchall()

            return render_template('UserHome.html', data=data)




@app.route("/NewNoc")
def NewNoc():
    return render_template('NewNoc.html')


@app.route("/newnoc", methods=['GET', 'POST'])
def newnoc():
    if request.method == 'POST':
        name1 = request.form['name']
        add = request.form['add']
        date = request.form['date']
        oname = request.form['oname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1citizenandpolicedb')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO noctb VALUES ('','" + name1 + "','" + add + "','" + date + "','" + oname + "','Waiting','','"+ session['uname'] +"')")
        conn.commit()
        conn.close()
        # return 'file register successfully'
        flash('Noc Info Save successfully')

    return render_template('NewNoc.html')



@app.route("/UNDetails")
def UNDetails():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1citizenandpolicedb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM noctb where Username='" + session['uname'] + "' ")
    data = cur.fetchall()
    return render_template('UNDetails.html', data=data)



@app.route("/ONDetails")
def ONDetails():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1citizenandpolicedb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM noctb where Status='Waiting'")
    data = cur.fetchall()
    return render_template('ONDetails.html', data=data)



@app.route("/Reject")
def Reject():
    id = request.args.get('id')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1citizenandpolicedb')
    cursor = conn.cursor()
    cursor.execute(
        "update noctb set Status='Rejected' where nid='" + id + "'")
    conn.commit()
    conn.close()
    flash('Noc Application is Rejected...!')
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1citizenandpolicedb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM noctb where Status='Waiting'")
    data = cur.fetchall()
    return render_template('ONDetails.html', data=data)



@app.route("/add")
def add():
    id = request.args.get('id')
    session['pid'] = id
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1citizenandpolicedb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM noctb  where nid='" + id + "' ")
    data = cur.fetchall()
    return render_template('ONUpdate.html', data=data)




@app.route("/update", methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        pid = session['pid']

        file = request.files['file']
        file.save("static/upload/" + file.filename)
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1citizenandpolicedb')
        cursor = conn.cursor()
        cursor.execute(
            "update noctb set Document='" + file.filename + "',Status='Approved' where nid='" + pid + "' ")
        conn.commit()
        conn.close()

        flash('Noc Approval successfully')
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1citizenandpolicedb')
        cur = conn.cursor()
        cur.execute("SELECT * FROM noctb where Status='Waiting'")
        data = cur.fetchall()
        return render_template('ONDetails.html', data=data)


@app.route('/download')
def download():
    id = request.args.get('id')
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1citizenandpolicedb')
    cursor = conn.cursor()
    cursor.execute("SELECT  *  FROM noctb where  nid = '" + str(id) + "'")
    data = cursor.fetchone()
    if data:
        filename = "static\\upload\\"+data[6]
        return send_file(filename, as_attachment=True)
    else:
        return 'Incorrect username / password !'




@app.route("/add1")
def add1():
    id = request.args.get('id')
    session['pid'] = id
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1citizenandpolicedb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM crimetb  where id='" + id + "' ")
    data = cur.fetchall()
    return render_template('Cadd.html', data=data)



@app.route("/update1", methods=['GET', 'POST'])
def update1():
    if request.method == 'POST':
        pid = session['pid']

        info = request.form['info']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1citizenandpolicedb')
        cursor = conn.cursor()
        cursor.execute(
            "update crimetb set Info='" + info + "',Status='Completed',OfficerName='"+ session['oname'] +"' where id='" + pid + "' ")
        conn.commit()
        conn.close()

        flash('Complaint Action Updated successfully')
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1citizenandpolicedb')
        cur = conn.cursor()
        cur.execute("SELECT * FROM crimetb where Status='Waiting'")
        data = cur.fetchall()
        return render_template('Cadd.html', data=data)




@app.route("/UComplaintInfo")
def UComplaintInfo():
    uname = session['uname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1citizenandpolicedb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM crimetb where UserName='"+ uname +"' ")
    data = cur.fetchall()
    return render_template('UComplaintInfo.html', data=data)



@app.route("/NewComplaint")
def NewComplaint():
    #sno = session['sno']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1citizenandpolicedb')
    cur = conn.cursor()
    cur.execute("SELECT StationNo FROM regtb  ")
    data = cur.fetchall()
    return render_template('NewComplaint.html', data=data)


@app.route("/newcomplaint", methods=['GET', 'POST'])
def newcomplaint():
    if request.method == 'POST':
        #oname = request.form['oname']
        #sno = request.form['sno']
        date = request.form['date']
        appli = request.form['appli']
        aadd = request.form['aadd']
        res = request.form['res']
        info = request.form['info']
        uname = session['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1citizenandpolicedb')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO crimetb VALUES ('','','','" + date + "','" + appli + "','" + aadd + "','" + res + "','" + info + "','Waiting','','"+ uname +"')")
        conn.commit()
        conn.close()
        flash('New Complaint Info Save successfully')

    return render_template('NewComplaint.html')

@app.route("/AComplaintInfo")
def AComplaintInfo():
    # sno = session['sno']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1citizenandpolicedb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM crimetb where StationNo=''")
    data = cur.fetchall()
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1citizenandpolicedb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM crimetb")
    data1 = cur.fetchall()
    return render_template('AComplaintInfo.html', data=data,data1=data1)




@app.route("/add2")
def add2():
    id = request.args.get('id')
    session['pid'] = id
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1citizenandpolicedb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM crimetb  where id='" + id + "' ")
    data = cur.fetchall()
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1citizenandpolicedb')
    cur = conn.cursor()
    cur.execute("SELECT StationNo FROM regtb  ")
    data1 = cur.fetchall()
    return render_template('Aupdate.html', data=data,data1=data1)



@app.route("/update2", methods=['GET', 'POST'])
def update2():
    if request.method == 'POST':
        pid = session['pid']

        info = request.form['info']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1citizenandpolicedb')
        cursor = conn.cursor()
        cursor.execute(
            "update crimetb set StationNo='" + info + "' where id='" + pid + "' ")
        conn.commit()
        conn.close()

        flash('Complaint Action Updated successfully')
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1citizenandpolicedb')
        cur = conn.cursor()
        cur.execute("SELECT * FROM crimetb where StationNo=''")
        data = cur.fetchall()
        return render_template('AComplaintInfo.html', data=data)





if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
