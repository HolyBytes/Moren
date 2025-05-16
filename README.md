# **📱 MOREN AI Assistant - Dokumentasi Lengkap (Termux & Desktop) 🖥️**

## **🌟 Deskripsi**
**MOREN** adalah asisten AI berbasis terminal yang menggunakan model **DeepHermes-3-Mistral 24B** dari OpenRouter. Dirancang untuk memberikan pengalaman chatting yang **santun, informatif, dan estetik** dengan nilai-nilai akhlak yang baik.

## **📂 Struktur File**
```
MoyrenAI/
├── README.md               # Dokumentasi proyek
├── tools_ai.py             # Script utama MOREN AI
└── requirements.txt        # Dependensi yang diperlukan
```

## **🛠️ Fungsi Utama**
| **Fungsi** | **Kegunaan** | **Dapat Diedit?** |
|------------|-------------|------------------|
| **`animated_loading()`** | Animasi saat AI berpikir | ✅ |
| **`get_time_greeting()`** | Salam berdasarkan waktu | ✅ |
| **`chat_with_ai()`** | Komunikasi dengan API | ⚠️ (Hati-hati) |
| **`border_box()`** | Membuat kotak dekoratif | ✅ |
| **`display_header()`** | Menampilkan header MOREN | ⚠️ |

## **✨ Bagian yang Bisa Diedit**
1. **🎨 Tampilan & Animasi**
   - Warna (`Colors` class)
   - Animasi loading (`animated_loading()`)
   - Salam waktu (`get_time_greeting()`)
   - Format tanggal (`get_time_info()`)

2. **💬 Sistem Prompt**
   - Sesuaikan kepribadian AI dalam `system_prompt`

3. **🔑 Konfigurasi API**
   - API Key (Ganti dengan milik sendiri)
   - Model AI (Pilihan di OpenRouter)

## **⛔ Jangan Diedit (Kecuali Paham Kode)**
1. **Struktur utama `chat_with_ai()`** - Agar API tidak error
2. **`calculate_max_tokens()`** - Memengaruhi biaya & stabilitas
3. **Import library** - Bisa menyebabkan program error

## **🐞 Perbaikan Bug & Typos**
1. **Kesalahan import:**
   ```python
   # Salah:
   from colorman import init, Fore, Back, Style
   
   # Benar:
   from colorama import init, Fore, Back, Style
   ```

2. **Kesalahan nama library:**
   ```python
   # Salah:
   from prettytable import Prettytable
   
   # Benar:
   from prettytable import PrettyTable
   ```

3. **Typo pada nama warna:**
   ```python
   # Salah:
   PRIMARY = Fore.COM  # Seharusnya CYAN
   RECENT = Fore.VELLOW  # Seharusnya YELLOW
   TDST = Fore.WEITE  # Seharusnya WHITE
   ```

## **📱 Cara Install di Termux**
1. **📥 Instal Python & Git**
   ```bash
   pkg update && pkg upgrade
   pkg install python git
   ```

2. **📋 Clone Repository**
   ```bash
   git clone https://github.com/HolyBytes/MoyrenAI.git
   cd MoyrenAI
   ```

3. **📚 Instal Dependensi**
   ```bash
   pip install requests colorama prettytable
   ```

4. **🚀 Jalankan MOREN AI**
   ```bash
   python tools_ai.py
   ```

## **💻 Cara Install di Windows/Linux**
1. **📥 Install Python 3.8+**
   - Download dari [python.org](https://www.python.org/downloads/)
   - Pastikan "Add Python to PATH" dicentang

2. **📋 Clone Repository**
   ```bash
   git clone https://github.com/HolyBytes/MoyrenAI.git
   cd MoyrenAI
   ```

3. **🧪 Buat Virtual Environment (Opsional)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

4. **📚 Install Dependensi**
   ```bash
   pip install -r requirements.txt
   # atau
   pip install requests colorama prettytable
   ```

5. **🚀 Jalankan Script**
   ```bash
   python tools_ai.py
   ```

## **✨ Kelebihan MOREN**
- 😊 **Ramah & Santun** – Dibangun dengan nilai-nilai akhlak yang baik
- 🎭 **Tampilan Estetik** – Warna, animasi, dan ASCII art menarik
- ⚙️ **Dinamis** – Token dihitung otomatis berdasarkan panjang pesan
- 🧠 **Multi-fungsi** – Untuk edukasi, hiburan, dan bantuan teknis
- 🔧 **Customizable** – Banyak bagian yang bisa disesuaikan

## **⚠️ Keterbatasan**
- 🌐 **Bergantung API** – Memerlukan internet & API key
- 💰 **Potensi Biaya** – Jika menggunakan model berbayar
- 🔌 **Tidak Offline** – Tidak bisa berjalan tanpa OpenRouter
- 📟 **Terbatas di Terminal** – Belum memiliki GUI

## **🚀 Fitur yang Bisa Dikembangkan**
1. **🖼️ GUI dengan Tkinter** (Agar bisa dipakai tanpa terminal)
2. **📴 Mode Offline** (Menggunakan model lokal seperti Llama.cpp)
3. **📝 Riwayat Chat** (Simpan percakapan ke file `.txt`)
4. **🔊 Suara (TTS)** (Tambahkan text-to-speech dengan `gTTS`)

## **📩 Kontak & Dukungan**
Untuk pertanyaan atau kolaborasi:
- **🌐 GitHub**: [github.com/HolyBytes](https://github.com/HolyBytes)
- **💬 Forum Diskusi**: [Coming Soon]

## **🔐 Lisensi**
MOREN menggunakan lisensi **MIT**:
- ✅ Gratis untuk proyek pribadi & komersial
- ✅ Boleh dimodifikasi dengan mencantumkan credit
- ⚠️ Tidak bertanggung jawab atas penyalahgunaan

## **🎯 Kesimpulan**
**MOREN AI** adalah asisten AI terminal yang santun, estetik dan customizable. Meski memiliki beberapa keterbatasan (seperti ketergantungan API), MOREN dapat dikembangkan sesuai kebutuhan pengguna.

**Terima kasih telah memilih MOREN AI! Semoga bermanfaat dan membawa keberkahan dalam aktivitas Anda. 🌷**
