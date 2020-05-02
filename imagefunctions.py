import whatimage
import pyheif
import exifread
from PIL import Image

def convFile(filepath):
    with open(filepath, 'rb') as f:
        data = f.read()
        fmt = whatimage.identify_image(data)
        '''
        tags = exifread.process_file(f)

        print(tags)
        print(fmt)
        '''
        if fmt == 'heic':

            heif_file = pyheif.read_heif(data)
            image = Image.frombytes(mode=heif_file.mode, size=heif_file.size, data=heif_file.data)

            if filepath.rfind('/') == -1:
                pathSep = '\\'
            else:
                pathSep = '/'

            file = filepath[filepath.rfind(pathSep)+1: filepath.rfind('.')]
            path = filepath[:filepath.rfind(pathSep)+1]

            image.save( path + file +".jpg", "JPEG")


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