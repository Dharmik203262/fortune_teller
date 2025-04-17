

import random

print("🔮 Welcome to Dharmik  Fortune Teller (22JE0698) 🔮")
mood = input("How are you feeling today? (happy/sad/neutral): ").lower()

fortunes = {
    "happy": [
        "✨ Great things await you, Dharmik ! Keep smiling. ✨",
        "😊 Today is your lucky day!"
    ],
    "sad": [
        "🌧 Don't worry, Aryan. Brighter days are coming.",
        "😢 It's okay to feel down. Tomorrow is a new start."
    ],
    "neutral": [
        "🌤 Things may be average now, but surprises are on the way!",
        "😐 Every day is a chance to make things better."
    ],
    "stressed": [
        "🧘‍♂️ Breathe, Dharmik. Peace is just a moment away.",
        "😣 Even storms pass. You'll handle this just fine."
    ]
}

if mood in fortunes:
    print(random.choice(fortunes[mood]))
else:
    print("🤔 I couldn't understand that mood. Try happy, sad, neutral, or stressed.")


