from smtplib import SMTP
import random
subject=" Brain Tournament 2021 Yılbaşı Çekiliş Sonucu "
Alici=["esmer07031993@gmail.com","muhammetalitulun@gmail.com","emryldrm2764@gmail.com","mustafakamayy@gmail.com","sametztrk6116@gmail.com","seffayldrm@gmail.com"]
Aliciisim=["Münir ESMER","Muhammet Ali TULUN","Emre YILDIRIM","Mustafa Kamay","Samet ÖZTÜRK","Sefa YILDIRIM"]
hediyealacaginkisi=["esmer07031993@gmail.com","muhammetalitulun@gmail.com","emryldrm2764@gmail.com","mustafakamayy@gmail.com","sametztrk6116@gmail.com","seffayldrm@gmail.com"]
Hediyealacaginkisiisim= ["Münir ESMER","Muhammet Ali TULUN","Emre YILDIRIM","Mustafa Kamay","Samet ÖZTÜRK","Sefa YILDIRIM"]
cekilisyapanmail = "restinwatch@gmail.com"
password = "kaptan@2760"
print(password)
kisisayisi=int(len(Alici))
print("kişi sayısı {}" .format(kisisayisi))
i=0
for i in range(0,kisisayisi):
    print("inin değeri :{} ".format(i))
    cekilis=random.randint(0,len(hediyealacaginkisi)-1)
    kisi1=str(hediyealacaginkisi[cekilis])
    kisi2=str(Alici[i])
    if kisi1!=kisi2:
        print("ifin içindeyiz :   hediyealacacağınkisi {}  Alici ise {}".format(hediyealacaginkisi[cekilis],Alici[i]))
        message = "Merhaba {};   bu arada bu bir test mesajıdır \n  Mükemmel bir hediye alman için şanslı kişin {} \n  Adres Bilgileri aşağıdaki gibidir.\n önemli not: Kamay çıkarsa kitaplık alın hukuk kitaplarını koysun gezegene adalaet dağıtsın.".format(Alici[i],hediyealacaginkisi[cekilis])
        print(message)
        del hediyealacaginkisi[cekilis]
        print(len(hediyealacaginkisi))
        #hediyealacaginkisi.remove(cekilis)
        icerik="Subject : {0}{1}\n\n".format(subject,message)

        mail=SMTP("smtp.gmail.com",587)
        #msg.encode("utf8")
        #mail=SMTP(smtp.gmail.com,587)
        mail.ehlo()
        mail.starttls()
        mail.login(cekilisyapanmail,password)
        mail.sendmail(cekilisyapanmail,Alici[i],message.encode("utf-8"))
        #mail.sendmail(cekilisyapanmail,Alici[i],message)
    else:
        i=i-1
        print("elsenin içindeyiz")



