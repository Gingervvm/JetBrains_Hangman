def get_percentage(real_number, round_digits=None):
    result_percentage = float(real_number) * 100
    result_round = round(result_percentage, int(round_digits)) if round_digits else round(result_percentage)
    return f"{result_round}%"