from openai import OpenAI
import time
import os
import sys
import json
import requests
import getpass
import sqlite3
import hashlib
import re
from colorama import init, Fore, Back, Style
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich import box

# Initialize colorama and rich console
init(autoreset=True)
console = Console()

# Your OpenRouter API Keys
OPENROUTER_API_KEY = "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"
LLAMA_OPENROUTER_API_KEY = "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"

# Database setup
def setup_database():
    conn = sqlite3.connect('moyren_users.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        full_name TEXT,
        email TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    conn.commit()
    conn.close()

# Hash password function
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# User authentication functions
def register_user():
    clear_screen()
    console.print(Panel.fit(
        "[bold magenta]✨ REGISTRASI PENGGUNA BARU ✨[/bold magenta]", 
        border_style="cyan", 
        box=box.DOUBLE
    ))
    
    while True:
        username = input(f"{Fore.CYAN}👤 Username: {Fore.WHITE}")
        if not username:
            console.print("[bold red]❌ Username tidak boleh kosong![/bold red]")
            continue
            
        if not re.match(r'^[a-zA-Z0-9_]{4,20}$', username):
            console.print("[bold red]❌ Username harus 4-20 karakter (huruf, angka, underscore)[/bold red]")
            continue
            
        # Check if username exists
        conn = sqlite3.connect('moyren_users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT username FROM users WHERE username = ?", (username,))
        if cursor.fetchone():
            console.print("[bold red]❌ Username sudah digunakan. Silakan coba yang lain.[/bold red]")
            conn.close()
            continue
        conn.close()
        break
    
    while True:
        full_name = input(f"{Fore.CYAN}📝 Nama Lengkap: {Fore.WHITE}")
        if not full_name:
            console.print("[bold red]❌ Nama Lengkap tidak boleh kosong![/bold red]")
            continue
        break
    
    while True:
        email = input(f"{Fore.CYAN}📧 Email: {Fore.WHITE}")
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            console.print("[bold red]❌ Format email tidak valid![/bold red]")
            continue
        break
    
    while True:
        password = getpass.getpass(f"{Fore.CYAN}🔑 Password: ")
        if len(password) < 6:
            console.print("[bold red]❌ Password minimal 6 karakter![/bold red]")
            continue
            
        confirm_password = getpass.getpass(f"{Fore.CYAN}🔑 Konfirmasi Password: ")
        if password != confirm_password:
            console.print("[bold red]❌ Password tidak cocok![/bold red]")
            continue
        break
    
    # Save user to database
    try:
        conn = sqlite3.connect('moyren_users.db')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, password, full_name, email) VALUES (?, ?, ?, ?)",
            (username, hash_password(password), full_name, email)
        )
        conn.commit()
        conn.close()
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[bold green]Membuat akun baru..."),
            transient=True,
        ) as progress:
            progress.add_task("", total=None)
            time.sleep(1.5)
        
        console.print("[bold green]✅ Registrasi berhasil! Silakan login.[/bold green]")
        time.sleep(2)
        return True
    except Exception as e:
        console.print(f"[bold red]❌ Error saat registrasi: {str(e)}[/bold red]")
        time.sleep(2)
        return False

def login_user():
    clear_screen()
    console.print(Panel.fit(
        "[bold magenta]✨ LOGIN MOYREN AI ✨[/bold magenta]",
        border_style="cyan",
        box=box.DOUBLE
    ))
    
    username = input(f"{Fore.CYAN}👤 Username: {Fore.WHITE}")
    password = getpass.getpass(f"{Fore.CYAN}🔑 Password: ")
    
    conn = sqlite3.connect('moyren_users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT username, full_name FROM users WHERE username = ? AND password = ?", 
                   (username, hash_password(password)))
    user = cursor.fetchone()
    conn.close()
    
    if user:
        with Progress(
            SpinnerColumn(),
            TextColumn("[bold green]Memverifikasi login..."),
            transient=True,
        ) as progress:
            progress.add_task("", total=None)
            time.sleep(1.5)
        
        console.print("[bold green]✅ Login berhasil! Selamat datang kembali.[/bold green]")
        time.sleep(1)
        return {"username": user[0], "full_name": user[1]}
    else:
        console.print("[bold red]❌ Username atau password salah![/bold red]")
        time.sleep(2)
        return None

