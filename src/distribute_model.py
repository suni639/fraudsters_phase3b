from sklearn.linear_model import LogisticRegression

def distribute_global_model(global_model, clients):
    """
    Distribute the global model to all clients.

    Args:
        global_model (LogisticRegression): The aggregated global model.
        clients (list): List of client instances.
    """
    for client in clients:
        client.receive_global_model(global_model.coef_)

# Example usage
if __name__ == "__main__":
    # Example global model distribution would be done here
    pass
