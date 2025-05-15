from openai import OpenAI
import time
import os
import sys
import base64
import getpass
from colorama import init, Fore, Back, Style
from datetime import datetime
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Initialize colorama
init(autoreset=True)

# Function to encrypt API key
def encrypt_api_key(api_key, password):
    salt = b'moyrenaisalt123456'  # In production, use a random salt and store it
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    f = Fernet(key)
    encrypted_key = f.encrypt(api_key.encode())
    return encrypted_key

# Function to decrypt API key
def decrypt_api_key(encrypted_key, password):
    try:
        salt = b'moyrenaisalt123456'  # Use the same salt as in encryption
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        f = Fernet(key)
        decrypted_key = f.decrypt(encrypted_key)
        return decrypted_key.decode()
    except Exception:
        return None

# Function to save encrypted API key
def save_api_key(api_key, password):
    encrypted_key = encrypt_api_key(api_key, password)
    config_dir = os.path.join(os.path.expanduser('~'), '.moyren')
    os.makedirs(config_dir, exist_ok=True)
    with open(os.path.join(config_dir, 'api_key.enc'), 'wb') as f:
        f.write(encrypted_key)
    
# Function to load encrypted API key
def load_api_key(password):
    config_dir = os.path.join(os.path.expanduser('~'), '.moyren')
    api_key_path = os.path.join(config_dir, 'api_key.enc')
    if os.path.exists(api_key_path):
        with open(api_key_path, 'rb') as f:
            encrypted_key = f.read()
        return decrypt_api_key(encrypted_key, password)
    return None

# Function to initialize OpenAI client
def init_client(api_key):
    if not api_key:
        return None
    
    return OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_current_time():
    now = datetime.now()
    hari = now.strftime("%A")
    tanggal = now.strftime("%d %B %Y")
    waktu = now.strftime("%H:%M:%S")
    return hari, tanggal, waktu

def display_banner():
    clear_screen()
    hari, tanggal, waktu = get_current_time()
    
    # Enhanced ASCII art with more aesthetics
    print(Fore.MAGENTA + Style.BRIGHT + """
╔══════════════════════════════════════════════════════════════╗
║   ███╗   ███╗ ██████╗ ██╗   ██╗██████╗ ███████╗███╗   ██╗   ║
║   ████╗ ████║██╔═══██╗╚██╗ ██╔╝██╔══██╗██╔════╝████╗  ██║   ║
║   ██╔████╔██║██║   ██║ ╚████╔╝ ██████╔╝█████╗  ██╔██╗ ██║   ║
║   ██║╚██╔╝██║██║   ██║  ╚██╔╝  ██╔══██╗██╔══╝  ██║╚██╗██║   ║
║   ██║ ╚═╝ ██║╚██████╔╝   ██║   ██║  ██║███████╗██║ ╚████║   ║
║   ╚═╝     ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝   ║
╚══════════════════════════════════════════════════════════════╝
""")
    
    print(Fore.CYAN + Style.BRIGHT + "         ✧･ﾟ: *✧･ﾟ:* ✨ Moyren AI Assistant ✨ *:･ﾟ✧*:･ﾟ✧")
    print()
    print(Fore.YELLOW + f"    📅 Hari     : {hari}")
    print(Fore.YELLOW + f"    🗓️ Tanggal  : {tanggal}")
    print(Fore.YELLOW + f"    🕒 Waktu    : {waktu}")
    print()
    print(Fore.GREEN + f"    🌠 Version  : 1.0.0 BETA | 🤖 Model: THUDM GLM-4-32B")
    print(Fore.BLUE + "    💻 Created by Ade Pratama (HolyBytes)")
    print(Fore.MAGENTA + "    🔗 GitHub   : https://github.com/HolyBytes/MoyrenAI")
    print(Fore.CYAN + "    ☕ Support  : https://saweria.co/HolyBytes")
    
    print(Fore.MAGENTA + "\n" + "─" * 70 + "\n")
    print(Fore.GREEN + Style.BRIGHT + "✨ Selamat datang! Senang bertemu denganmu! ✨")
    print(Fore.YELLOW + "💬 Aku Moyren, siap membantumu dengan apapun. Silakan bertanya ya~")
    print(Fore.CYAN + "🔍 Ketik 'menu' kapan saja untuk kembali ke menu utama\n")

