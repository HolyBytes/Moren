# **MOREN AI Assistant - Dokumentasi Lengkap**  

## **📌 Deskripsi**  
**MOREN** adalah asisten AI berbasis terminal yang menggunakan model **DeepHermes-3-Mistral 24B** dari OpenRouter. Dibangun dengan Python, MOREN dirancang untuk memberikan pengalaman chatting yang **santun, informatif, dan estetik**, khususnya untuk pengguna yang menginginkan interaksi AI dengan nilai-nilai akhlak yang baik.  

---

## **🔧 Fungsi & Kegunaan Script**  

### **1. Fungsi Utama**  
| **Fungsi** | **Kegunaan** | **Dapat Diedit?** | **Alasan** |
|------------|-------------|------------------|------------|
| **`animated_loading()`** | Menampilkan animasi loading saat AI berpikir | ✅ | Bisa dimodifikasi untuk efek visual berbeda |
| **`get_time_greeting()`** | Memberikan salam berdasarkan waktu (Pagi/Siang/Sore/Malam) | ✅ | Bisa disesuaikan dengan budaya lokal |
| **`get_time_info()`** | Menampilkan waktu & tanggal dalam format Indonesia | ✅ | Format tanggal bisa diubah sesuai kebutuhan |
| **`animate_text()`** | Efek ketik manual untuk pesan MOREN | ✅ | Kecepatan ketik bisa diatur |
| **`border_box()`** | Membuat kotak dekoratif untuk teks | ✅ | Bisa diganti dengan gaya border lain |
| **`display_header()`** | Menampilkan header (ASCII art, info waktu, tabel) | ⚠️ (Sebaiknya tidak) | Mengandung branding MOREN |
| **`calculate_max_tokens()`** | Menghitung token dinamis berdasarkan panjang input | ⚠️ (Hanya jika paham AI) | Memengaruhi performa API |
| **`chat_with_ai()`** | Mengirim & menerima respons dari API OpenRouter | ⚠️ (Hanya API Key & Model) | Mengubah ini bisa merusak fungsi utama |
| **`format_chat_history()`** | Memformat riwayat obrolan | ✅ | Bisa disesuaikan gaya chat |
| **`typewriter_effect()`** | Animasi teks seperti mesin ketik | ✅ | Bisa diatur kecepatannya |
| **`main()`** | Fungsi utama yang menjalankan semua logika | ⚠️ (Hanya untuk pengembang) | Inti program, edit hati-hati |

---

## **⚙️ Bagian yang Bisa & Tidak Bisa Diedit**  

### **✅ Bisa Diedit (Customizable)**
1. **Animasi & Tampilan**  
   - Warna (`Colors` class)  
   - Efek ketik (`typewriter_effect()`)  
   - Animasi loading (`animated_loading()`)  
   - Format waktu (`get_time_info()`)  

2. **Sistem Prompt**  
   - Bisa diubah di `system_prompt` (dalam `main()`) untuk menyesuaikan kepribadian AI.  

3. **Konfigurasi API**  
   - **API Key** (Ganti dengan milik sendiri)  
   - **Model AI** (Bisa pilih model lain di OpenRouter)  

### **❌ Tidak Disarankan Diedit (Kecuali Paham Kode)**
1. **Struktur Utama `chat_with_ai()`**  
   - Mengubah ini bisa menyebabkan API error.  
2. **Logika Token (`calculate_max_tokens()`)**  
   - Memengaruhi biaya & stabilitas API.  
3. **Header & Tampilan Awal (`display_header()`)**  
   - Mengandung identitas MOREN, sebaiknya tetap ada.  

---

## **✨ Kelebihan MOREN**  
✔ **Ramah & Santun** – Dibangun dengan nilai-nilai akhlak yang baik.  
✔ **Tampilan Estetik** – Warna, animasi, dan ASCII art yang menarik.  
✔ **Dinamis** – Token dihitung otomatis berdasarkan panjang pesan.  
✔ **Multi-fungsi** – Bisa digunakan untuk edukasi, hiburan, dan bantuan teknis.  
✔ **Open Customization** – Banyak bagian yang bisa disesuaikan.  

---

## **⚠️ Kekurangan MOREN**  
✖ **Bergantung API** – Memerlukan koneksi internet & API key.  
✖ **Biaya API** – Jika pakai model berbayar, bisa ada biaya.  
✖ **Tidak Offline** – Tidak bisa jalan tanpa OpenRouter.  
✖ **Terbatas di Terminal** – Belum punya GUI (Graphical User Interface).  

---

## **📩 Kontak & Dukungan**  
Untuk pertanyaan atau kolaborasi, silakan hubungi:  
- **GitHub**: [github.com/HolyBytes](https://github.com/HolyBytes)  
- **Forum Diskusi**: [Coming Soon]  

---

## **🔐 Lisensi**  
**MOREN** menggunakan lisensi **MIT**, artinya:  
✅ Bisa digunakan **gratis** untuk proyek pribadi & komersial.  
✅ Boleh **dimodifikasi** asalkan tetap mencantumkan credit.  
✅ **Tidak bertanggung jawab** atas penyalahgunaan.  

---

### **🎯 Kesimpulan**  
MOREN adalah **asisten AI terminal yang santun & customizable**, cocok untuk yang ingin AI dengan sentuhan akhlak baik. Meski punya beberapa keterbatasan (seperti ketergantungan API), MOREN tetap bisa dikembangkan lebih lanjut sesuai kebutuhan pengguna.  

**Selamat mencoba! Semoga bermanfaat. 🌷**
