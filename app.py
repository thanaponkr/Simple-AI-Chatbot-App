from flask import Flask, render_template, request
import google.generativeai as genai

# --- ตั้งค่า ---
GEMINI_API_KEY = "AIzaSyAS9G8mi1qdon725OadRIGvVY02g6Wl-EU" # !!! อย่าลืมใส่ Key ของคุณ !!!
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

app = Flask(__name__)

# สร้างลิสต์สำหรับเก็บประวัติการแชท
chat_history = [
    {'role': 'ai', 'text': 'สวัสดีครับ! มีอะไรให้ผมช่วยไหม?'}
]

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_prompt = request.form['prompt']
        
        # เพิ่มข้อความของผู้ใช้ลงในประวัติ
        chat_history.append({'role': 'user', 'text': user_prompt})
        
        # ส่งคำถามไปให้ Gemini
        response = model.generate_content(user_prompt)
        ai_response = response.text
        
        # เพิ่มคำตอบของ AI ลงในประวัติ
        chat_history.append({'role': 'ai', 'text': ai_response})

    # ส่งประวัติการแชททั้งหมดไปให้หน้าเว็บ
    return render_template('index.html', history=chat_history)

if __name__ == '__main__':
    app.run(debug=True)