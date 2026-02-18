class Camera:
    def take_photo(self):
        print("Фото сделано.")

class Speaker:
    def play_sound(self):
        print("Воспроизведение звука...")

class VideoBell(Camera, Speaker):
    def ring(self):
        print("Кто-то пришел!")
        self.take_photo() # Используем метод первого родителя
        self.play_sound() # Используем метод второго родителя

# Видеозвонок объединяет камеру и динамик
bell = VideoBell()
bell.ring()