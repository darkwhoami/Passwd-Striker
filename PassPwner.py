# Date: 11.03.2023 17:00
# Author: 1337rce
# Description: Passwd Generator
import sys
import os
import time


def banner():
    os.system('clear')
    print('''\033[91m⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⢀⠎⠀⠀⢀⣀⣤⣤⣀⣘⣿⣿⣿⣆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⣏⡀⠀⠀⠈⣉⣻⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡠⠂⠀⠏⣀⡀⠀⠀⠀⠉⠛⠿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⠀⠀⠀⣴⣤⣴⠞⢻⣿⠛⢿⣆⠀⠀⣿⣠⣿⣿⣿⣿⣿   ___________⠀⠀⠀⠀⠀
⠀⠀⠀⣿⣿⠟⠀⡘⠋⠉⣙⣻⣇⠀⢹⣿⣿⣿⣿⣿⣿⣇⠀ ⠀⠀CREATED
⠀⠀⠀⣿⣡⡄⠚⠻⢿⣿⣿⠿⣿⡆⢻⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀1337RCE
⠀⠀⠀⣿⡿⢿⢆⠀⠀⠥⣖⣿⣿⣿⡈⣿⣿⣿⣿⣿⣿⣿⣿⡄-----------⠀⠀
⠀⠀⠤⠁⠤⢤⣦⣶⣿⣿⣿⣿⣿⣿⣷⣬⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀
⠀⠀⠀⠀⠀⠀⠈⠙⠻⡿⢿⣿⠿⠛⢻⠛⢿⣿⣿⣿⣿⣿⡿⠿⠛⠀
⠀⠀⠀⠀⠀⣀⡀⢀⣪⣀⣀⠀⣀⣠⣤⣷⣾⣿⣿⣿⣿⣿⣿⣷⣄⠀
⠀⠀⣐⣋⣿⣿⣿⠿⡿⠁⢠⣾⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷
⣠⣾⣿⣿⣿⠁⠀⢠⠁⢠⠏⣿⡿⠁⣸⡝⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿\033[93mH4ck1ng T007K1t (\033[96m1337RCE\033[93m) 

    ''')
    print('''\033[91m
            \033[91m [\033[96m*\033[91m] \033[97mCreated \033[5m\033[1;91m=  \033[97m1337RCE   \033[25m 
            \033[91m [\033[96m*\033[91m] \033[97mCreated \033[5m\033[1;91m=  \033[97m1337RCE   \033[25m 
    	    \033[91m [\033[96m*\033[91m] \033[97mCreated \033[5m\033[1;91m=  \033[97m1337RCE   \033[25m 	
    ''')


def logo():
    os.system('clear')
    print('''\033[91m⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢀⢀⠎⠀⠀⢀⣀⣤⣤⣀⣘⣿⣿⣿⣆⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢠⣏⡀⠀⠀⠈⣉⣻⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⡠⠂⠀⠏⣀⡀⠀⠀⠀⠉⠛⠿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
    ⠀⠀⠀⣴⣤⣴⠞⢻⣿⠛⢿⣆⠀⠀⣿⣠⣿⣿⣿⣿⣿   ___________⠀⠀⠀⠀⠀
    ⠀⠀⠀⣿⣿⠟⠀⡘⠋⠉⣙⣻⣇⠀⢹⣿⣿⣿⣿⣿⣿⣇⠀ ⠀⠀CREATED
    ⠀⠀⠀⣿⣡⡄⠚⠻⢿⣿⣿⠿⣿⡆⢻⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀1337RCE
    ⠀⠀⠀⣿⡿⢿⢆⠀⠀⠥⣖⣿⣿⣿⡈⣿⣿⣿⣿⣿⣿⣿⣿⡄-----------⠀⠀
    ⠀⠀⠤⠁⠤⢤⣦⣶⣿⣿⣿⣿⣿⣿⣷⣬⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀
    ⠀⠀⠀⠀⠀⠀⠈⠙⠻⡿⢿⣿⠿⠛⢻⠛⢿⣿⣿⣿⣿⣿⡿⠿⠛⠀
    ⠀⠀⠀⠀⠀⣀⡀⢀⣪⣀⣀⠀⣀⣠⣤⣷⣾⣿⣿⣿⣿⣿⣿⣷⣄⠀
    ⠀⠀⣐⣋⣿⣿⣿⠿⡿⠁⢠⣾⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷
    ⣠⣾⣿⣿⣿⠁⠀⢠⠁⢠⠏⣿⡿⠁⣸⡝⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿\033[93mH4ck1ng T007K1t (\033[96m1337RCE\033[93m) 

        ''')


banner()
get_language = int(input('\033[93m[*]Enter language!\n[1]Ru\n[2]En\n1337@set:$> '))
while not get_language > 0 or get_language > 2:
    os.system('clear')
    print('\033[91m1337@kali:$> Sorry this is not correct action!')
    get_language = int(input('\033[93m[*]Enter language!\n[1]Ru\n[2]En\n1337@set:$> '))
os.system('clear')
banner()


class List:

    def __init__(self):

        self.items = []

    def __contains__(self, item):

        return item in self.items

    def __iter__(self):

        while len(self.items):

            yield self.items.pop(0)

    def __len__(self):

        return len(self.items)

    def append(self, item, front=False):

        for _ in (item, item.lower(), item.title(), item.upper()):

            if _ in self.items:

                continue

            if front:

                self.items.insert(0, _)

            else:

                self.items.append(_)


