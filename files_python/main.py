# Запис даних у файл
def write_to_file(filename): 
  with open(filename, 'w') as file:
    while True:
      data =  input("Введіть дані для запису (або 'q' для виходу): ")
      if data == 'q':
        break
      file.write(data + '\n')

# Читання даних з файлу
def read_from_file(filename): 
  with open(filename, 'r') as file:
    content = file.read()
    print("Вміст файлу:")
    print(content)

# Головна функція
def main(): 
  filename = input("Введіть ім'я файлу: ")
  # Запис даних у файл 
  write_to_file(filename) 
  # Виведення даних з файлу 
  read_from_file(filename)

# Виклик головної функції 
main()