def display_menu():
    print(Fore.CYAN + Style.BRIGHT + "\n╭────────────── 🌸 Menu Utama 🌸 ──────────────╮")
    print(Fore.YELLOW + "│                                              │")
    print(Fore.YELLOW + "│   [1] 🗨️  Mulai Chat dengan Moyren           │")
    print(Fore.YELLOW + "│   [2] ℹ️  Informasi Moyren                   │")
    print(Fore.YELLOW + "│   [3] ❓  FAQ                               │")
    print(Fore.YELLOW + "│   [4] 🔑  Pengaturan API Key                 │")
    print(Fore.YELLOW + "│   [5] 🚪  Keluar                             │")
    print(Fore.YELLOW + "│                                              │")
    print(Fore.CYAN + "╰──────────────────────────────────────────────╯")
    print(Fore.MAGENTA + "\n" + "─" * 70)

def display_info():
    print(Fore.CYAN + Style.BRIGHT + "\n╭────────────── ℹ️ Informasi Moyren AI ──────────────╮")
    print(Fore.YELLOW + """│                                                    │
│  ✨ Moyren adalah asisten AI berbahasa Indonesia     │
│     yang dikembangkan oleh Ade Pratama (HolyBytes).  │
│     Dibangun dengan teknologi canggih untuk membantu │
│     Anda dalam berbagai kebutuhan sehari-hari.       │
│                                                      │
│  🌿 Fitur Utama:                                     │
│     - Asisten pribadi yang ramah dan sopan          │
│     - Bantuan dalam pekerjaan dan studi             │
│     - Teman diskusi dan bertukar ide                │
│     - Penghasil konten kreatif                      │
│     - Pemecah masalah sehari-hari                   │
│                                                      │
│  🛠️ Spesifikasi Teknis:                              │
│     • Model: THUDM GLM-4-32B                        │
│     • Platform: OpenRouter API                      │
│     • Bahasa: Indonesia & Inggris                   │
│     • Versi: 1.0.0 BETA                             │
│                                                      │
│  💌 "Moyren hadir untuk membuat hidupmu lebih       │
│     mudah dan menyenangkan!"                         │
│                                                      │""")
    print(Fore.CYAN + "╰──────────────────────────────────────────────────╯")
    print(Fore.MAGENTA + "\n" + "─" * 70)
    input(Fore.GREEN + "\n🌸 Tekan Enter untuk kembali ke menu utama...")

def display_faq():
    faq_items = [
        {
            "question": "✧ Apakah data saya aman saat berbicara dengan Moyren?",
            "answer": "Moyren tidak menyimpan data percakapan Anda. Semua interaksi bersifat sementara dan hanya untuk memberikan respons yang tepat."
        },
        {
            "question": "✧ Apa saja yang bisa Moyren bantu?",
            "answer": "Saya bisa membantu dalam:\n- Menjawab pertanyaan umum\n- Bantuan belajar/mengajar\n- Penulisan kreatif\n- Pemrograman dasar\n- Terjemahan bahasa\n- Dan banyak lagi!"
        },
        {
            "question": "✧ Bagaimana cara menggunakan Moyren dengan baik?",
            "answer": "Gunakan kalimat yang jelas dan lengkap. Contoh:\n\"Moyren, tolong jelaskan tentang fotosintesis\"\n\"Bantu buatkan puisi tentang hujan\""
        },
        {
            "question": "✧ Apakah Moyren gratis?",
            "answer": "Ya! Versi beta ini sepenuhnya gratis untuk digunakan."
        },
        {
            "question": "✧ Siapa pengembang Moyren?",
            "answer": "Moyren dikembangkan oleh Ade Pratama (HolyBytes), seorang developer muda dari Indonesia."
        }
    ]
    
    print(Fore.CYAN + Style.BRIGHT + "\n╭────────────── ❓ FAQ - Pertanyaan Umum ──────────────╮")
    print(Fore.YELLOW + "│                                                      │")
    
    for i, item in enumerate(faq_items, 1):
        question = item['question']
        answer = item['answer'].replace('\n', '\n│    ')
        print(Fore.YELLOW + f"│  {i}. {question}")
        print(Fore.WHITE + f"│    ➤ {answer}")
        if i < len(faq_items):
            print(Fore.YELLOW + "│                                                      │")
    
    print(Fore.YELLOW + "│                                                      │")
    print(Fore.CYAN + "╰──────────────────────────────────────────────────────╯")
    print(Fore.MAGENTA + "\n" + "─" * 70)
    input(Fore.GREEN + "\n🌸 Tekan Enter untuk kembali ke menu utama...")

