magistr = {"Лермонтов", "Достоевский", "Пушкин", "Тютчев"}
dom_knigi = {"Толстой", "Грибоедов", "Чехов", "Пушкин"}
buk_market = {"Пушкин", "Достоевский", "Маяковский"}
galereya = {"Чехов", "Тютчев", "Пушкин"}

shops = {
    "Магистр": magistr,
    "ДомКниги": dom_knigi,
    "БукМаркет": buk_market,
    "Галерея": galereya,
}

print("Магазины, где можно купить книги Пушкина и Тютчева:")
for shop_name, books in shops.items():
    if "Пушкин" in books and "Тютчев" in books:
        print(f"- {shop_name}")
