from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

group = {1: "синий",
         2: "зеленый",
         3: "красный"}

books = [
    {"title": "Мастер и Маргарита",
     "author": "Булгаков М.А.",
     "price": 581.50},
    {"title": "Белая гвардия",
     "author": "Булгаков М.А.",
     "price": 600.00},
    {"title": "Война и мир",
     "author": "Толстой Л.Н.",
     "price": 899.99},
    {"title": "Анна Каренина",
     "author": "Толстой Л.Н.",
     "price": 450.10},
    {"title": "Игрок",
     "author": "Достоевский Ф.М.",
     "price": 234.55}
]

result_html = template.render(name="color", list=group, num=2, # задание 1
                              list2=books, start=1, finish=5)  # задание 2

# создадим файл для HTML-страницы
f = open('test.html', 'w', encoding ='utf-8-sig')

# выводим сгенерированную страницу в файл
f.write(result_html)

f.close()




