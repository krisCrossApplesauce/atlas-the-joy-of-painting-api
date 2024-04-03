import pandas as pd


# ep_dates_df = pd.read_csv('dirty_data/episode_dates.csv')

# ep_dates_df.insert(0, 'episode_id', range(1, len(ep_dates_df) + 1))

# ep_dates_df['month'] = ep_dates_df['air_date'].str.split().str[0]

# ep_dates_df.to_csv('clean_data/episode_dates.csv', index=False)



# ep_dates_df = pd.read_csv('clean_data/episode_dates.csv')
# month_eps_df = pd.read_csv('clean_data/months.csv')

# month_eps_list = []
# months_list= ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
# for m in months_list:
#     temp = []
#     for i in ep_dates_df.index:
#         if ep_dates_df['month_name'][i] == m:
#             temp.append(ep_dates_df['episode_id'][i])
#     month_eps_list.append(temp)

# month_eps_df['episode_id'] = month_eps_list

# month_eps_df.to_csv('clean_data/months.csv', index=False)



# ep_colors_df = pd.read_csv('clean_data/episode_colors.csv')
# color_eps_df = pd.read_csv('clean_data/colors.csv')

# color_eps_list = []
# for i in range(1, 19):
#     temp = []
#     for ii in ep_colors_df.index:
#         if i in list(eval(ep_colors_df['color_id'][ii])):
#             temp.append(ep_colors_df['episode_id'][ii])
#     color_eps_list.append(temp)

# color_eps_df['episode_id'] = color_eps_list

# color_eps_df.to_csv('clean_data/colors.csv', index=False)



ep_subjects_df = pd.read_csv('clean_data/episode_subjects.csv')
subject_eps_df = pd.read_csv('clean_data/subjects.csv')

subject_eps_list = []
for i in range(1, 68):
    temp = []
    for ii in ep_subjects_df.index:
        if i in list(eval(ep_subjects_df['subject_id'][ii])):
            temp.append(ep_subjects_df['episode_id'][ii])
    subject_eps_list.append(temp)

subject_eps_df['episode_id'] = subject_eps_list

subject_eps_df.to_csv('clean_data/subjects.csv', index=False)
