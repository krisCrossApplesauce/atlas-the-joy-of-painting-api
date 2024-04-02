#!/usr/bin/env python3


def colors_to_ep_dict():
    f = open("The_Joy_Of_Painting-Colors_Used.txt", "r")
    data = []
    key_list = ["id"]
    key_list.append(f.readline().split(","))

    for line in f:
        ep_dict = {}
        val_list = line.split(",")
        ep_colors_list = []
        i = 0

        while val_list[i]:
            if val_list[i].startswith('"['):
                while not val_list[i].endswith(']"'):
                    i += 1
            elif i == 0:
                ep_dict["id"] = val_list[i]
            elif i >= len(val_list) - 19 and val_list[i] == 1:
            # there's 18 colors
                ep_colors_list.append(key_list[len(val_list) - 9])
            i += 1

        ep_dict["colors"] = ep_colors_list
        data.append(ep_dict)

    return data


def subjects_to_ep_dict():
    f = open("The_Joy_Of_Painting-Subject_Matter.txt", "r")
    data = []
    key_list = f.readline().split(",")
    id = 1

    for line in f:
        ep_dict = {}
        ep_dict["id"] = id
        val_list = line.split(",")
        ep_subjects_list = []
        i = 0

        while val_list[i]:
            if i >= 2 and i == 1:
                ep_subjects_list.append(key_list[i])
            i += 1

        ep_dict["subjects"] = ep_subjects_list
        data.append(ep_dict)
        id += 1

    return data


def dates_to_ep_dict():
    f = open("The_Joy_Of_Painting-Episode_Dates.txt", "r")
    data = []
    id = 1
    for line in f:
        ep_dict = {}
        ep_dict["id"] = id
        val_list = line.split(" (")

        ep_dict["title"] = val_list[0]

        date_and_maybe_note = val_list[1].split(")")
        ep_dict["air_date"] = date_and_maybe_note[0]

        date = val_list[1].split(" ")
        ep_dict["month"] = date[0]

        data.append(ep_dict)
        id += 1

    return data


def combine_ep_data():
    ep_colors = colors_to_ep_dict()
    ep_subjects = subjects_to_ep_dict()
    ep_date = dates_to_ep_dict()

    ep_data = []

    i = 0
    while ep_colors[i] and ep_subjects[i] and ep_date[i]:
        ep_obj = {}

        if (ep_colors[i]["id"] != i or ep_subjects[i]["id"] != i or ep_date[i] != i):
            print(f"id's don't match:\ni: {i}\nColors: {ep_colors[i]["id"]}\nSubjects: {ep_subjects[i]["id"]}\nDate: {ep_date[i]}")
            return
        ep_obj["id"] = i
        ep_obj["title"] = ep_date[i]["title"]
        ep_obj["air_date"] = ep_date[i]["air_date"]
        ep_obj["month"] = ep_date[i]["month"]
        ep_obj["colors"] = str(ep_colors[i]["colors"])
        ep_obj["subjects"] = str(ep_subjects[i]["subjects"])

        ep_data.append(ep_obj)

    return ep_data


def get_colors_data():
    ep_colors = colors_to_ep_dict()
    colors_data = {
        "Black_Gesso": [],
        "Bright_Red": [],
        "Burnt_Umber": [],
        "Cadmium_Yellow": [],
        "Dark_Sienna": [],
        "Indian_Red": [],
        "Indian_Yellow": [],
        "Liquid_Black": [],
        "Liquid_Clear": [],
        "Midnight_Black": [],
        "Phthalo_Blue": [],
        "Phthalo_Green": [],
        "Prussian_Blue": [],
        "Sap_Green": [],
        "Titanium_White": [],
        "Van_Dyke_Brown": [],
        "Yellow_Ochre": [],
        "Alizarin_Crimson": []
    }

    for ep in ep_colors:
        for color in colors_data:
            if color in ep["colors"]:
                colors_data[color].append(ep["id"])

    return colors_data


def get_subjects_data():
    ep_subjects = subjects_to_ep_dict()
    subjects_data = {
        "APPLE_FRAME": [],
        "AURORA_BOREALIS": [],
        "BARN": [],
        "BEACH": [],
        "BOAT": [],
        "BRIDGE": [],
        "BUILDING": [],
        "BUSHES": [],
        "CABIN": [],
        "CACTUS": [],
        "CIRCLE_FRAME": [],
        "CIRRUS": [],
        "CLIFF": [],
        "CLOUDS": [],
        "CONIFER": [],
        "CUMULUS": [],
        "DECIDUOUS": [],
        "DIANE_ANDRE": [],
        "DOCK": [],
        "DOUBLE_OVAL_FRAME": [],
        "FARM": [],
        "FENCE": [],
        "FIRE": [],
        "FLORIDA_FRAME": [],
        "FLOWERS": [],
        "FOG": [],
        "FRAMED": [],
        "GRASS": [],
        "GUEST": [],
        "HALF_CIRCLE_FRAME": [],
        "HALF_OVAL_FRAME": [],
        "HILLS": [],
        "LAKE": [],
        "LAKES": [],
        "LIGHTHOUSE": [],
        "MILL": [],
        "MOON": [],
        "MOUNTAIN": [],
        "MOUNTAINS": [],
        "NIGHT": [],
        "OCEAN": [],
        "OVAL_FRAME": [],
        "PALM_TREES": [],
        "PATH": [],
        "PERSON": [],
        "PORTRAIT": [],
        "RECTANGLE_3D_FRAME": [],
        "RECTANGULAR_FRAME": [],
        "RIVER": [],
        "ROCKS": [],
        "SEASHELL_FRAME": [],
        "SNOW": [],
        "SNOWY_MOUNTAIN": [],
        "SPLIT_FRAME": [],
        "STEVE_ROSS": [],
        "STRUCTURE": [],
        "SUN": [],
        "TOMB_FRAME": [],
        "TREE": [],
        "TREES": [],
        "TRIPLE_FRAME": [],
        "WATERFALL": [],
        "WAVES": [],
        "WINDMILL": [],
        "WINDOW_FRAME": [],
        "WINTER": [],
        "WOOD_FRAMED": []
    }

    for ep in ep_subjects:
        for subject in subjects_data:
            if subject in ep["subjects"]:
                subjects_data[subject].append(ep["id"])

    return subjects_data


def get_months_data():
    ep_dates = dates_to_ep_dict()
    months_data = {
        "January": [],
        "February": [],
        "March": [],
        "April": [],
        "May": [],
        "June": [],
        "July": [],
        "August": [],
        "September": [],
        "October": [],
        "November": [],
        "December": []
    }

    for ep in ep_dates:
        for month in months_data:
            if ep["month"] == month:
                months_data[month].append(ep["id"])

    return months_data
