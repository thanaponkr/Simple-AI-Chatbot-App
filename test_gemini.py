import google.generativeai as genai

# --- ตั้งค่า ---
# !!! วาง API Key ที่คุณคัดลอกมา ตรงนี้ !!!
GEMINI_API_KEY = "AIzaSyAS9G8mi1qdon725OadRIGvVY02g6Wl-EU"

# --- กำหนดค่า API Key ให้กับ Library ---
genai.configure(api_key=GEMINI_API_KEY)

# --- เลือกรุ่นโมเดล ---
model = genai.GenerativeModel('gemini-1.5-flash') # เป็นรุ่นใหม่ที่เร็วและเหมาะกับงานแชท

# --- คำถามที่เราจะส่งไป ---
prompt = "ช่วยอธิบายแนวคิดของ 'ควอนตัมคอมพิวเตอร์' แบบง่ายๆ ให้หน่อย"

# --- ส่งคำถามและรับคำตอบ ---
print("กำลังส่งคำถามไปให้ Gemini...")
try:
    response = model.generate_content(prompt)
    
    # --- แสดงผลลัพธ์ ---
    print("\n--- คำตอบจาก Gemini ---")
    print(response.text)

except Exception as e:
    print(f"เกิดข้อผิดพลาด: {e}")