import os


# seperate folder
def prj_dir(directory):
    if not os.path.exists(directory):
        print('creating a dir' + directory)
        os.makedirs(directory)

# creating queqed files and alredy crawled ones


def dat_files(prj_nm, base_url):
    queued = prj_nm + '/queue.txt'
    crawled = prj_nm + '/crawled.txt'
    if not os.path.isfile(queued):
        write_file(queued, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

# creating a new file and writing to it and also appending data and also  in python


def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()


def append_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


def delete_file(path):
    with open(path, 'w'):
        pass


def file_set(file_name):
    res = set()
    with open(file_name, 'rt') as f:
        for line in f:
            res.add(line.replace('\n', ''))
        return res
# read through the set


def set_file(lin, file):
    delete_file(file)
    for link in sorted(lin):
        append_file(file, link)
