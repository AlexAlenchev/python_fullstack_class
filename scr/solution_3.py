book_volume = 2  # м³
stationery_volume = 1.5  # м³
toy_volume = 3  # м³

book_quantity = int(input("Введите количество коробок с книгами: "))
stationery_quantity = int(input("Введите количество коробок с канцтоварами: "))
toy_quantity = int(input("Введите количество коробок с игрушками: "))

total_volume = book_volume  *  book_quantity + stationery_volume  *  stationery_quantity + toy_volume  *  toy_quantity

print(f"Для хранения всех товаров потребуется общий объем в {total_volume} м³.")
