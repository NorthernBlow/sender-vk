import vk, random, time

# Функция парсера файла с аккаунтами (надо дописать)
def get_accounts(filename="accounts.txt"):
    with open(filename) as file:
        b = []
        for line in file:
            b.append(line[0:len(line) - 1])
    return b


if __name__ == "__main__":
    api = vk.API(
            access_token='',
            v='5.131',
            proxy='' # proxy settings
            )
    #print(api.users.get(user_ids=1))
    #print(get_accounts())

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Начинаю рассылку. Жди...")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    b = [] # сюда сохраняем id которым уже была отправлена рассылка
    limit = 19 # ограничение сообщений для рассылки (по умолчанию 20)

    with open("users_success.txt") as users_success_file:
        for uid_skip in users_success_file:
            b.append(uid_skip[0:len(uid_skip) - 1])

    print("== Загружаю базу пользователей которым уже отправлялась рассылка")
    #time.sleep(30)

    with open("users_db.txt") as file:
        for uid in file:
            try:
                b.index(uid[0:len(uid) - 1])
                print("- Пропущен id: " + uid)
            except ValueError:
                if limit > 0:
                    time.sleep(120)
                    try:
                        api.messages.send(
                                random_id=random.randint(1, 9999),
                                peer_id=uid[9:len(uid) - 1],
                                message="Привет!\n\nКрутые, вкусные одноразки в Белгороде, — от 300 рублей!\nЕсли интересно, напиши мне что-нибудь.\nЗай, не грусти 😘"
                                )
                        with open("users_success.txt", "a") as users_success_file:
                            users_success_file.write(str(uid))
                        limit = limit - 1
                        print("+ Сообщение " + limit + " отправлено для id: " + uid)
                        #time.sleep(300)
                    except Exception as e:
                        print(f"х Не могу отправить сообщение:\n>>> {e}")
                else:
                    print("== Достигнут лимит отправки сообщений")

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Готово. Всем спасибо. Все свободны.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
