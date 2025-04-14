low = 1
high = 10

print("🧠 Think of a number between 1 and 10, and I'll try to read your mind! 🔮")

while low <= high:
    guess = (low + high) // 2  # Binary search technique
    print(f"🤖 Is your number {guess}? 🤔")

    feedback = input("🔼 Enter 'h' if too high, 🔽 'l' if too low, ✅ 'c' if correct: ").lower()

    if feedback == "h":
        high = guess - 1
        print("📉 Okay, I'll guess lower! ⬇️")
    elif feedback == "l":
        low = guess + 1
        print("📈 Got it! I'll try a higher number. ⬆️")
    elif feedback == "c":
        print(f"🎉 Woohoo! I guessed your number {guess} correctly! 🏆🎊")
        break
    else:
        print("⚠️ Oops! Invalid input. Please enter only 'h', 'l', or 'c'. 🚫")

if low > high:
    print("😅 Uh-oh... I think you gave inconsistent answers. Let's try again! 🔄")
