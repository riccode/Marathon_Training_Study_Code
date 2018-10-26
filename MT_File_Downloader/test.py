import os
import pandas as pd
import re

participant_id = 'MT015'
PARTICIPANT_DIR = "C:/Users/Running Injury Clini/Desktop/Marathon Training/" + participant_id


print("UPDATING DATA TRACKING LOG...")
if not os.path.isfile(
        "C:/Users/Running Injury Clini/Desktop/Marathon Training/data_tracking_log.csv"):
    colnames = ['participant_id', 'date', 'garmin_file', 'lumo_file', 'upload', 'notes']
    update = pd.DataFrame(columns=colnames)
    update.to_csv('C:/Users/Running Injury Clini/Desktop/Marathon Training/data_tracking_log.csv',
                  header=True, index=False)

colnames = ['participant_id', 'date', 'garmin_file', 'lumo_file', 'upload', 'notes']
participant_update = pd.DataFrame(columns=colnames)

dates = [d for d in os.listdir(PARTICIPANT_DIR) if os.path.isdir(os.path.join(PARTICIPANT_DIR, d))]
dates = [d for d in dates if not re.search('reports', d)]

for file in dates:
    path = PARTICIPANT_DIR + '/' + file
    count_garmin = 0
    garmin_path = path + '/' + 'Garmin'
    result = [re.search('csv', gfile) for gfile in os.listdir(garmin_path)]
    for r in result:
        if r:
            count_garmin = count_garmin + 1

    count_garmin = int(count_garmin / 2)

    count_lumo = 0
    lumo_path = path + '/' + 'Lumo'
    result = [re.search('csv', lfile) for lfile in os.listdir(lumo_path)]
    for r in result:
        if r:
            count_lumo = count_lumo + 1

    count_upload = 0
    upload_path = path + '/' + 'Upload'
    result = [re.search('csv', ufile) for ufile in os.listdir(upload_path)]
    for r in result:
        if r:
            count_upload = count_upload + 1
    count_upload = count_upload

    note = ''
    if count_garmin > 1:
        note = note + ' Multiple Garmin Files'
    if count_lumo > 1:
        note = note + ' Multiple Lumo Files'

    note = note.strip()
    participant_update.loc[len(participant_update)] = [participant_id, file, count_garmin, count_lumo, count_upload,
                                                       note]

existing_log = pd.read_csv(
    "C:/Users/Running Injury Clini/Desktop/Marathon Training/data_tracking_log.csv")

existing_log.drop(existing_log[existing_log.participant_id == participant_id].index, inplace=True)
update_log = existing_log.append(participant_update, ignore_index=True)
update_log.to_csv("C:/Users/Running Injury Clini/Desktop/Marathon Training/data_tracking_log.csv",
                  header=True, index=False)

print('DATA TRACKING LOG UPDATED!!')