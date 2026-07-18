import requests
from datetime import datetime

# --- อย่าลืมเอา Token และ ID ของคุณมาใส่ตรงนี้นะครับ ---
TELEGRAM_TOKEN = "8676723064:AAGaGYaTdZcbj7VQO3PyMI83gxvP724AXkU"
CHAT_ID = "7392332179"

def get_real_thailand_trends():
    # ใช้ rss2json เป็นนินจาตัวกลาง เพื่อหลบระบบป้องกันบอทของ Google
    url = "https://api.rss2json.com/v1/api.json?rss_url=https://trends.google.com/trends/trendingsearches/daily/rss?geo=TH"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        trends = []
        if data.get('status') == 'ok':
            # ดึงมาเฉพาะ 5 อันดับแรกที่ฮิตที่สุด
            for item in data['items'][:5]:
                keyword = item.get('title', 'N/A')
                trends.append({"keyword": keyword})
        return trends
    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")
        return []

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
    trends = get_real_thailand_trends()
    
    msg = f"🚀 <b>[Real-Time] อัปเดตเทรนด์เสิร์ชจริงในไทย</b>\n📅 ประจำวันที่: {today}\n"
    msg += "━━━━━━━━━━━━━━━━━━━━\n"
    
    if trends:
        msg += "💡 <i>คนไทยกำลังแห่เสิร์ชสิ่งนี้มากที่สุด รีบเอาคีย์เวิร์ดไปโยงกับสินค้าด่วน!</i>\n"
        msg += "━━━━━━━━━━━━━━━━━━━━\n\n"
        for i, item in enumerate(trends, 1):
            msg += f"🔥 <b>{i}. {item['keyword']}</b>\n\n"
    else:
        msg += "❌ ข้อมูลเทรนด์ยังไม่มา หรือระบบกำลังพักเหนื่อย\n\n"
        
    msg += "━━━━━━━━━━━━━━━━━━━━\n"
    msg += "🎯 <b>แนวทางการต่อยอดทำเงินวันนี้:</b>\n"
    msg += "ให้นำคีย์เวิร์ดด้านบนไปค้นหาใน Shopee/TikTok เพื่อดูว่ามีสินค้าอะไรที่กำลังเป็นกระแส หรือหยิบสินค้าใกล้เคียงมาทำคอนเทนต์ได้เลยครับ ลุย! 💪"
    
    send_telegram_message(msg)

if __name__ == "__main__":
    main()
