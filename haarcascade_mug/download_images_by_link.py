import urllib.request
import cv2
import numpy as np
import os

# Gets Image Database from a ImageNet URL


def store_raw_images(image_folder, image_url_list, image_starting_index=1):
    image_list = urllib.request.urlopen(image_url_list).read().decode()
    image_index = image_starting_index

    if not os.path.exists(image_folder):
        os.makedirs(image_folder)
        # Split at Next Line
    for image in image_list.split('\n'):
        try:
            print(image)
            print(image_index)
            urllib.request.urlretrieve(
                image, image_folder + '/' + str(image_index) + '.jpg')
            img = cv2.imread(image_folder + '/' +
                             str(image_index) + '.jpg', cv2.IMREAD_GRAYSCALE)
            # should be larger than samples / pos pic
            resized_img = cv2.resize(img, (100, 100))
            cv2.imwrite(image_folder + '/' +
                        str(image_index) + '.jpg', resized_img)
            image_index = image_index + 1
        except Exception as e:
            print(str(e))


def delete_false_images(image_folder, false_image_folder):
    for file_type in [image_folder]:
        for img in os.listdir(file_type):
            for false_image in os.listdir(false_image_folder):
                try:
                    # print(false_image)
                    current_image_path = str(file_type) + '/' + str(img)
                    false_image = cv2.imread(
                        false_image_folder + '/' + str(false_image))
                    image = cv2.imread(current_image_path)

                    if false_image.shape == image.shape and not(np.bitwise_xor(false_image, image).any()):
                        print('shitty image detected')
                        print(current_image_path)
                        os.remove(current_image_path)

                except Exception as e:
                    print(str(e))


def create_path_txt(image_folder):
    for file_type in [image_folder]:
        for img in os.listdir(file_type):
            if file_type == image_folder:
                line = file_type + '/' + img + '\n'
                with open('bg.txt', 'a') as f:
                    f.write(line)
            # elif file_type == 'pos':
            #     line = file_type+'/'+img+' 1 0 0 50 50\n'
            #     with open('info.dat','a') as f:
            #         f.write(line)


if __name__ == '__main__':
    image_folder = 'neg'
    false_image_folder = 'false_images'
    # Pos Images Link
    image_url_list = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n03797390'
    # Neg Images Link
    # images_link = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513'
    # images_link = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n07942152'

    # store_raw_images(image_folder, image_url_list)
    # delete_false_images(image_folder, false_image_folder)
    create_path_txt(image_folder)
