from operator import truediv
import os
import cv2
import numpy as np

#KEYWORDS
# keyPoints -- points in the image that are particularly interesting and stand out in some way
# descriptors -- ways of describing keyPoints

def fingerprint(sampleStr: str):
    sample = cv2.imread(sampleStr, 0)

    ret, sample = cv2.threshold(sample, 127, 255, 0)

    size = np.size(sample)
    skel = np.zeros(sample.shape, np.uint8)

    element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))

    while True:
        open = cv2.morphologyEx(sample, cv2.MORPH_OPEN, element)

        temp = cv2.subtract(sample, open)

        eroded = cv2.erode(sample, element)
        skel = cv2.bitwise_or(skel, temp)

        sample = eroded.copy()

        if cv2.countNonZero(sample)==0:
            break

    cv2.imshow("Skeleton", skel)
    cv2.waitKey(0)

    #variable to check the best possible match 
    bestScore = 0

    filename = "Not found"
    image = None

    keyPointsSample, keyPointsOriginal, matchPoint = None, None, None

    counter = 0
    sizeOfDataSet = 1
    #iterate through entire dataset (320 for testing reasons)
    for file in [file for file in os.listdir("fingers_data_base")][:sizeOfDataSet]:
        # if (counter/sizeOfDataSet * 100) % 10 == 0:
            # print(counter/sizeOfDataSet * 100)
        counter += 1
        
        fingerTest = cv2.imread("fingers_data_base/" + file, 0)
        retFingerTest, fingerTest = cv2.threshold(fingerTest, 127, 255, 0)

        sizeFingImg = np.size(fingerTest)
        skelFingImg = np.zeros(fingerTest.shape, np.uint8)

        elementFingImg = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))

        while True:
            openFingImg = cv2.morphologyEx(fingerTest, cv2.MORPH_OPEN, elementFingImg)

            tempFingImg = cv2.subtract(fingerTest, openFingImg) 

            erodedFingImg = cv2.erode(fingerTest, elementFingImg)
            skelFingImg = cv2.bitwise_or(skelFingImg, tempFingImg)

            fingerTest = erodedFingImg.copy()

            if cv2.countNonZero(fingerTest)==0:
                break
        
        cv2.imshow("Skeleton", skelFingImg)
        cv2.waitKey(0)
        #scale invariant transform that allows us to extract key points and descriptors
        #for individual images
        sift = cv2.SIFT_create()

        keyPoints_skel, descriptors_skel = sift.detectAndCompute(skel, None)
        keyPoints_Original, descriptors_Original = sift.detectAndCompute(skelFingImg, None)

        matches = cv2.FlannBasedMatcher({'algorithm': 1, 'trees': 10}, 
                                        {}).knnMatch(descriptors_skel, descriptors_Original, k=2)
                                        

        matchPoints = []

        # change required distance to lower in order to increase accuracy
        for p, q in matches:
            if p.distance < 0.1 * q.distance:
                matchPoints.append(p)

        keypoints = 0
        if len(keyPoints_skel) < len(keyPoints_Original):
            keypoints = len(keyPoints_skel)
        else:
            keypoints = len(keyPoints_Original)

        if len(matchPoints) / keypoints * 100 > bestScore:
            bestScore = len(matchPoints) / keypoints * 100
            filename = file
            image = skelFingImg
            keyPointsSample, keyPointsOriginal, matchPoint = keyPoints_skel, keyPoints_Original, matchPoints

    scoreToUnlock = 60.00
    print("Best match is: " + filename)
    print("Score: " + str(round(bestScore, 2)) + " Required: " + str(scoreToUnlock))

    unlockedFlag = False
    if (bestScore > scoreToUnlock):
        unlockedFlag = True
    else:
        unlockedFlag = False

    if bestScore != 0:
        result = cv2.drawMatches(skel, keyPointsSample, image, keyPointsOriginal, matchPoint[0::20], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
        result = cv2.resize(result, None, fx=1.0, fy=1.0)
        cv2.imshow("Result", result)
        cv2.waitKey()
        cv2.destroyAllWindows()
    else:
        print("No match found")

    return unlockedFlag, filename


