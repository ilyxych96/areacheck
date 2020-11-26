import csv

with open('user_coordinates.csv') as f:
    reader = csv.reader(f)
    users = tuple(reader)

    
with open('place_zone_coordinates.csv') as f:
    reader = csv.reader(f)
    restaurants_list = tuple((reader))
    
    
def user_in_polygon(user_id, restaraunt_id):
    in_polygon_flag = False
                    
    user_location = (users[user_id][1], users[user_id][2])
    restaraunt_area = restaraunts[restaraunt_id]
    edge_test = []
    x = float(user_location[0])
    y = float(user_location[1])
    for item in range(len(restaraunt_area)):    
        xp = float(restaraunts[restaraunt_id][int(item)][0])
        yp = float(restaraunts[restaraunt_id][int(item)][1])
        xp_prev = float(restaraunts[restaraunt_id][int(item-1)][0])
        yp_prev = float(restaraunts[restaraunt_id][int(item-1)][1])
        if (((yp <= y and y < yp_prev) or (yp_prev <= y and y < yp)) and (x > (xp_prev - xp) * (y - yp) / (yp_prev - yp) + xp)):
            in_polygon_flag = not in_polygon_flag
    
    return in_polygon_flag


users_id = tuple([int(user[0]) for user in users[1:]])
restaraunts_avalible_for_user = dict.fromkeys(users_id, 0)

restaraunts = {}
for item in restaurants_list[1:]:
    restaraunts.setdefault(item[0], []).append(item[1:])

for user in users_id:
    for restaraunt in restaraunts:
        if user_in_polygon(user, restaraunt) == True:
            restaraunts_avalible_for_user[user] += 1
    
with open('Avalible_restaraunts.csv', "w+", newline="") as file:
    columns = ["id", "number_of_places_available"]
    writer = csv.writer(file)
    writer.writerow(columns)
    keys = list(restaraunts_avalible_for_user.keys())
    values = list(restaraunts_avalible_for_user.values())
    writer.writerows(zip(keys, values))
    


