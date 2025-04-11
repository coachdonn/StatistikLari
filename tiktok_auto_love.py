import keyboard
import time

print("🎯 Auto-Love TikTok Live by pressing 'L' key repeatedly")

jumlah_tap = int(input("🔢 Masukkan jumlah love (contoh: 100): "))
delay = float(input("⏱️ Masukkan delay antar love (dalam detik, contoh: 0.5): "))

print("\n⏳ Kamu punya 3 detik untuk klik jendela browser TikTok Live!")
time.sleep(3)

for i in range(jumlah_tap):
    keyboard.press_and_release('l')
    print(f"❤️ Love ke-{i+1}")
    time.sleep(delay)

print("\n✅ Selesai! Semua love telah dikirim 🚀")
