from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication , QWidget ,QPushButton, QLabel,QListWidget,QLineEdit,QTextEdit,QInputDialog,QHBoxLayout,QVBoxLayout,)
import json
app = QApplication([])
notes_win = QWidget()
notes_win.setWindowTitle('умные заметки')
notes_win.resize(900,600)
list_notes = QListWidget()
list_notes_label = QLabel('список заметок')
button_note_create = QPushButton('Создать заметку')
button_note_del = QPushButton('Удалить заметку')
button_note_save =QPushButton('сохранить заметку')
field_tag= QLineEdit('')
field_tag.setPlaceholderText('Введите тег ....')
field_text = QTextEdit()
button_note_add = QPushButton('добавить к заметке')
button_tag_add = QPushButton('добавить к заметке')
button_tag_serch = QPushButton('Искать заметку по тегу')
button_note_del = QPushButton('Открепить от заметки')
button_note_serch = QPushButton('Искать заметку по тегу')
button_tag_del = QPushButton('добавить к тегу')
list_tags = QListWidget()
list_tags_label = QLabel('Список тегов')
layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)
col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)
row_1 = QHBoxLayout()
row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)
col_2.addLayout(row_1)
col_2.addLayout(row_2)
col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)
row_3 = QHBoxLayout()
row_3.addWidget(button_tag_add)
row_3.addWidget(field_tag)
row_3 = QHBoxLayout()
row_3.addWidget(button_tag_add)
row_3.addWidget(button_tag_del)
row_4 = QHBoxLayout()
row_4.addWidget(button_tag_serch)

col_2.addLayout(row_2)
col_2.addLayout(row_4)
layout_notes.addLayout(col_1,  stretch= 2)
layout_notes.addLayout(col_2, stretch= 1)
notes_win.setLayout(layout_notes)



def add_note():
    note_name, ok =QInputDialog.getText(notes_win, 'Добавить заметку','Название заметки')
    if ok and note_name != '':
        notes[note_name] = {'текст': '','теги':[]}
        list_notes.addItem(note_name)
        list_tags.addItems(notes[note_name]['теги'])
        print(notes)
def show_note():
    key = list_notes.selectedIndexes
    print(key)
    field_text.setText(notes[key]['текст'])
    list_tags.clear()
    list_tags.addItem(notes[key]['теги'])
def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key]['текст'] = field_text.toPlainText()
        with open ('notes_data.json','w') as file :
            json.dump(notes , file , sort_keys=True, ensure_ascii=False)
        print('notes')
    else:
        print('Заметка для сохранения не выбрана!')
def del_note ():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        del notes[key]
        list_notes.clear()
        list_tags.clear()
        field_text.clear()
        list_notes.addItems(notes)
        with open('notes_data.json','w') as file:
            json.dump(notes,file , sort_keys= True , ensure_ascii = False)
        print(notes)
    else:
        print('заметка для удаления не выбрана!')
def add_tag ():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = field_tag.text()
        if not tag in notes[key]['теги']:
            notes[key]['теги'].append(tag)
            list_tags.addItem(tag)
            field_tag.clear()
        with open ('notes_data.json','w') as file:
            json.dump(notes , file, sort_keys = True , ensure_ascii = False)
        print(notes)
    else:
        print('Заметка для добавления тега не выбрана!')
def del_tag ():
    if list_tags.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = list_tags.selectedItems()[0].text()
        notes[key]['теги'].remove(tag)
        list_tags.clear()
        list_tags.addItems(notes[key]['теги'])
        with open('notes_data.json','w') as file:
            json.dump(notes , file, sort_keys = True , ensure_ascii = False)
    else:
        print('Тег для удаления не выбран!')































notes_win.show()
app.exec_()