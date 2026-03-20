def detect_anomalies(data):
    anomalies = []
    for item in data:
        if item["cost"] > 200:
            anomalies.append(item)
    return anomalies
