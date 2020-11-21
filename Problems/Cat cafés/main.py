cafe = input()
cafe_dict = {}
while cafe != "MEOW":
    cafe_cats = cafe.split()
    cafe_name = cafe_cats[0]
    cat_number = int(cafe_cats[1])
    cafe_dict[cafe_name] = cat_number
    cafe = input()
max_num = 0
the_cafe = ""
for selected_cafe in cafe_dict:
    num = cafe_dict.get(selected_cafe)
    if num > max_num:
        max_num = num
        the_cafe = selected_cafe
print(the_cafe)

