def read_file(file_name: str) -> list:
	data = []
	with open(file_name, 'rt', encoding='utf-8') as file:
		temp = file.readlines()
		data.append(file_name)
		data.append(str(len(temp)))
		data.append(''.join(temp))
	return data


def sort_files_by_len(file_name_list: list) -> list:
	data_storage = []

	for file in file_name_list:
		data_storage.append(read_file(file))
	data_storage.sort(key=lambda e: e[1])

	for id_ in range(0, len(data_storage)):
		data_storage[id_] = '\n'.join(data_storage[id_])
	return data_storage

def writing_to_file(file_name: str, data_to_write: list):
	with open(file_name, 'wt', encoding='utf-8') as file:
		file.write('\n'.join(data_to_write))


writing_to_file('result.txt',sort_files_by_len(['1.txt', '2.txt', '3.txt']))