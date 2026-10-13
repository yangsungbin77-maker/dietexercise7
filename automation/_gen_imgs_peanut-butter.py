# -*- coding: utf-8 -*-
"""땅콩버터 다이어트 고르는 법 글 이미지 2장 fal flux-pro → webp. 상표·글자 없음."""
import os, sys, urllib.request, io
if not os.environ.get("FAL_KEY"):
    for line in open(r"C:/Users/use/.config/fal/credentials", encoding="utf-8"):
        if line.strip().startswith("FAL_KEY="):
            os.environ["FAL_KEY"] = line.strip().split("=", 1)[1].strip().strip('"').strip("'")
sys.path.insert(0, r"C:/Users/use/클로드 코드/TheLastDay-troy")
import fal_lib
from PIL import Image

OUT = r"C:/Users/use/dietexercise7/src/assets/posts"
os.makedirs(OUT, exist_ok=True)
NEG = ", plain unlabeled glass jar with no label, no text, no words, no letters, no logos, no brand names, no people, no hands"

JOBS = [
    ("peanut-butter-diet-guide.webp", "landscape_16_9",
     "Full-frame cinematic realistic photograph, edge to edge with no black bars, of an open clear glass jar of natural creamy peanut butter with a thin layer of natural oil on top, a few whole roasted peanuts in shells scattered on a light oak kitchen counter, a slice of whole grain toast on a small ceramic plate, soft warm morning window light, shallow depth of field, calm minimal healthy kitchen mood" + NEG),
    ("peanut-butter-diet-guide-label.webp", "landscape_4_3",
     "Cinematic realistic close-up photograph of a stainless steel measuring tablespoon filled with a level scoop of natural peanut butter resting beside an open plain glass jar of peanut butter on a pale linen cloth, small digital kitchen scale in soft focus background with blank display, roasted peanuts nearby, soft diffused daylight, warm neutral tones" + NEG),
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
