# Jack Morris 05/19/16

import cv2
from faceswap import create_face_swap

def output_swapped_image(image):
  cv2.imwrite('output.jpg', image)
  
def main():
  # get initial image
  # base_image = load_first_image()
  base_image = 'trump.jpg'
  # get image for face swap
  face_image = 'obama.jpg'
  # face_image = load_second_image()
  # swap faces
  swap_image = create_face_swap(base_image, face_image)
  # output image
  output_swapped_image(swap_image)

main()