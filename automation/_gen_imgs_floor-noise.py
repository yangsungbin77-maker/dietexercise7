# -*- coding: utf-8 -*-
"""층간소음 운동매트 글 이미지 3장 fal flux-pro → webp. 상표 없음."""
import os, sys, urllib.request, io
sys.path.insert(0, r"C:/Users/use/클로드 코드/TheLastDay-troy")
import fal_lib
from PIL import Image

OUT = r"C:/Users/use/dietexercise7/src/assets/posts"
os.makedirs(OUT, exist_ok=True)

JOBS = [
    ("floor-noise-workout-mat.webp", "landscape_16_9",
     "Cinematic realistic photo of a bright modern Korean apartment living room with a home workout corner, thick soft gray interlocking foam floor mats covering the wooden floor, a coral colored yoga mat rolled out on top, a pair of small dumbbells and a water bottle resting on the mat, soft natural window light, calm minimal home-fitness aesthetic, warm light tones with coral accents, no text, no words, no letters, no logos, no brand names, no people"),
    ("floor-noise-workout-mat-thickness.webp", "landscape_4_3",
     "Cinematic realistic close-up product photo of four exercise floor mats stacked in a staircase arrangement on a light wooden floor so their side edges show different thicknesses, from a thin yoga mat to a very thick foam play mat, one dense black rubber tile, one gray EVA foam puzzle tile with interlocking edge, one coral TPE mat, soft studio side lighting, clean bright background, no text, no words, no letters, no logos, no brand names, no numbers, no people"),
    ("floor-noise-workout-mat-layering.webp", "square_hd",
     "Cinematic realistic photo of a cozy apartment room corner home gym, a stationary exercise bike standing on a dense black rubber floor mat, next to it light gray interlocking foam puzzle mats with a coral yoga mat layered on top, a foam roller beside, bright soft daylight, tidy minimal interior, warm light tones, no text, no words, no letters, no logos, no brand names, no people"),
]

import sys as _s
ONLY=_s.argv[1:]
for fname, size, prompt in JOBS:
    if ONLY and fname not in ONLY: continue
    r = fal_lib.run("fal-ai/flux-pro/v1.1",
                    {"prompt": prompt, "image_size": size, "num_images": 1,
                     "safety_tolerance": "5"}, poll=3, maxwait=180)
    raw = urllib.request.urlopen(r["images"][0]["url"], timeout=120).read()
    img = Image.open(io.BytesIO(raw)).convert("RGB")
    p = os.path.join(OUT, fname)
    img.save(p, "WEBP", quality=88, method=6)
    print("saved", p, img.size)
