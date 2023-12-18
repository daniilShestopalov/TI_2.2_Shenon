import ShannonFano
from Visual import visualize_tree, generate_codes



if __name__ == "__main__":
    probabilities_dict = {
        "Z1": 0.347,
        "Z2": 0.09,
        "Z3": 0.085,
        "Z4": 0.04,
        "Z5": 0.25,
        "Z6": 0.045,
        "Z7": 0.013,
        "Z8": 0.046,
        "Z9": 0.022,
        "Z10": 0.062

    }
    try:
        symbols = list(probabilities_dict.keys())
        probabilities = list(probabilities_dict.values())
        print("Sorted prob")
        sorted_d = dict(sorted(probabilities_dict.items(), key=lambda item: item[1], reverse=True))
        sorted_probabilities_output = "\n".join([f"{key} : {value}" for key, value in sorted_d.items()])
        print(sorted_probabilities_output)
        print("Code")

        tree = ShannonFano.shannon_fano_stepwise(symbols, probabilities)
        codes = generate_codes(tree)
        sorted_probabilities_and_codes_output = "\n".join([f"{key} : {value}, Code: {codes[key]}" for key, value in
                                                           probabilities_dict.items()])
        print(sorted_probabilities_and_codes_output)
        visualize_tree(tree).view()

        print("H,L and R:")
        H = ShannonFano.entropy(probabilities_dict)
        L = ShannonFano.average_code_length(probabilities_dict, codes)
        R = round(L, 3) - round(H, 3)
        print(f'H = {round(H, 3)}')
        print(f'L = {round(L, 3)}')
        print(f'R = {round(R, 3)}')

    except ValueError as e:
        print(e)
