import os

#Each website you crawl is a separate project (folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project folder for ' + directory)
        os.makedirs(directory)

#Create queue and crawled files (if not created)
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

#Create a new file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

#Add data to existing file
def append_file(path, data):
    with open(path, 'a') as f:
        f.write(data + '\n')

#Delete the contents of a file
def clear_file(path):
    with open(path, 'w'):
        pass

#Read a file and convert each line to set items
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results

#Iterate through a set, each item will be a new line in the file
def set_to_file(links, file):
    clear_file(file)
    for link in sorted(links):
        append_file(file, link)

create_project_dir('gebouw-t')
create_data_files('gebouw-t', 'https://gebouw-t.nl/')