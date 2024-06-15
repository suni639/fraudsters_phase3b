import pickle
import os

def load_model(file_path):
    """
    Load a logistic regression model from a .pkl file.

    Args:
        file_path (str): Path to the .pkl file.

    Returns:
        dict: Loaded logistic regression model as a dictionary.
    """
    with open(file_path, 'rb') as file:
        model = pickle.load(file)
    return model

def load_all_models(model_dir, num_clients):
    """
    Load all logistic regression models from a directory.

    Args:
        model_dir (str): Directory containing the model .pkl files.
        num_clients (int): Number of client models to load.

    Returns:
        list: List of loaded logistic regression models as dictionaries.
    """
    models = []
    for i in range(num_clients):
        model_path = os.path.join(model_dir, f'model_{i}.pkl')
        print(f"Loading model from {model_path}")  # Debugging information
        models.append(load_model(model_path))
    return models

def inspect_model_structure(model):
    """
    Inspect the structure of the loaded model.

    Args:
        model (dict): The loaded model dictionary.

    Returns:
        None
    """
    if isinstance(model, dict):
        print("Model is a dictionary with keys:", model.keys())
    else:
        print("Model type:", type(model))
        print("Model attributes:", dir(model))

if __name__ == "__main__":
    # Use absolute path for the data directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_dir = os.path.join(current_dir, '../data/models')
    num_clients = 5

    print(f"Model directory: {model_dir}")  # Debugging information

    local_models = load_all_models(model_dir, num_clients)
    for i, model in enumerate(local_models):
        print(f"Inspecting structure of model {i}")
        inspect_model_structure(model)
        print(f"Model {i} coefficients: {model['coef_']}")
