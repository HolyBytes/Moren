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

# Your OpenRouter API Key
OPENROUTER_API_KEY = "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"

# Function to initialize OpenAI client
def init_client():
    return OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=OPENROUTER_API_KEY,
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
    print(Fore.GREEN + f"    🌠 Version  : 1.0.0 BETA | 🤖 Model: Meta Llama 3.3 8B Instruct")
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
    print(Fore.YELLOW + "│   [4] 🚪  Keluar                             │")
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
│     • Model: Meta Llama 3.3 8B Instruct             │
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
    try:
        start_time = time.time()
        response = client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "https://github.com/HolyBytes/MoyrenAI",
                "X-Title": "Moyren AI"
            },
            model="meta-llama/llama-3.3-8b-instruct:free",
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
    # Initialize client with the hardcoded API key
    client = init_client()
    
    while True:
        display_banner()
        display_menu()
        
        choice = input(Fore.GREEN + "\n🌸 Pilih menu [1-4]: " + Fore.WHITE).strip()
        
        if choice == "1":
            chat_interface(client)
            
        elif choice == "2":
            display_info()
            
        elif choice == "3":
            display_faq()
            
        elif choice == "4":
            display_goodbye()
            sys.exit()
            
        else:
            print(Fore.RED + "❌ Pilihan tidak valid. Silakan pilih 1-4 ya~")
            time.sleep(1)

if __name__ == "__main__":
    main()
