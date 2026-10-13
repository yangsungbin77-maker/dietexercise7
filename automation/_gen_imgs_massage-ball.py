# -*- coding: utf-8 -*-
"""마사지볼·땅콩볼 추천 글 이미지 4장 fal flux-pro → webp. 상표 없음."""
import os, sys, urllib.request, io
sys.path.insert(0, r"C:/Users/use/클로드 코드/TheLastDay-troy")
import fal_lib
from PIL import Image

OUT = r"C:/Users/use/dietexercise7/src/assets/posts"
os.makedirs(OUT, exist_ok=True)
NEG = ", no text, no words, no letters, no logos, no brand names, no faces"

JOBS = [
    ("massage-ball-peanut-ball-recommend.webp", "landscape_16_9",
     "Full-frame realistic photograph, edge to edge image with no black bars, no letterbox, of several massage balls on a light wooden floor next to a rolled grey yoga mat: a small solid orange rubber ball, a spiky blue ball, and a peanut-shaped double ball, soft warm window light, shallow depth of field, calm minimal home fitness corner" + NEG),
    ("massage-ball-peanut-ball-recommend-types.webp", "landscape_4_3",
     "Cinematic realistic studio flat-lay comparison of different massage balls arranged in a row on a neutral beige surface: smooth hard rubber ball, spiky textured ball, soft silicone ball, cork ball, and a peanut shaped double ball, even soft lighting, product comparison aesthetic" + NEG),
    ("massage-ball-peanut-ball-recommend-peanut.webp", "square_hd",
     "Realistic photograph close-up of a matte rubber peanut-shaped double massage ball made of two joined balls with a deep groove in the middle, slightly textured grippy surface, resting on a yoga mat, seamless solid object with no seams, soft side lighting, muted teal and grey tones, minimal home workout setting" + NEG),
    ("massage-ball-peanut-ball-recommend-size.webp", "landscape_16_9",
     "Cinematic realistic photo of massage balls in three sizes lined up from small to large on a wooden shelf beside a foam roller, a small ball, a medium ball and a large soft ball, natural daylight, tidy home gym storage aesthetic" + NEG),
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
