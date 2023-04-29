#начни тут создавать приложение с умными заметками
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QRadioButton, QGroupBox, QButtonGroup, QLineEdit, QTextEdit, QListWidget, QInputDialog


import json
notes = {
    'Добро пожаловать!' : {
        'текст' : 'Это самое лучшее приложение заметок в мире!',
        'теги' : ['добро', 'инструкция']
    }
}



def add_note():
    note_name, ok = QInputDialog.getText(window, 'Добавить заметку', 'Название заметки')
    if ok and note_name != '':
        notes[note_name] = {'текст' : '', 'теги' : []}
        list_notes.addItem(note_name)
        list_tags.addItems(notes[note_name]['теги'])        

def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key]['текст'] = text_field.toPlainText()
        with open('notes_data.json', 'w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)

def del_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        del notes[key]
        list_notes.clear()
        list_tags.clear()
        text_field.clear()
        list_notes.addItems(notes)
        with open('notes_data.json', 'w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)

def add_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = text_line.text()
        if not tag in notes[key]['теги']:
            notes[key]['теги'].append(tag)
            list_tags.addItem(tag)
            text_line.clear()
            with open('notes_data.json', 'w') as file:
                json.dump(notes, file, sort_keys=True, ensure_ascii=False)


def del_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = text_line.text()
        notes[key]['теги'].remove(tag)
        list_tags.removeItem(tag)
        text_line.clear()
        with open('notes_data.json', 'w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)


with open('notes_data.json', 'w') as file:
    json.dump(notes, file)


app = QApplication([])

window = QWidget()
window.setWindowTitle('Умные заметки')

text_field = QTextEdit()
text_field.setText('Тут можно что-то написать')

text1 = QLabel('Список заметок')

h_layout1 = QHBoxLayout()
text1 = QLabel('Список заметок')
h_layout1.addWidget(text1)

h_layout2 = QHBoxLayout()
list_notes = QListWidget()
h_layout2.addWidget(list_notes)

h_layout3 = QHBoxLayout()
btn_createNote = QPushButton('Создать заметку')
btn_deleteNote = QPushButton('Удалить заметку')
h_layout3.addWidget(btn_createNote)
h_layout3.addWidget(btn_deleteNote)


h_layout4 = QHBoxLayout()
btn_saveNote = QPushButton('Сохранить заметку')
h_layout4.addWidget(btn_saveNote)

h_layout5 = QHBoxLayout()
text2 = QLabel('Список тегов')
h_layout5.addWidget(text2)


h_layout6 = QHBoxLayout()
list_tags = QListWidget()
h_layout6.addWidget(list_tags)

h_layout7 = QHBoxLayout()
text_line = QLineEdit()
text_line.setPlaceholderText('Введите тег....')
h_layout7.addWidget(text_line)


h_layout8 = QHBoxLayout()
btn_addNote = QPushButton('Добавить к заметке')
btn_rewoundNote = QPushButton('Открепить от заметку')
h_layout8.addWidget(btn_addNote)
h_layout8.addWidget(btn_rewoundNote)


h_layout9 = QHBoxLayout()
btn_findTag = QPushButton('Искать заметки по тегу')
h_layout9.addWidget(btn_findTag)


v_layout1 = QVBoxLayout()
v_layout1.addWidget(text_field)
v_layout2 = QVBoxLayout()
v_layout2.addLayout(h_layout1)
v_layout2.addLayout(h_layout2)
v_layout2.addLayout(h_layout3)
v_layout2.addLayout(h_layout4)
v_layout2.addLayout(h_layout5)
v_layout2.addLayout(h_layout6)
v_layout2.addLayout(h_layout7)
v_layout2.addLayout(h_layout8)
v_layout2.addLayout(h_layout9)

main_layout = QHBoxLayout()
main_layout.addLayout(v_layout1)
main_layout.addLayout(v_layout2)

window.setLayout(main_layout)

def show_note():
    key = list_notes.selectedItems()[0].text()
    text_field.setText(notes[key]['текст'])
    list_tags.clear()
    list_tags.addItems(notes[key]['теги'])
    
list_notes.itemClicked.connect(show_note)

btn_createNote.clicked.connect(add_note)
btn_saveNote.clicked.connect(save_note)
btn_deleteNote.clicked.connect(del_note)
btn_addNote.clicked.connect(add_tag)
btn_rewoundNote.clicked.connect(del_tag)

with open ('notes_data.json', 'r') as file:
    notes = json.load(file)
list_notes.addItems(notes)
 
window.show()
app.exec()
