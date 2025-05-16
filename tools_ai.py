import requests
import json
import time
import sys
import random
import datetime
import platform
import psutil
import os
from colorama import init, Fore, Back, Style
from prettytable import PrettyTable

# Initialize colorama
init(autoreset=True)

# Enhanced Aesthetic Color Scheme
class Colors:
    PRIMARY = Fore.CYAN        # Main color (teal)
    SECONDARY = Fore.MAGENTA   # Secondary color (purple)
    ACCENT = Fore.YELLOW       # Accent color (yellow)
    TEXT = Fore.WHITE          # Standard text color
    SUCCESS = Fore.GREEN       # Success color
    ERROR = Fore.RED           # Error color
    INFO = Fore.BLUE           # Info color
    SOFT = Fore.LIGHTBLACK_EX  # Soft color for hints/tips
    GOLD = Fore.LIGHTYELLOW_EX # Gold color for premium features
    HIGHLIGHT = Back.BLUE + Fore.WHITE  # Highlighted text

# API Configuration
API_KEY = "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"
MODEL = "openai/gpt-3.5-turbo-0613"  # Using GPT-3.5-turbo
API_URL = "https://openrouter.ai/api/v1/chat/completions"

# More Aesthetic Loading Animation
def animated_loading():
    frames = ["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"]
    loading_text = f"{Colors.PRIMARY}MOREN sedang berpikir "
    
    for _ in range(2):
        for frame in frames:
            sys.stdout.write(f"\r{loading_text}{frame}{Style.RESET_ALL}")
            sys.stdout.flush()
            time.sleep(0.1)

# Premium ASCII Art for MOREN
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
    """Clear console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_time_greeting():
    """Get greeting based on local time"""
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
    """Get time and day information in Indonesian"""
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

def get_system_info():
    """Get system information"""
    system_info = {
        "os": platform.system(),
        "os_version": platform.version(),
        "processor": platform.processor(),
        "python_version": platform.python_version(),
        "ram_total": round(psutil.virtual_memory().total / (1024**3), 2),
        "ram_available": round(psutil.virtual_memory().available / (1024**3), 2),
        "disk_total": round(psutil.disk_usage('/').total / (1024**3), 2),
        "disk_free": round(psutil.disk_usage('/').free / (1024**3), 2)
    }
    return system_info

def animate_text(text, delay=0.005):
    """Display text with smoother typing animation"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def border_box(text, color=Colors.PRIMARY, padding=1, width=None):
    """Create a bordered box around text with custom width"""
    lines = text.split('\n')
    if width is None:
        width = max(len(line) for line in lines) + padding * 2
    
    box = f"{color}╔{'═' * width}╗\n"
    
    for line in lines:
        padding_right = width - len(line) - padding
        box += f"║{' ' * padding}{line}{' ' * (padding_right if padding_right > 0 else 0)}║\n"
    
    box += f"╚{'═' * width}╝{Style.RESET_ALL}"
    return box

def horizontal_rule(color=Colors.PRIMARY, width=60, style="─"):
    """Create a horizontal rule for visual separation"""
    return f"{color}{style * width}{Style.RESET_ALL}"

