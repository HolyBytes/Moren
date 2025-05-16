# **📌 MOREN AI Assistant - Panduan Lengkap (Termux & Desktop)**

Berikut adalah dokumentasi **lengkap** untuk menjalankan **MOREN AI** di Termux/Desktop, termasuk bagian yang bisa diedit, cara instalasi, dan perbaikan bug.

---

## **📂 Struktur File**
```
MoyrenAI/
├── README.md               # Dokumentasi proyek
├── tools_ai.py             # Script utama MOREN AI
└── requirements.txt        # Dependensi yang diperlukan
```

---

## **🛠️ Bagian yang Bisa & Tidak Bisa Diedit**

### **✅ Bisa Diedit (Customizable)**
| **File/Bagian**          | **Apa yang Bisa Diubah?**                  | **Contoh Modifikasi** |
|--------------------------|--------------------------------------------|-----------------------|
| **`tools_ai.py`**        | Warna (`Colors` class)                    | Ganti `PRIMARY = Fore.CYAN` jadi `PRIMARY = Fore.BLUE` |
|                          | Animasi loading (`animated_loading()`)     | Ubah simbol `⣾⣽⣻` jadi `⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏` |
|                          | Salam (`get_time_greeting()`)              | Tambahkan salam khusus seperti "Selamat berkah hari!" |
|                          | System Prompt (`system_prompt`)            | Sesuaikan kepribadian AI (contoh: jadi lebih formal) |
| **`README.md`**          | Deskripsi, instruksi, kontak               | Update sesuai kebutuhan proyek |

### **❌ Tidak Disarankan Diedit (Kecuali Paham Kode)**
| **File/Bagian**          | **Alasan**                                |
|--------------------------|-------------------------------------------|
| **Struktur `chat_with_ai()`** | Jika salah edit, API bisa error |
| **`calculate_max_tokens()`**  | Memengaruhi biaya & stabilitas API |
| **Import library** (`requests`, `colorama`, dll) | Jika dihapus, program error |

---

## **🔧 Perbaikan Bug & Typos**
Beberapa kesalahan dalam kode yang perlu diperbaiki:
1. **`colorama` salah ketik jadi `colorman`** (Baris 7)  
   ```python
   # Salah:
   from colorman import init, Fore, Back, Style
   
   # Benar:
   from colorama import init, Fore, Back, Style
   ```
2. **`PrettyTable` salah ketik jadi `Prettytable`** (Baris 8)  
   ```python
   # Salah:
   from prettytable import Prettytable
   
   # Benar:
   from prettytable import PrettyTable
   ```
3. **Kesalahan nama warna di `Colors` class**  
   ```python
   # Salah:
   PRIMARY = Fore.COM  # Seharusnya Fore.CYAN
   RECENT = Fore.VELLOW  # Seharusnya Fore.YELLOW
   TDST = Fore.WEITE  # Seharusnya Fore.WHITE
   ```

---

## **📥 Cara Install di Termux**
### **1. Instal Python & Git**
```bash
pkg update && pkg upgrade
pkg install python git
```

### **2. Clone Repository**
```bash
git clone https://github.com/HolyBytes/MoyrenAI.git
cd MoyrenAI
```

### **3. Instal Dependensi**
```bash
pip install requests colorama prettytable
```

### **4. Jalankan MOREN AI**
```bash
python tools_ai.py
```

---

## **💻 Cara Install di Windows/Linux**
### **1. Install Python 3.8+**
- Download dari [python.org](https://www.python.org/downloads/)  
- Pastikan **"Add Python to PATH"** dicentang.

### **2. Clone Repository (Git) atau Download Manual**
```bash
git clone https://github.com/HolyBytes/MoyrenAI.git
cd MoyrenAI
```

### **3. Buat Virtual Environment (Opsional)**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### **4. Install Dependensi**
```bash
pip install -r requirements.txt  # Jika ada
# atau
pip install requests colorama prettytable
```

### **5. Run Script**
```bash
python tools_ai.py
```

---

## **⚡ Fitur Tambahan yang Bisa Dikembangkan**
1. **GUI dengan Tkinter** (Agar bisa dipakai tanpa terminal).  
2. **Mode Offline** (Pakai model lokal seperti Llama.cpp).  
3. **Riwayat Chat** (Simpan percakapan ke file `.txt`).  
4. **Suara (TTS)** Tambahkan text-to-speech dengan `gTTS`.  

---

## **📌 Kesimpulan**
- ✔ **MOREN AI** siap dipakai di Termux & PC.  
- ✔ **Bug sudah diperbaiki** (typo `colorama`, `PrettyTable`, dll).  
- ✔ **Customizable** untuk warna, animasi, dan prompt.  
- ❌ **Jangan edit fungsi kritis** (`chat_with_ai()`, token calculation).  

**🚀 Selamat mencoba!** Untuk pertanyaan, buka **Issue** di [GitHub](https://github.com/HolyBytes/MoyrenAI).
