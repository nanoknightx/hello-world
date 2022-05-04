from itertools import tee


def main():
    """Calculates time difference between two dates."""

    test = (5, 3, 23, 22, 24, 4, 20, 45)

    days = test[4] - test[0]
    hours = test[5] - test[1]
    minutes = test[6] - test[2]
    seconds = test[7] - test[3]

    sum = (days * 24 * 60 * 60) + (hours * 60 * 60) + (minutes * 60) + seconds

    total_days = sum // 86400
    sum = sum - total_days * 86400
    total_hours = sum // 3600
    sum = sum - total_hours * 3600
    total_minutes = sum // 60
    sum = sum - total_hours * 60
    total_seconds = sum % 60


    print(total_days, total_hours, total_minutes, total_seconds)

if __name__ == "__main__":
    main()