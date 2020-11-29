from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
from flask_mysqldb import MySQL
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt

#  Kullanıcı Kayıt Formu
class RegisterForm(Form):
    name= StringField("İsim",validators=[validators.Length(min=2,max=15),validators.DataRequired("Lütfen Bütün alanları doldurunuz.")])
    surname= StringField("Soyisim",validators=[validators.Length(min=2,max=15),validators.DataRequired("Lütfen Bütün alanları doldurunuz.")])
    email=StringField("Email Adresi",validators=[validators.Email("Email adresi geçerli değil."),validators.DataRequired("Lütfen Bütün alanları doldurunuz.")])
    password=PasswordField("Parola:",validators=[
        validators.DataRequired("Şifre alanı boş bırakılamaz..."),
        validators.equal_to(fieldname="confirm",message="girilen şifreler aynı değil!")

    ])
    confirm= PasswordField("Şifre Doğrula:",validators=[
        validators.DataRequired("Şifre alanı boş bırakılamaz..."),
        validators.equal_to(fieldname="confirm",message="girilen şifreler aynı değil!")

    ])




app=Flask(__name__)
app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]=""
app.config["MYSQL_DB"]="dileyenbulur"
app.config["MYSQL_CURSORCLASS"]="DictCursor"

mysql=MySQL(app=app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ek-hizmetler")
def ek_hizmetler():
    return render_template("ek_hizmetler.html")
@app.route("/nasil-calisir")
def nasil_calisir():
    return render_template("nasil_calisir.html")
@app.route("/kayit-ol",methods=["GET","POST"])
def kayit_ol():
    form= RegisterForm(request.form)

    
    if form.validate_on_submit():
        return redirect('index')

        
    else:
        return render_template("kayit_ol.html",form=form)

    
@app.route("/giris-yap")
def giris_yap():
    return render_template("giris_yap.html")
if __name__=="__main__":
    app.run(debug=True)