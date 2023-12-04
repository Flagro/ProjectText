from abc import ABC, abstractmethod


archive_formats = ['.zip', '.rar', '.7z']
table_formats = ['.csv', '.xls', '.xlsx', 'xlsb', 'xlsm']
text_formats = ['.txt', '.html', '.xml', '.json', '.md', '.rst', '.tex', '.odt',
                '.docx', '.doc', '.epub', '.fb2', '.djvu', '.rtf', '.pdf']


class Parser(ABC):
    def __init__(self, file_extension, temp_folder_path):
        self._file_extension = file_extension
        self._temp_folder_path = temp_folder_path

    @abstractmethod
    def parse(self, path):
        pass


class ArchiveParser(Parser):
    def parse(self, path):
        # Extract archive and process its contents
        pass


class TableParser(Parser):
    def parse(self, path):
        # Process table file (e.g., CSV, Excel)
        pass


class TextParser(Parser):
    def parse(self, path):
        # Process text file
        pass


def get_file_parser(file_extension, temp_folder_path):
    file_extension = file_extension.lower()
    if file_extension in archive_formats:
        return ArchiveParser(file_extension, temp_folder_path)
    elif file_extension in table_formats:
        return TableParser(file_extension, temp_folder_path)
    elif file_extension in text_formats:
        return TextParser(file_extension, temp_folder_path)
    else:
        raise Exception("Unsupported file format: {}".format(file_extension))
