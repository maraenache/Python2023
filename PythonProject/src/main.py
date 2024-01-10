import argparse
from src.game_app import GameApp


def main():
    parser = argparse.ArgumentParser(description="Play solitaire.")

    parser.add_argument('-instant_victory', dest='instant_victory', default=False, action="store_true")
    args = parser.parse_args()  # only for dev use> python solitaire.py -instant_victory, not part of the game

    game_manager = GameApp(args.instant_victory)
    game_manager.start_game()


if __name__ == "__ main__":
    main()
