def percent_change(baseline, proposed):
    if baseline == 0:
        return 0 if proposed == 0 else 100.0
    return round(((proposed - baseline) / baseline) * 100, 2)