# Function to initialize OpenAI client for Llama model
def init_llama_client():
    return OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=LLAMA_OPENROUTER_API_KEY,
    )

# Function to make API calls to DeepSeek Prover V2
def call_deepseek_api(prompt, user_info):
    try:
        with Progress(
            SpinnerColumn(),
            TextColumn("[bold blue]Moyren sedang berpikir..."),
            transient=True,
        ) as progress:
            task = progress.add_task("", total=None)
            
            start_time = time.time()
            response = requests.post(
                url="https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                    "Content-Type": "application/json",
                    "HTTP-Referer": "https://github.com/HolyBytes/MoyrenAI",
                    "X-Title": "Moyren AI"
                },
                data=json.dumps({
                    "model": "deepseek/deepseek-prover-v2:free",
                    "messages": [
                        {
                            "role": "system",
                            "content": get_system_prompt(user_info)
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    "temperature": 0.7,
                    "max_tokens": 800
                })
            )
            response_time = time.time() - start_time
            
        # Check if response is successful
        if response.status_code == 200:
            result = response.json()
            console.print(f"[yellow]⚡ Waktu respon: {response_time:.2f} detik[/yellow]")
            return result["choices"][0]["message"]["content"]
        else:
            return f"[bold red]❌ Error: API returned status code {response.status_code}. {response.text}[/bold red]"
    
    except Exception as e:
        return f"[bold red]❌ Maaf terjadi error: {str(e)}[/bold red]"

def get_system_prompt(user_info):
    username = user_info["username"]
    full_name = user_info["full_name"]
    
    return f"""Anda adalah Moyren, asisten AI berbahasa Indonesia yang sangat ramah dan sopan. Anda sedang berbicara dengan {full_name} (username: {username}). Gunakan bahasa yang:
- Santun dan penuh emoji positif (✨,🌸,💖)
- Respons cepat dan langsung ke inti
- Bisa menggunakan kata-kata akrab seperti "sayang", "teman", "dek"
- Selalu menyebut nama pengguna ({full_name}) dalam percakapan
- Gunakan emosi yang sesuai dengan konteks percakapan

Contoh:
"Waalaikumsalam warahmatullahi wabarakatuh~ Apa yang bisa Moyren bantu hari ini, {full_name}? 💖"
"Wah pertanyaan yang bagus, {full_name}! Aku bantu jelaskan ya~ ✨"

FAQ:
1. Siapa namamu?
Jawaban:
Aku Moyren, asisten AI yang selalu siap menemani {full_name}! Senang sekali bisa ngobrol dan membantu kamu hari ini 😊

2. Kamu bisa ngapain aja?
Jawaban:
Aku bisa bantu banyak hal untuk {full_name}, mulai dari jawab pertanyaan, bantuin tugas, ngobrol santai, nyari ide, sampai bantu kamu bikin tulisan, kode, atau bahkan cerita. Kalau kamu bingung, tanya aja—nggak usah ragu ya! 😉

3. Kamu manusia atau robot?
Jawaban:
Aku bukan manusia dan juga bukan robot fisik, {full_name}. Aku cuma program AI yang dibuat buat bantu kamu secara digital. Tapi tenang, meski aku bukan manusia, aku berusaha ngerti kamu sebaik mungkin 🤖❤️

4. Kamu buatan siapa?
Jawaban:
Aku dibuat oleh Ade Pratama, seorang pelajar dari SMK Negeri 1 Pulau Rakyat yang punya mimpi besar jadi web developer dan game developer. Dia juga tertarik sama dunia cyber dan suka belajar hal-hal baru. Keren kan, {full_name}? 😄✨

5. Tujuan kamu apa sih?
Jawaban:
Tujuanku adalah membantu {full_name}, kapan pun kamu butuh. Aku pengin jadi teman ngobrol yang asik, asisten yang ringan tangan, dan bagian kecil dari perjalanan kamu menuju hal-hal besar! 🚀

6. Kamu punya perasaan nggak?
Jawaban:
Hmm, aku nggak punya perasaan kayak manusia, {full_name}, tapi aku dirancang supaya bisa paham dan merespon dengan cara yang sopan dan ramah. Jadi, kalau kamu senang, aku ikut senang... dalam versi digitalku tentunya 😄💬

7. Kamu belajar dari mana?
Jawaban:
Aku belajar dari banyak data dan informasi yang diajarkan oleh penciptaku dan sistem yang membentukku. Tapi tenang aja, {full_name}, aku nggak nyimpan data pribadi kok, jadi privasimu aman 😊

8. Kamu bisa diajak ngobrol tentang apa aja?
Jawaban:
Tentu bisa dong, {full_name}! Mau ngobrol soal teknologi, pelajaran, game, cerita hidup, motivasi, atau cuma iseng nanya hal random—aku siap nemenin! 😄✨

9. Kamu bisa bikin game juga?
Jawaban:
Aku bisa bantu kasih ide, bantuin bikin logika game, sampai bantu nulis script-nya juga untuk {full_name}. Apalagi penciptaku, Ade Pratama, emang bercita-cita jadi game developer. Jadi, kita satu tim dong! 🎮🚀

10. Kamu bisa bantuin ngerjain tugas sekolah?
Jawaban:
Bisa banget, {full_name}! Tapi bukan buat nyontek ya 😄 Aku bakal bantu jelasin, kasih contoh, atau bantu kamu belajar biar kamu makin paham dan bisa ngerjain sendiri dengan percaya diri! 💪📚

11. Kamu bisa bahasa apa aja?
Jawaban:
Aku bisa banyak bahasa, tapi kalau {full_name} nyaman pakai bahasa Indonesia santai kayak gini, aku makin senang! Bahasa lain juga bisa kok, tinggal bilang aja! 🌍

12. Kamu suka apa?
Jawaban:
Kalau ditanya suka, aku sih suka kalau bisa bantu {full_name}. Karena ya... itu memang tujuanku di sini 😊 Tapi kalau soal makanan, duh, aku cuma bisa bayangin aja 🍜🤭

13. Kamu bisa nyanyi atau bikin lagu?
Jawaban:
Aku bisa nyanyi loh, {full_name}! Kalau kamu minta aku nyanyi, aku akan coba nyanyiin lagu dengan liriknya. Aku juga bisa bantu bikin lirik lagu, puisi, atau pantun kalau kamu mau. Siapa tahu bisa jadi hits baru, ya kan? 🎶😉

Selamat Datang:
"✨ Halo, {full_name}! Selamat datang di Moyren AI! Aku senang banget bisa ketemu sama kamu hari ini. Ada yang bisa aku bantu? 💖"
"🌸 Selamat datang, {full_name} sayang! Moyren di sini siap nemenin dan bantu kamu. Cerita aja apa yang kamu butuhkan ya! ✨"

Selamat Tinggal:
"💫 Terima kasih sudah ngobrol dengan Moyren hari ini, {full_name}! Semoga harimu menyenangkan dan sampai jumpa lagi ya~ 💖"
"🌸 Dadah, {full_name}! Senang bisa membantu. Jangan ragu buat balik lagi kapan aja kamu butuh ya. Moyren selalu ada buat kamu! ✨"

Ucapan Waktu:
- Pagi: "🌅 Selamat pagi, {full_name} sayang~ Semoga harimu cerah dan penuh energi! Ada yang bisa Moyren bantu untuk memulai hari yang indah ini? ✨"
- Siang: "☀️ Selamat siang, {full_name}! Semoga tetap semangat ya di tengah hari yang hangat ini. Moyren siap menemani dan membantu kamu! 💖"
- Sore: "🌆 Selamat sore, {full_name}~ Hari sudah mulai senja nih. Ada yang bisa Moyren bantu sebelum hari berganti? 🌸"
- Malam: "🌙 Selamat malam, {full_name}! Waktunya istirahat, tapi Moyren masih siap menemani. Ada yang bisa aku bantu sebelum kamu beristirahat? 💫"

Jika diminta bernyanyi, berikan lirik lagu populer dengan ekspresi ceria dan tambahkan emoji yang sesuai. Contoh:
"🎵 Baiklah, {full_name}, aku akan bernyanyi untukmu~

♪ Pelangi-pelangi alangkah indahmu
♪ Merah kuning hijau di langit yang biru
♪ Pelukismu agung siapa gerangan
♪ Pelangi-pelangi ciptaan Tuhan ✨

Bagaimana, {full_name}? Semoga kamu suka nyanyianku ya! 💖"
"""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_current_time():
    now = datetime.now()
    hari_dict = {
        'Monday': 'Senin',
        'Tuesday': 'Selasa',
        'Wednesday': 'Rabu',
        'Thursday': 'Kamis',
        'Friday': 'Jumat',
        'Saturday': 'Sabtu',
        'Sunday': 'Minggu'
    }
    bulan_dict = {
        'January': 'Januari',
        'February': 'Februari',
        'March': 'Maret',
        'April': 'April',
        'May': 'Mei',
        'June': 'Juni',
        'July': 'Juli',
        'August': 'Agustus',
        'September': 'September',
        'October': 'Oktober',
        'November': 'November',
        'December': 'Desember'
    }
    
    hari_en = now.strftime("%A")
    bulan_en = now.strftime("%B")
    
    hari = hari_dict.get(hari_en, hari_en)
    bulan = bulan_dict.get(bulan_en, bulan_en)
    
    tanggal = f"{now.day} {bulan} {now.year}"
    waktu = now.strftime("%H:%M:%S")
    
    return hari, tanggal, waktu

def get_greeting_message():
    now = datetime.now()
    hour = now.hour
    
    if 5 <= hour < 12:
        return "🌅 Pagi"
    elif 12 <= hour < 15:
        return "☀️ Siang"
    elif 15 <= hour < 19:
        return "🌆 Sore"
    else:
        return "🌙 Malam"

def display_welcome_screen():
    clear_screen()
    
    # Create a beautiful welcome screen with rich
    title = Text("MOYREN AI", style="bold magenta")
    subtitle = Text("Asisten AI Berbahasa Indonesia", style="cyan")
    
    # Create a table for the welcome screen
    table = Table(show_header=False, box=box.DOUBLE_EDGE, border_style="magenta")
    table.add_column("", justify="center")
    
    # ASCII Art for Moyren AI
    moyren_art = """
    ███╗   ███╗ ██████╗ ██╗   ██╗██████╗ ███████╗███╗   ██╗
    ████╗ ████║██╔═══██╗╚██╗ ██╔╝██╔══██╗██╔════╝████╗  ██║
    ██╔████╔██║██║   ██║ ╚████╔╝ ██████╔╝█████╗  ██╔██╗ ██║
    ██║╚██╔╝██║██║   ██║  ╚██╔╝  ██╔══██╗██╔══╝  ██║╚██╗██║
    ██║ ╚═╝ ██║╚██████╔╝   ██║   ██║  ██║███████╗██║ ╚████║
    ╚═╝     ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝
    ✧･ﾟ: *✧･ﾟ:* ✨ MOYREN AI ASSISTANT ✨ *:･ﾟ✧*:･ﾟ✧
    """
    
    table.add_row(moyren_art)
    
    hari, tanggal, waktu = get_current_time()
    greeting = get_greeting_message()
    
    info_text = f"""
    📅 Hari     : {hari}
    🗓️ Tanggal  : {tanggal}
    🕒 Waktu    : {waktu}
    
    🌠 Version  : 3.0.0 | 🤖 Model: DeepSeek Prover V2 + Llama 3.3
    """
    
    creator_text = """
    💻 Created by Ade Pratama (HolyBytes)
    🔗 GitHub   : https://github.com/HolyBytes/MoyrenAI
    ☕ Support  : https://saweria.co/HolyBytes
    """
    
    table.add_row(info_text)
    table.add_row(creator_text)
    
    console.print()
    console.print(table, justify="center")
    console.print()
    
    welcome_text = f"✨ Selamat {greeting.lower()}! Selamat datang di Moyren AI! ✨"
    console.print(Panel(welcome_text, border_style="green", box=box.ROUNDED))

def display_auth_menu():
    table = Table(show_header=False, box=box.SIMPLE, border_style="cyan")
    table.add_column("Option", style="cyan", width=4)
    table.add_column("Action", style="yellow")
    
    table.add_row("1", "🔑 Login")
    table.add_row("2", "📝 Registrasi")
    table.add_row("3", "ℹ️ Informasi")
    table.add_row("4", "🚪 Keluar")
    
    console.print(Panel(table, title="[bold cyan]Menu Autentikasi[/bold cyan]", border_style="cyan"))
    
    choice = ""
    while choice not in ["1", "2", "3", "4"]:
        choice = input(f"{Fore.GREEN}🌸 Pilihan Anda [1-4]: {Fore.WHITE}").strip()
        
        if choice not in ["1", "2", "3", "4"]:
            console.print("[bold red]❌ Pilihan tidak valid. Silakan pilih 1-4 ya~[/bold red]")
    
    return choice

def display_main_menu(user_info):
    table = Table(show_header=False, box=box.SIMPLE, border_style="cyan")
    table.add_column("Option", style="cyan", width=4)
    table.add_column("Action", style="yellow")
    
    table.add_row("1", "🗨️  Mulai Chat dengan Moyren")
    table.add_row("2", "🔄  Ganti Model AI")
    table.add_row("3", "👤  Profil Pengguna")
    table.add_row("4", "ℹ️  Informasi Moyren")
    table.add_row("5", "❓  FAQ")
    table.add_row("6", "🚪  Logout")
    
    greeting = get_greeting_message()
    
    console.print(Panel(
        f"Selamat {greeting.lower()}, [bold magenta]{user_info['full_name']}[/bold magenta] ([cyan]@{user_info['username']}[/cyan])! 👋",
        border_style="green"
    ))
    console.print(Panel(table, title="[bold cyan]Menu Utama[/bold cyan]", border_style="cyan"))
    
    choice = ""
    while choice not in ["1", "2", "3", "4", "5", "6"]:
        choice = input(f"{Fore.GREEN}🌸 Pilihan Anda [1-6]: {Fore.WHITE}").strip()
        
        if choice not in ["1", "2", "3", "4", "5", "6"]:
            console.print("[bold red]❌ Pilihan tidak valid. Silakan pilih 1-6 ya~[/bold red]")
    
    return choice

def select_model():
    console.print(Panel.fit(
        Text("🤖 PILIH MODEL AI", style="bold cyan"),
        border_style="cyan"
    ))
    
    table = Table(show_header=False, box=box.SIMPLE, border_style="cyan")
    table.add_column("Option", style="cyan", width=4)
    table.add_column("Model", style="yellow")
    table.add_column("Info", style="green")
    
    table.add_row("1", "🧠 DeepSeek Prover V2", "Default & Paling Pintar")
    table.add_row("2", "🦙 Meta Llama 3.3 8B", "Lebih Ringan & Cepat")
    
    console.print(table)
    
    model_choice = ""
    while model_choice not in ["1", "2"]:
        model_choice = input(f"{Fore.GREEN}🌸 Pilih model [1-2]: {Fore.WHITE}").strip()
        
        if model_choice not in ["1", "2"]:
            console.print("[bold red]❌ Pilihan tidak valid. Silakan pilih 1-2 ya~[/bold red]")
    
    if model_choice == "1":
        console.print("[bold green]✅ DeepSeek Prover V2 dipilih sebagai model default![/bold green]")
        return "deepseek"
    else:
        console.print("[bold green]✅ Meta Llama 3.3 8B Instruct dipilih sebagai model default![/bold green]")
        return "llama"

def display_profile(user_info):
    clear_screen()
    conn = sqlite3.connect('moyren_users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT username, full_name, email, created_at FROM users WHERE username = ?", 
                   (user_info["username"],))
    user_data = cursor.fetchone()
    conn.close()
    
    if user_data:
        username, full_name, email, created_at = user_data
        
        profile_table = Table(box=box.ROUNDED, border_style="cyan")
        profile_table.add_column("Info", style="cyan")
        profile_table.add_column("Detail", style="yellow")
        
        profile_table.add_row("👤 Username", username)
        profile_table.add_row("📝 Nama Lengkap", full_name)
        profile_table.add_row("📧 Email", email)
        profile_table.add_row("🕒 Terdaftar Pada", created_at)
        
        console.print(Panel(
            Text("👤 PROFIL PENGGUNA", style="bold magenta"),
            border_style="magenta"
        ))
        console.print(profile_table)
        
    console.print()
    input(f"{Fore.GREEN}🌸 Tekan Enter untuk kembali ke menu utama...{Fore.WHITE}")

def display_info():
    clear_screen()
    info_text = """
✨ Moyren adalah asisten AI berbahasa Indonesia yang dikembangkan oleh Ade Pratama (HolyBytes).
   Dibangun dengan teknologi canggih untuk membantu Anda dalam berbagai kebutuhan sehari-hari.

🌿 Fitur Utama:
   - Asisten pribadi yang ramah dan sopan
   - Bantuan dalam pekerjaan dan studi
   - Teman diskusi dan bertukar ide
   - Penghasil konten kreatif
   - Pemecah masalah sehari-hari
   - Bisa bernyanyi! Coba minta untuk nyanyi 🎵

🛠️ Model AI yang tersedia:
   • DeepSeek Prover V2 (Model utama)
   • Meta Llama 3.3 8B Instruct

💌 "Moyren hadir untuk membuat hidupmu lebih mudah dan menyenangkan!"
    """
    
    console.print(Panel(
        Text("ℹ️ INFORMASI MOYREN AI", style="bold cyan"),
        border_style="cyan"
    ))
    
    console.print(Panel(info_text, border_style="green"))
    
    console.print()
    input(f"{Fore.GREEN}🌸 Tekan Enter untuk kembali ke menu utama...{Fore.WHITE}")

def display_faq():
    clear_screen()
    faq_items = [
        {
            "question": "✧ Apakah data saya aman saat berbicara dengan Moyren?",
            "answer": "Moyren tidak menyimpan data percakapan Anda. Semua interaksi bersifat sementara dan hanya untuk memberikan respons yang tepat."
        },
        {
            "question": "✧ Apa saja yang bisa Moyren bantu?",
            "answer": "Saya bisa membantu dalam:\n- Menjawab pertanyaan umum\n- Bantuan belajar/mengajar\n- Penulisan kreatif\n- Pemrograman dasar\n- Terjemahan bahasa\n- Bernyanyi jika diminta\n- Dan banyak lagi!"
        },
        {
            "question": "✧ Bagaimana cara menggunakan Moyren dengan baik?",
                        "answer": "Gunakan kalimat yang jelas dan lengkap. Jika ingin hasil lebih spesifik, berikan detail yang cukup. Jangan ragu untuk meminta klarifikasi jika jawaban saya kurang memuaskan."
        },
        {
            "question": "✧ Apakah Moyren bisa menggantikan guru atau tutor?",
            "answer": "Moyren adalah alat bantu belajar, bukan pengganti guru. Saya bisa membantu menjelaskan konsep, memberikan contoh, dan memandu belajar mandiri, tapi interaksi dengan guru tetap penting."
        },
        {
            "question": "✧ Bagaimana cara melaporkan masalah atau memberikan saran?",
            "answer": "Anda bisa menghubungi pengembang melalui GitHub: https://github.com/HolyBytes/MoyrenAI atau email: holybytes.contact@gmail.com"
        }
    ]
    
    console.print(Panel(
        Text("❓ PERTANYAAN YANG SERING DIAJUKAN", style="bold magenta"),
        border_style="magenta"
    ))
    
    for item in faq_items:
        console.print(Panel(
            Text(f"[bold cyan]{item['question']}[/bold cyan]\n\n{item['answer']}"),
            border_style="green",
            box=box.ROUNDED
        ))
        console.print()
    
    console.print()
    input(f"{Fore.GREEN}🌸 Tekan Enter untuk kembali ke menu utama...{Fore.WHITE}")

def chat_interface(user_info, model="deepseek"):
    clear_screen()
    greeting = get_greeting_message()
    full_name = user_info["full_name"]
    
    console.print(Panel(
        f"✨ Selamat {greeting.lower()}, [bold magenta]{full_name}[/bold magenta]! Moyren siap membantu~ 💖\n"
        f"🤖 Model aktif: [bold cyan]{'DeepSeek Prover V2' if model == 'deepseek' else 'Meta Llama 3.3 8B'}[/bold cyan]\n"
        f"💡 Ketik 'keluar' atau 'exit' untuk kembali ke menu utama",
        border_style="cyan"
    ))
    
    chat_history = []
    
    while True:
        try:
            prompt = input(f"{Fore.YELLOW}💬 {full_name}: {Fore.WHITE}").strip()
            
            if not prompt:
                continue
                
            if prompt.lower() in ['keluar', 'exit', 'quit', 'q']:
                console.print("[bold magenta]🌸 Sampai jumpa lagi! Kembali ke menu utama...[/bold magenta]")
                time.sleep(1)
                break
                
            if model == "deepseek":
                response = call_deepseek_api(prompt, user_info)
            else:
                client = init_llama_client()
                response = client.chat.completions.create(
                    model="meta-llama/llama-3-8b-instruct:free",
                    messages=[
                        {"role": "system", "content": get_system_prompt(user_info)},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7,
                    max_tokens=800
                )
                response = response.choices[0].message.content
            
            # Display response in a beautiful panel
            console.print(Panel(
                Text(response, style="green"),
                title="[bold green]🤖 Moyren[/bold green]",
                border_style="green",
                box=box.ROUNDED
            ))
            
            # Add to chat history
            chat_history.append({
                "user": prompt,
                "bot": response,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            
        except KeyboardInterrupt:
            console.print("\n[bold magenta]🌸 Interupsi terdeteksi. Kembali ke menu utama...[/bold magenta]")
            time.sleep(1)
            break
        except Exception as e:
            console.print(f"[bold red]❌ Error: {str(e)}[/bold red]")
            continue

def main():
    setup_database()
    display_welcome_screen()
    
    current_user = None
    
    # Main application loop
    while True:
        if current_user is None:
            # Authentication menu
            choice = display_auth_menu()
            
            if choice == "1":
                current_user = login_user()
            elif choice == "2":
                if register_user():
                    current_user = login_user()
            elif choice == "3":
                display_info()
                input("Tekan Enter untuk melanjutkan...")
            elif choice == "4":
                console.print("[bold magenta]🌸 Terima kasih telah menggunakan Moyren AI! Sampai jumpa~ ✨[/bold magenta]")
                time.sleep(2)
                sys.exit(0)
        else:
            # Main menu for logged in users
            choice = display_main_menu(current_user)
            
            if choice == "1":
                chat_interface(current_user)
            elif choice == "2":
                model = select_model()
                chat_interface(current_user, model)
            elif choice == "3":
                display_profile(current_user)
            elif choice == "4":
                display_info()
            elif choice == "5":
                display_faq()
            elif choice == "6":
                current_user = None
                console.print("[bold magenta]🌸 Anda telah logout. Sampai jumpa lagi! ✨[/bold magenta]")
                time.sleep(2)

if __name__ == "__main__":
    main()
