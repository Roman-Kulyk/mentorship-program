clothes_list = ["Purple t-shirt",
                "Green hoodie",
                "Yellow dress",
                "Purple sweater",
                "Green polo shirt",
                "Yellow raincoat",
                "Purple leggings",
                "Green jacket",
                "Yellow scarf",
                "Purple shorts",
                "Green cardigan",
                "Yellow blouse",
                "Purple socks",
                "Green trousers",
                "Yellow skirt",
                "Purple tank top",
                "Green blazer",
                "Yellow hat",
                "Purple jeans",
                "Green tracksuit"
                ]
purple_clothes = []
yellow_clothes = []
green_clothes = []
for i in clothes_list:
    if i.startswith("Purple"):
        purple_clothes.append(i)
    elif i.startswith("Yellow"):
        yellow_clothes.append(i)
    else:
        green_clothes.append(i)
print(purple_clothes)
print(yellow_clothes)
print(green_clothes)