# Exercise 1 🗣️ Language Code Validator
sup_lang_code = ["en", "zh", "ms", "ja", "ko", "de"]
lang_code = input("Enter language code: ")

while lang_code not in sup_lang_code:
    print("❌ Unsupported language! Try again pls")
    lang_code = input("Enter language code: ")

print("OK, language set to ",lang_code)

# Exercise 2 📄 Word Count Checker
print("Minimum charge is 50 words. Maximum limit is 10,000 words")
wwc = float(input("Enter wwc: "))

while wwc < 50 or wwc > 10000:
    print("Minimum charge is 50 words. Maximum limit is 10,000 words. Try again")
    wwc = float(input("Enter wwc: "))
print("✅ Word count saved: ",wwc," words")

# Exercise 3 💰 Price Calculator with Validation
if lang_code == "en":
    unit_rate = 0.2   # English rate
elif lang_code == "zh":
    unit_rate = 0.06   # Chinese rate
elif lang_code == "ms":
    unit_rate = 0.045  # Malay rate
elif lang_code == "ja":
    unit_rate = 0.08   # Japanese rate
else:
    unit_rate = 0.07   # Default rate
total_rate = wwc * unit_rate
print("💵 Total price: USD ",total_rate)