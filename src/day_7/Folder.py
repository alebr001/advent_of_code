class Folder:
    def __init__(self, own_name, sub_folders, files, parent=None, total_file_size=0):
        self.own_name = own_name
        self.sub_folders = sub_folders
        self.files = files
        self.total_file_size = total_file_size
        self.parent = parent

    ##########
    # SETTERS
    ##########

    def add_folder(self, param):
        self.sub_folders.append(param)

    def add_file(self, row):
        self.files.append(row)

    def add_size_group_total(self, size):
        self.total_file_size += size

    ##########
    # GETTERS
    ##########

    def get_total_file_size(self):
        return self.total_file_size

    def get_own_name(self):
        return self.own_name

    def get_parent(self):
        return self.parent

    def get_folder(self, folder_name):
        for folder in self.sub_folders:
            if folder.own_name == folder_name:
                return folder
        return self

    def get_folder_names(self):
        temp = []
        for folder in self.sub_folders:
            temp.append(folder.own_name)
        return temp

    def get_sub_folders(self):
        return self.sub_folders
