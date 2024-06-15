import numpy as np
from pysnark.runtime import snark

def generate_update_correctness_proof(model_coef, initial_model_coef, data, learning_rate):
    """
    Generate a proof that the model updates were performed correctly.

    Args:
        model_coef (list): Updated model coefficients.
        initial_model_coef (list): Initial model coefficients before update.
        data (list of tuples): Training data (features and labels).
        learning_rate (float): Learning rate used for the update.

    Returns:
        Proof: Generated proof.
    """
    updated_coef = []
    for coef, init_coef in zip(model_coef, initial_model_coef):
        update = init_coef - learning_rate * sum(x * (y - coef * x) for x, y in data)
        updated_coef.append(update)
    
    proof = snark.prove(updated_coef == model_coef)
    return proof

if __name__ == "__main__":
    from sklearn.linear_model import LogisticRegression
    import numpy as np
    from load_models import load_all_models

    # Generate some dummy data for testing
    X = np.array([[0.1, 0.2], [0.2, 0.1], [0.3, 0.4]])
    y = np.array([0, 1, 0])
    data = list(zip(X, y))

    # Load the initial and updated models
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_dir = os.path.join(current_dir, '../data/models')
    num_clients = 5
    local_models = load_all_models(model_dir, num_clients)
    
    initial_model = local_models[0]  # Assuming we are using the first model as initial
    updated_model = {'coef_': initial_model['coef_'] - 0.01}  # Example update

    # Generate proof
    learning_rate = 0.01
    proof = generate_update_correctness_proof(updated_model['coef_'], initial_model['coef_'], data, learning_rate)
    print("Proof generated:", proof)
