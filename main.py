import requests
from datetime import datetime

# --- ใส่ Token และ ID ของคุณตรงนี้ ---
TELEGRAM_TOKEN = "8676723064:AAGaGYaTdZcbj7VQO3PyMI83gxvP724AXkU"
CHAT_ID = "7392332179"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    requests.post(url, json=payload)

def main():
    today = datetime.now().strftime("%d/%m/%Y")
    
    msg = f"🚀 <b>ลายแทง Affiliate ประจำวัน</b>\n📅 {today}\n"
    msg += "━━━━━━━━━━━━━━━━━━━━\n\n"
    
    msg += "🔥 <b>1. Shopee (สินค้าขายดีประจำสัปดาห์):</b>\n"
    msg += "กดดูที่นี่ 👉 <a href='https://shopee.co.th/top_products'>เช็ก Top Products</a>\n"
    msg += "<i>(เลื่อนดูหมวดหมู่ที่ถนัด แล้วหยิบลิงก์ไปแปลงในระบบ Affiliate)</i>\n\n"
    
    msg += "🎵 <b>2. TikTok Shop (ศูนย์คริเอเตอร์):</b>\n"
    msg += "กดดูที่นี่ 👉 <a href='https://affiliate.tiktok.com/'>ตลาดสินค้า TikTok</a>\n"
    msg += "<i>(ล็อกอินแล้วดูแท็บ 'สินค้าขายดี' หรือ 'ค่าคอมสูง')</i>\n\n"
    
    msg += "━━━━━━━━━━━━━━━━━━━━\n"
    msg += "💡 <i>ความพร้อมที่สุด คือการเริ่มทำทั้งๆ ที่ยังไม่พร้อม! เปิดลิงก์แล้วลุยทำคลิปกันเลย!</i> 💪"
    
    send_telegram_message(msg)

if __name__ == "__main__":
    main()
