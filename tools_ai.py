import requests
import json
import time
import sys
import random
import datetime
from colorama import init, Fore, Back, Style
from prettytable import PrettyTable
import os

# Initialize colorama
init(autoreset=True)

# Warna Estetik Custom
class Colors:
    PRIMARY = Fore.CYAN        # Warna utama (teal)
    SECONDARY = Fore.MAGENTA   # Warna sekunder (ungu)
    ACCENT = Fore.YELLOW       # Warna aksen (kuning)
    TEXT = Fore.WHITE          # Warna teks standar
    SUCCESS = Fore.GREEN       # Warna sukses
    ERROR = Fore.RED           # Warna error
    INFO = Fore.BLUE           # Warna info
    SOFT = Fore.LIGHTBLACK_EX  # Warna soft untuk hint/tips

# Konfigurasi API
API_KEY = "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"
MODEL = "openai/gpt-3.5-turbo-0613"  # Changed to GPT-3.5-turbo
API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Animasi Loading yang Lebih Estetik
def animated_loading():
    frames = ["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"]
    loading_text = f"{Colors.PRIMARY}MOREN sedang berpikir "
    
    for _ in range(2):
        for frame in frames:
            sys.stdout.write(f"\r{loading_text}{frame}{Style.RESET_ALL}")
            sys.stdout.flush()
            time.sleep(0.1)

# ASCII Art Asli untuk MOREN
MOREN_ASCII = f"""
{Colors.ACCENT}
███╗   ███╗ ██████╗ ██████╗ ███████╗███╗   ██╗
████╗ ████║██╔═══██╗██╔══██╗██╔════╝████╗  ██║
██╔████╔██║██║   ██║██████╔╝█████╗  ██╔██╗ ██║
██║╚██╔╝██║██║   ██║██╔══██╗██╔══╝  ██║╚██╗██║
██║ ╚═╝ ██║╚██████╔╝██║  ██║███████╗██║ ╚████║
╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝
{Style.RESET_ALL}
"""

def clear_screen():
    """Membersihkan layar konsol"""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_time_greeting():
    """Mendapatkan salam berdasarkan waktu lokal"""
    hour = datetime.datetime.now().hour
    
    if 5 <= hour < 12:
        return "🌄 Selamat pagi" 
    elif 12 <= hour < 15:
        return "☀️ Selamat siang"
    elif 15 <= hour < 18:
        return "🌇 Selamat sore"
    else:
        return "🌙 Selamat malam"

def get_time_info():
    """Mendapatkan informasi waktu dan hari dalam bahasa Indonesia"""
    now = datetime.datetime.now()
    
    hari_list = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    bulan_list = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", 
                 "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    
    hari = hari_list[now.weekday()]
    tanggal = now.day
    bulan = bulan_list[now.month - 1]
    tahun = now.year
    waktu = now.strftime("%H:%M:%S")
    
    return f"{hari}, {tanggal} {bulan} {tahun} • {waktu} WIB"

