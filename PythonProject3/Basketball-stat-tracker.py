# 🏀 Basketball Stats Tracker (Phase 1 Mini Project)

roster = [
    {"player": "LeBron", "points": [30, 28, 25],
     "assists": [5, 7, 9], "rebounds": [7, 9, 8]},
    {"player": "AD", "points": [22, 18, 20],
     "assists": [3, 9, 7], "rebounds": [2, 6, 9]},
    {"player": "Reaves", "points": [15, 17, 12],
     "assists": [4, 10, 13], "rebounds": [4, 10, 13]},
]

print(roster)

def total_points(points_list):
    return sum(points_list)

def average_points(points_list):
    return sum(points_list) / len(points_list)


print(total_points([30, 28, 25]))
print(average_points([30, 28, 25]))

for player in roster:
    name = player["player"]
    total = total_points(player["points"])
    pts_avg = average_points(player["points"])
    ast_avg = average_points(player["assists"])
    reb_avg = average_points(player["rebounds"])

    print(f"{name}: PTS: {pts_avg:.1f} | AST: {ast_avg:.1f} | REB: {reb_avg:.1f}")

def best_player(roster):
    best_name = ""
    best_avg = 0
    for player in roster:
        avg = average_points(player["points"])
        if avg > best_avg:
            best_avg = avg
            best_name = player["player"]
    return best_name, best_avg

def best_overall_player(roster):
    best_name = ""
    best_score = 0
    for player in roster:
        avg_pts = average_points(player["points"])
        avg_ast = average_points(player["assists"])
        avg_reb = average_points(player["rebounds"])
        overall = avg_pts + avg_ast + avg_reb
        if overall > best_score:
            best_score = overall
            best_name = player["player"]
    return best_name, best_score

name, score = best_overall_player(roster)
print(f"🏆 Best Overall Player: {name} (Impact Score: {score:.1f})")

name, avg = best_player(roster)
print(f"Best Player: {name} ({avg:.1f})")