class PassGen:

    def __init__(self):

        self.words = []

        self.b_days = []

        self.is_alive = True

        self.password_list = List()

        self.suffix = [_ for _ in range(124)]

    def get_input(self):

        while self.is_alive:

            if get_language == 1:
                os.system('clear')
                logo()
                print('\033[93m1337@kali: !Введите ключевые слова для генерации! ')
                time.sleep(0.1)
                print('\033[96m1337@kali: !Введите "genpwn" после того как вы ввели нужные слова!')
            elif get_language == 2:
                os.system('clear')
                logo()
                print('\033[93m1337@kali: !Enter the passwords that will be generated!')
                time.sleep(0.1)
                print('\033[96m1337@kali: !Print "genpwn" after you have entered words for generation.! ')
            try:

                user_input = str(input('\033[91m1337@pwn:$> ')).strip()

            except:

                self.is_alive = False

            if not self.is_alive or not user_input:

                continue

            if user_input.lower() != 'genpwn':

                self.append_data(user_input)

            else:

                self.generate()

                self.is_alive = False

                continue

            print('\n')

    def append_data(self, data):

        if len(data.split('-')) == 3:  # birthday

            if not data in self.b_days:

                self.b_days.append(data)

        elif data.isdigit():  # number

            if not data in self.suffix:

                self.suffix.insert(0, data)

            self.password_list.append(data, front=True)

        elif len([_ for _ in data if _.isdigit()]) == (len(data) - 1):  # float

            if not data in self.suffix:

                self.suffix.insert(0, data)

                self.suffix.insert(0, ''.join(
                    [_ for _ in data if _.isdigit()]))

            self.password_list.append(data, front=True)

            self.password_list.append(''.join(

                [_ for _ in data if _.isdigit()]), front=True)

        elif data.isalpha():  # words

            if not data.lower() in self.words:

                self.words.append(data)

        elif len([_ for _ in data if not _.isalpha() and not _.isdigit()]) == len(data):  # symbol

            if not data in self.suffix:

                self.suffix.insert(0, data)

        else:  # password

            self.password_list.append(data, front=True)

    def generate(self):

        print('root:Создание словаря может занять несколько-секунд\n')
        time.sleep(0.1)
        print('-Пожалуйста подождите')

        for suffix in self.suffix:

            for word in self.words:

                self.password_list.append(word)

                self.password_list.append(f'{word}{suffix}')

                self.password_list.append(f'{suffix}{word}')

                self.password_list.append(f'{suffix}{word}{suffix}')

                for bday in self.b_days:

                    day = bday.split('-')[1]

                    month = bday.split('-')[0]

                    year = bday.split('-')[-1]

                    plain_bday = bday.replace('-', '')

                    self.password_list.append(plain_bday)

                    self.password_list.append(f'{word}{year}')

                    self.password_list.append(f'{word}{year[2:]}')

                    self.password_list.append(f'{word}{plain_bday}')

                    self.password_list.append(f'{day}{word}')

                    self.password_list.append(f'{day[-1]}{word}')

                    self.password_list.append(f'{year}{word}')

                    self.password_list.append(f'{year[2:]}{word}')

                    self.password_list.append(f'{month}{word}')

                    self.password_list.append(f'{month[-1]}{word}')

                    self.password_list.append(f'{month}{day}{word}')

                    self.password_list.append(f'{month[-1]}{day}{word}')

                    self.password_list.append(f'{month}{day[-1]}{word}')

                    self.password_list.append(f'{month[-1]}{day[-1]}{word}')

                    self.password_list.append(f'{day}{month}{word}')

                    self.password_list.append(f'{day[-1]}{month}{word}')

                    self.password_list.append(f'{day}{month[-1]}{word}')

                    self.password_list.append(f'{day[-1]}{month[-1]}{word}')

                    self.password_list.append(f'{month}{day}{word}{year}')

                    self.password_list.append(f'{month}{day}{word}{year[2:]}')

                    self.password_list.append(f'{month[-1]}{day}{word}{year}')

                    self.password_list.append(

                        f'{month[-1]}{day}{word}{year[2:]}')

                    self.password_list.append(f'{month}{day[-1]}{word}{year}')

                    self.password_list.append(

                        f'{month}{day[-1]}{word}{year[2:]}')

                    self.password_list.append(

                        f'{month[-1]}{day[-1]}{word}{year}')

                    self.password_list.append(

                        f'{month[-1]}{day[-1]}{word}{year[2:]}')

                    self.password_list.append(f'{month}{word}{suffix}')

                    self.password_list.append(f'{month[-1]}{word}{suffix}')

                    self.password_list.append(f'{day}{word}{suffix}')

                    self.password_list.append(f'{day[-1]}{word}{suffix}')

                    self.password_list.append(f'{suffix}{word}{month}')

                    self.password_list.append(f'{suffix}{word}{month[-1]}')

                    self.password_list.append(f'{suffix}{word}{day}')

                    self.password_list.append(f'{suffix}{word}{day[-1]}')

                    self.password_list.append(f'{suffix}{word}{year}')

                    self.password_list.append(f'{suffix}{word}{year[2:]}')

        with open('1337_lst.pass', 'wt', encoding='utf-8') as output_file:
            time.sleep(0.1)
            if get_language == 1:
                time.sleep(0.1)
                logo()
                print(f'1337@kali: ~Сгенерированных слов составляет  {len(self.password_list)} возможных паролей ~')
                input(' ~ Нажмите enter чтобы завершить процесс скрипта ~')

            elif get_language == 2:
                time.sleep(0.1)
                logo()
                print(f'1337@kali: ~The words generated are  {len(self.password_list)} possible passwords ~')
                input(' ~ Click enter to complete the script process ~ ')

            for pwd in self.password_list:

                output_file.write(f'{pwd}\n')


if __name__ == '__main__':

    PassGen().get_input()
