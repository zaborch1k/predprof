import get_data

def interp_data():
    data = get_data.get_data_dates()
    main_data = {}
    for i in data:
        date = '.'.join(i[0])
        d = i[1]['message']
        flats_count = d['flats_count']['data']
        windows_for_flat = d['windows_for_flat']['data']
        wind = d['windows']['data']
        windows = [wind['floor_'+str(i+1)] for i in range(0, flats_count)]
        
        data1 = [flats_count, windows, windows_for_flat]
        main_data[date] = data1
    return main_data

def count_data(date):
    main_data = interp_data()
    data = main_data[date]
    num = dcount(main_data[date])
    return [date, data, num]

def dcount(data):
    room_floor = data[0]
    room_light = data[1]
    windows = data[2]

    apart_data = []
    for i in room_light:
        apart1 = True if True in i[:windows[0]+1] else False
        apart2 = True if True in i[windows[0]:windows[0]+windows[1]+1] else False
        apart3 = True if True in i[windows[0]+windows[1]:] else False
        apart_data.append(apart1)
        apart_data.append(apart2)
        apart_data.append(apart3)

    apart_data = apart_data[::-1]
    apart_light = []
        
    for i in range(len(apart_data)):
        if apart_data[i] == True:
            apart_light.append(i+1),
    return apart_light