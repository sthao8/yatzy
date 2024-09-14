from player import Die, Player

def main():
    player = Player()
    player.roll_die()

    player.print_dice_values()
    one_player_turn(player)

def one_player_turn(player: Player):
    for turn_no in range(2):
        print(f"\nTURN {turn_no}")

        reroll = input("Reroll any die? [A]ll, [S]ome, [N]one: ").lower()
        match reroll:
            case "a":
                player.roll_die()
                turn_no += 1
            case "s":
                while True:
                    dice_names_to_keep = input("Which dice do you want to keep: ").lstrip(" ").rstrip(" ").split(", ")
                    dice_names_to_keep_int = [int(name) for name in dice_names_to_keep]
                    if set(dice_names_to_keep_int).issubset(player.dice_names):
                        break
                    print(f"Invalid dice name! Valid choices: {player.dice_names}")
                dice_to_reroll = [dice_name for dice_name in dice_names_to_keep if dice_name not in dice_names_to_keep]
                player.roll_die(*dice_to_reroll)
                turn_no += 1
            case "n":
                turn_no += 2
                break
            case "q":
                return
            case _:
                print("Invalid choice! Try again")
                continue
        
        player.print_dice_values()


if __name__ == "__main__":
    main()