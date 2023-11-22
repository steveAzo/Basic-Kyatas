def to_industrial(time):
    if isinstance(time, int):
        industrial_minute = (10 * time) / 6
        industrial_hour = round((industrial_minute / 100), 2)
        return industrial_hour
    elif isinstance(time, str):
        t_time = time.split(':')
        time_in_minutes = [int(i) for i in t_time ]
        # The next line tries to convert time to normal minutes
        normal = (60 * time_in_minutes[0] + time_in_minutes[1])
        industrial = (10 * normal) / 6
        hour = round((industrial / 100), 2)
        return hour
    else:
        return 'Error'


def to_normal(time):
    industry_minutes = 100 * time
    normal_minutes = (6 * industry_minutes) / 10
    hours, minutes = divmod(normal_minutes, 60)
    return f"{int(hours)}:{int(round(minutes)):02d}"