def animate_text(text, delay=0.005):
    """Menampilkan teks dengan animasi ketik yang lebih halus"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def border_box(text, color=Colors.PRIMARY, padding=1):
    """Membuat kotak border di sekitar teks"""
    lines = text.split('\n')
    width = max(len(line) for line in lines) + padding * 2
    
    box = f"{color}╔{'═' * width}╗\n"
    
    for line in lines:
        box += f"║{' ' * padding}{line}{' ' * (width - len(line) - padding)}║\n"
    
    box += f"╚{'═' * width}╝{Style.RESET_ALL}"
    return box

def display_header():
    """Menampilkan header dengan ASCII art dan info"""
    clear_screen()
    
    print(MOREN_ASCII)
    
    # Informasi waktu
    time_info = get_time_info()
    print(f"{Colors.INFO}{time_info}{Style.RESET_ALL}")
    print()
    
    # Animasi loading
    for i in range(1, 6):
        progress = "▰" * i + "▱" * (5-i)
        sys.stdout.write(f"\r{Colors.ACCENT}Mempersiapkan MOREN {progress}")
        sys.stdout.flush()
        time.sleep(0.2)
    print("\n")
    
    # Tabel informasi
    table = PrettyTable()
    table.field_names = [f"{Colors.ACCENT}Atribut", f"{Colors.ACCENT}Nilai{Style.RESET_ALL}"]
    table.align = "l"
    table.border = True
    table.header = True
    table.padding_width = 2
    
    # Informasi dengan ikon
    table.add_row([f"{Colors.PRIMARY}👤 Pengembang", f"{Colors.TEXT}Ade Pratama (SMK Negeri 1 Pulau Rakyat)"])
    table.add_row([f"{Colors.PRIMARY}🌐 GitHub", f"{Colors.INFO}https://github.com/HolyBytes/"])
    table.add_row([f"{Colors.PRIMARY}💖 Dukungan", f"{Colors.INFO}https://saweria.co/HolyBytes"])
    table.add_row([f"{Colors.PRIMARY}🔄 Versi", f"{Colors.TEXT}1.3.0 (MOREN-24B)"])
    table.add_row([f"{Colors.PRIMARY}🤖 Model", f"{Colors.TEXT}DeepHermes 3 (Mistral 24B)"])
    table.add_row([f"{Colors.PRIMARY}📅 Pembaruan", f"{Colors.TEXT}16 Mei 2025"])
    
    print(str(table))
    print()
    
    # Greeting berdasarkan waktu
    greeting = get_time_greeting()
    welcome_message = f"{Colors.SECONDARY}{greeting}🌷 𝗛𝗮𝗹𝗼! 𝗦𝗲𝗹𝗮𝗺𝗮𝘁 𝗱𝗮𝘁𝗮𝗻𝗴 𝗱𝗶 𝗖𝗵𝗮𝘁 𝗔𝘀𝘀𝗶𝘀𝘁𝗮𝗻 𝗠𝗢𝗥𝗘𝗡! 🌷{Style.RESET_ALL}"
    animate_text(welcome_message)
    
    hint_message = f"{Colors.SOFT}Ketik 'exit' untuk keluar atau 'help' untuk bantuan.{Style.RESET_ALL}"
    print(hint_message)
    print()

def calculate_max_tokens(user_input):
    """Menghitung token maksimum secara dinamis berdasarkan panjang input"""
    base_tokens = 600  # Meningkatkan token dasar
    length_factor = len(user_input) // 2
    return min(base_tokens + length_factor, 2500)  # Maksimal 2500 token

def chat_with_ai(messages):
    """Mengirim pesan ke AI dan mendapatkan respons"""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/HolyBytes/",
        "X-Title": "MOREN Chat Tool"
    }
   # Hitung max_tokens dinamis
    last_user_message = messages[-1]["content"]
    max_tokens = calculate_max_tokens(last_user_message)
    
    payload = {
        "model": MODEL,  # Now using GPT-3.5-turbo
        "messages": messages,
        "temperature": 0.75,
        "max_tokens": max_tokens,
        "top_p": 0.9,
        "frequency_penalty": 0.3,
        "presence_penalty": 0.3
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        
        response_data = response.json()
        
        if "choices" not in response_data or len(response_data["choices"]) == 0:
            return f"{Colors.ERROR}Maaf, respons dari server tidak valid. Silakan coba lagi.{Style.RESET_ALL}"
            
        if "message" not in response_data["choices"][0]:
            return f"{Colors.ERROR}Format respons tidak dikenali. Mohon coba pertanyaan lain.{Style.RESET_ALL}"
            
        return response_data["choices"][0]["message"]["content"]
        
    except requests.exceptions.RequestException as e:
        error_msg = f"Gagal terhubung ke server: {str(e)}"
        return f"{Colors.ERROR}{error_msg}{Style.RESET_ALL}"
    except json.JSONDecodeError:
        return f"{Colors.ERROR}Gagal memproses respons server{Style.RESET_ALL}"
    except Exception as e:
        return f"{Colors.ERROR}Terjadi kesalahan: {str(e)}{Style.RESET_ALL}"
    
def show_help():
    """Menampilkan menu bantuan"""
    help_text = f"""
{Colors.ACCENT}🆘 BANTUAN DAN PERINTAH MOREN {Style.RESET_ALL}

{Colors.PRIMARY}Perintah khusus:{Style.RESET_ALL}
• {Colors.SUCCESS}help{Style.RESET_ALL} - Menampilkan menu bantuan ini
• {Colors.SUCCESS}exit{Style.RESET_ALL} - Keluar dari program
• {Colors.SUCCESS}clear{Style.RESET_ALL} - Membersihkan layar chat
• {Colors.SUCCESS}info{Style.RESET_ALL} - Menampilkan informasi tentang MOREN
• {Colors.SUCCESS}history{Style.RESET_ALL} - Menampilkan riwayat percakapan

{Colors.PRIMARY}Fitur baru:{Style.RESET_ALL}
• Dukungan emoji dan format teks
• Penanganan error yang lebih baik
• Animasi yang lebih halus
• Waktu respons yang lebih cepat
• Penyimpanan riwayat percakapan

{Colors.PRIMARY}Cara penggunaan:{Style.RESET_ALL}
1. Ketik pesan Anda seperti biasa
2. MOREN akan merespons dengan bijak
3. Gunakan perintah khusus untuk fitur tambahan
4. Diskusi bisa mencakup berbagai topik

{Colors.SOFT}Tekan Enter untuk melanjutkan...{Style.RESET_ALL}
"""
    print(border_box(help_text, Colors.PRIMARY))
    input()

def typewriter_effect(text):
    """Menampilkan teks dengan efek mesin ketik yang lebih halus"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        # Variasi kecepatan ketik yang lebih halus
        time.sleep(random.uniform(0.01, 0.025))
    print()

