def main():
    time_string = input("What time is it? ").strip()
    time_converted = convert(time_string)
    if 7.0 <= time_converted <= 8.0:
        print("breakfast time")
    elif 12.0 <= time_converted <= 13.0:
        print("lunch time")
    elif 18.0 <= time_converted <= 19.0:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + float(minutes) / 60


if __name__ == "__main__":
    main()
