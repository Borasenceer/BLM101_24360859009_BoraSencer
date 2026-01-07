# Bilgisayar Mühendisliğine Giriş Dönem Projesi
# Bora Sencer 24360859009
# Konumuz Python ile HTML Dosyası Oluşturma

print("--Web Sitesi Oluşturucu--")
print("-" * 30)

# Kullanıcıdan verileri alıyoruz
ad_soyad = input("1- Adınız ve Soyadınız: ")
bolum = input("2- Okuduğunuz Bölüm: ")
dersler = input("3- Aldığınız Dersleri Yazınız(Virgülle ayırın): ")
biyografi = input("4- Biyografiniz: ")
hedef = input("5- Hedefleriniz: ")
konum = input("6- Nerede Kalıyorsunuz ?: ")

# Virgülleri HTML liste etiketleri ile değiştiriyoruz (replace'i bunun için kullanıyoruz)
ders_html_kodu = dersler.replace(",", "</li><li>")

# Başa ve sona eksik kalan etiketleri ekliyoruz
ders_html_kodu = "<li>" + ders_html_kodu + "</li>"

# Şimdi HTML kodunu hazırlıyoruz

html_kod = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{ad_soyad} - Web Sayfası</title>
</head>
<body style="background-color: #f4f4f4; margin: 40px;">

    <!-- Hoşgeldin yazısı: Kırmızı, kalın ve büyük -->
    <div style="color: red; font-weight: bold; font-size: 40px; margin-bottom: 20px;">
        Web Sayfama Hoşgeldiniz!
    </div>

    <!-- İsim: Siyah ve altına gri çizgi çekilmiş -->
    <h1 style="color: black; border-bottom: 2px solid gray;">{ad_soyad}</h1>
    
    <p style="font-size: 17px;"><strong>Bölüm:</strong> {bolum}</p>
    <p style="font-size: 17px;"><strong>Konum:</strong> {konum}</p>

    <!-- Aldığım dersler kısmı: Lacivert -->
    <h2 style="color: navy;">Aldığım Dersler</h2>
    
    <!-- Liste: Arka planı beyaz -->
    <ul>
        {ders_html_kodu}
    </ul>
    
    <!-- Biyografi Başlığı: Lacivert -->
    <h2 style="color: navy;">Biyografi</h2>
    <p>{biyografi}</p>

    <!-- Hedefler başlığı: Lacivert -->
    <h2 style="color: navy;">Hedefler</h2>
    <p>{hedef}</p>

</body>
</html>
"""

# Burda artık dosyayı kaydediyoruz (open ile dosya açıyoruz w ile dosyaya yazıcağımızı söylüyoruz sonra yazıyoruz)
dosya = open("index.html", "w", encoding="utf-8")
dosya.write(html_kod)
dosya.close()

print("-" * 30)
print("index.html dosyası başarıyla oluşturuldu.")