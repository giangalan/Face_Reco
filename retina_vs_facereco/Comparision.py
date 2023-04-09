from datetime import datetime

import ImageDraw
from PIL import Image,ImageDraw
img_file1 = 'Wedding.jpg'
img_file2 = 'IT_Fest.jpg'

start = datetime.now()

def retina(img_file):
    from retinaface import RetinaFace
    img = Image.open(img_file)
    draw= ImageDraw.Draw(img)
    resp = RetinaFace.detect_faces(img_file)
    
    c=0
    for item in resp.items():
        top = item[1]['facial_area'][1]
        right = item[1]['facial_area'][2]
        bottom = item[1]['facial_area'][3]
        left = item[1]['facial_area'][0]
        draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))
        # text_width, text_height = draw.textsize(str(c))
        # draw.rectangle(((left, bottom - text_height + 2), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
        # draw.text((left + 6, bottom - text_height + 2), str(c), fill=(255, 255, 255, 255))
        c+=1
    img.show()
    print ('counted ',c,' faces')
    
    

def face_reco(img_file):
    import face_recognition
    img = Image.open(img_file)
    draw= ImageDraw.Draw(img)
    image = face_recognition.load_image_file(img_file)
    image_locations= face_recognition.face_locations(image)
    image_encoding= face_recognition.face_encodings(image, image_locations)

    for (top, right, bottom, left), face_encoding in zip(image_locations, image_encoding):
        # See if the face is a match for the known face(s)

        # If a match was found in known_face_encodings, just use the first one.
        # if True in matches:
        #     first_match_index = matches.index(True)
        #     name = known_face_names[first_match_index]

        # Or instead, use the known face with the smallest distance to the new face

        # Draw a box around the face using the Pillow module
        draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

        # Draw a label with a name below the face
        # text_width, text_height = draw.textsize('j')
        # draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
        # draw.text((left + 6, bottom - text_height - 5),'j', fill=(255, 255, 255, 255))
    img.show()
    print(image_locations)

retina(img_file2)
# face_reco()
end = datetime.now()
print (end-start)