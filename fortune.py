

print("🔮 Welcome to Dharmik Fortune Teller (22JE0968) 🔮")
mood = input("How are you feeling today? (happy/sad/neutral): ").lower()

if mood == "happy":
    print("✨ Your fortune: Great things await you, Dharmik! Keep smiling. ✨")
elif mood == "sad":
    print("🌧 Your fortune: Tough times don’t last, but tough people do.")
elif mood == "neutral":
    print("🌤 Your fortune: A surprise is waiting around the corner.")
else:
    print("🤔 I don't have a fortune for that mood. Try happy/sad/neutral.")

