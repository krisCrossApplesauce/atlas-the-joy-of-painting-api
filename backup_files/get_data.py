#!/usr/bin/env python3
"""
gets the data from the files
"""
import csv


def colors_to_ep_dict():
# returns a list of incomplete episode objects
# that each contain their id and colors list
    f = open("../dirty_data/The_Joy_Of_Painting-Colors_Used.txt", "r")
    data = []
    key_list = ["id"]
    key_list.append(f.readline().split(","))

    for line in f:
        ep_dict = {}
        val_list = line.split(',')
        print(f'{val_list}')
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
# returns a list of incomplete episode objects
# that each contain their id and subjects list
    f = open("../dirty_data/The_Joy_Of_Painting-Subject_Matter.txt", "r")
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
# returns a list of incomplete episode objects
# that each contain their id, title, date, and month
    f = open("../dirty_data/The_Joy_Of_Painting-Episode_Dates.txt", "r")
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


def get_episodes_data():
# uses the data collected from the separate files to create and
# return a list of episode objects for the episodes table
    ep_colors = colors_to_ep_dict()
    ep_subjects = subjects_to_ep_dict()
    ep_date = dates_to_ep_dict()

    ep_data = []

    i = 0
    while ep_colors[i] and ep_subjects[i] and ep_date[i]:
        ep_obj = {}

        if (ep_colors[i][id] != i or ep_subjects[i][id] != i or ep_date[i] != i):
            print(f"id's don't match:\ni: {i}\nColors: {ep_colors[i][id]}\nSubjects: {ep_subjects[i][id]}\nDate: {ep_date[i]}")
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
# returns a list of color objects for the color table
    ep_colors = colors_to_ep_dict()
    f = open("../dirty_data/The_Joy_Of_Painting-Colors_Used.txt", "r")
    colors = f.readline().split(",")
    colors_data = []

    id = 0
    while colors[id + 9]:
        color_obj = {}
        color_obj["id"] = id
        color_obj["name"] = colors[id + 9]
        episodes = []

        for ep in ep_colors:
            if color_obj["name"] in ep["colors"]:
                episodes.append(ep["id"])

        color_obj["episodes"] = str(episodes)
        colors_data.append(color_obj)
        id += 1

    return colors_data


def get_subjects_data():
# returns a list of subject objects for the subject table
    ep_subjects = subjects_to_ep_dict()
    f = open("../dirty_data/The_Joy_Of_Painting-Subject_Matter.txt", "r")
    subjects = f.readline().split(",")
    subjects_data = []

    id = 0
    while subjects[id + 2]:
        subject_obj = {}
        subject_obj["id"] = id
        subject_obj["name"] = subjects[id + 2]
        episodes = []

        for ep in ep_subjects:
            if subject_obj["name"] in ep["subjects"]:
                episodes.append(ep["id"])

        subject_obj["episodes"] = str(episodes)
        subjects_data.append(subject_obj)
        id += 1

    return subjects_data


def get_months_data():
# returns a list of month objects for the month table
    ep_dates = dates_to_ep_dict()
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    months_data = []

    id = 1
    while id <= 12:
        month_obj = {}
        month_obj["id"] = id
        month_obj["name"] = months[id - 1]
        episodes = []

        for ep in ep_dates:
            if ep["month"] == month_obj["name"]:
                episodes.append(ep["id"])

        month_obj["episodes"] = str(episodes)
        months_data.append(month_obj)
        id += 1

    return months_data


def write_data_to_csvfile(filename, dicts, fields):
# to write the data into a csv file
    with open(filename, "w") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(dicts)


# writing the data into their corresponding csv files :)
ep_dicts = get_episodes_data()
ep_fields = ["id", "title", "air_date", "month", "colors", "subjects"]
write_data_to_csvfile("../dirty_data/episode_data.csv", ep_dicts, ep_fields)

colors_dicts = get_colors_data()
subjects_dicts = get_subjects_data()
months_dicts = get_months_data()
other_fields = ["id", "name", "episodes"]

write_data_to_csvfile("../dirty_data/colors_data.csv", colors_dicts, other_fields)
write_data_to_csvfile("../dirty_data/subjects_data.csv", subjects_dicts, other_fields)
write_data_to_csvfile("../dirty_data/months_data.csv", months_dicts, other_fields)
