import os

dir_path = "static\media"

file_list = os.listdir(dir_path)
images = [i for i in file_list]

keys = []

for number in range(len(file_list)):
    new_name = 'string' + str(number)
    keys.append(new_name)

print(keys)
print(images)

pathmedia = r'static/media/'

print(pathmedia)

images = [pathmedia + filename for filename in images]

image_dict = dict(zip(keys, images))

print(image_dict)