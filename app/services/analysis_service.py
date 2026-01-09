import random
from pathlib import Path

UPLOAD_DIR = Path(__file__).parent.parent.parent / "uploads"

SKIN_TYPES = ["Oily", "Dry", "Combination", "Normal", "Sensitive"]

POSSIBLE_ISSUES = [
    "Acne",
    "Hyperpigmentation",
    "Wrinkles",
    "Dark Circles",
    "Redness",
    "Dryness",
    "Puffiness",
    "Uneven Texture"
]

def verify_image_exists(image_id: str) -> bool:
    """
    Verify if an image with the given image_id exists.
    
    Args:
        image_id: The image identifier
        
    Returns:
        bool: True if image exists, False otherwise
    """
    #jpg_path = UPLOAD_DIR / f"{image_id}.jpg"
    jpeg_path = UPLOAD_DIR / f"{image_id}.jpeg"
    png_path = UPLOAD_DIR / f"{image_id}.png"
    
    return jpeg_path.exists() or png_path.exists()
 
async def analyze_image(image_id: str) -> dict:

    if not verify_image_exists(image_id):
        raise ValueError(f"Image with id '{image_id}' not found")
    
    skin_type = random.choice(SKIN_TYPES)
    num_issues = random.randint(0, 4)
    issues = random.sample(POSSIBLE_ISSUES, num_issues)
    confidence = round(random.uniform(0.75, 0.99), 2)
    
    return {
        "image_id": image_id,
        "skin_type": skin_type,
        "issues": issues,
        "confidence": confidence
    }