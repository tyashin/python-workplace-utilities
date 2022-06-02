import os

from PIL import Image

if __name__ == '__main__':
    orig_img_dir = os.path.join(os.getcwd(), 'orig_img')
    max_size = int(input('Enter max size width/height of image: '))

    for root, dirs, files in os.walk(orig_img_dir):
        for file in files:
            try:
                if file.endswith('.jpg') or file.endswith('.png'):
                    img_obj = Image.open(os.path.join(root, file))
                    width, height = img_obj.size
                    if width > height:
                        new_width = max_size
                        new_height = int(height * max_size / width)
                    else:
                        new_height = max_size
                        new_width = int(width * max_size / height)

                    img_obj = img_obj.resize((new_width, new_height), Image.LANCZOS)
                    img_obj.save(os.path.join(root, file))
                    img_obj.close()
            except IOError:
                print("cannot convert ", file)

    print('Done!')
