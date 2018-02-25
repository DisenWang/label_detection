


def run_quickstart():

    import io
    import os


    from os import listdir
    from os.path import isfile, join
    import numpy

    # Imports the Google Cloud client library
    # [START migration_import]
    from google.cloud import vision
    from google.cloud.vision import types
    # [END migration_import]
    # Create the list

    label_list = []

    # Start the loop
    for i in xrange(1,10):
    # Instantiates a client
    # [START migration_client]
        client = vision.ImageAnnotatorClient()
    # [END migration_client]
    #read all images
        mypath='/Users/disenwang/Github_stuff/picture_analysis/img'

        onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]

        images = numpy.empty(len(onlyfiles), dtype=object)
    # The name of the image file to annotate
        file_name = os.path.join(
            os.path.dirname(__file__),
            '/Users/disenwang/Github_stuff/picture_analysis/img/%s') % (i)

    # Loads the image into memory
        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

            image = types.Image(content=content)

    # Performs label detection on the image file
        response = client.label_detection(image=image)
        labels = response.label_annotations

        print('Labels:')
        for label in labels:
            print(label.description)
    # [END vision_quickstart]


if __name__ == '__main__':
    run_quickstart()
