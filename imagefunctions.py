import whatimage
import pyheif
from PIL import Image
import os.path

def convFile(filepath):
    try:
        with open(filepath, 'rb') as f:
            data = f.read()
            fmt = whatimage.identify_image(data)

             

            if fmt == 'heic':
                if filepath.rfind('/') == -1:
                    pathSep = '\\'
                else:
                    pathSep = '/'

                file = filepath[filepath.rfind(pathSep)+1: filepath.rfind('.')]
                path = filepath[:filepath.rfind(pathSep)+1]

                if os.path.isfile(path + file +".jpg"):
                    return 2
                    
                heif_file = pyheif.read_heif(data)
                image = Image.frombytes(mode=heif_file.mode, size=heif_file.size, data=heif_file.data)
                image.save( path + file +".jpg", "JPEG")

                return 1
    except:
        return 0


def checkFile(filepath):
    with open(filepath, 'rb') as f:
        data = f.read()
        fmt = whatimage.identify_image(data)
        if fmt == 'heic':
            return True
        else:
            return False


if __name__ == '__main__':

    #convFile('IMG_8619.HEIC')
    print( checkFile('IMG_8619.HEIC') )