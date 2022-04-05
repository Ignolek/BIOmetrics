import sys
import cv2 as cv


# webhook test

def main() -> None:
    print("Hello world")

    img = cv.imread('Finger/testFinger.jpg')
    cv.imshow('Default', img)

    # OpenCV functions that may be useful in the future
    
    # Converting to grayscale
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('Gray', gray)

    # Blur
    blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
    cv.imshow('Blur', blur)

    # Edge Cascade
    edges = cv.Canny(img, 50, 50)
    cv.imshow('Canny Edges', edges)

    # Dilatation
    dilated = cv.dilate(edges, (7, 7), iterations = 3)
    cv.imshow('Dilated', dilated)

    # Erodation
    eroded = cv.erode(dilated, (3, 3), iterations = 1)
    cv.imshow('Eroded', eroded)

    cv.waitKey(0)

    sys.exit(0)


if __name__ == "__main__":
    main()