def display_api_settings():
    print(Fore.CYAN + Style.BRIGHT + "\n╭────────────── 🔑 Pengaturan API Key ──────────────╮")
    print(Fore.YELLOW + "│                                                  │")
    print(Fore.YELLOW + "│   [1] ➕ Tambah/Update API Key                   │")
    print(Fore.YELLOW + "│   [2] 🔍 Cek Status API Key                      │")
    print(Fore.YELLOW + "│   [3] 🗑️  Hapus API Key                          │")
    print(Fore.YELLOW + "│   [4] ↩️  Kembali ke Menu Utama                  │")
    print(Fore.YELLOW + "│                                                  │")
    print(Fore.CYAN + "╰──────────────────────────────────────────────────╯")
    
    choice = input(Fore.GREEN + "\n🌸 Pilih opsi [1-4]: " + Fore.WHITE).strip()
    
    if choice == "1":
        api_key = getpass.getpass(Fore.YELLOW + "📝 Masukkan API Key baru: ")
        if not api_key:
            print(Fore.RED + "❌ API Key tidak boleh kosong!")
            time.sleep(2)
            return
            
        password = getpass.getpass(Fore.YELLOW + "🔐 Buat password untuk enkripsi: ")
        if not password:
            print(Fore.RED + "❌ Password tidak boleh kosong!")
            time.sleep(2)
            return
            
        save_api_key(api_key, password)
        print(Fore.GREEN + "✅ API Key berhasil disimpan dan dienkripsi!")
        time.sleep(2)
        
    elif choice == "2":
        password = getpass.getpass(Fore.YELLOW + "🔐 Masukkan password untuk memeriksa API Key: ")
        api_key = load_api_key(password)
        
        if api_key:
            masked_key = api_key[:4] + "*" * (len(api_key) - 8) + api_key[-4:]
            print(Fore.GREEN + f"✅ API Key tersedia: {masked_key}")
        else:
            print(Fore.RED + "❌ API Key tidak ditemukan atau password salah!")
        time.sleep(2)
        
    elif choice == "3":
        password = getpass.getpass(Fore.YELLOW + "🔐 Masukkan password untuk konfirmasi: ")
        api_key = load_api_key(password)
        
        if api_key:
            confirm = input(Fore.RED + "⚠️ Yakin ingin menghapus API Key? (y/n): ").lower()
            if confirm == 'y':
                config_dir = os.path.join(os.path.expanduser('~'), '.moyren')
                api_key_path = os.path.join(config_dir, 'api_key.enc')
                if os.path.exists(api_key_path):
                    os.remove(api_key_path)
                    print(Fore.GREEN + "✅ API Key berhasil dihapus!")
                else:
                    print(Fore.RED + "❌ File API Key tidak ditemukan!")
            else:
                print(Fore.YELLOW + "⚠️ Penghapusan dibatalkan.")
        else:
            print(Fore.RED + "❌ Password salah atau API Key tidak ditemukan!")
        
        time.sleep(2)

def display_goodbye():
    clear_screen()
    print(Fore.MAGENTA + Style.BRIGHT + """
╭──────────────────────────────────────────────────╮
│                                                  │
│         Terima kasih telah menggunakan           │
│            ✨ Moyren AI Assistant ✨              │
│                                                  │
╰──────────────────────────────────────────────────╯
""")
    print(Fore.CYAN + "      💖 Sampai jumpa lagi! Semoga harimu menyenangkan!")
    print(Fore.YELLOW + "      🌙 Jangan ragu untuk kembali kapan saja ya~")
    print(Fore.GREEN + "\n" + "─" * 70)
    time.sleep(2)

