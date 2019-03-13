def create_2_level_position_array(pieces_position_list):
    pieces_position_list_2_level = [None] * len(pieces_position_list)
    
    for i, v in enumerate(pieces_position_list):
        a = v.split("_")
        pieces_position_list_2_level[i] = {"position": a[0], "color": a[1]}
    return pieces_position_list_2_level


def get_column_color(column, pieces_position_list_2_level):
    return [i["color"] for i in pieces_position_list_2_level if i["position"] == column]


def create_2_level_color_map(pieces_position_list):
    li = [''] * 7
    for i in range(7):
        li[i] = ['****'] * 6
    pieces_position_list_2_level = create_2_level_position_array(pieces_position_list)
    position = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    for i in range(7):
        column_color = get_column_color(position[i], pieces_position_list_2_level)
        for j in range(len(column_color)):
            li[i][j] = column_color[j]
    return li

def who_is_winner(pieces_position_list):
    result = "Draw"
    for i in range(len(pieces_position_list)):
        result = who_is_winner_per_count(pieces_position_list[:i+1])
        if result != "Red" and result != "Yellow":
            continue
    return result
        

def who_is_winner_per_count(pieces_position_list):
    li = create_2_level_color_map(pieces_position_list)

    result = []
    result += who_win_in_column(li)

    li_rotated = rotate_map(li)
    result += who_win_in_column(li)
    
    result += who_win_in_45_degree(li_rotated)

    result = set(result)
    if "Red" in result:
        return "Red"
    elif "Yellow" in result:
        return "Yellow"
    else:
        return "Draw"
        

def who_win_in_column(color_map):
    result = []
    for i, column in enumerate(color_map):
        for j in range(len(column)-3):
            if column[j] == column[j+1] == column[j+2] == column[j+3] and column[j] != '****':
                result.append(column[j])
    return result

def who_win_in_45_degree(color_map):
    result = []
    for i in range(3):
        for j in range(4):
            if color_map[i][j] == color_map[i+1][j+1] == color_map[i+2][j+2] == color_map[i+3][j+3] and color_map[i][j] != '****':
                result.append(color_map[i][j])
    for i in range(3):
        for j in range(3, 7):
            if color_map[i][j] == color_map[i+1][j-1] == color_map[i+2][j-2] == color_map[i+3][j-3] and color_map[i][j] != '****':
                result.append(color_map[i][j])
    return result


def rotate_map(color_map):
    li = [''] * 6
    for i in range(6):
        li[i] = ['****'] * 7
    for i in range(7):
        for j in range(6):
            li[j][i] = color_map[i][j]
    return li

def print_2_level_array(arr):
    print("\n===============print 2 level array: ============\n")
    for i in arr:
        print(i)

pieces_position_list = ["C_Yellow", "E_Red", "G_Yellow", "B_Red", "D_Yellow", "B_Red", "B_Yellow", "G_Red", "C_Yellow", "C_Red","D_Yellow", "F_Red", "E_Yellow", "A_Red", "A_Yellow", "G_Red", "A_Yellow", "F_Red", "F_Yellow", "D_Red","B_Yellow", "E_Red", "D_Yellow", "A_Red", "G_Yellow", "D_Red", "D_Yellow", "C_Red"]

pieces_position_list2= ["C_Yellow", "B_Red", "B_Yellow", "E_Red", "D_Yellow", "G_Red", "B_Yellow", "G_Red", "E_Yellow", "A_Red", "G_Yellow", "C_Red", "A_Yellow", "A_Red", "D_Yellow", "B_Red", "G_Yellow", "A_Red", "F_Yellow", "B_Red", "D_Yellow", "A_Red", "F_Yellow", "F_Red", "B_Yellow", "F_Red", "F_Yellow", "G_Red", "A_Yellow", "F_Red", "C_Yellow", "C_Red", "G_Yellow", "C_Red", "D_Yellow", "D_Red", "E_Yellow", "D_Red", "E_Yellow", "C_Red", "E_Yellow", "E_Red"]

# print(who_is_winner(pieces_position_list))
print(who_is_winner(pieces_position_list2))

