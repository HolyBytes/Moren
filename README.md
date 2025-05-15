# Cara Setup dan Menjalankan Moyren AI di Termux

## Langkah 1: Install Termux dari F-Droid
Termux dari Play Store sudah tidak diupdate. Disarankan untuk menginstall dari F-Droid:
https://f-droid.org/en/packages/com.termux/

## Langkah 2: Update & Upgrade Termux
```bash
pkg update && pkg upgrade -y
```

## Langkah 3: Install Paket Dasar yang Diperlukan
```bash
pkg install python git python-pip openssl libffi -y
```

## Langkah 4: Install Library Python yang Dibutuhkan
```bash
pip install openai colorama cryptography
```

## Langkah 5: Clone Repository dari GitHub
```bash
cd ~
git clone https://github.com/HolyBytes/MoyrenAI.git
cd MoyrenAI
```

## Langkah 6: Jalankan Moyren AI
```bash
python tools_ai.py
```

## Langkah 7: Setup API Key
Setelah aplikasi berjalan:
1. Pilih menu [4] untuk pengaturan API Key
2. Pilih opsi [1] untuk menambahkan API Key
3. Masukkan API Key OpenRouter Anda (daftar di https://openrouter.ai/ jika belum punya)
4. Buat password untuk mengenkripsi API Key
5. Kembali ke menu utama dan pilih [1] untuk mulai menggunakan Moyren

## Catatan Tambahan
- Pastikan API Key Anda valid dan memiliki akses ke model THUDM GLM-4-32B
- Jika mendapat error terkait izin, jalankan perintah ini untuk memberikan izin penyimpanan: `termux-setup-storage`
- Jika terjadi error saat instalasi package, coba: `pip install --upgrade pip` lalu ulangi instalasi
- Repository ini menggunakan file utama `tools_ai.py` bukan `moyren.py` sesuai yang terlihat pada screenshot
