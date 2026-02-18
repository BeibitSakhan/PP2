class ChatRoom:
    history = []  # Общая история сообщений

    def send_message(self, user, text):
        entry = f"{user}: {text}"
        ChatRoom.history.append(entry)

# Все пользователи пишут в один и тот же список history