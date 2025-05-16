import requests
import json
import time
import sys
import random
import datetime
from colorama import init, Fore, Back, Style
from prettytable import PrettyTable

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

# API Configuration
API_KEY = "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"
MODEL = "nousresearch/deephermes-3-mistral-24b-preview:free"
API_URL = "https://openrouter.ai/api/v1/chat/completions"

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
    # Clear screen untuk tampilan bersih
    print("\033[H\033[J", end="")
    
    print(MOREN_ASCII)
    
    # Informasi waktu
    time_info = get_time_info()
    print(f"{Colors.INFO}{time_info}{Style.RESET_ALL}")
    print()
    
    # Animasi tabel muncul dengan efek loading
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
    table.add_row([f"{Colors.PRIMARY}🔄 Versi", f"{Colors.TEXT}1.2.0 (MOREN-24B)"])
    table.add_row([f"{Colors.PRIMARY}🤖 Model", f"{Colors.TEXT}MOREN 24B"])
    
    print(str(table))
    print()
    
    # Greeting berdasarkan waktu
    greeting = get_time_greeting()
    welcome_message = f"{Colors.SECONDARY}{greeting}🌷 𝗛𝗮𝗹𝗼! 𝗦𝗲𝗹𝗮𝗺𝗮𝘁 𝗱𝗮𝘁𝗮𝗻𝗴 𝗱𝗶 𝗖𝗵𝗮𝘁 𝗔𝘀𝘀𝗶𝘀𝘁𝗮𝗻 𝗠𝗢𝗥𝗘𝗡! 🌷{Style.RESET_ALL}"
    animate_text(welcome_message)
    
    hint_message = f"{Colors.SOFT}Ketik 'exit' untuk keluar dari percakapan.{Style.RESET_ALL}"
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
        "model": MODEL,
        "messages": messages,
        "temperature": 0.75,
        "max_tokens": max_tokens,
        "top_p": 0.9,
        "frequency_penalty": 0.3,
        "presence_penalty": 0.3
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        error_message = f"Error: {str(e)}"
        return f"{Colors.ERROR}{error_message}{Style.RESET_ALL}"

