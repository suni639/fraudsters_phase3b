from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def evaluate_global_model(global_model, X_test, y_test):
    """
    Evaluate the global model on the test data.

    Args:
        global_model (LogisticRegression): Aggregated global model.
        X_test (np.ndarray): Test data features.
        y_test (np.ndarray): Test data labels.

    Returns:
        float: Accuracy of the global model.
    """
    predictions = global_model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    return accuracy

# Example usage
if __name__ == "__main__":
    # Load your test data and evaluate the model
    pass
