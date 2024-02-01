import eel

# Указываем путь к HTML-файлу
eel.init('web')

# Определяем функцию обратного вызова для кнопки
@eel.expose
def my_python_function(param):
    print(f"Button clicked with parameter: {param}")

# Запускаем Eel с указанием пути к HTML-файлу
eel.start('main.html', size=(300, 200))
