# import required package
import cv2

# Load the B&amp;W image
img = cv2.imread('asstes\\o-BLACK-AND-WHITE-PHOTOGRAPHS-facebook.jpg', 0)

# Apply a pseudocolor effect to the B&amp;W image

colorized = cv2.applyColorMap(img, cv2.COLORMAP_JET)

# Save the colorized image
cv2.imwrite('colorized_image.jpg', colorized)