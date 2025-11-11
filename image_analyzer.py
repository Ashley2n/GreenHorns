import cv2
import numpy as np
import requests

def buffer_file(file):
    return np.frombuffer(file.read(), np.uint8)

def decode_file(file_bytes):
    return cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

def analyze_image(img1):
    """Analyze uploaded image directly from memory (no saving)"""
    # Read the uploaded file bytes
    # file_bytes = np.frombuffer(img1_file.read(), np.uint8)

    img = cv2.imdecode(img1, cv2.IMREAD_COLOR)
    if img is None:
        raise ValueError("Image could not be decoded. Check the uploaded file format.")

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

def compare_images(img1, img2_dict):
    """Compare uploaded image to API image"""


    # Fetch API image
    response = requests.get(img2_dict['image_url'])
    if response.status_code != 200:
        raise ValueError(f"Error: Could not fetch image from {img2_dict['image_url']}")


    img2 = cv2.imdecode(np.frombuffer(response.content, np.uint8), cv2.IMREAD_COLOR)
    img1_decoded = cv2.imdecode(img1, cv2.IMREAD_COLOR)


    if img2 is None or img1_decoded is None:
        raise ValueError("Error: Could not decode both images.")

    # Convert both to HSV and compare color histograms
    hsv1 = cv2.cvtColor(img1_decoded, cv2.COLOR_BGR2HSV)
    hsv2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

    hist1 = cv2.calcHist([hsv1], [0, 1], None, [50, 60], [0, 180, 0, 256])
    hist2 = cv2.calcHist([hsv2], [0, 1], None, [50, 60], [0, 180, 0, 256])

    cv2.normalize(hist1, hist1)
    cv2.normalize(hist2, hist2)

    similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
    return {
    "similarity": round(similarity * 100, 2),
    "status": "success",
    "details": {
        "img1_shape": img1_decoded.shape,
        "img2_shape": img2.shape
    }
}

# def compare_images(img1_path, img2_path):
#     """Compare two images using histogram similarity"""
#
#
#     file_bytes = np.frombuffer(img1_path.read(), np.uint8)
#     img1 = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
#
#     # Get API image from URL (no saving)
#     # response = requests.get(api_image_url)
#
#
#     # img1 = cv2.imread(img1_path)
#     # print("Image Url", img2_path['image_url'])
#
#     response = requests.get(img2_path['image_url'], stream=True)
#     if response.status_code != 200:
#         raise ValueError(f"Error: Could not fetch image from {img2_path['image_url']}")
#
#     image_bytes = np.asarray(bytearray(response.content), dtype=np.uint8)
#     # img2 = cv2.imdecode(image_bytes, cv2.IMREAD_COLOR)
#     img2 = cv2.imdecode(np.frombuffer(response.content, np.uint8), cv2.IMREAD_COLOR)
#
#     if img2 is None:
#         raise ValueError("Error: Could not decode remote image.")
#
#
#
#     # img2 = cv2.imread(img2_path)
#
#     # Convert to HSV for color-based comparison
#     hsv1 = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
#     hsv2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
#
#     hist1 = cv2.calcHist([hsv1], [0, 1], None, [50, 60], [0, 180, 0, 256])
#     hist2 = cv2.calcHist([hsv2], [0, 1], None, [50, 60], [0, 180, 0, 256])
#
#     cv2.normalize(hist1, hist1, 0, 1, cv2.NORM_MINMAX)
#     cv2.normalize(hist2, hist2, 0, 1, cv2.NORM_MINMAX)
#
#     similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
#     return round(similarity * 100, 2)
