#a
from PIL import Image
import numpy as np

def img_to_array(path, output_file_rgb = "img_dogo.txt",output_file_grey = "grey_dogo.txt"):
    img = Image.open(path)
    img_array = np.array(img)
    if img.mode == 'RGB' :
        img_array_flattened = img_array.flatten()
        np.savetxt(output_file_rgb, img_array_flattened, fmt='%d')

        return img_array, img_array.shape, 'RGB'
    
    elif img.mode == 'L':
        img_array_flattened = img_array.flatten()
        np.savetxt(output_file_grey, img_array_flattened, fmt='%d')

        return img_array, img_array.shape, 'Grayscale'


img_array, original_shape, img_type = img_to_array('/Users/pranavchawla/Downloads/Original_Doge_meme.jpg')



#b
import numpy as np
from PIL import Image

def load_array_from_txt(file_path, original_shape, img_type):
    loaded_array = np.loadtxt(file_path, dtype=int)
    
    reshaped_array = loaded_array.reshape(original_shape)
    
    print(f"Loaded array shape: {reshaped_array.shape}")
    return reshaped_array

if img_type == 'RGB':
    img_array_loaded = load_array_from_txt("/Users/pranavchawla/Desktop/assignment1/img_dogo.txt", original_shape, img_type)

elif img_type == 'Grayscale':
    img_array_loaded = load_array_from_txt("grey_dogo.txt", original_shape, img_type)

img = Image.fromarray(img_array_loaded.astype('uint8'), mode=img_type)
img.show()









