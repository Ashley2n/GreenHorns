import cv2
import numpy as np

def analyze_image(image_path):
    """Basic analysis of color and brightness"""
    img = cv2.imread(image_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Compute average color
    avg_color = img_rgb.mean(axis=(0, 1))  # [R, G, B]
    avg_color_hex = '#%02x%02x%02x' % tuple(avg_color.astype(int))

    # Brightness (average pixel intensity)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    brightness = np.mean(gray)

    # Detect "overcooked" areas (very dark pixels)
    dark_pixels = np.sum(gray < 50)
    total_pixels = gray.size
    overcooked_percent = (dark_pixels / total_pixels) * 100

    result = {
        "average_color": avg_color_hex,
        "brightness": round(brightness, 2),
        "overcooked_percent": round(overcooked_percent, 2)
    }

    return result


def compare_images(img1_path, img2_path):
    """Compare two images using histogram similarity"""
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)

    # Convert to HSV for color-based comparison
    hsv1 = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
    hsv2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

    hist1 = cv2.calcHist([hsv1], [0, 1], None, [50, 60], [0, 180, 0, 256])
    hist2 = cv2.calcHist([hsv2], [0, 1], None, [50, 60], [0, 180, 0, 256])

    cv2.normalize(hist1, hist1, 0, 1, cv2.NORM_MINMAX)
    cv2.normalize(hist2, hist2, 0, 1, cv2.NORM_MINMAX)

    similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
    return round(similarity * 100, 2)
