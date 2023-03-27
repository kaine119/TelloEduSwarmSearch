def generate_serial_obj():
    file = open('serials.txt')
    serials = file.read()
    file.close()

    serials = serials.split('\n')
    serial_obj = {}

    for serial in serials:
        if serial != '':
            label, sn, mac = serial.split("\t")
            mac = mac.lower()
            mac = mac[:2] + ':' + mac[2:4] + ":" + mac[4:6]
            serial_obj[int(label)] = (sn, mac)

    return serial_obj


def get_mac_addr_from_num(num_arr):
    serial_obj = generate_serial_obj()

    mac_arr = []
    for num in num_arr:
        mac_arr.append(serial_obj[num][1])

    return mac_arr


def get_number_from_mac_addr(mac_to_find):
    serial_obj = generate_serial_obj()

    for number, (_, mac) in serial_obj.items():
        if mac == mac_to_find:
            return number

    return -1


def get_sn_from_num(num_arr):
    serial_obj = generate_serial_obj()

    sn_arr = []
    for num in num_arr:
        sn_arr.append(serial_obj[num][0])

    return sn_arr


if __name__ == "__main__":
    print(get_mac_addr_from_num([1, 5, 3, 4]))

