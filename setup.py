# setup a talk from template

from os import path
from shutil import copyfile, copytree

template_dir = path.dirname(path.realpath(__file__))
talk_dir = template_dir + "/.."

print('Setting up the talk\n')

# copy index
template_index = template_dir + "/index.html"
talk_index = talk_dir + "/index.html"
if path.exists(talk_index):
    print(' - Talk index already exists')
else:
    copyfile(template_index, talk_index)
    print(' - Talk index created')

# copy slides
template_slides = template_dir + "/slides"
talk_slides = talk_dir + "/slides"
if path.exists(talk_slides):
    print(' - Talk slides already exists')
else:
    copytree(template_slides, talk_slides)
    print(' - Talk slides created')

# copy images
template_images = template_dir + "/images"
talk_images = talk_dir + "/images"
if path.exists(talk_images):
    print(' - Talk images already exists')
else:
    copytree(template_images, talk_images)
    print(' - Talk images created')

# copy talk.css
template_css = template_dir + "/css/talk.css"
talk_css = talk_dir + "/talk.css"
if path.exists(talk_css):
    print(' - Talk css already exists')
else:
    copyfile(template_css, talk_css)
    print(' - Talk css created')

print ('\nComplete')
