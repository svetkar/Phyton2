def my_func(argv):
    global vyr_v_chasah, stavka_v_chas, premiya
    try:
        vyr_v_chasah = float(vyr_v_chasah)
        stavka_v_chas = float(stavka_v_chas)
        premiya = float(premiya)
        zp = round((vyr_v_chasah * stavka_v_chas) + premiya, 2)
        print(f'Заработная плата равна: {zp}')
    except ValueError:
        print('Введены некорректные значения')


from sys import argv

try:
    script_name, vyr_v_chasah, stavka_v_chas, premiya = argv
    my_func(argv)
except ValueError:
    print('Введено неверное число параметров')