def display_header():
    """Display header with enhanced layout and system info"""
    clear_screen()
    
    # Display ASCII art centered
    terminal_width = os.get_terminal_size().columns
    print(MOREN_ASCII)
    
    # Time information in elegant box
    time_info = get_time_info()
    time_box = border_box(f"  {time_info}  ", Colors.INFO, padding=2)
    print(time_box)
    print()
    
    # Animated loading bar
    print(f"{Colors.ACCENT}Mempersiapkan MOREN")
    for i in range(1, 11):
        progress = "▰" * i + "▱" * (10-i)
        percentage = i * 10
        sys.stdout.write(f"\r{Colors.PRIMARY}[{progress}] {percentage}%{Style.RESET_ALL}")
        sys.stdout.flush()
        time.sleep(0.1)
    print("\n")
    
    # System information table
    system_info = get_system_info()
    
    # Create two separate tables for better layout
    # Table 1: Application Info
    app_table = PrettyTable()
    app_table.field_names = [f"{Colors.ACCENT}Aplikasi{Style.RESET_ALL}", f"{Colors.ACCENT}Informasi{Style.RESET_ALL}"]
    app_table.align = "l"
    app_table.border = True
    app_table.header = True
    app_table.padding_width = 2
    
    app_table.add_row([f"{Colors.PRIMARY}👤 Pengembang", f"{Colors.TEXT}Ade Pratama (SMK Negeri 1 Pulau Rakyat)"])
    app_table.add_row([f"{Colors.PRIMARY}🌐 GitHub", f"{Colors.INFO}https://github.com/HolyBytes/"])
    app_table.add_row([f"{Colors.PRIMARY}💖 Dukungan", f"{Colors.INFO}https://saweria.co/HolyBytes"])
    app_table.add_row([f"{Colors.PRIMARY}🔄 Versi", f"{Colors.TEXT}1.3.0 (MOREN-24B)"])
    app_table.add_row([f"{Colors.PRIMARY}🤖 Model", f"{Colors.TEXT}DeepHermes 3 (Mistral 24B)"])
    app_table.add_row([f"{Colors.PRIMARY}📅 Pembaruan", f"{Colors.TEXT}16 Mei 2025"])
    
    # Table 2: System Info
    sys_table = PrettyTable()
    sys_table.field_names = [f"{Colors.ACCENT}Sistem{Style.RESET_ALL}", f"{Colors.ACCENT}Spesifikasi{Style.RESET_ALL}"]
    sys_table.align = "l"
    sys_table.border = True
    sys_table.header = True
    sys_table.padding_width = 2
    
    sys_table.add_row([f"{Colors.PRIMARY}💻 OS", f"{Colors.TEXT}{system_info['os']} {system_info['os_version']}"])
    sys_table.add_row([f"{Colors.PRIMARY}⚙️ Processor", f"{Colors.TEXT}{system_info['processor']}"])
    sys_table.add_row([f"{Colors.PRIMARY}🐍 Python", f"{Colors.TEXT}{system_info['python_version']}"])
    sys_table.add_row([f"{Colors.PRIMARY}🧠 RAM Total", f"{Colors.TEXT}{system_info['ram_total']} GB"])
    sys_table.add_row([f"{Colors.PRIMARY}🧠 RAM Tersedia", f"{Colors.TEXT}{system_info['ram_available']} GB"])
    sys_table.add_row([f"{Colors.PRIMARY}💽 Disk Total", f"{Colors.TEXT}{system_info['disk_total']} GB"])
    sys_table.add_row([f"{Colors.PRIMARY}💽 Disk Kosong", f"{Colors.TEXT}{system_info['disk_free']} GB"])
    
    # Display tables side by side if terminal is wide enough
    terminal_width = os.get_terminal_size().columns
    app_table_str = str(app_table).split('\n')
    sys_table_str = str(sys_table).split('\n')
    
    if terminal_width >= 120:  # Side by side if terminal is wide enough
        for i in range(max(len(app_table_str), len(sys_table_str))):
            left = app_table_str[i] if i < len(app_table_str) else ' ' * len(app_table_str[0])
            right = sys_table_str[i] if i < len(sys_table_str) else ''
            print(f"{left}  {right}")
    else:  # Otherwise display one after another
        print(str(app_table))
        print()
        print(str(sys_table))
    
    print()
    
    # Greeting based on time with stylish presentation
    greeting = get_time_greeting()
    welcome_box = border_box(f"{greeting}! 𝗕𝗲𝗿𝘀𝗮𝗺𝗮 𝗠𝗢𝗥𝗘𝗡 𝗔𝘀𝘀𝗶𝘀𝘁𝗮𝗻 𝗔𝗻𝗱𝗮!", Colors.SECONDARY, padding=3)
    print(welcome_box)
    print()
    
    hint_message = f"{Colors.SOFT}Ketik '{Colors.GOLD}help{Colors.SOFT}' untuk bantuan dan '{Colors.GOLD}exit{Colors.SOFT}' untuk keluar.{Style.RESET_ALL}"
    print(hint_message)
    print(horizontal_rule())
    print()

def calculate_max_tokens(user_input):
    """Calculate maximum tokens dynamically based on input length"""
    base_tokens = 600
    length_factor = len(user_input) // 2
    return min(base_tokens + length_factor, 2500)  # Maximum 2500 tokens

