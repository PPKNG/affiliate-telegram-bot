import requests
import xml.etree.ElementTree as ET
from datetime import datetime

# --- เอา Token และ ID จาก Telegram ของคุณมาใส่ตรงนี้เหมือนเดิม ---
TELEGRAM_TOKEN = "8676723064:AAGaGYaTdZcbj7VQO3PyMI83gxvP724AXkU"
CHAT_ID = "7392332179"

def get_real_thailand_trends():
    # ดึงข้อมูลจาก Google Trends RSS Feed ของประเทศไทยโดยตรง
    url = "https://trends.google.com/trends/trendingsearches/daily/rss?geo=TH"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return []
        
        # ใช้ response.content (Bytes) เพื่อป้องกันปัญหาเรื่องการถอดรหัสภาษาไทยใน XML
        root = ET.fromstring(response.content)
        
        # กำหนด Namespace สำหรับดึงแท็กพิเศษของ Google (จำนวนการเสิร์ช)
        namespaces = {'ht': 'http://www.google.com/trends/trendingsearches/daily'}
        
        trends = []
        for item in root.findall('.//item'):
            keyword = item.find('title').text
            
            # ดึงข้อมูลจำนวนคนเสิร์ช
            traffic_el = item.find('ht:approx_traffic', namespaces)
            traffic = traffic_el.text if traffic_el is not None else "N/A"
            
            trends.append({"keyword": keyword, "traffic": traffic})
            
            # เอาเฉพาะ Top 5 อันดับแรกที่ฮิตที่สุดในวันนั้น
            if len(trends) >= 5:
                break
        return trends
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการดึงข้อมูล: {e}")
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
    msg += "💡 <i>คนไทยกำลังแห่เสิร์ชสิ่งนี้มากที่สุด รีบเอาคีย์เวิร์ดไปโยงกับสินค้าใน Shopee / TikTok ด่วน!</i>\n"
    msg += "━━━━━━━━━━━━━━━━━━━━\n\n"
    
    if trends:
        for i, item in enumerate(trends, 1):
            msg += f"🔥 <b>{i}. {item['keyword']}</b>\n"
            msg += f"📈 ยอดการเสิร์ช: <code>{item['traffic']} ครั้ง</code>\n\n"
    else:
        msg += "❌ ไม่สามารถดึงข้อมูลเทรนด์ได้ในขณะนี้ กรุณาตรวจสอบการเชื่อมต่อ\n\n"
        
    msg += "━━━━━━━━━━━━━━━━━━━━\n"
    msg += "🎯 <b>แนวทางการต่อยอดทำเงินวันนี้:</b>\n"
    msg += "ให้นำคีย์เวิร์ดด้านบนไปค้นหาใน Shopee/TikTok เพื่อดูว่ามีสินค้าอะไรที่กำลังเป็นกระแส หรือหยิบสินค้าใกล้เคียงมาทำคอนเทนต์เกาะกระแสได้เลยครับ ลุย! 💪"
    
    send_telegram_message(msg)

if __name__ == "__main__":
    main()
