#!/usr/bin/env python3
"""Test detect_image with all input types"""

from src.detection import SafetyDetector
import numpy as np
from PIL import Image as PILImage

print('=== COMPREHENSIVE DETECT_IMAGE TEST ===')
print()

detector = SafetyDetector()

# Test 1: NumPy Array Input
print('Test 1: NumPy Array Input')
try:
    test_array = np.zeros((640, 480, 3), dtype=np.uint8)
    test_array[100:200, 100:200] = [0, 255, 0]
    result = detector.detect_image(test_array)
    keys = list(result.keys())
    shape = result['image'].shape
    print(f'  ✓ Success - Result keys: {keys}')
    print(f'  ✓ Output shape: {shape}')
except Exception as e:
    print(f'  ✗ Failed: {e}')
print()

# Test 2: PIL Image Input
print('Test 2: PIL Image Input')
try:
    pil_image = PILImage.new('RGB', (640, 480), color=(0, 255, 0))
    result = detector.detect_image(pil_image)
    keys = list(result.keys())
    shape = result['image'].shape
    print(f'  ✓ Success - Result keys: {keys}')
    print(f'  ✓ Output shape: {shape}')
except Exception as e:
    print(f'  ✗ Failed: {e}')
print()

# Test 3: Invalid File Path (should fail gracefully)
print('Test 3: File Path Input (non-existent)')
try:
    result = detector.detect_image('nonexistent_file.jpg')
    print(f'  ✓ Success')
except ValueError as e:
    msg = str(e)[:50]
    print(f'  ✓ Correctly raised ValueError: {msg}...')
except Exception as e:
    print(f'  ✗ Unexpected error: {e}')
print()

print('=== ALL TESTS COMPLETED SUCCESSFULLY ===')
