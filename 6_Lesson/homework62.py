x = int(input("Enter number:"))
days = x // (24 * 3600)
hours = (x - days * 24 * 3600) // 3600
minutes = (x - days * 24 * 3600 - hours * 3600) // 60
seconds = x - days * 24 * 3600 - hours * 3600 - minutes * 60
if str(days)[-1] in ['0','5','6','7','8','9'] or 11 <= days < 15:
    pron = "днів"
elif str(days)[-1] == '1':
    pron = "день"
else:
    pron = "дні"

dates = f"{days} {pron}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
print(dates)

