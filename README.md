# Moyren AI Assistant - Panduan Instalasi di Termux

```
╔══════════════════════════════════════════════════════════════╗
║   ███╗   ███╗ ██████╗ ██╗   ██╗██████╗ ███████╗███╗   ██╗   ║
║   ████╗ ████║██╔═══██╗╚██╗ ██╔╝██╔══██╗██╔════╝████╗  ██║   ║
║   ██╔████╔██║██║   ██║ ╚████╔╝ ██████╔╝█████╗  ██╔██╗ ██║   ║
║   ██║╚██╔╝██║██║   ██║  ╚██╔╝  ██╔══██╗██╔══╝  ██║╚██╗██║   ║
║   ██║ ╚═╝ ██║╚██████╔╝   ██║   ██║  ██║███████╗██║ ╚████║   ║
║   ╚═╝     ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝   ║
╚══════════════════════════════════════════════════════════════╝
              ASISTEN TERMUX AI BERBAHASA INDONESIA
           Dikembangkan oleh Ade Pratama (HolyBytes)
```
## 📋 Daftar Isi
- [Tentang Moyren AI](#-tentang-moyren-ai)
- [Persyaratan Sistem](#-persyaratan-sistem)
- [Panduan Instalasi Termux](#-panduan-instalasi-termux)
  - [Langkah 1: Install Termux](#langkah-1-install-termux-dari-f-droid)
  - [Langkah 2: Setup Dasar Termux](#langkah-2-setup-dasar-termux)
  - [Langkah 3: Install Paket yang Diperlukan](#langkah-3-install-paket-yang-diperlukan)
  - [Langkah 4: Instalasi Library Python](#langkah-4-instalasi-library-python)
  - [Langkah 5: Clone Repository](#langkah-5-clone-repository)
  - [Langkah 6: Jalankan Moyren AI](#langkah-6-jalankan-moyren-ai)
  - [Langkah 7: Setup API Key](#langkah-7-setup-api-key)
- [Panduan Instalasi untuk PC/Laptop](#-panduan-instalasi-untuk-pclaptop)
- [Mendapatkan API Key OpenRouter](#-mendapatkan-api-key-openrouter)
- [Fitur Moyren AI](#-fitur-moyren-ai)
- [Pemecahan Masalah (Troubleshooting)](#-pemecahan-masalah-troubleshooting)
- [Versi Alternatif](#-versi-alternatif)
- [FAQ](#-faq)
- [Lisensi](#-lisensi)
- [Kontak & Dukungan](#-kontak--dukungan)

## 🌟 Tentang Moyren AI

Moyren AI adalah asisten kecerdasan buatan berbahasa Indonesia yang dikembangkan untuk memberikan pengalaman percakapan yang natural dan membantu pengguna dalam berbagai kebutuhan. Dibangun menggunakan model THUDM GLM-4-32B melalui OpenRouter API, Moyren hadir dengan antarmuka terminal yang menarik dan colorful.

## 💻 Persyaratan Sistem

- Android 7.0+ untuk menjalankan Termux
- Minimal 100MB ruang penyimpanan kosong
- Koneksi internet yang stabil
- API Key dari OpenRouter (gratis untuk penggunaan terbatas)

## 📱 Panduan Instalasi Termux

### Langkah 1: Install Termux dari F-Droid

> ⚠️ **PENTING**: Termux dari Google Play Store sudah tidak diupdate dan mungkin tidak kompatibel dengan Android versi terbaru.

1. Download dan install Termux dari [F-Droid](https://f-droid.org/en/packages/com.termux/)
2. Jika mengalami kesulitan mengakses F-Droid, unduh APK Termux langsung dari [GitHub Releases](https://github.com/termux/termux-app/releases)

### Langkah 2: Setup Dasar Termux

Setelah instalasi, buka Termux dan jalankan perintah berikut:

```bash
termux-setup-storage
```

Ini akan memberikan izin aplikasi Termux untuk mengakses penyimpanan perangkat Anda. Kemudian jalankan:

```bash
apt update && apt upgrade -y
```

> 💡 **Tips**: Jika diminta konfirmasi selama proses upgrade, ketik 'y' dan tekan Enter.

### Langkah 3: Install Paket yang Diperlukan

```bash
pkg install python git python-pip openssl libffi libcrypt libcrypto openssl-tool -y
```

Paket-paket ini diperlukan untuk menjalankan Moyren AI dengan benar.

### Langkah 4: Instalasi Library Python

```bash
pip install --upgrade pip
pip install openai colorama cryptography
```

> 💡 **Tips**: Jika mengalami error saat instalasi cryptography, coba solusi ini:
> 
> ```bash
> LDFLAGS="-L/system/lib64/" CFLAGS="-I/data/data/com.termux/files/usr/include/" pip install cryptography
> ```

### Langkah 5: Clone Repository

```bash
cd ~
git clone https://github.com/HolyBytes/MoyrenAI.git
cd MoyrenAI
```

### Langkah 6: Jalankan Moyren AI

```bash
python tools_ai.py
```

> 📝 **Catatan**: Nama file utama aplikasi adalah `tools_ai.py`, bukan `moyren.py` seperti yang mungkin terlihat di beberapa screenshot.

### Langkah 7: Setup API Key

1. Setelah aplikasi berjalan, pilih menu [4] untuk pengaturan API Key
2. Pilih opsi [1] untuk menambahkan API Key
3. Masukkan API Key OpenRouter Anda
4. Buat password untuk mengenkripsi API Key (ingat baik-baik password ini!)
5. Kembali ke menu utama dan pilih [1] untuk mulai menggunakan Moyren

## 🖥️ Panduan Instalasi untuk PC/Laptop

### Windows

1. Install [Python 3.8+](https://www.python.org/downloads/) (pastikan opsi "Add Python to PATH" dicentang)
2. Install [Git for Windows](https://gitforwindows.org/)
3. Buka Command Prompt atau PowerShell dan jalankan:

```powershell
pip install --upgrade pip
pip install openai colorama cryptography
git clone https://github.com/HolyBytes/MoyrenAI.git
cd MoyrenAI
python tools_ai.py
```

### Linux/macOS

1. Install paket yang diperlukan:

```bash
# Untuk Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip git

# Untuk macOS (dengan Homebrew)
brew install python git
```

2. Install library yang diperlukan dan jalankan aplikasi:

```bash
pip3 install --upgrade pip
pip3 install openai colorama cryptography
git clone https://github.com/HolyBytes/MoyrenAI.git
cd MoyrenAI
python3 tools_ai.py
```

## 🔑 Mendapatkan API Key OpenRouter

1. Daftar akun di [OpenRouter](https://openrouter.ai/)
2. Setelah login, akses dashboard Anda
3. Pada menu API, klik "Create API Key"
4. Beri nama API Key (misalnya "Moyren AI")
5. Copy API Key yang dihasilkan untuk digunakan pada aplikasi Moyren

> 💡 **Tips**: OpenRouter menawarkan kredit gratis untuk pengguna baru, yang cukup untuk mencoba Moyren AI.

## ✨ Fitur Moyren AI

- 💬 Chat interaktif dengan AI berbahasa Indonesia
- 🌸 Antarmuka terminal yang colorful dan menarik
- 🔒 Penyimpanan API Key terenkripsi untuk keamanan
- 🧠 Akses ke model AI THUDM GLM-4-32B yang powerfull
- 🌐 Kemampuan memahami dan merespons bahasa Indonesia dengan natural

## ⚠️ Pemecahan Masalah (Troubleshooting)

### Error: "No module named 'X'"

```bash
pip install X  # Ganti X dengan nama modul yang tidak ditemukan
```

### Error: "Failed building wheel for cryptography"

Coba solusi berikut:

```bash
pkg install rust build-essential -y
CARGO_BUILD_TARGET=aarch64-linux-android pip install cryptography --no-binary cryptography
```

Untuk Android 32-bit:

```bash
CARGO_BUILD_TARGET=armv7-linux-androideabi pip install cryptography --no-binary cryptography
```

### Error: "Permission denied"

```bash
chmod +x tools_ai.py
python tools_ai.py
```

### Error Terkait SSL/TLS

```bash
pip install --upgrade certifi
```

Jika masih bermasalah:

```bash
export PYTHONHTTPSVERIFY=0
python tools_ai.py
```

> ⚠️ **Peringatan**: Setting PYTHONHTTPSVERIFY=0 mengurangi keamanan koneksi. Gunakan hanya untuk testing.

### Error "ImportError: cannot import name '_Cryptography_ffi_backend'"

```bash
pip uninstall cryptography
pkg install rust clang -y
RUSTFLAGS="-C lto=no" pip install cryptography --no-binary cryptography
```

### Error Saat Menggunakan API OpenRouter

1. Pastikan API key valid dan tidak kedaluwarsa
2. Periksa koneksi internet Anda
3. Periksa kredit/saldo yang tersisa di akun OpenRouter Anda

## 🔄 Versi Alternatif

### Menggunakan Model AI Alternatif

Jika Anda mengalami masalah dengan model THUDM GLM-4-32B, Anda dapat mengubah kode untuk menggunakan model lain:

1. Buka file `tools_ai.py` dengan editor teks
2. Cari baris `model="thudm/glm-4-32b:free"`
3. Ganti dengan salah satu model berikut:
   - `"anthropic/claude-3-opus:free"` (Lebih akurat tapi lebih lambat)
   - `"meta-llama/llama-3-70b-instruct:free"` (Alternatif bagus)
   - `"google/gemma-1.1-8b-it:free"` (Lebih ringan, cocok untuk perangkat lemah)

### Versi Lite untuk Perangkat dengan Spesifikasi Rendah

Untuk perangkat dengan RAM atau penyimpanan terbatas, Anda bisa mencoba versi "lite" dengan mengurangi fitur UI:

1. Buka file `tools_ai.py`
2. Cari bagian `display_banner()` dan `display_menu()`
3. Ganti dengan versi yang lebih sederhana atau beri komentar pada bagian yang lebih dekoratif

## ❓ FAQ

### Apakah saya dapat menggunakan Moyren tanpa koneksi internet?
Tidak, Moyren AI memerlukan koneksi internet untuk berkomunikasi dengan API OpenRouter.

### Berapa biaya menggunakan Moyren AI?
OpenRouter memberikan kredit gratis untuk pengguna baru. Setelah kredit habis, biayanya sangat terjangkau, sekitar $0.15-$0.30 per 1000 token.

### Apakah Moyren menyimpan data percakapan saya?
Tidak, semua percakapan terjadi secara real-time dan tidak disimpan secara permanen.

### Bagaimana cara memperbaharui Moyren ke versi terbaru?
```bash
cd ~/MoyrenAI
git pull origin main
```

### Dapatkah saya menggunakan API key dari OpenAI/Anthropic langsung?
Tidak, Moyren dirancang khusus untuk bekerja dengan OpenRouter API.

## 📄 Lisensi

Moyren AI dirilis di bawah [MIT License](LICENSE).

## 📞 Kontak & Dukungan

- GitHub: [HolyBytes/MoyrenAI](https://github.com/HolyBytes/MoyrenAI)
- Donasi: [Saweria](https://saweria.co/HolyBytes)

---

<div align="center">
  <p>Dibuat di buat oleeh ADE PRATAMA untuk komunitas termux AI Indonesia</p>
  <p>© 2025 Ade Pratama (HolyBytes) - All Rights Reserved</p>
</div>
