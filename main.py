import sys
import cv2 as cv


# webhook test

def main() -> None:
    print("Hello world")
    img = cv.imread('Finger/testFinger.jpg')

    cv.imshow('Default', img)

    # Converting to grayscale
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('Gray', gray)

    cv.waitKey(0)

    sys.exit(0)


if __name__ == "__main__":
    main()