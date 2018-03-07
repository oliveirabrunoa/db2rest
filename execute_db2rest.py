from DB2Rest.db2rest import LoadModelClasses

if __name__ == '__main__':
    CONFIG_FILE = 'DB2Rest/to_generate_models.json'
    load_models = LoadModelClasses(CONFIG_FILE)
    load_models.generate_file()
