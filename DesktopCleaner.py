import os
import time
import filecmp

# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
# source = ['C:\\Users\\Zack\\Desktop']

source = 'C:\\Users\\Zack\\Desktop'
sourcelist = os.listdir(source)
# Заметьте, что для имён, содержащих пробелы, необходимо использовать
# двойные кавычки внутри строки.
# 2. Резервные копии должны храниться в основном каталоге резерва.
target_dir = 'C:\\my life my rules\\Personal files\\from desktop' # Подставьте тот путь, который вы будете использовать.

# 3. Файлы помещаются в zip-архив.
# 4. Текущая дата служит именем подкаталога в основном каталоге
today = target_dir + os.sep + time.strftime('%Y%m%d')
# Текущее время служит именем zip-архива


target = today
for symbols in target:
	if symbols==" ":
		target='"'+target+'"'
		print("В таргете были пробелы, но мы это поправили")
		break

# Создаём каталог, если его ещё нет
if not os.path.exists(today):
	os.mkdir(today) # создание каталога
print('Каталог успешно создан', today)


source_allfiles=source+"\\*.*"
print(source_allfiles + " " + target)

copy_command = "COPY {0} {1}".format(source_allfiles,target)
# copy_command = "COPY {0} {1}".format(" ".join(sourcelist),target)
print (copy_command)

# chdir_command = "chdir {0}".format(source_allfiles)
# os.system(chdir_command)


#__________________________________________
# Проверка идентичности файлов
# filename="123.txt"
# source_backup_file=source+os.sep+filename
# target_backup_file=target[1:-1]+os.sep+filename+''
# print('source={0} \n target={1}'.format(source_backup_file,target_backup_file))

# cmp сравнивает при помощи os.stat
# if filecmp.cmp(source_backup_file,target_backup_file):
# 	print("Файлы равны")
# else:
# 	print("Файлы не равны")
#__________________________________________




#_____________
# Запускаем копирование файлов
# if os.system(copy_command) == 0:
# 	print('Файлы скопированы в ', target)
# 	os.system("del /Q {0}".format(source_allfiles))
# else:
# 	print('Скопировать файлы НЕ УДАЛОСЬ')


