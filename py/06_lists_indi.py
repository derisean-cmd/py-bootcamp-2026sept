# Exercise 1 🗣️ List of Supported Languages
lang_code = ["en", "zh", "ms", "ja", "ko", "de"]
print("Total supported languages: ", len(lang_code))
print("Primary language: ", lang_code[0])
for x in lang_code:
    print("Translating:", x)

# Exercise 2 📄 Batch Word Count
wordcount = [1200, 3500, 800, 5400]
total = 0
for x in wordcount:
    total += x
print("Combined word count: ",total)

# Exercise 3 💰 Calculate Batch Pricing
rate = 0.06 # RM, per word
grand_total = 0 #dont forget tot add an empty box as the variable, used for sum at the end

for x in wordcount:
    locale_cost = x * rate
    print("Each Locale costs: ",locale_cost)
    grand_total += locale_cost
print("Total proj costs: ",grand_total)