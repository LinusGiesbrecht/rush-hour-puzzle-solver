import game


def main():

    game.solve_puzzles("sample-input.txt", with_ucs=True, with_algo_a=False, with_gbfs=False, create_output_files=True, create_excel_file=True)


if __name__ == "__main__":
    main()
