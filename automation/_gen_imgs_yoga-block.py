# -*- coding: utf-8 -*-
"""요가블록·요가스트랩 고르는 법 글 이미지 2장 fal flux-pro → webp. 상표 없음."""
import os, sys, urllib.request, io
sys.path.insert(0, r"C:/Users/use/클로드 코드/TheLastDay-troy")
import fal_lib
from PIL import Image

OUT = r"C:/Users/use/dietexercise7/src/assets/posts"
os.makedirs(OUT, exist_ok=True)

JOBS = [
    ("yoga-block-strap-guide.webp", "landscape_16_9",
     "Cinematic realistic photo of two plain foam yoga blocks and a neatly coiled cotton yoga strap with a metal D-ring buckle resting on an unrolled yoga mat on a light wooden home floor, soft natural window light, calm minimal home-fitness mood, shallow depth of field, no text, no words, no letters, no logos, no brand names, no people"),
    ("yoga-block-strap-guide-materials.webp", "landscape_4_3",
     "Cinematic realistic close-up product comparison of three plain yoga blocks side by side on a neutral linen surface: a light colored foam block, a natural cork block with visible grain, and a smooth light wooden block, rounded beveled edges visible, soft studio lighting, texture detail, no text, no words, no letters, no logos, no brand names, no people"),
]

only = sys.argv[1:]
for fname, size, prompt in JOBS:
    if only and fname not in only:
        continue
    r = fal_lib.run("fal-ai/flux-pro/v1.1",
                    {"prompt": prompt, "image_size": size, "num_images": 1,
                     "safety_tolerance": "5"}, poll=3, maxwait=180)
    raw = urllib.request.urlopen(r["images"][0]["url"], timeout=120).read()
    img = Image.open(io.BytesIO(raw)).convert("RGB")
    p = os.path.join(OUT, fname)
    img.save(p, "WEBP", quality=88, method=6)
    print("saved", p, img.size)
