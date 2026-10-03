import os
import json
import google.generativeai as genai

# GitHub Secrets orqali keladigan API kalit
API_KEY = os.getenv("GEMINI_API_KEY")

def asosiy_agent():
    if not API_KEY:
        print("Xatolik: GEMINI_API_KEY topilmadi!")
        return

    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = (
        "YouTube Shorts uchun qiziqarli, tomoshabinni jalb qiluvchi mavzu o'ylab top. "
        "Format quyidagicha bo'lsin:\n"
        "1. Video sarlavhasi (Title)\n"
        "2. Tavsif (Description)\n"
        "3. Shorts uchun 40-50 soniyalik ssenariy matni\n"
        "4. Kalit so'zlar / teglar (#shorts, va boshqalar)"
    )

    print("Gemini orqali YouTube kontenti tayyorlanmoqda...")
    response = model.generate_content(prompt)

    natija = response.text
    print("\n--- TAYYORLANGAN KONTENT ---\n")
    print(natija)

    # Natijani faylga yozib qo'yish
    with open("songi_kontent.txt", "w", encoding="utf-8") as f:
        f.write(natija)
        
    print("\nKontent 'songi_kontent.txt' fayliga muvaffaqiyatli saqlandi.")

if __name__ == "__main__":
    asosiy_agent()
  
