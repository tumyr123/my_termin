# Импорт библиотек
import pyautogui as maus
import keyboard as key
from pygame import mixer

# Создали начальные коэффициэнты и добавили путь к файлам
move_min = 65 #внутри строки
move_max = 75 #между строчек

p_x = 573
p_y = 621


find_color = (0, 0, 0)

string_I_2 = [1,1,2]
string_I = [1,1,1]
string_F = [3,1,3]
string_M = [3,1,1]
string_G = [2,2,3]
string_D = [2,1,3]

scroll_I = [0,0,0]
scroll_F = [-1000,0,-1000]
scroll_M = [0,0,0]
scroll_G = [0,0,-1000]
scroll_D = [-1000,0,-200]

restart_I = [[1,0],
             [1,0]]

restart_I_2 = [[1,0],
             [2,0]]

restart_M = [[1,0],
             [1,0]]
restart_D = [[1,0],
             [3,-200]]
restart_F = [[1,0],
             [3,-1000]]

# Ввод данных про себя
def input_data():
    maus.scroll(-1000)
    maus.moveTo(780,557)
    maus.click()
    maus.moveTo(748,691)
    maus.click()
    maus.moveTo(926,702)
    maus.click()
    maus.scroll(-1000)
    maus.moveTo(875,672)
    maus.click()

# Функция для звука
def sound():
    mixer.init()
    mixer.music.load("sound.mp3")
    mixer.music.play()


# Повторный ввод для консульств
def restart_func(matrix_restart,delta,sleep):
    maus.moveTo(711, 405)
    maus.click()
    maus.move(0, move_min*delta)
    maus.click()
    maus.move(0, -move_min * delta)
    # maus.sleep(1 + sleep)
    # maus.sleep(1)
    for i in range(2):
        if i == 1:
            maus.sleep(1 + sleep)
        maus.click()
        maus.move(0,move_min*matrix_restart[i][0])
        maus.scroll(matrix_restart[i][1])

        # maus.sleep(1)
        maus.click()
        maus.move(0, -move_min * matrix_restart[i][0])
        maus.move(0,move_max)

    # maus.click()

# Функция для перехода на консульство
def input_data_konsulstvo(scroll,srting_int,sleep):
    maus.scroll(-1000)
    maus.moveTo(764, 326)
    for i in range(3):
        if i != 0:
            maus.sleep(0.1 + sleep)
        maus.click()
        maus.move(0, move_min * srting_int[i])
        maus.scroll(scroll[i])

        maus.click()
        maus.move(0, -move_min * srting_int[i])
        maus.move(0,move_max)
    maus.click()

# Функция рекурсии для повторения
def restart_func_General_repeat(matrix_restart,delta,sleep):
    maus.sleep(1+sleep)
    pix = maus.pixel(p_x, p_y)
    if pix == find_color:
        restart_func(matrix_restart, delta,sleep)
        restart_func_General_repeat(matrix_restart,delta,sleep)
    else:
        sound()

# Функция для автоматического повтора
def restart_func_General(matrix_restart,delta,sleep):
    restart_func(matrix_restart,delta,sleep)
    restart_func_General_repeat(matrix_restart,delta,sleep)


# гребанная задержка
sleep = 2


# Считывание клавиш
while True:
    if key.is_pressed("1"):
        input_data()
    elif key.is_pressed("2"):
        maus.moveTo(711, 405)
        # maus.mouseInfo()
    elif key.is_pressed("3"):
        sound()
        # print(maus.pixel(p_x, p_y))
    elif key.is_pressed("4"):
        print(maus.pixel(p_x, p_y))
    elif key.is_pressed("5"):
        pass
    elif key.is_pressed("caps lock") and not key.is_pressed("caps lock+alt") and not key.is_pressed("alt+caps lock"):
        # restart_func_General(restart_M,2)
        # restart_func_General(restart_F, 2,sleep)
        # restart_func_General(restart_D, 2, sleep)
        # ДЛЯ СТАРШЕ 16 ЛЕТ
        restart_func_General(restart_I, 2, sleep)
        # ДЛЯ МЛАДШЕ 16 ЛЕТ
        # restart_func_General(restart_I_2, 2, sleep)
    elif key.is_pressed("alt+caps lock"):
        # input_data_konsulstvo(scroll_M,string_M)
        # input_data_konsulstvo(scroll_F, string_F,sleep)
        # input_data_konsulstvo(scroll_D, string_D,sleep)
        # ДЛЯ СТАРШЕ 16 ЛЕТ
        input_data_konsulstvo(scroll_I, string_I, sleep)
        # ДЛЯ МЛАДШЕ 16 ЛЕТ
        # input_data_konsulstvo(scroll_I, string_I_2, sleep)
