from tkinter import *
from tkinter import messagebox
root = Tk()

#Pencere Boyutu
root.geometry()
#Sıra Değişkenleri
r = 0
c = 0
#Giriş 1
Giriş_1_info = Label(root, text = "İlk sayı:", font = "20")
Giriş_1_info.grid(row = r , column = c)
Giriş_1 = Entry(root, bg  = "grey", width = 10)
Giriş_1.grid(row = r + 1, column = c, padx = 10, pady = 10)
#Giriş 2
Giriş_2_info = Label(root, text = "İkinci sayı:", font = "20")
Giriş_2_info.grid(row = r  , column = c + 1)
Giriş_2 = Entry(root, bg  = "grey", width = 10)
Giriş_2.grid(row = r + 1, column = c + 1,  padx = 10, pady = 10)
#İşlemler
def Toplama () : 
    try:
        global Sonuç
        Sonuç =str(int(Giriş_1.get()) + int(Giriş_2.get()))
        #Sonuç Çubuğu
        SonuçÇubuğu = Label(root, text = "Sonuç: " + Sonuç , font = 25)
        SonuçÇubuğu.grid(row = r + 5, columnspan = 2)
    except ValueError:
        messagebox.showinfo("HATA", "SAYI GİRİN")

def Çıkarma () :
    try:
        global Sonuç
        Sonuç =str(int(Giriş_1.get()) - int(Giriş_2.get()))
        #Sonuç Çubuğu
        SonuçÇubuğu = Label(root, text = "Sonuç: " + Sonuç , font = 25)
        SonuçÇubuğu.grid(row = r + 5, columnspan = 2)
    except ValueError:
        messagebox.showinfo("HATA", "SAYI GİRİN")
def Çarpma () :
    try:
        global Sonuç
        Sonuç =str(int(Giriş_1.get())*int(Giriş_2.get()))
        #Sonuç Çubuğu
        SonuçÇubuğu = Label(root, text = "Sonuç: " + Sonuç , font = 25)
        SonuçÇubuğu.grid(row = r + 5, columnspan = 2)
    except ValueError:
        messagebox.showinfo("HATA", "SAYI GİRİN")
def Bölme () :
    try :
        global Sonuç
        Sonuç =str(int(Giriş_1.get())/int(Giriş_2.get()))
        #Sonuç Çubuğu
        SonuçÇubuğu = Label(root, text = "Sonuç: " + Sonuç , font = 25)
        SonuçÇubuğu.grid(row = r + 5, columnspan = 2)
    except ValueError:
        messagebox.showinfo("HATA", "SAYI GİRİN")
    except ZeroDivisionError:
        messagebox.showinfo("TANIMSIZ", "BÖLEN 0 OLAMAZ")
#İşlem seçimi
ButonGenişliği = 5
ButonYüksekliği = 1
ButonBoşluğu_yatay = 1
ButonBoşluğu_dikey = 1
İşlem_Seçimi_info = Label(root, text = "Hangi işlem ?", font = "20")
İşlem_Seçimi_info.grid(row = r + 2, columnspan = 2)
İşlem_Seçimi_1 = Button(root, text = "+", font = "50", width = ButonGenişliği, height = ButonYüksekliği, command = Toplama)
İşlem_Seçimi_1.grid(row = r + 3 , column = c, padx = ButonBoşluğu_yatay , pady = ButonBoşluğu_dikey)
İşlem_Seçimi_2 = Button(root, text = "-", font = "30", width = ButonGenişliği, height = ButonYüksekliği, command = Çıkarma)
İşlem_Seçimi_2.grid(row = r + 3 , column = c + 1, padx = ButonBoşluğu_yatay , pady = ButonBoşluğu_dikey)
İşlem_Seçimi_3 = Button(root, text = "*", font = "30", width = ButonGenişliği, height = ButonYüksekliği, command = Çarpma)
İşlem_Seçimi_3.grid(row = r + 4 , column = c, padx = ButonBoşluğu_yatay , pady = ButonBoşluğu_dikey)
İşlem_Seçimi_4 = Button(root, text = "/", font = "30", width = ButonGenişliği, height = ButonYüksekliği, command = Bölme)
İşlem_Seçimi_4.grid(row = r + 4 , column = c + 1, padx = ButonBoşluğu_yatay , pady = ButonBoşluğu_dikey)

root.mainloop()