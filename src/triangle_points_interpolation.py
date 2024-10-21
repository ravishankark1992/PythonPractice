import cv2 as cv
import numpy as np

def create_triangle(img):
    

    A = (200,200)
    B = (400,200)
    C = (300,100)

    cv.line(img, A, B, (255,0,0), 2)
    cv.line(img, B, C, (255,0,0), 2)
    cv.line(img, C, A, (255,0,0), 2)

    cv.imshow('Triangle', img)
    cv.waitKey(0)


def create_line(img, P1, P2):

    cv.line(img, P1, P2, (0,0,255), 1)
    cv.waitKey(0)
    return

def main():
    img = np.zeros((512,512,3), np.uint8)
    create_triangle(img)
    P1 = (201, 200)
    P2 = (220, 220)
    create_line(P1, P2)
