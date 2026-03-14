Bu depo, YouTube videolarını yüksek kaliteli MP3 dosyalarına dönüştüren modern arayüzlü masaüstü uygulamasının **kaynak kodlarını** içermektedir.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![CustomTkinter](https://img.shields.io/badge/UI-CustomTkinter-orange?style=for-the-badge)
![yt--dlp](https://img.shields.io/badge/Engine-yt--dlp-red?style=for-the-badge)

## 📂 Proje İçeriği

* **`main.py`**: Uygulamanın tüm mantığını, arayüz tasarımını ve indirme motorunu barındıran ana kaynak kodu.
* **`DengoDownloader.spec`**: PyInstaller ile uygulamanın nasıl paketlendiğini ve hangi kütüphanelerin dahil edildiğini gösteren yapılandırma dosyası.

## ⚙️ Teknik Özellikler

* **Multi-Threading:** İndirme işlemleri arka planda yürütülür, bu sayede arayüz (GUI) asla donmaz.
* **Dinamik Klasör Seçimi:** Kullanıcı `tkinter.filedialog` aracılığıyla dosyaların kaydedileceği dizini çalışma anında seçebilir.
* **Hata Yönetimi:** Geçersiz linkler veya bağlantı sorunları için kullanıcıya geri bildirim sağlayan hata yakalama blokları.

## 🛠️ Geliştiriciler İçin Çalıştırma Notları

Kodları yerel makinenizde çalıştırmak için:

1. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install customtkinter yt-dlp
