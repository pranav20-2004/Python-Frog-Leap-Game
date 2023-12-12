def display_game(positions):
    print("[0 , 1, 2, 3, 4, 5, 6]")
    print(positions)
def main():
    positions=['G', 'G', 'G', '-', 'B', 'B', 'B']
#'G'- Green Frogs
#'B'- Brown Frogs
#'-'- Blank Space
    while True:
        display_game(positions)
        move = input("Press 'q' to quit else \n Enter the position of the piece: ")
        
        if move== 'q':
            print("YOU LOSE")
            break
        
        try:
            move=int(move)
        except ValueError:
            print("Invalid Move")
            continue
        if move < 0 or move >6:
            print('Invalid move')
            continue
        if positions[move]=='-':
            print("Invalid Move")
            continue
        
        pos2 = 0
        if positions[move]== "G":
            if move + 1 <=6 and positions[move + 1] == '-':
                pos2 = move+1
            elif move + 2<=6 and positions[move + 2] == '-' and positions[move + 1 ]== 'B':
                pos2= move +2 
            else:
                print("Invalid Move")
                continue
        elif positions[move]== 'B':
            if move -1 >=0 and positions[move - 1]=='-':
                pos2=move -1
            elif move - 2 >=0 and positions[move - 2]=='-' and positions[move - 1]=='G':
                pos2=move - 2
            else:
                print("Invalid Move")
                continue
        positions[move],positions[pos2]= positions[pos2],positions[move]
        
        if positions ==  ['B', 'B', 'B', '-', 'G', 'G', 'G']:
            display_game(positions)
            print("You Win!")
            break
        valid_moves_exist = False
        for i in range(len(positions)):
            if positions[i] == 'G' and i + 1 <= 6 and positions[i + 1] == '-':
                valid_moves_exist = True
                break
            elif positions[i] == 'G' and i + 2 <= 6 and positions[i + 2] == '-' and positions[i + 1] == 'B':
                valid_moves_exist = True
                break
            elif positions[i] == 'B' and i - 1 >= 0 and positions[i - 1] == '-':
                valid_moves_exist = True
                break
            elif positions[i] == 'B' and i - 2 >= 0 and positions[i - 2] == '-' and positions[i - 1] == 'G':
                valid_moves_exist = True
                break

        if not valid_moves_exist:
            display_game(positions)
            print("Game Over - No Valid Moves Left")
            break

if __name__ == "__main__":
    main()