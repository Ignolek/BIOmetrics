import os
import cv2

#KEYWORDS
# keyPoints -- points in the image that are particularly interesting and stand out in some way
# descriptors -- ways of describing keyPoints

#load image to check
sample = cv2.imread("102_3 (3)_painted.tif")


#variable to check the best possible match 
bestScore = 0

filename = None
image = None

keyPointsSample, keyPointsOriginal, matchPoint = None, None, None

counter = 0
#iterate through entire dataset (320 for testing reasons)
for file in [file for file in os.listdir("fingers_data_base")][:320]:
    if counter % 10 == 0:
        print(counter)
    counter += 1
    fingerprintImage = cv2.imread("fingers_data_base/" + file)
    #scale invariant transform that allows us to extract key points and descriptors
    #for individual images
    sift = cv2.SIFT_create()

    keyPoints_Sample, descriptors_Sample = sift.detectAndCompute(sample, None)
    keyPoints_Original, descriptors_Original = sift.detectAndCompute(fingerprintImage, None)

    #Comment how does it work
    matches = cv2.FlannBasedMatcher({'algorithm': 1, 'trees': 10}, 
                                    {}).knnMatch(descriptors_Sample, descriptors_Original, k=2)

    matchPoints = []

    for p, q in matches:
        if p.distance < 0.1 * q.distance:
            matchPoints.append(p)

    keypoints = 0
    if len(keyPoints_Sample) < len(keyPoints_Original):
        keypoints = len(keyPoints_Sample)
    else:
        keypoints = len(keyPoints_Original)

    if len(matchPoints) / keypoints * 100 > bestScore:
        bestScore = len(matchPoints) / keypoints * 100
        filename = file
        image = fingerprintImage
        keyPointsSample, keyPointsOriginal, matchPoint = keyPoints_Sample, keyPoints_Original, matchPoints

print("Best match is: " + filename)
print("Score: " + str(bestScore))
    
result = cv2.drawMatches(sample, keyPointsSample, image, keyPointsOriginal, matchPoint, None)
result = cv2.resize(result, None, fx=1.0, fy=1.0)
cv2.imshow("Result", result)
cv2.waitKey()
cv2.destroyAllWindows()