def chat_with_ai(client, prompt):
    if client is None:
        return f"{Fore.RED}❌ API Key tidak ditemukan atau tidak valid. Silakan tambahkan API Key di pengaturan."
        
    try:
        start_time = time.time()
        response = client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "https://github.com/HolyBytes/MoyrenAI",
                "X-Title": "Moyren AI"
            },
            model="thudm/glm-4-32b:free",
            messages=[
                {
                    "role": "system",
                    "content": """Anda adalah Moyren, asisten AI berbahasa Indonesia yang sangat ramah dan sopan. Gunakan bahasa yang:
- Santun dan penuh emoji positif (✨,🌸,💖)
- Respons cepat dan langsung ke inti
- Bisa menggunakan kata-kata akrab seperti "sayang", "teman", "dek"

Contoh:
"Waalaikumsalam warahmatullahi wabarakatuh~ Apa yang bisa Moyren bantu? 💖"
"Wah pertanyaan yang bagus! Aku bantu jelaskan ya~ ✨"
"""
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=800
        )
        response_time = time.time() - start_time
        print(Fore.YELLOW + f"⚡ Waktu respon: {response_time:.2f} detik")
        return response.choices[0].message.content
    except Exception as e:
        return f"{Fore.RED}❌ Maaf terjadi error: {str(e)}"

def chat_interface(client):
    if client is None:
        print(Fore.RED + "\n❌ API Key tidak ditemukan atau tidak valid.")
        print(Fore.YELLOW + "📝 Silakan tambahkan API Key di pengaturan terlebih dahulu.")
        time.sleep(3)
        return
        
    print(Fore.CYAN + Style.BRIGHT + "\n╭────────────── 💬 Mode Percakapan Aktif 💬 ──────────────╮")
    print(Fore.YELLOW + "│                                                           │")
    print(Fore.YELLOW + "│    ✨ Ketik 'menu' untuk kembali ke menu utama            │")
    print(Fore.YELLOW + "│                                                           │")
    print(Fore.CYAN + "╰───────────────────────────────────────────────────────────╯\n")
    
    while True:
        user_input = input(f"{Fore.GREEN}👤 Anda: {Fore.WHITE}").strip()
        
        if user_input.lower() in ['menu', 'kembali', 'exit', 'quit']:
            print(Fore.CYAN + "\n💖 Baiklah, kembali ke menu utama ya~")
            time.sleep(1)
            break
            
        if not user_input:
            print(Fore.YELLOW + "🌸 Mohon masukkan pertanyaan ya sayang~")
            continue
            
        print(Fore.BLUE + "\n🤖 Moyren sedang memproses...")
        response = chat_with_ai(client, user_input)
        
        # Print dengan border
        print(f"\n{Fore.CYAN}✨ Moyren: {Fore.WHITE}")
        print(Fore.CYAN + "┌" + "─" * 68 + "┐")
        
        # Split response into lines to fit in the box
        lines = []
        for paragraph in response.split('\n'):
            current_line = ""
            for word in paragraph.split():
                if len(current_line + " " + word) <= 66:
                    if current_line:
                        current_line += " " + word
                    else:
                        current_line = word
                else:
                    lines.append(current_line)
                    current_line = word
            if current_line:
                lines.append(current_line)
            if paragraph != response.split('\n')[-1]:  # Don't add empty lines after the last paragraph
                lines.append("")
                
        # Print response with borders
        for line in lines:
            padding = 66 - len(line)
            print(Fore.CYAN + "│ " + Fore.WHITE + line + " " * padding + Fore.CYAN + " │")
            
        print(Fore.CYAN + "└" + "─" * 68 + "┘\n")

def main():
    # Check if API key exists
    api_key = None
    client = None
    
    while True:
        display_banner()
        display_menu()
        
        # Show API key status
        config_dir = os.path.join(os.path.expanduser('~'), '.moyren')
        api_key_path = os.path.join(config_dir, 'api_key.enc')
        api_status = "✅ Terdeteksi" if os.path.exists(api_key_path) else "❌ Tidak ditemukan"
        print(Fore.YELLOW + f"\n🔑 Status API Key: {api_status}")
        
        choice = input(Fore.GREEN + "\n🌸 Pilih menu [1-5]: " + Fore.WHITE).strip()
        
        if choice == "1":
            # Load API key if needed
            if client is None and os.path.exists(api_key_path):
                password = getpass.getpass(Fore.YELLOW + "🔐 Masukkan password untuk mengakses API Key: ")
                api_key = load_api_key(password)
                if api_key:
                    client = init_client(api_key)
                else:
                    print(Fore.RED + "❌ Password salah atau API Key bermasalah!")
                    time.sleep(2)
                    continue
            
            chat_interface(client)
            
        elif choice == "2":
            display_info()
            
        elif choice == "3":
            display_faq()
            
        elif choice == "4":
            display_api_settings()
            # Reset client to force re-authentication if API key changed
            client = None
            
        elif choice == "5":
            display_goodbye()
            sys.exit()
            
        else:
            print(Fore.RED + "❌ Pilihan tidak valid. Silakan pilih 1-5 ya~")
            time.sleep(1)

if __name__ == "__main__":
    main()
