import os,json,base64,time

def json_reader(file_path=''):
    path = os.getcwd() + file_path
    file_name = os.path.basename(path)
    
    try:
        with open(path, 'r') as f:
            if file_name.endswith(".json"):
                return json.load(f), file_name.split('.')[0]
            else:
                return f.read(), file_name.split('.')[0]
    except Exception as e:
        return False, e

def execute_value(files_require):
    value_have = {}
    value_prefix = 'Json_'
    backslash_char = "\\"
    files_first = files_require[0].split(backslash_char)[2]
    
    count = 0
    for file_path in files_require:
        f = file_path.split(backslash_char)[2]
        file_read, base_name = json_reader(file_path)
        if file_read != False:
            count += 1
            val = f"{value_prefix}{base_name} = file_read"
            exec(val)
            if file_path.split(backslash_char)[2] == files_first:
                files_first = 'done'
            if files_first == 'done':
                custom_console = eval(f'{value_prefix}en')
                color_esc_0 = f'\x1b[38;5;{custom_console["Notification"]["Info"]["color"]}'
                header_content = custom_console["IconMessages"]["1"] % (f'{color_esc_0}{custom_console["Notification"]["Info"]["text"]}\x1b[0m')
                message = f'\x1b[38;5;{custom_console["Notification"]["Info"]["color"]}'+(custom_console["Installer"]["LoaderJson"]["Successfully"] % (f))+'\x1b[0m'
                print(f'{header_content}{message}')
            else:
                print(f'{file_path} read done!')
            code = base64.b64encode(json.dumps(eval(f'{value_prefix}{base_name}')).encode()).decode()
            value_have.update({f"{value_prefix}{base_name}": code})
        else:
            if files_first == 'done':
                if file_path.split(backslash_char)[2] != 'en':
                    custom_console = eval(f'{value_prefix}en')
                    color_esc_0 = f'\x1b[38;5;{custom_console["Notification"]["Alert"]["color"]}'
                    header_content = custom_console['IconMessages']['1'] % (f'{color_esc_0}{custom_console["Notification"]["Alert"]["text"]}\x1b[0m')
                    message = f'\x1b[38;5;{custom_console["Notification"]["Alert"]["color"]}'+(custom_console["Installer"]["LoaderJson"]["Failed"] % (f, base_name))+'\x1b[0m'
                    print(f'{header_content}{message}')
            else:
                print(f'{file_path} failed read!')
        time.sleep(0.1)
    return value_have

def json_decoder_base64(name,json_val):
    return json.loads(base64.b64decode(json_val[name])).decode()

files_requirement = ['\\languages\\en.json', '\\languages\\th.json', '\\settings\\menu.json']
json_storage = execute_value(files_require=files_requirement)
list_value = json_storage.keys()
