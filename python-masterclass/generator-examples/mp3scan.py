import os
import fnmatch
import id3reader_p3 as id3reader


def find_music(start, extension):
    for path, directories, files in os.walk(start):
        for file in fnmatch.filter(files, f'*.{extension}'):
            absolute_path = os.path.abspath(path)  # create absolute path
            yield os.path.join(absolute_path, file)  # use it in yielded values


error_list = []

for f in find_music('D:\Music', 'mp3'):
    try:
        id3r = id3reader.Reader(f)
        print(
            f"Artist: {id3r.get_value('performer')}, Album: {id3r.get_value('album')}, "
            f"Track: {id3r.get_value('track')}, Song: {id3r.get_value('title')}")
    except:
        error_list.append(f)

for error_file in error_list:
    print(error_file)
