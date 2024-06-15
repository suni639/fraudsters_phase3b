import numpy as np

def aggregate_updates(models):
    """
    Aggregate the updates from the verified local models.

    Args:
        models (list of dict): List of verified local model dictionaries.

    Returns:
        np.ndarray: Aggregated model coefficients.
    """
    num_models = len(models)
    avg_coef = sum([model['coef_'] for model in models]) / num_models
    return avg_coef

if __name__ == "__main__":
    # Example usage
    # Create some dummy models
    model1 = {'coef_': np.array([[0.4, 0.6]])}
    model2 = {'coef_': np.array([[0.5, 0.5]])}
    model3 = {'coef_': np.array([[0.6, 0.4]])}
    
    models = [model1, model2, model3]
    
    # Aggregate updates
    aggregated_coef = aggregate_updates(models)
    print("Aggregated coefficients:", aggregated_coef)
