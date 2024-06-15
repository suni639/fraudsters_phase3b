from pysnark.runtime import snark

def verify_update_correctness_proof(proof, model_coef, initial_model_coef, data, learning_rate):
    """
    Verify the proof that the model updates were performed correctly.

    Args:
        proof (Proof): Proof of update correctness.
        model_coef (list): Updated model coefficients.
        initial_model_coef (list): Initial model coefficients before update.
        data (list of tuples): Training data (features and labels).
        learning_rate (float): Learning rate used for the update.

    Returns:
        bool: True if the proof is valid, False otherwise.
    """
    try:
        snark.verify(proof)
        return True
    except:
        return False

if __name__ == "__main__":
    from generate_proofs import generate_update_correctness_proof
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
    
    # Verify proof
    is_valid = verify_update_correctness_proof(proof, updated_model['coef_'], initial_model['coef_'], data, learning_rate)
    print("Proof valid:", is_valid)