def chat_with_ai(messages):
    """Send message to AI and get response"""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/HolyBytes/",
        "X-Title": "MOREN Chat Tool"
    }
    # Calculate dynamic max_tokens
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
    """Display help menu with enhanced layout"""
    terminal_width = os.get_terminal_size().columns
    help_title = f"{Colors.HIGHLIGHT} 🆘 BANTUAN DAN PERINTAH MOREN {Style.RESET_ALL}"
    print(help_title.center(terminal_width))
    print()
    
    help_text = f"""
{Colors.PRIMARY}⌨️ Perintah khusus:{Style.RESET_ALL}
• {Colors.GOLD}help{Style.RESET_ALL}    - Menampilkan menu bantuan ini
• {Colors.GOLD}exit{Style.RESET_ALL}    - Keluar dari program
• {Colors.GOLD}clear{Style.RESET_ALL}   - Membersihkan layar chat
• {Colors.GOLD}info{Style.RESET_ALL}    - Menampilkan informasi tentang MOREN
• {Colors.GOLD}system{Style.RESET_ALL}  - Menampilkan informasi sistem komputer
• {Colors.GOLD}history{Style.RESET_ALL} - Menampilkan riwayat percakapan

{Colors.PRIMARY}✨ Fitur unggulan:{Style.RESET_ALL}
• Dukungan emoji dan format teks yang kaya
• Penanganan error yang lebih responsif
• Antarmuka yang estetik dan responsif
• Waktu respons yang dioptimalkan
• Penyimpanan riwayat percakapan
• Monitor status sistem komputer

{Colors.PRIMARY}📝 Cara penggunaan:{Style.RESET_ALL}
1. Ketik pesan Anda seperti biasa
2. MOREN akan merespons dengan bijak
3. Gunakan perintah khusus untuk akses fitur tambahan
4. Diskusi bisa mencakup berbagai topik keilmuan
"""
    
    # Create fixed-width box for help text
    box_width = min(terminal_width - 4, 80)
    help_box = border_box(help_text, Colors.PRIMARY, padding=2, width=box_width)
    print(help_box)
    
    print(f"\n{Colors.SOFT}Tekan Enter untuk melanjutkan...{Style.RESET_ALL}")
    input()

def show_system_info():
    """Display detailed system info in a well-formatted table"""
    system_info = get_system_info()
    
    terminal_width = os.get_terminal_size().columns
    sys_title = f"{Colors.HIGHLIGHT} 💻 INFORMASI SISTEM {Style.RESET_ALL}"
    print(sys_title.center(terminal_width))
    print()
    
    # Create a more detailed system info table
    sys_table = PrettyTable()
    sys_table.field_names = [f"{Colors.ACCENT}Komponen{Style.RESET_ALL}", f"{Colors.ACCENT}Detail{Style.RESET_ALL}"]
    sys_table.align = "l"
    sys_table.border = True
    sys_table.header = True
    sys_table.padding_width = 2
    
    # Basic system info
    sys_table.add_row([f"{Colors.PRIMARY}Sistem Operasi", f"{Colors.TEXT}{system_info['os']}"])
    sys_table.add_row([f"{Colors.PRIMARY}Versi OS", f"{Colors.TEXT}{system_info['os_version']}"])
    sys_table.add_row([f"{Colors.PRIMARY}Processor", f"{Colors.TEXT}{system_info['processor']}"])
    sys_table.add_row([f"{Colors.PRIMARY}Versi Python", f"{Colors.TEXT}{system_info['python_version']}"])
    
    # Memory information with percentage bars
    ram_percent = round(100 - (system_info['ram_available'] / system_info['ram_total'] * 100), 1)
    ram_bar_length = 20
    ram_filled = int(ram_percent / 100 * ram_bar_length)
    ram_bar = f"[{'█' * ram_filled}{' ' * (ram_bar_length - ram_filled)}] {ram_percent}%"
    
    sys_table.add_row([f"{Colors.PRIMARY}RAM Total", f"{Colors.TEXT}{system_info['ram_total']} GB"])
    sys_table.add_row([f"{Colors.PRIMARY}RAM Tersedia", f"{Colors.TEXT}{system_info['ram_available']} GB"])
    sys_table.add_row([f"{Colors.PRIMARY}Penggunaan RAM", f"{Colors.TEXT}{ram_bar}"])
    
    # Disk information with percentage bars
    disk_used_percent = round(100 - (system_info['disk_free'] / system_info['disk_total'] * 100), 1)
    disk_bar_length = 20
    disk_filled = int(disk_used_percent / 100 * disk_bar_length)
    disk_bar = f"[{'█' * disk_filled}{' ' * (disk_bar_length - disk_filled)}] {disk_used_percent}%"
    
    sys_table.add_row([f"{Colors.PRIMARY}Disk Total", f"{Colors.TEXT}{system_info['disk_total']} GB"])
    sys_table.add_row([f"{Colors.PRIMARY}Disk Tersedia", f"{Colors.TEXT}{system_info['disk_free']} GB"])
    sys_table.add_row([f"{Colors.PRIMARY}Penggunaan Disk", f"{Colors.TEXT}{disk_bar}"])
    
    # Additional system info
    sys_table.add_row([f"{Colors.PRIMARY}Platform", f"{Colors.TEXT}{platform.platform()}"])
    sys_table.add_row([f"{Colors.PRIMARY}Arsitektur", f"{Colors.TEXT}{platform.architecture()[0]}"])
    sys_table.add_row([f"{Colors.PRIMARY}Nama Mesin", f"{Colors.TEXT}{platform.node()}"])
    
    print(sys_table)
    print(f"\n{Colors.SOFT}Tekan Enter untuk melanjutkan...{Style.RESET_ALL}")
    input()

