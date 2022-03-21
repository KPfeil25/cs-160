def is_pos_int(string):
    for i in range(0, len(string)):
        if (string[i] < '0' or string[i] > '9'):
            return False
    if (int(string) == 0):
        return False
    return True

def is_float(string):
    dot_counter = 0
    for i in range(0, len(string)):
        if string[i] == '.':
            dot_counter = dot_counter + 1    
    if dot_counter != 1:
        print("Not a floating point value!")
        return False
    for i in range(0, len(string)):
        if string[i] != '.' and (string[i] < '0' or string[i] > '9'):
            print("Not an floating point value!")
            return False
    print("Is a floating point value!")
    return True

def main():
    left_t = 0
    right_t = 100.0

    while (True):
        thermal_in = input("Thermal Conductivity(float): ")
        if (is_float(thermal_in) and float(thermal_in) != 0):
            thermal = float(thermal_in)
            break

    while (True):
        density_in = input("Density(float): ")
        if (is_float(density_in) and float(density_in) != 0):
            density = float(density_in)
            break

    while (True):
        specific_in = input("Specific Heat(float): ")
        if (is_float(specific_in) and float(specific_in) != 0):
            specific = float(specific_in)
            break

    while (True):
        i_temp_in = input("Initial Temp of Wire(float): ")
        if (is_float(i_temp_in) and float(i_temp_in) != 0):
            i_temp = float(i_temp_in)
            break

    while (True):
        l_temp_in = input("Left Temperature(float): ")
        if (is_float(l_temp_in) and float(l_temp_in) != 0):
            l_temp = float(l_temp_in)
            break

    while (True):
        r_temp_in = input("Right Temperature(float): ")
        if (is_float(r_temp_in) and float(r_temp_in) != 0):
            r_temp = float(r_temp_in)
            break
    
    while (True):
        i_length = input("Length of wire(integer): ")
        if (is_pos_int(i_length)):
            length = int(i_length)
            break

    while (True):
        sec_in = input("Number of sections(integer):")
        if (is_pos_int(sec_in)):
            num_sections = int(sec_in)
            break
    
    while (True):
        init_time = input("Number of time Intervals(integer)")
        if (is_pos_int(init_time)):
            time = int(init_time)
            break

    while (True):
        change_in_time_in = input("Change in time per Interval(float): ")
        if (is_float(change_in_time_in) and float (change_in_time_in) != 0):
            change_in_time = float(change_in_time_in)
            break
    
    change_in_x = length / num_sections

    stability = (thermal * change_in_time) / ((change_in_x ** 2) * specific * density)

    if (stability < 0.5):
        print(str(stability) + " is the stability and it is stable enough to proceed")
        uold = [i_temp] * num_sections
        uold[0] = l_temp
        uold[num_sections - 1] = r_temp
        unew = uold[:]

        for index in range(time):
            for i in range(1, num_sections - 1):
                unew[i] = stability * (uold[i+1] - 2 * uold[i] + uold[i-1]) + uold[i]
                uold = unew[:]
    else:
        print("Not stable enough")

main()