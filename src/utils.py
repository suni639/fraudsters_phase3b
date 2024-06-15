import pickle

def save_model(model, file_path):
    """
    Save a logistic regression model to a .pkl file.

    Args:
        model (LogisticRegression): The model to save.
        file_path (str): Path to the .pkl file.
    """
    with open(file_path, 'wb') as file:
        pickle.dump(model, file)

def load_model(file_path):
    """
    Load a logistic regression model from a .pkl file.

    Args:
        file_path (str): Path to the .pkl file.

    Returns:
        LogisticRegression: Loaded logistic regression model.
    """
    with open(file_path, 'rb') as file:
        model = pickle.load(file)
    return model