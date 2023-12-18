from itertools import combinations

import graphviz







probabilities_dict = {
    "Z1": 0.274,
    "Z2": 0.09,
    "Z3": 0.1,
    "Z4": 0.115,
    "Z5": 0.19,
    "Z6": 0.09,
    "Z7": 0.034,
    "Z8": 0.022,
    "Z9": 0.025,
    "Z10": 0.06
}

symbols = list(probabilities_dict.keys())
probabilities = list(probabilities_dict.values())
print("Sorted prob")
sorted_d = dict(sorted(probabilities_dict.items(), key=lambda item: item[1], reverse=True))
sorted_probabilities_output = "\n".join([f"{key} : {value}" for key, value in sorted_d.items()])
print(sorted_probabilities_output)
print("Code")

tree = shannon_fano_stepwise(symbols, probabilities)
codes = generate_codes(tree)
sorted_probabilities_and_codes_output = "\n".join([f"{key} : {value}, Code: {codes[key]}" for key, value in
                                                   probabilities_dict.items()])
print(sorted_probabilities_and_codes_output)
visualize_tree(tree).view()