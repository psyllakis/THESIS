import numpy as np


def transition(spliced, initial):
    """ transform time into the format minute.sec m sec
        time was not in the form of 0-60 but it had the actual time. for example 11:30
        so we transition it in a form that would be suitable for the graphs.
    """
    hour = int(spliced[0])
    minutes = int(spliced[1])
    hour_initial = int(initial[0])
    minutes_initial = int(initial[1])

    # the transition
    hour_real = hour - hour_initial
    minutes_real = minutes - minutes_initial

    # in case that the minutes_real is less than 0 means that the hour has changed for example from 9 to 10
    # in that case we need to add 60 in order that the result is positive and correct.
    if minutes_real < 0 and hour_real == 1:
        minutes_real = 60 + minutes_real

    return float(str(minutes_real) + "." + spliced[2] + spliced[3])


def time_points(sum_of_time):
    """
        This function returns the time in a suitable form, which is 0.0 to 60(we know that because the examination
        takes place for about 0 to 40 minutes). It can work of course for more time!
    """
    # initial is a list of the starting time split in an array with its elements containing the initial hour min
    # sec and m sec.
    # splice is a temporal list that contains for each moment the variables of time (hour minute sec m sec)
    # the for loop adds a "0"  in the beginning of every variable of time(hour minute sec m sec if it originally
    # had length of 1) because we want each variable to have at least a length of 2
    # for each element of sum_of_time after we use the function transition we load the modified values in a new array
    # that will be our new time for now on.

    time_point = []
    initial = sum_of_time[0].split("-")

    for i in range(len(sum_of_time)):
        spliced = sum_of_time[i].split("-")
        for num in range(4):
            if len(spliced[num]) == 1:
                spliced[num] = "0" + spliced[num]
        time_point.append(transition(spliced, initial))

    return time_point


def per_minute(time_point, metric, sorted_table, sum_of_time):
    """ this function finds the frames and time points that score the best P.S.N.R. score every minute and returns them
    """
    # definition start
    sum_of_all_time = []
    sum_of_all_frames = []
    initial = int(time_point[0])
    start_pos = 0
    sub_metric = []
    temp = 0
    # definition end

    for i in range(len(sorted_table)):
        if int(time_point[i]) == initial:
            sub_metric.append(metric[i])
            temp = 0
        elif int(time_point[i]) == initial + 1:
            meg = np.max(sub_metric)
            for k in range(start_pos, i-1):
                if metric[k] == meg:
                    sum_of_all_time.append(sum_of_time[k])
                    sum_of_all_frames.append(sorted_table[k])
            start_pos = i
            initial = int(time_point[i])
            sub_metric = [metric[i]]
            temp = 1

    if temp == 0:
        meg = np.max(sub_metric)
        for k in range(start_pos, len(sorted_table)):
            if metric[k] == meg:
                sum_of_all_time.append(sum_of_time[k])
                sum_of_all_frames.append(sorted_table[k])

    return sum_of_all_time, sum_of_all_frames
