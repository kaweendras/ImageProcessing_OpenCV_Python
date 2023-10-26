import cv2

# Load the original image
original_image = cv2.imread('original_image.jpg')

# Load the watermark image with transparency (e.g., PNG image with transparency)
watermark = cv2.imread('watermark.png', -1)

# Get the dimensions of the original image
height, width, _ = original_image.shape

# Resize the watermark image to fit the bottom-right corner
watermark_width = int(width / 4)  # Adjust the size as needed
watermark_height = int(watermark_width * watermark.shape[0] / watermark.shape[1])
watermark = cv2.resize(watermark, (watermark_width, watermark_height))

# Create an overlay image
overlay = original_image.copy()

# Blend the watermark with the original image
x_offset = width - watermark_width
y_offset = height - watermark_height
for c in range(0, 3):
    overlay[y_offset:y_offset + watermark_height, x_offset:x_offset + watermark_width, c] = (
        overlay[y_offset:y_offset + watermark_height, x_offset:x_offset + watermark_width, c] * (1 - watermark[:, :, 3] / 255.0) +
        watermark[:, :, c] * (watermark[:, :, 3] / 255.0)
    )

# Update the original image with the watermark
cv2.imwrite('watermarked_image.jpg', overlay)
