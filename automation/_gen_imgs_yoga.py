# -*- coding: utf-8 -*-
"""요가매트 추천 글 이미지 2장 fal flux-pro → webp. 상표 없음."""
import os, sys, urllib.request, io
sys.path.insert(0, r"C:/Users/use/클로드 코드/TheLastDay-troy")
import fal_lib
from PIL import Image

OUT = r"C:/Users/use/dietexercise7/src/assets/posts"
os.makedirs(OUT, exist_ok=True)

JOBS = [
    ("yoga-mat-guide.webp",
     "Cinematic clean product photo of a rolled and an unrolled yoga mat on a bright wooden home floor near a window, soft morning light, a water bottle and towel beside it, calm minimal home-fitness aesthetic, no text, no words, no letters, no logos, no brand names, no people"),
    ("yoga-mat-materials.webp",
     "Cinematic flat-lay of several yoga mats in different colors and thicknesses stacked and fanned out to show texture and edges, studio lighting on a neutral background, comparison aesthetic showing material differences, no text, no words, no letters, no logos, no people"),
]

for fname, prompt in JOBS:
    r = fal_lib.run("fal-ai/flux-pro/v1.1",
                    {"prompt": prompt, "image_size": "landscape_16_9", "num_images": 1,
                     "safety_tolerance": "5"}, poll=3, maxwait=180)
    raw = urllib.request.urlopen(r["images"][0]["url"], timeout=120).read()
    img = Image.open(io.BytesIO(raw)).convert("RGB")
    p = os.path.join(OUT, fname)
    img.save(p, "WEBP", quality=88, method=6)
    print("saved", p, img.size)
