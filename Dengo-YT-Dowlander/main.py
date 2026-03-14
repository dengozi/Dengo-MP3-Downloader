import customtkinter as ctk
import yt_dlp
from tkinter import messagebox, filedialog
import threading
import os

# Varsayılan klasör Masaüstü
secilen_klasor = os.path.join(os.path.expanduser("~"), "Desktop")


def klasor_sec():
    global secilen_klasor
    dizin = filedialog.askdirectory()
    if dizin:
        secilen_klasor = dizin
        klasor_etiketi.configure(text=f"Klasör: {os.path.basename(secilen_klasor)}")


def indir_thread_baslat():
    threading.Thread(target=indir_islemi, daemon=True).start()


def indir_islemi():
    video_url = link_giris.get()

    if not video_url:
        messagebox.showwarning("Hata", "Lütfen bir link yapıştır!")
        return

    try:
        durum_etiketi.configure(text="Ses dosyası hazırlanıyor...", text_color="yellow")

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(secilen_klasor, '%(title)s.%(ext)s'),
            'noplaylist': True,
            # EĞER FFmpeg'i bir klasöre çıkardıysan yolu buraya ekle:
            # 'ffmpeg_location': r'C:\ffmpeg\bin',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])

        durum_etiketi.configure(text="MP3 İndirildi!", text_color="green")
        messagebox.showinfo("Başarılı", "Şarkı başarıyla MP3 olarak kaydedildi!")

    except Exception as e:
        durum_etiketi.configure(text="Hata!", text_color="red")
        messagebox.showerror("Hata", f"İndirme başarısız: {e}")


# --- Arayüz ---
ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.title("Dengo MP3 Downloader")
app.geometry("500x400")

ctk.CTkLabel(app, text="🎵 YouTube MP3 İndirici", font=("Arial", 24, "bold")).pack(pady=30)

link_giris = ctk.CTkEntry(app, placeholder_text="Şarkı linkini buraya yapıştır...", width=400, height=45)
link_giris.pack(pady=10)

secme_butonu = ctk.CTkButton(app, text="📁 Kaydedilecek Yeri Seç", fg_color="transparent", border_width=2,
                             command=klasor_sec)
secme_butonu.pack(pady=10)

klasor_etiketi = ctk.CTkLabel(app, text="Varsayılan: Masaüstü", font=("Arial", 11, "italic"))
klasor_etiketi.pack()

indir_butonu = ctk.CTkButton(app, text="MP3 OLARAK İNDİR", command=indir_thread_baslat,
                             font=("Arial", 16, "bold"), height=50, fg_color="#1DB954",
                             hover_color="#18a34a")  # Spotify yeşili :)
indir_butonu.pack(pady=30)

durum_etiketi = ctk.CTkLabel(app, text="Hazır", font=("Arial", 12))
durum_etiketi.pack()

app.mainloop()