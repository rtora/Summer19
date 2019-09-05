import run_rat_spn_fashion_mnist

run_rat_spn_fashion_mnist.structure_dict = {}
# depth 1
run_rat_spn_fashion_mnist.structure_dict[1] = [{'num_recursive_splits': 14, 'num_input_distributions': 15, 'num_sums': 10}]
# depth 2
run_rat_spn_fashion_mnist.structure_dict[2] = [{'num_recursive_splits': 12, 'num_input_distributions': 15, 'num_sums': 15}]
# depth 3
run_rat_spn_fashion_mnist.structure_dict[3] = [{'num_recursive_splits': 12, 'num_input_distributions': 14, 'num_sums': 12}]
# depth 4
run_rat_spn_fashion_mnist.structure_dict[4] = [{'num_recursive_splits': 10, 'num_input_distributions': 15, 'num_sums': 10}]
run_rat_spn_fashion_mnist.base_result_path = "quick_results/ratspn/fashion_mnist/"
run_rat_spn_fashion_mnist.param_configs = [{'dropout_rate_input': 0.5, 'dropout_rate_sums': 0.5}]
run_rat_spn_fashion_mnist.num_epochs = 60

run_rat_spn_fashion_mnist.run()
