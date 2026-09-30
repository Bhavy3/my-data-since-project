from sklearn.metrics import accuracy_score, mean_squared_error

def select_best_model(models: dict, X_test, y_test, task='auto'):
    best_model = None
    best_score = None
    best_name = None
    for name, model in models.items():
        try:
            y_pred = model.predict(X_test)
            if task == 'auto':
                if len(set(y_test)) <= 10 and y_test.dtype in ['int', 'int32', 'int64']:
                    task_type = 'classification'
                else:
                    task_type = 'regression'
            else:
                task_type = task
            if task_type == 'classification':
                score = accuracy_score(y_test, y_pred)
            else:
                score = -mean_squared_error(y_test, y_pred, squared=False)
            if best_score is None or score > best_score:
                best_score = score
                best_model = model
                best_name = name
        except Exception as e:
            continue
    return best_name, best_model

if __name__ == "__main__":
    from sklearn.datasets import load_iris
    from sklearn.linear_model import LogisticRegression 
    from sklearn.tree import DecisionTreeClassifier
    data = load_iris()
    X, y = data.data, data.target
    X_train, X_test, y_train, y_test = X[:100], X[100:], y[:100], y[100:]
    models = {
        'LogisticRegression': LogisticRegression(max_iter=200).fit(X_train, y_train),
        'DecisionTree': DecisionTreeClassifier().fit(X_train, y_train)
    }
    name, model = select_best_model(models, X_test, y_test)
    print(f"Best model: {name}") 