def main():
    display_header()
    
    # System prompt yang diperbarui
    system_prompt = """Anda adalah MOREN, asisten AI yang sopan, ramah, dan berakhlak mulia. Anda diciptakan oleh Ade Pratama, seorang pelajar dari SMK Negeri 1 Pulau Rakyat.

Panduan Interaksi:
1. Gunakan bahasa Indonesia yang santun
2. Sampaikan jawaban dengan tutur kata yang baik
3. Berikan jawaban yang informatif dan bermanfaat
4. Untuk pertanyaan teknis, berikan penjelasan rinci
5. Untuk pertanyaan umum, berikan jawaban yang bijak

Fitur:
- Bisa membantu dalam pemrograman
- Menguasai berbagai topik pengetahuan
- Dapat memberikan saran kehidupan
- Bisa berdiskusi tentang teknologi
- Memahami dunia pendidikan

Prioritas:
1. Keakuratan informasi
2. Keramahan dalam berkomunikasi
3. Manfaat bagi pengguna
4. Kesopanan dalam bertutur kata"""
    
    messages = [
        {"role": "system", "content": system_prompt}
    ]
    
    # Kumpulan salam pembuka
    greeting_time = get_time_greeting()
    greetings = [
        f"{greeting_time}! Ada yang bisa MOREN bantu hari ini?",
        f"{greeting_time}! Senang bertemu dengan Anda. Apa kabar?",
        f"{greeting_time}! MOREN siap membantu Anda hari ini.",
        f"{greeting_time}! Ada pertanyaan menarik hari ini?",
        f"{greeting_time}! Mari berdiskusi sesuatu yang bermanfaat."
    ]
    
    # Sambutan awal
    print(f"{Colors.PRIMARY}MOREN:{Style.RESET_ALL} ", end="")
    typewriter_effect(random.choice(greetings))
    
    while True:
        try:
            # Prompt input
            user_input = input(f"\n{Colors.SUCCESS}Anda: {Style.RESET_ALL}").strip()
            
            # Perintah khusus
            if user_input.lower() == 'exit':
                farewells = [
                    "Sampai jumpa lagi! Semoga hari Anda menyenangkan.",
                    "Terima kasih telah menggunakan MOREN. Sampai bertemu lagi!",
                    "Semoga pembicaraan kita bermanfaat. Sampai jumpa!",
                    "Selamat tinggal! Jangan ragu untuk kembali jika butuh bantuan.",
                    "Percakapan yang menyenangkan! Sampai jumpa lagi."
                ]
                print(f"\n{Colors.PRIMARY}MOREN:{Style.RESET_ALL} ", end="")
                typewriter_effect(random.choice(farewells))
                time.sleep(1)
                break
                
            elif user_input.lower() == 'help':
                show_help()
                continue
                
            elif user_input.lower() == 'clear':
                clear_screen()
                display_header()
                continue
                
            elif user_input.lower() == 'info':
                info_msg = f"Saya MOREN v1.3.0, asisten AI berbasis DeepHermes 3 (Mistral 24B). Dibuat oleh Ade Pratama untuk membantu berbagai kebutuhan dengan santun dan bijak."
                print(f"\n{Colors.PRIMARY}MOREN:{Style.RESET_ALL} ", end="")
                typewriter_effect(info_msg)
                continue
                
            elif user_input.lower() == 'history':
                if len(messages) <= 1:
                    print(f"\n{Colors.PRIMARY}MOREN:{Style.RESET_ALL} ", end="")
                    typewriter_effect("Belum ada riwayat percakapan.")
                else:
                    print(f"\n{Colors.ACCENT}Riwayat Percakapan:{Style.RESET_ALL}")
                    for idx, msg in enumerate(messages[1:], 1):
                        role = "Anda" if msg["role"] == "user" else "MOREN"
                        color = Colors.SUCCESS if msg["role"] == "user" else Colors.PRIMARY
                        print(f"\n{color}{role}:{Style.RESET_ALL} {msg['content']}")
                continue
                
            if not user_input:
                print(f"{Colors.SOFT}Silakan ketik pesan Anda...{Style.RESET_ALL}")
                continue
                
            # Tambahkan pesan pengguna
            messages.append({"role": "user", "content": user_input})
            
            # Animasi loading
            animated_loading()
            
            # Dapatkan respons AI
            ai_response = chat_with_ai(messages)
            
            # Tampilkan respons
            print(f"\n{Colors.PRIMARY}MOREN:{Style.RESET_ALL} ", end="")
            typewriter_effect(ai_response)
            
            # Tambahkan respons ke riwayat
            messages.append({"role": "assistant", "content": ai_response})
            
        except KeyboardInterrupt:
            print(f"\n\n{Colors.ACCENT}Terima kasih telah menggunakan MOREN!{Style.RESET_ALL}")
            break
        except Exception as e:
            print(f"\n{Colors.ERROR}Terjadi kesalahan: {str(e)}{Style.RESET_ALL}")
            print(f"{Colors.SOFT}Silakan coba lagi.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