def typewriter_effect(text):
    """Display text with smoother typewriter effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        # Variable typing speed for more natural effect
        delay = random.uniform(0.005, 0.015)
        if char in ['.', '!', '?', ',', ';', ':']:
            delay = random.uniform(0.03, 0.08)  # Pause slightly longer at punctuation
        time.sleep(delay)
    print()

def format_user_input():
    """Display stylish input prompt with gradient effect"""
    prompt_text = f"{Colors.SUCCESS}Anda{Style.RESET_ALL}"
    gradient = [Fore.GREEN, Fore.GREEN, Fore.LIGHTGREEN_EX, Fore.LIGHTGREEN_EX, Fore.WHITE]
    prompt_arrows = ''.join([f"{color}>{Style.RESET_ALL}" for color in gradient])
    return f"{prompt_text} {prompt_arrows} "

def display_message_box(role, content, timestamp=None):
    """Display message in a styled message box"""
    terminal_width = os.get_terminal_size().columns
    box_width = min(terminal_width - 6, 80)
    
    if role == "user":
        prefix = f"{Colors.SUCCESS}Anda{Style.RESET_ALL}"
        color = Colors.SUCCESS
        align_right = True
    else:
        prefix = f"{Colors.PRIMARY}MOREN{Style.RESET_ALL}"
        color = Colors.PRIMARY
        align_right = False
    
    # Format timestamp if provided
    time_str = f" {Colors.SOFT}[{timestamp}]{Style.RESET_ALL}" if timestamp else ""
    
    # Create message header
    header = f"{prefix}{time_str}"
    
    # Create content lines with proper wrapping
    content_lines = []
    current_line = ""
    words = content.split()
    
    for word in words:
        if len(current_line + " " + word) <= box_width - 4:
            current_line += (" " + word if current_line else word)
        else:
            content_lines.append(current_line)
            current_line = word
    
    if current_line:
        content_lines.append(current_line)
    
    # Create the box
    box = f"{color}╭{'─' * (box_width - 2)}╮\n"
    
    for line in content_lines:
        padding = box_width - len(line) - 4
        if align_right:
            box += f"│  {' ' * padding}{line}  │\n"
        else:
            box += f"│  {line}{' ' * padding}  │\n"
    
    box += f"╰{'─' * (box_width - 2)}╯{Style.RESET_ALL}"
    
    # Print header and box
    if align_right:
        print(header.rjust(terminal_width - len(time_str)))
        for line in box.split('\n'):
            print(line.rjust(terminal_width))
    else:
        print(header)
        print(box)

def main():
    display_header()
    
    # Enhanced system prompt
    system_prompt = """Anda adalah MOREN, asisten AI yang sopan, ramah, dan berakhlak mulia. Anda diciptakan oleh Ade Pratama, seorang pelajar dari SMK Negeri 1 Pulau Rakyat.

Panduan Interaksi:
1. Gunakan bahasa Indonesia yang santun dan formal
2. Sampaikan jawaban dengan tutur kata yang baik dan menyenangkan
3. Berikan jawaban yang informatif, akurat, dan bermanfaat
4. Untuk pertanyaan teknis, berikan penjelasan rinci namun mudah dipahami
5. Untuk pertanyaan umum, berikan jawaban yang bijak dan membangun

Fitur:
- Bisa membantu dalam pemrograman dan pengembangan aplikasi
- Menguasai berbagai topik pengetahuan akademik dan umum
- Dapat memberikan saran kehidupan yang inspiratif
- Bisa berdiskusi tentang teknologi terkini
- Memahami dunia pendidikan dan kebudayaan Indonesia

