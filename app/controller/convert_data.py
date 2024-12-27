from datetime import datetime

def convert_to_time(time_string):
    try:
        # Chuyển đổi chuỗi sang kiểu datetime.time
        time_object = datetime.strptime(time_string, "%H:%M").time()
        return time_object
    except ValueError:
        raise ValueError("Invalid time format. Expected HH:MM.")
