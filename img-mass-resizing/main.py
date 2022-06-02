import os

from PIL import Image

if __name__ == '__main__':
    orig_img_dir = os.path.join(os.getcwd(), 'orig_img')
    resized_img_dir = os.path.join(os.getcwd(), 'resized_img')
    max_size = int(input('Enter max size width/height of image: '))

    for img in os.listdir(orig_img_dir):
        try:
            img_path = os.path.join(orig_img_dir, img)
            img_obj = Image.open(img_path)
            width, height = img_obj.size
            if width > height:
                new_width = max_size
                new_height = int(height * max_size / width)
            else:
                new_height = max_size
                new_width = int(width * max_size / height)
            img_obj = img_obj.resize((new_width, new_height), Image.LANCZOS)
            img_obj.save(os.path.join(resized_img_dir, img))
        except IOError:
            print("cannot convert", img_path)
