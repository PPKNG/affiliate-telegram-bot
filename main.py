import requests
from datetime import datetime

# --- เอา Token และ ID มาใส่ในเครื่องหมายคำพูดด้านล่างนี้ ---
TELEGRAM_TOKEN = "8676723064:AAGaGYaTdZcbj7VQO3PyMI83gxvP724AXkU"
CHAT_ID = "7392332179"

def get_trending_products():
    # ข้อมูลสินค้าจำลอง (เตรียมไว้สำหรับเชื่อม API จริงในอนาคต)
    return [
        {"name": "หูฟังไร้สายตัดเสียงรบกวน", "platform": "Shopee", "commission": "15%"},
        {"name": "มินิโปรเจกเตอร์พกพา", "platform": "TikTok", "commission": "20%"},
        {"name": "เก้าอี้ทำงานเพื่อสุขภาพ", "platform": "Shopee", "commission": "10%"},
    ]

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
    products = get_trending_products()
    
    # สรุปข้อความเป็นภาษาไทย
    msg = f"🚀 <b>อัปเดตสินค้า Affiliate มาแรง</b>\n📅 ประจำวันที่: {today}\n"
    msg += "━━━━━━━━━━━━━━━━━━━━\n\n"
    
    for i, item in enumerate(products, 1):
        msg += f"<b>{i}. {item['name']}</b>\n"
        msg += f"📍 <i>{item['platform']}</i> | 💰 ค่าคอม: {item['commission']}\n\n"
        
    msg += "━━━━━━━━━━━━━━━━━━━━\n"
    msg += "💡 <i>ตื่นมารับเงิน ลุยทำคอนเทนต์ป้ายยากันเลยวันนี้!</i> 💪"
    
    send_telegram_message(msg)

if __name__ == "__main__":
    main()
