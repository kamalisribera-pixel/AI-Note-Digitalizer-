# Decision 001

## Problem

OCR performs poorly on noisy images.

## Decision

Add image preprocessing before OCR.

## Reason

Cleaner input improves OCR accuracy.

## Alternatives

- No preprocessing
- Only grayscale

## Trade-off

Slightly slower processing but significantly better OCR.

## Goal of Preprocessing
- I/P = Raw image
- O/P = OCR Ready Image

Image -> Load Image -> Resize -> Noise Removal -> Grayscale -> Contrast Enchancement -> Shadow Removal -> Deskew -> Thresholding -> Morphological Operations -> Sharpen -> Save image
