import os
import cv2
import numpy as np
from keras.preprocessing.image import ImageDataGenerator


def load_images_from_folder(folder_path, target_size=(224, 224)):
    images = []
    labels = []
    class_names = os.listdir(folder_path)

    for label in class_names:
        class_folder = os.path.join(folder_path, label)
        for filename in os.listdir(class_folder):
            img_path = os.path.join(class_folder, filename)
            img = cv2.imread(img_path)
            if img is not None:
                img = cv2.resize(img, target_size)
                images.append(img)
                labels.append(label)
    
    return np.array(images), np.array(labels)

def augment_images(X, y, augment_size=1000):
    datagen = ImageDataGenerator(
        rotation_range=20,
        width_shift_range=0.1,
        height_shift_range=0.1,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest'
    )

    datagen.fit(X)
    aug_iter = datagen.flow(X, y, batch_size=augment_size, shuffle=True)
    X_aug, y_aug = next(aug_iter)
    
    return X_aug, y_aug