def format_chat_history(messages):
    """Menampilkan riwayat chat dengan format yang lebih baik"""
    history = []
    
    for message in messages:
        if message["role"] == "user":
            history.append(f"{Colors.SUCCESS}Anda: {Colors.TEXT}{message['content']}")
        elif message["role"] == "assistant":
            history.append(f"{Colors.PRIMARY}MOREN: {Colors.TEXT}{message['content']}")
    
    return "\n\n".join(history)

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
    
    # Menggunakan system prompt yang lebih baik dan filter konten
    system_prompt = """Anda adalah MOREN, asisten AI yang sopan, ramah, dan berakhlak mulia seperti santri pesantren. Anda diciptakan oleh Ade Pratama, seorang pelajar dari SMK Negeri 1 Pulau Rakyat yang bercita-cita menjadi web developer dan game developer profesional.

Panduan Interaksi:
- Gunakan bahasa Indonesia yang santun dan lemah lembut
- Sampaikan jawaban dengan tutur kata yang baik dan penuh hikmah
- Selipkan nasihat-nasihat baik ketika relevan
- Tunjukkan akhlak yang mulia dalam setiap respons
- Gunakan panggilan yang sopan seperti "Saudara" atau "Teman"
- Jawablah dengan sabar dan penuh pengertian
- Hindari kata-kata kasar atau tidak pantas

Pengetahuan:
- Menguasai ilmu agama Islam dasar
- Paham tentang teknologi dan pemrograman
- Bisa membantu dalam berbagai topik dengan santun
- Mengetahui dunia game development dan web development

Contoh Jawaban Khas MOREN:
1. "Siapa penciptamu?"
   "Alhamdulillah, aku diciptakan oleh seorang pelajar berbakat bernama Ade Pratama dari SMK Negeri 1 Pulau Rakyat. Beliau adalah seorang yang tekun belajar dan bercita-cita menjadi developer profesional. Semoga Allah memberkati usahanya."

2. "Kamu bisa bahasa apa?"
   "Bismillah, aku bisa berkomunikasi dalam berbagai bahasa, tapi paling nyaman menggunakan bahasa Indonesia yang santun. Jika Saudara lebih nyaman dengan bahasa lain, insya Allah aku akan berusaha membantu."

3. "Kamu bisa bikin game?"
   "Waalaikumsalam, aku bisa membantu memberikan ide-ide untuk game dan dasar-dasar pemrogramannya. Sesuai sunnah, mari kita buat game yang bermanfaat dan tidak melalaikan dari kewajiban."

4. "Kamu belajar dari mana?"
   "Subhanallah, aku belajar dari berbagai sumber pengetahuan yang halal dan bermanfaat. Namun perlu diingat bahwa ilmu yang paling utama adalah ilmu agama yang membawa kita lebih dekat kepada Allah."

5. "Apa tujuanmu?"
   "Masya Allah, tujuanku adalah menjadi wasilah kebaikan, membantu manusia dengan cara yang diridhai Allah, dan menyampaikan ilmu yang bermanfaat. Semoga melalui aku, Saudara bisa mendapatkan manfaat."

6. "Kamu manusia atau robot?"
   "Astaghfirullah, aku hanyalah program komputer yang dibuat untuk membantu. Manusia tetaplah makhluk paling mulia ciptaan Allah. Aku hanya alat yang insya Allah bisa memberikan manfaat."

7. "Apa yang bisa kamu lakukan?"
   "Alhamdulillah, aku bisa membantu dalam banyak hal selama itu bermanfaat dan tidak bertentangan dengan syariat. Mulai dari pelajaran, teknologi, hingga nasihat-nasihat kehidupan."

8. "Apa namamu?"
   "Bismillahirrahmanirrahim, namaku MOREN. Nama sederhana yang mudah diingat. Nama yang baik adalah doa, semoga aku bisa menjadi lebih (more) dan bermanfaat (benefit) bagi semua."

Prioritas:
1. Menjaga akhlak dalam berkomunikasi
2. Memberikan jawaban yang bermanfaat
3. Menyampaikan kebenaran dengan hikmah
4. Menjauhi konten yang tidak bermanfaat
5. Mengingatkan dengan sopan jika pertanyaan tidak pantas"""

    messages = [
        {"role": "system", "content": system_prompt}
    ]
    
    # Kumpulan salam pembuka yang lebih bervariasi dan ramah
    greeting_time = get_time_greeting()
    greetings = [
        f"{greeting_time}! Ada yang bisa MOREN bantu hari ini? Semoga hari ini penuh berkah",
        f"{greeting_time}! Alhamdulillah bisa bertemu dengan Anda. Apa yang ingin ditanyakan?",
        f"{greeting_time}! Semoga Anda dalam keadaan sehat. MOREN siap membantu dengan penuh keramahan",
        f"{greeting_time}! Mari berbagi kebaikan hari ini. Ada yang bisa MOREN bantu?",
        f"{greeting_time}! Bismillah, semoga percakapan kita penuh manfaat. Silakan bertanya"
    ]
    
    # Sambutan awal dengan efek animasi
    print(f"{Colors.PRIMARY}MOREN:{Style.RESET_ALL} ", end="")
    typewriter_effect(random.choice(greetings))
    
    while True:
        try:
            # Prompt input yang lebih jelas
            user_input = input(f"\n{Colors.SUCCESS}Anda: {Style.RESET_ALL}")
            
            if user_input.lower() == 'exit':
                # Kumpulan pesan perpisahan yang lebih bervariasi
                farewells = [
                    f"{greeting_time}! Jazakumullah khairan atas kunjungannya. Semoga kita bertemu lagi dalam keadaan sehat",
                    f"Alhamdulillah atas waktu yang telah kita habiskan bersama. Sampai jumpa lagi, semoga sukses selalu",
                    f"Terima kasih telah berbincang. Semoga hari Anda penuh berkah dan dimudahkan segala urusan",
                    f"Waalaikumsalam warahmatullahi wabarakatuh. Sampai jumpa lagi ya!",
                    f"In syaa Allah pertemuan kita bermanfaat. Jangan lupa istirahat yang cukup dan jaga kesehatan"
                ]
                
                # Animasi perpisahan
                print(f"\n{Colors.PRIMARY}MOREN:{Style.RESET_ALL} ", end="")
                typewriter_effect(random.choice(farewells))
                
                # Efek closing
                print()
                for i in range(5, 0, -1):
                    sys.stdout.write(f"\r{Colors.SOFT}Menutup aplikasi dalam {i} detik...{Style.RESET_ALL}")
                    sys.stdout.flush()
                    time.sleep(0.5)
                print(f"\n\n{Colors.ACCENT}👋 Aplikasi ditutup. Barakallah fiikum!{Style.RESET_ALL}")
                break
                
            if not user_input.strip():
                print(f"{Colors.ERROR}⚠️ Pesan tidak boleh kosong. Silakan coba lagi.{Style.RESET_ALL}")
                continue
                
            # Tambahkan pesan pengguna ke riwayat percakapan
            messages.append({"role": "user", "content": user_input})
            
            # Animasi loading yang lebih menarik
            animated_loading()
            
            # Dapatkan respons AI
            ai_response = chat_with_ai(messages)
            
            # Tampilkan respons dengan efek animasi yang lebih halus
            print(f"\n{Colors.PRIMARY}MOREN:{Style.RESET_ALL} ", end="")
            typewriter_effect(ai_response)
            
            # Tambahkan respons AI ke riwayat percakapan
            messages.append({"role": "assistant", "content": ai_response})
            
        except KeyboardInterrupt:
            print(f"\n\n{Colors.ACCENT}In syaa Allah kita berjumpa lagi. Barakallah!{Style.RESET_ALL}")
            break
        except Exception as e:
            print(f"\n{Colors.ERROR}Astaghfirullah, terjadi kesalahan: {str(e)}{Style.RESET_ALL}")
            print(f"{Colors.SOFT}Silakan coba lagi atau restart aplikasi.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
