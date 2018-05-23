MCTS_CONFIG = {
    "c_puct": 5,
    "c_iterations": 400,
    "c_duration": 950
}

DATA_CONFIG = {
    # one of "random", "botzone", "default_mcts", "alpha_zero"
    "agents": [
        ("botzone", ["./training_data/hdl.exe"]),
        ("botzone", ["./training_data/deep.exe"])
    ],
    "process_num": 2,
    "buffer_size": 10000,
    "data_path": "./training_data",
    "data_files": [
        # after read out, file name will be marked ".consumed"
    ]
}

TRAINING_CONFIG = {
    "num_epoches": 5,
    "batch_size": 512,
    "learning_rate": 2e-3,
    "momentum": 0.9,
    "kl_target": 0.02,
    "eval_period": 100,
    "eval_rounds": 11,
    "model_file": "latest",
    "model_path": "./trained_models"
}
