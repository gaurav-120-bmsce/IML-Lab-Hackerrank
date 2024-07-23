white_balls_x = 5
black_balls_x = 4
total_balls_x = white_balls_x + black_balls_x
prob_white_x = white_balls_x / total_balls_x
prob_black_x = black_balls_x / total_balls_x

white_balls_y = 7
black_balls_y = 6
total_balls_y = white_balls_y + black_balls_y
prob_white_y = white_balls_y / total_balls_y
prob_black_y = black_balls_y / total_balls_y

new_total_balls_y = total_balls_y + 1

prob_black_from_y_if_white = black_balls_y / new_total_balls_y
prob_black_from_y_if_black = (black_balls_y + 1) / new_total_balls_y

total_prob_black_from_y = prob_black_from_y_if_black * prob_black_x + prob_black_from_y_if_white * prob_white_x

print(total_prob_black_from_y)
