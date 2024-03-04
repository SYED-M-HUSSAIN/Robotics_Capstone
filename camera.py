import cv2

# Create a VideoCapture object to capture video from the default camera (index 0)
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Display the frame in a window
    cv2.imshow('Camera', frame)

    # Wait for a key press (1 millisecond)
    key = cv2.waitKey(1)

    # Check if the 'q' key was pressed, if so, break out of the loop
    if key == ord('q'):
        break

# Release the camera
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
