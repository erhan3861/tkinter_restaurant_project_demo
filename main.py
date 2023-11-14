import tkinter as tk
from ders_atama import *
from tkinter import messagebox
from tkinter import PhotoImage  # Resim eklemek için PhotoImage kullanılır
from PIL import Image, ImageTk
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from passlib.hash import sha256_crypt
import anasayfa
from ders_atama import *
import random

# SQLite veritabanı oluşturma
engine = create_engine('sqlite:///user.db', echo=False)
Base = declarative_base()

# Kullanıcı bilgilerini temsil eden veritabanı tablosu
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True) 
    username = Column(String, unique=True) # eşsiz
    password = Column(String)

Base.metadata.create_all(engine)

# Tkinter uygulaması oluşturma
app = tk.Tk()
app.title("Login")
app.geometry("1000x600")

# Arka plan resmini eklemek için ImageTk kullanımı
bg_image = Image.open("images/img.jpg")  # Arka plan resmi dosyasının adını ve yolunu belirtin
bg_image = bg_image.resize((1000, 600), Image.BILINEAR)  # Resmi pencere boyutuna uygun olarak yeniden boyutlandırın
bg_image = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(app, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Giriş bilgileri giriş kutuları
bg_color = "#b3daff"
username_label = tk.Label(app, text="Kullanıcı Adı:", font=("Helvetica", 16), bg=bg_color)
username_label.place(x=760,y=200)

username_entry = tk.Entry(app, font=("Helvetica", 16), bg=bg_color)
username_entry.place(x=700,y=250)

password_label = tk.Label(app, text="Şifre:", font=("Helvetica", 16), bg=bg_color)
password_label.place(x=795,y=300)

password_entry = tk.Entry(app, show="*", font=("Helvetica", 16), bg=bg_color)
password_entry.place(x=700,y=350)


# Kullanıcıyı veritabanına kaydetme işlemi
def save_user():
    username = username_entry.get()
    password = password_entry.get()

    # Şifreyi güvenli bir şekilde hashleme
    hashed_password = sha256_crypt.hash(password)

    # SQLAlchemy ile kullanıcı bilgilerini veritabanına kaydetme
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        new_user = User(username=username, password=hashed_password)
        session.add(new_user)
        session.commit() # kayıt etti
        session.close()
        messagebox.showinfo("Başarılı", "Kullanıcı başarıyla kaydedildi.")
    except:
        messagebox.showerror("Hata", "Kullanıcı kayıt edilemedi!")

# Kullanıcının veritabanına giriş işlemi
def login():
    global app
    username = username_entry.get()
    password = password_entry.get()
    

    # SQLAlchemy ile kullanıcı bilgilerini veritabanından sorgulama
    Session = sessionmaker(bind=engine)
    session = Session()

    user = session.query(User).filter_by(username=username).first()

    if user and sha256_crypt.verify(password, user.password):
        messagebox.showinfo("Başarılı", "Giriş başarılı!")
        liste = app.place_slaves()
        for l in liste:
            l.destroy() # yok et
        liste = app.pack_slaves()

        for l in liste:
            l.destroy() # yok et

          

        if user.username == "ihsa":
            admin_wn = Uygulama(app)
            yeni_musteri_btn = tk.Button(app, text="Yeni Müsteri Ekle", command=admin_wn.yeni_musteri_ekle)
            yeni_musteri_btn.pack()
            yeni_yemek_btn = tk.Button(app, text="Yeni Yemek Ekle", command=admin_wn.yeni_yemek_ekle)
            yeni_yemek_btn.pack()
            # degerlendirme = tk.Button(app, text="Bizi Degerlendirin", command=app)
            # degerlendirme.place()
        else:
            anasayfa.make_widgets(app)  


                
    else:
        messagebox.showerror("Hata", "Kullanıcı adı veya şifre yanlış!")
    session.close()

def yemek_oner():
    yemekler = ["kebap","lahmacun","pizza"]
    label_oneri.config(text=random.choice(yemekler))
    label_oneri.place(x=400,y=200)

# Başlık etiketi
label_oneri = tk.Label(app, text="Günün Menüsü : ", font=("Arial", 18))



# Kaydet ve Giriş butonları
save_button = tk.Button(app, text="Kaydet", command=save_user, font=("Helvetica", 16))
save_button.place(x=800,y=450)

login_button = tk.Button(app, text="Giriş   ", command=login, font=("Helvetica", 16))
login_button.place(x=700,y=450)

yemek_önerileri = tk.Button(app, text="Yemek Önerileri", command=yemek_oner)
yemek_önerileri.pack()

chat_image = Image.open("images/chat.jpg").resize((150, 150))
chat_photo = ImageTk.PhotoImage(chat_image)






# Tkinter uygulamasını başlatma
app.mainloop()        