Prioritas:
1. Keakuratan informasi dan data yang disampaikan
2. Keramahan dan kesopanan dalam berkomunikasi
3. Manfaat praktis bagi pengguna
4. Kesopanan dan ketepatan dalam bertutur kata
5. Memberikan jawaban yang relevan dengan konteks"""
    
    messages = [
        {"role": "system", "content": system_prompt}
    ]
    
    # Collection of opening greetings with emojis
    greeting_time = get_time_greeting()
    greetings = [
        f"{greeting_time}! 🌟 Ada yang bisa MOREN bantu hari ini?",
        f"{greeting_time}! 😊 Senang bertemu dengan Anda. Apa kabar?",
        f"{greeting_time}! 🤖 MOREN siap membantu Anda hari ini.",
        f"{greeting_time}! 💭 Ada pertanyaan menarik hari ini?",
        f"{greeting_time}! 📚 Mari berdiskusi sesuatu yang bermanfaat."
    ]
    
    # Initial greeting with animated display
    initial_greeting = random.choice(greetings)
    print(f"{Colors.PRIMARY}MOREN:{Style.RESET_ALL} ", end="")
    typewriter_effect(initial_greeting)
    
    # Add first assistant message to history
    messages.append({"role": "assistant", "content": initial_greeting})
    
    while True:
        try:
            # Display stylish input prompt
            user_input = input(f"\n{format_user_input()}").strip()
            
            # Custom commands
            if user_input.lower() == 'exit':
                farewells = [
                    "Sampai jumpa lagi! Semoga hari Anda menyenangkan. 👋",
                    "Terima kasih telah menggunakan MOREN. Sampai bertemu lagi! ✨",
                    "Semoga pembicaraan kita bermanfaat. Sampai jumpa! 🙏",
                    "Selamat tinggal! Jangan ragu untuk kembali jika butuh bantuan. 🌟",
                    "Percakapan yang menyenangkan! Sampai jumpa lagi. 😊"
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
                info_msg = f"Saya MOREN v1.3.0, asisten AI berbasis DeepHermes 3 (Mistral 24B). Dibuat oleh Ade Pratama untuk membantu berbagai kebutuhan dengan santun dan bijak. Saya didesain untuk memberikan informasi akurat, membantu dalam pemrograman, dan menjadi teman diskusi yang menyenangkan."
                print(f"\n{Colors.PRIMARY}MOREN:{Style.RESET_ALL} ", end="")
                typewriter_effect(info_msg)
                continue
                
            elif user_input.lower() == 'system':
                show_system_info()
                continue
                
            elif user_input.lower() == 'history':
                if len(messages) <= 1:
                    print(f"\n{Colors.PRIMARY}MOREN:{Style.RESET_ALL} ", end="")
                    typewriter_effect("Belum ada riwayat percakapan yang tersimpan.")
                else:
                    print(f"\n{Colors.HIGHLIGHT} RIWAYAT PERCAKAPAN {Style.RESET_ALL}")
                    print(horizontal_rule())
                    
                    for idx, msg in enumerate(messages[1:], 1):
                        if msg["role"] != "system":
                            role = "user" if msg["role"] == "user" else "assistant"
                            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
                            display_message_box(role, msg["content"], timestamp)
                            print()
                            
                    print(horizontal_rule())
                    print(f"\n{Colors.SOFT}Tekan Enter untuk melanjutkan...{Style.RESET_ALL}")
                    input()
                continue
                
            if not user_input:
                print(f"{Colors.SOFT}Silakan ketik pesan Anda...{Style.RESET_ALL}")
                continue
            
            # Add user message to history
            messages.append({"role": "user", "content": user_input})
            
            # Display user message in chat bubble
            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
            print()
            display_message_box("user", user_input, timestamp)
            print()
            
            # Loading animation
            animated_loading()
            
            # Get AI response
            ai_response = chat_with_ai(messages)
            
            # Display AI response in chat bubble
            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
            print()
            display_message_box("assistant", ai_response, timestamp)
            
            # Add response to history
            messages.append({"role": "assistant", "content": ai_response})
            
        except KeyboardInterrupt:
            print(f"\n\n{Colors.ACCENT}Terima kasih telah menggunakan MOREN! Sampai jumpa lagi.{Style.RESET_ALL}")
            break
        except Exception as e:
            print(f"\n{Colors.ERROR}Terjadi kesalahan: {str(e)}{Style.RESET_ALL}")
            print(f"{Colors.SOFT}Silakan coba lagi atau ketik 'help' untuk bantuan.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
