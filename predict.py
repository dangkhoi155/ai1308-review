def predict(scores):
    """Nhan có di?m cao nh?t trong dict {nhan: di?m}."""
    return max(scores, key=scores.get)
