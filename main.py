import cv2
import pytesseract

# Load the image
image = cv2.imread("document.jpg")

# Preprocess the image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# Perform OCR
text = pytesseract.image_to_string(thresh, lang="eng")

# Save the extracted text
with open("document_text.txt", "w") as f:
    f.write(text)

print("OCR Result:")
print(text)
