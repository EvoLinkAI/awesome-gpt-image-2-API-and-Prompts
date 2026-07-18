# 📣 Ad Creative Cases

> Part of [awesome-gpt-image-2-prompts](../README.md)

### Case 90: [4-Panel Japanese Digital Ad Banner Grid](https://x.com/makaneko_AI/status/2045764016858087720) (by [@makaneko_AI](https://x.com/makaneko_AI))

| Output |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-prompts" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts/main/images/ui_case90/output.jpg" width="300" alt="Output image"></a> |

**Prompt:**

```
{
  "type": "2x2 grid of Japanese digital advertisement banners",
  "layout": {
    "structure": "4 equal quadrants",
    "quadrants": [
      {
        "position": "top-left",
        "theme": "Travel",
        "subject": "A couple holding hands on a white sand beach, looking out at turquoise ocean water under a bright blue sky.",
        "elements": ["red hibiscus flower in bottom left corner"],
        "text_labels": [
          "今年こそ、解き放て。",
          "{argument name=\"travel destination\" default=\"沖縄旅行\"}",
          "3日間の癒やし旅",
          "航空券+ホテル",
          "39,800円〜",
          "絶景、グルメ、体験 ぜんぶ叶う!"
        ],
        "icons": {
          "count": 3,
          "descriptions": ["airplane", "hotel building", "car"]
        }
      },
      {
        "position": "top-right",
        "theme": "Skincare",
        "subject": "Close-up portrait of a young woman with glowing, dewy skin, eyes closed, gently touching her cheeks.",
        "elements": [
          "soft pink gradient background",
          "dynamic water splash effects",
          "pink cosmetic jar labeled '{argument name=\"skincare product name\" default=\"LUMIÈRE\"} Brightening Gel'"
        ],
        "text_labels": [
          "毛穴・くすみ卒業!",
          "透明感あふれる",
          "水光肌へ",
          "新感覚スキンケア",
          "初回限定 78%OFF",
          "{argument name=\"discount price\" default=\"1,980円\"}"
        ],
        "badges": {
          "count": 3,
          "style": "gold circular",
          "labels": ["毛穴ケア", "高保湿", "ハリ・ツヤ"]
        }
      },
      {
        "position": "bottom-left",
        "theme": "Gourmet Food",
        "subject": "Thick, sliced, medium-rare steak sizzling on a dark grill plate.",
        "elements": [
          "garlic chips",
          "rosemary sprig",
          "dark background with smoke and glowing embers"
        ],
        "text_labels": [
          "とろける旨さ!",
          "{argument name=\"food item\" default=\"黒毛和牛\"}",
          "贅沢ステーキ",
          "期間限定",
          "特別価格",
          "通常価格 8,980円",
          "4,980円"
        ],
        "badges": {
          "count": 1,
          "style": "red circular",
          "labels": ["A4 A5等級"]
        }
      },
      {
        "position": "bottom-right",
        "theme": "Online Education",
        "subject": "Young man in a blue shirt studying at a desk, writing in a notebook next to an open laptop.",
        "elements": ["bright indoor lighting", "desk environment"],
        "text_labels": [
          "スキマ時間で",
          "{argument name=\"education goal\" default=\"最短合格!\"}",
          "オンライン資格講座",
          "スマホで完結",
          "効率学習で差がつく!",
          "今だけ! 受講料 20%OFF"
        ],
        "badges": {
          "count": 1,
          "style": "blue circular",
          "labels": ["受講者数 10万人 突破!"]
        },
        "icons": {
          "count": 2,
          "descriptions": ["smartphone", "open book"]
        }
      }
    ]
  }
}
```

### Case 112: [Anime Character Brand Identity & Merch Board](https://x.com/chi_vc_/status/2046061073720369228) (by [@chi_vc_](https://x.com/chi_vc_))

| Output |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-prompts" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts/main/images/poster_case112/output.jpg" width="300" alt="Output image"></a> |

**Prompt:**

```
{
  "type": "brand identity and merchandise design board",
  "theme": {
    "color_palette": "{argument name=\"theme color\" default=\"pastel pink\"} and white",
    "motif": "{argument name=\"motif\" default=\"cherry blossoms\"} and pink hearts"
  },
  "character": {
    "description": "anime girl with short brown bob hair, pink eyes, wearing a white hoodie, gentle smile"
  },
  "branding": {
    "main_logo": "{argument name=\"character name\" default=\"癒音ちー\"}",
    "sub_logo": "{argument name=\"character subtext\" default=\"ゆおんちー\"}"
  },
  "layout": {
    "sections": [
      {
        "type": "header banner",
        "position": "top",
        "elements": ["large main logo", "sub logo", "cherry blossom graphics", "character portrait on the right"]
      },
      {
        "type": "product packaging",
        "position": "middle left",
        "elements": ["1 square box with heart-shaped transparent window showing pink heart candies", "character illustration on box", "2 individual candy wrappers", "5 scattered heart candies"]
      },
      {
        "type": "promotional poster",
        "position": "middle right",
        "elements": ["character portrait", "heart-shaped candy bowl", "main logo", "text '4.26 NEW OPEN'", "text '{argument name=\"social handle\" default=\"@yuonchii\"}'"]
      },
      {
        "type": "horizontal web banner",
        "position": "lower middle",
        "elements": ["main logo", "cherry blossoms", "character portrait on the right"]
      },
      {
        "type": "social media profile mockup",
        "position": "bottom left",
        "elements": ["header image with logo", "1 circular profile picture", "handle '{argument name=\"social handle\" default=\"@yuonchii\"}'", "1 follow button", "mock bio text"]
      },
      {
        "type": "merchandise collection",
        "position": "bottom right",
        "count": 9,
        "items": ["1 white t-shirt with logo", "1 white mug with character", "4 round pin badges", "1 acrylic keychain", "2 candy packets"]
      }
    ]
  }
}
```

### Case 108: [Dark Mode Marketing Case Study UI](https://x.com/IndieDevHailey/status/2044974254769463312) (by [@IndieDevHailey](https://x.com/IndieDevHailey))

| Output |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-prompts" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts/main/images/poster_case108/output.jpg" width="300" alt="Output image"></a> |

**Prompt:**

```
{
  "type": "UI/UX landing page mockup",
  "theme": "dark mode, sleek modern aesthetic, glassmorphism, {argument name=\"primary accent color\" default=\"neon purple and blue\"} glowing accents",
  "header": {
    "logo": "{argument name=\"brand name\" default=\"goViralX\"}",
    "top_right_tag": "VIRAL CAMPAIGN CASE STUDY"
  },
  "layout": {
    "sections": [
      {
        "name": "Hero",
        "headline": "{argument name=\"hero headline\" default=\"How We Created 10M+ Viral Impact\"}",
        "subheadline": "3天引爆全网, 助力品牌实现指数级增长",
        "stats_row": {
          "count": 4,
          "labels": ["总播放量", "互动率", "转化咨询", "执行周期"],
          "values": ["{argument name=\"main statistic\" default=\"10,240,000+\"}", "18.7%", "3,200+", "72小时"]
        },
        "visual": "cinematic shot of a person in a hoodie looking at glowing digital screens and graphs, large play button overlay"
      },
      {
        "name": "Strategy",
        "title": "Our 3-Day Execution Strategy",
        "layout_type": "vertical timeline",
        "steps_count": 3,
        "elements_per_step": ["timeline node", "title", "bullet points", "video thumbnail with play button", "description box"]
      },
      {
        "name": "Performance",
        "title": "Data-Driven Performance",
        "left_column": {
          "stat_cards_count": 4,
          "values": ["10M+", "43%", "28,000+", "3,200+"]
        },
        "right_column": {
          "charts_count": 2,
          "chart_1": "line graph showing 7-day growth peaking at Day 3",
          "chart_2": "horizontal segmented bar chart showing platform distribution (TikTok 52%, Instagram 24%, X 15%, YouTube 9%)"
        }
      },
      {
        "name": "Keys to Success",
        "title": "The 3 Keys to Viral Success",
        "cards_count": 3,
        "card_elements": ["glowing icon (fire, target, antenna)", "title", "description", "VIEW DETAIL link"]
      },
      {
        "name": "Social Proof",
        "title": "TRUSTED BY CREATORS & BRANDS",
        "left_column": {
          "logos_count": 8,
          "grid": "2x4",
          "brands": ["SHEIN", "SHOPLINE", "Blueglass", "instacart", "lemon8", "mi", "CIDER", "bellroy"]
        },
        "right_column": {
          "testimonial_cards_count": 2,
          "elements": ["quote", "author title (SaaS Founder, Growth Manager)"]
        }
      },
      {
        "name": "Call to Action",
        "title": "READY TO GO VIRAL?",
        "interactive_elements": ["text input field", "glowing button with text '{argument name=\"call to action text\" default=\"获取专属增长方案 ->\"}'"],
        "visual": "3D render of a rocket ship taking off with purple and blue flames"
      }
    ]
  }
}
```

### Case 107: [18-Panel Mascot Brand Identity Document](https://x.com/Colin_Leeee/status/2044802802149650631) (by [@Colin_Leeee](https://x.com/Colin_Leeee))

| Output |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-prompts" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts/main/images/poster_case107/output.jpg" width="300" alt="Output image"></a> |

**Prompt:**

```
{
  "type": "18-panel brand identity and character design document",
  "brand": {
    "name": "{argument name=\"brand name\" default=\"沐阳 MUYANG TEA\"}",
    "industry": "{argument name=\"industry\" default=\"tea shop\"}",
    "colors": ["{argument name=\"primary color\" default=\"yellow\"}", "{argument name=\"secondary color\" default=\"green\"}", "white", "brown", "dark green"]
  },
  "subject": "{argument name=\"character description\" default=\"3D rendered cute Shiba Inu mascot wearing a green apron\"}",
  "layout": {
    "grid": "3 columns by 6 rows",
    "sections": [
      {
        "title": "01 品牌DNA分析 / BRAND DNA ANALYSIS",
        "elements": ["logo", "5 color swatches", "6 icons", "target audience charts"]
      },
      {
        "title": "02 概念构思 / CONCEPT MOODBOARD",
        "elements": ["5 photo references", "4 mood icons", "design equation"]
      },
      {
        "title": "03 形态研究 / FORM STUDY",
        "elements": ["4 logo anatomy icons", "4 evolution steps", "4 silhouettes"]
      },
      {
        "title": "04 概念探索 / CONCEPT EXPLORATION",
        "elements": ["12 line-art character sketches"]
      },
      {
        "title": "05 精细线稿 / REFINED LINE ART",
        "elements": ["3 rows of front and side line art with proportion guides"]
      },
      {
        "title": "06 细节精修 / DETAIL REFINEMENT",
        "elements": ["2 full-body renders with labels", "4 circular close-ups"]
      },
      {
        "title": "07 表情设定 / EXPRESSION SHEET",
        "elements": ["11 3D rendered head expressions"]
      },
      {
        "title": "08 姿势库 / POSE LIBRARY",
        "elements": ["9 full-body 3D rendered poses"]
      },
      {
        "title": "09 转身视图 / TURNAROUND VIEW",
        "elements": ["5 full-body 3D renders", "5 matching line-art views"]
      },
      {
        "title": "10 色彩开发 / COLOR DEVELOPMENT",
        "elements": ["5 rows of 5-color palettes", "color psychology text"]
      },
      {
        "title": "11 材质规格 / MATERIAL SPECIFICATION",
        "elements": ["5 texture swatches", "property sliders", "4 manufacturing icons"]
      },
      {
        "title": "12 色彩应用 / COLOR APPLICATION",
        "elements": ["4 color variant renders", "2 light/dark renders", "4 contrast rating circles"]
      },
      {
        "title": "13 构造指南 / CONSTRUCTION GUIDE",
        "elements": ["2 line-art diagrams for geometry and grid"]
      },
      {
        "title": "14 设计系统规则 / DESIGN SYSTEM RULES",
        "elements": ["minimum size icons", "clear space diagram", "4 usage examples"]
      },
      {
        "title": "15 资产变体 / ASSET VARIANTS",
        "elements": ["3 size variants", "3 line-art variants", "3 simplified flat heads"]
      },
      {
        "title": "16 数字应用 / DIGITAL APPLICATIONS",
        "elements": ["1 app icon", "2 social avatars", "UI elements", "3-step animation cycle"]
      },
      {
        "title": "17 实物应用 / PHYSICAL APPLICATIONS",
        "elements": ["plush toy mockup", "packaging mockup", "merchandise mockup", "storefront mockup"]
      },
      {
        "title": "18 最终主视觉 / FINAL RENDERING",
        "elements": ["large high-res 3D render of mascot holding tea", "logo", "file format list"]
      }
    ]
  }
}
```

### Case 166: [Japanese Chinese Food Delivery Flyer](https://x.com/xc5_/status/2048310696686014935) (by [@xc5_](https://x.com/xc5_))

| Output |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-prompts" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts/main/images/poster_case166/output.jpg" width="300" alt="Output image"></a> |

**Prompt:**

```
A Japanese neighborhood Chinese restaurant delivery flyer for mailbox posting (3:4 aspect ratio). Designed to look like a double-sided B5 print.

Flyer characteristics (following the grammar of real delivery flyers):
- Flashy red and yellow color scheme.
- Large text at the top: "Delivery Available! {argument name="shop name" default="Mona-Hanten"}" (shadowed Gothic font).
- An illustration of a {argument name="character" default="Chinese girl in a red cheongsam with a brown short bob"} holding ramen and saying "Welcome!" in a speech bubble.
- A menu photo grid (4x3) featuring various dishes: different types of ramen, fried rice, gyoza, sweet and sour pork, shrimp in chili sauce, mapo tofu, liver and leek stir-fry, tenshinhan, twice-cooked pork, spring rolls, annin tofu, and fried rice sets.
- Names and prices for each dish.
- A large yellow banner saying "Free delivery on all menu items over ¥1,000!".
- "Order by phone! ☎ 072-XX-XXXX" emphasized with a red circle.
- Business hours "11:00-22:00 (Closed on Tuesdays)".
- Delivery area map (simple schematic map).
- Coupon (perforated line for clipping): "One free plate of gyoza with this flyer!".

Texture of cheap paper printing. Includes fold marks. Precision that could be mistaken for a real Japanese delivery flyer.
```

### Case 167: [Pastel Jellyfish Room Goods Poster](https://x.com/Ayu_AI_0912/status/2048309565817766139) (by [@Ayu_AI_0912](https://x.com/Ayu_AI_0912))

| Output |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-prompts" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts/main/images/poster_case167/output.jpg" width="300" alt="Output image"></a> |

**Prompt:**

```
{"type":"pastel lifestyle poster / character room-goods feature sheet","theme":"soft dreamy lavender jellyfish aesthetic","style":"Japanese cute editorial graphic, airy white background, pastel lilac palette, delicate handwritten notes, sparkles and tiny doodles, soft product photography mixed with magazine layout","subject":{"character":{"name":"{argument name=\"character name\" default=\"くらげちゃん\"}","appearance":"young woman with a short platinum-blonde bob haircut, wearing a fluffy pale-lavender zip hoodie over a white inner top, shown from chest up on the lower right, face intentionally obscured with a plain beige rectangle"}},"layout":{"orientation":"vertical poster","background":"clean white with faint pastel doodles of stars, bubbles, tiny jellyfish, and musical notes","sections":[{"title":"header","position":"top","count":5,"labels":["speech bubble intro","main title","small subtitle GOODS","horizontal lavender ribbon tagline","round badge on the top right"]},{"title":"featured goods grid","position":"upper and middle left","count":6,"labels":["ゆらゆらくらげランプ","くらげと夢見るベッドリネン","くらげシェルミラー","くらげグラデマグ","くらげのときめき収納ボックス","くらげふわもこマット"]},{"title":"side handwritten note","position":"upper right","count":1,"labels":["みんなも くらげちゃんRoomで いっしょに まったりしよー♡♡"]},{"title":"room concept box","position":"lower left","count":1,"labels":["くらげちゃんの お部屋作りのこだわり"]},{"title":"pick up circle","position":"lower center-left","count":1,"labels":["Pick up!"]}],"product_images":{"count":6,"items":[{"name":"ゆらゆらくらげランプ","description":"small translucent jellyfish-shaped lamp on a white base, glowing softly in pale blue-lavender"},{"name":"くらげと夢見るベッドリネン","description":"plush pastel-lavender bed with fluffy comforter and pillows, dreamy cozy bedroom styling"},{"name":"くらげシェルミラー","description":"small tabletop mirror with a puffy shell-like pastel-lilac frame and rounded base"},{"name":"くらげグラデマグ","description":"ceramic mug with lavender-to-pink gradient and a simple jellyfish illustration"},{"name":"くらげのときめき収納ボックス","description":"pastel storage box holding cosmetics and small bottles, decorated with a jellyfish emblem"},{"name":"くらげふわもこマット","description":"small fluffy cloud-like or jellyfish-like mat in pale lavender and white"}]},"text_elements":{"main_title":"{argument name=\"headline text\" default=\"くらげちゃんの お部屋アイテム\"}","badge_text":"くらげちゃんの Room お部屋作りの こだわりポイントも 教えちゃうよ。","tagline":"ふわふわで甘くて、ちょっぴり夢みたいな私のお部屋へようこそ♡","speech_bubble":"くらげちゃんの お気に入りだけ集めた お部屋アイテムを紹介するよ♪","concept_points":{"count":3,"items":["色は白とラベンダーで統一!","光が集まるふわっとした空間に","お友達入りのアイテムに囲まれて 自分らしくいられる空間を大切にしてるよ♪"]},"product_blurbs":"each product has a short handwritten Japanese description in a cute casual font beside or below the image"},"composition":"the poster is left-heavy with product cards and text, while the character portrait occupies the lower right third, slightly overlapping the layout","color_palette":{"count":5,"colors":["white","pastel lavender","soft lilac","pale gray-violet","touches of pastel blue-pink gradient"]},"rendering_notes":"keep everything very soft, feminine, and cozy; rounded corners on all product photos; mix of bold Japanese headline typography and light handwritten annotations; subtle shadows; clean high-key lighting; social-media-ready editorial collage aesthetic"}
```

### Case 143: [Magical Seed Packet Diorama](https://x.com/AllaAisling/status/2048156345518768190) (by [@AllaAisling](https://x.com/AllaAisling))

| Output |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-prompts" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts/main/images/poster_case143/output.jpg" width="300" alt="Output image"></a> |

**Prompt:**

```
Epic 3D scene: a weathered seed packet lying open on a potting bench, its promise erupting into the garden it describes. The illustration on the front becomes real. {argument name="plant type" default="[PLANT / FLOWER]"} growing at full scale from the paper, roots visible through the packet's base pushing into soil below.
{argument name="detail left" default="[DETAIL 1]"} in full bloom at one corner. {argument name="detail right" default="[DETAIL 2]"} mid-growth at the other, not yet what it will be.
Tiny insects that belong to this plant, {argument name="insect type" default="[BEE / BUTTERFLY / BEETLE]"}, hovering at correct scale.
The written instructions on the back become garden calendar, "sow in spring" manifests as actual spring light. "full sun" manifests as a single shaft of it, hitting the tallest bloom perfectly.
Scattered seeds between packet and soil each showing their germination stage, split coat, first root, first shoot, first leaf.
The packet's torn top edge becomes a treeline.
Potting bench surface with soil scatter and water droplets.
Tilt-shift depth of field, greenhouse morning light, the packet as the garden it always intended.
```

<!-- Case 17: Luxury Chronograph Watch Ad (by @AlwaveNazca) -->
### Case 17: [Luxury Chronograph Watch Ad](https://x.com/AlwaveNazca/status/2048147643809865950) (by [@AlwaveNazca](https://x.com/AlwaveNazca))

| Output |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-prompts" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts/main/images/poster_case144/output.jpg" width="300" alt="Output image"></a> |

**Prompt:**

```
A dramatic luxury product advertising image for a motorsport-inspired chronograph wristwatch in a dark studio. Center-left foreground, show a single stainless steel chronograph watch standing upright at a slight three-quarter angle, with a black dial, two red-accent subdials, slim silver hour markers, a tachymeter bezel, and visible crown and pushers on the right side. The watch has a black leather strap with bold red stitching along both edges and a sporty premium finish. To the right of the watch, place one black square presentation box slightly behind it, textured like leather, with red stitching around the lid and a silver embossed eye-shaped logo above the text “NESS STUDIO” and smaller red text “TRACK SURFACE.” At the top center of the composition, add the same silver eye logo with the words “NESS STUDIO” and smaller “BY NICOLAS.” Across the background, place one oversized blurred word, {argument name="headline text" default="PRECISION"}, in large gray capital letters spanning nearly the full width. The scene is set against a deep black background with cinematic red and white horizontal light streaks crossing behind the products from left to right, suggesting speed and racetrack energy. Use a glossy wet ground plane with reflective texture, catching red highlights and mirrorlike reflections beneath the watch and box. At the bottom center, add the text “CHRONOGRAPH SERIES” in clean white spaced capitals with thin red horizontal lines extending on both sides, and below it smaller red capitals reading {argument name="tagline text" default="ALSACE MADE"}. Color palette: black, charcoal gray, silver steel, vivid racing red, and a touch of white. Lighting should be high-contrast and premium, with crisp specular highlights on the metal case, subtle soft fill on the box, and moody shadows. Overall style: ultra-polished commercial product photography, luxury watch campaign, sharp focus on the products, sleek branding, high-end automotive aesthetic.
```

<!-- Case 17: Neon Nike Lumina Ad Poster (by @AlwaveNazca) -->
### Case 17: [Neon Nike Lumina Ad Poster](https://x.com/AlwaveNazca/status/2048147643809865950) (by [@AlwaveNazca](https://x.com/AlwaveNazca))

| Output |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-prompts" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts/main/images/poster_case145/output.jpg" width="300" alt="Output image"></a> |

**Prompt:**

```
A high-energy vertical Nike fashion campaign poster featuring a single athletic young woman mid-jump against a futuristic neon studio background. She is captured in a dynamic airborne pose with one knee bent up, the other leg folded back, one arm extended outward and the other bent near her chest, conveying motion and power. Her face is obscured by a clean rectangular blur block centered over the face. She wears a cropped iridescent white hooded windbreaker with a black zipper and small Nike logo on the chest, holographic metallic lavender-blue leggings with a subtle Nike swoosh on the thigh, a black branded waistband visible above the leggings, and white chunky Nike sneakers. Her brown hair is tied in a high ponytail flying outward with the jump. Behind her, enormous glowing white serif letters spell “NIKE” across the upper half, with a small white Nike swoosh centered above the word. Across the middle background, the phrase “LUMINA” appears once in wide bold glowing letters with a horizontal glitch and scanline distortion effect, partially obscured by the model. The color palette is saturated magenta, violet, cyan, and electric blue with strong bloom, glossy highlights, lens flares, and chromatic aberration. Add sweeping circular light trails wrapping around the model’s legs and body, suggesting speed and motion. The overall style is premium sportswear advertising, ultra-polished, cinematic, high contrast, hyperreal retouching, crisp product detail, dramatic rim lighting, and a luminous holographic aesthetic. Place 2 small text lines at the bottom: bottom left reads {argument name="tagline text" default="LIGHT. MOTION. ENERGY."}, bottom right reads {argument name="collection name" default="NIKE LUMINA COLLECTION"} followed by a small Nike swoosh. Include exactly 3 visible Nike swooshes total: 1 above the large NIKE headline, 1 on the jacket chest, and 1 on the leggings.
```

<!-- Case 17: Streetwear Sneaker Poster Ad (by @AlwaveNazca) -->
### Case 17: [Streetwear Sneaker Poster Ad](https://x.com/AlwaveNazca/status/2048147643809865950) (by [@AlwaveNazca](https://x.com/AlwaveNazca))

| Output |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-prompts" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts/main/images/poster_case146/output.jpg" width="300" alt="Output image"></a> |

**Prompt:**

```
Create a bold streetwear poster advertisement for {argument name="brand name" default="NESS STUDIO"} featuring a young adult model seated casually on the ground in a low-angle fashion pose, one knee raised and one leg extended toward the camera so the sneaker in front appears oversized and dominant. The model wears a dark brown oversized leather bomber jacket, a black shirt, light blue loose-fit jeans, white socks, and chunky black-white-gray sneakers with a red accent in the sole and the {argument name="brand name" default="NESS STUDIO"} logo visible on the shoe side and tongue. The face is intentionally obscured by a soft rectangular blur block centered over the face. Use an off-white textured paper background with distressed grunge design elements and collage layering. Behind the model, place a large rough red paint brushstroke shape spanning diagonally across the center. Add black ink splatters, sketch circles, torn paper scraps, and hand-painted graffiti accents. Include 4 major graphic doodles: a large black X in the upper right, a hand-drawn upward arrow in the lower left, a rough crown sketch in the lower right, and a circular scribble near the top center. In the upper left, place a stylized eye logo above the text "{argument name="brand name" default="NESS STUDIO"}" and a smaller tagline below reading "A MOMENT OF YOUR STYLE". On the left middle area, add the handwritten slogan "INNOVATE CREATE INSPIRE" in stacked black brush lettering. On the right middle area, place a torn black paper patch with the handwritten white slogan "BUILT DIFFERENT MOVE DIFFERENT" and a red underline stroke. In the lower left near the shoe, add a black distressed label sticker containing a globe scribble, the text "{argument name="brand name" default="NESS STUDIO"}", and a barcode. Along the bottom footer, create a clean horizontal strip with 3 social media icons and handles separated by thin vertical dividers: Instagram, Facebook, and Twitter, each followed by "@NESS.STUDIO". The overall style should be edgy, urban, youthful, high-contrast, editorial street fashion, mixing product advertising photography with graffiti poster design, collage textures, and dynamic branding.
```

### Case 147: [Editorial Osaka Six Sweatshirt Ad](https://x.com/_LaurentB/status/2048126606313464040) (by [@_LaurentB](https://x.com/_LaurentB))

| Output |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-prompts" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts/main/images/poster_case147/output.jpg" width="300" alt="Output image"></a> |

**Prompt:**

```
A clean editorial fashion advertisement poster on a pale powder-blue studio background with a glossy reflective floor. The composition is vertical and minimal, dominated by oversized bold white condensed sans-serif typography in the background reading “OSAKA SIX:” on the top line and “006 REMAINS” below, filling most of the upper half behind the subject. In the top right corner, small white branding text reads “Designed by ARTTEESHOW.” Centered in the lower middle is an oversized forest-green crewneck sweatshirt standing upright like a sculptural object, with soft heavy cotton fabric, dropped shoulders, extra-long sleeves pooled on the floor, and a small black neck label that reads ARTTEESHOW. On the chest of the sweatshirt is a large abstract collage print made from torn paper fragments in beige, tan, black, gray, white, and vivid red, arranged vertically like layered scraps. Leaning against the right side of the giant sweatshirt is a slim female fashion model with long straight black hair, wearing a matching {argument name="sweatshirt color" default="forest green"} sweatshirt and relaxed wide-leg sweatpants with clean white low-top sneakers. She is posed in profile with a calm detached editorial attitude, one hand in her pocket, her body reclining diagonally against the giant garment, legs extended forward; her face is obscured by a soft rectangular blur for an anonymous art-fashion look. The smaller worn sweatshirt has the same abstract torn-paper collage graphic centered on the chest. At the bottom center, add 2 lines of small white copy text: “Made for comfort, worn for confidence.” and “Because life feels better when someone’s carrying the weight of the world.” The image should feel like a premium conceptual streetwear campaign from the early 1990s reimagined as contemporary luxury advertising, with crisp studio lighting, soft shadows, subtle floor reflections, precise product focus, surreal scale contrast between the oversized sweatshirt and the model, and a polished magazine-poster aesthetic.
```

### Case 148: [Editorial Perfume Shot on Moss](https://x.com/Salmaaboukarr/status/2048103506125463983) (by [@Salmaaboukarr](https://x.com/Salmaaboukarr))

| Output |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-prompts" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts/main/images/poster_case148/output.jpg" width="300" alt="Output image"></a> |

**Prompt:**

```
A high-end editorial product photograph of a single luxury perfume bottle centered in a warm earthy still-life scene. The product is a clear rectangular glass bottle filled with golden amber liquid, topped with a glossy rounded black cap, with a clean white front label that reads "BYREDO", "BAL D’AFRIQUE", and "EAU DE PARFUM". Place the bottle upright on 1 curved piece of pale weathered driftwood, surrounded by a dense carpet of 1 layer of rich green moss covering the foreground and lower frame. Use a minimal studio composition with the product isolated against a smooth warm brown-to-amber gradient background, softly illuminated like sunset light. Light the scene with dramatic directional warm light from the upper right, creating a bright glow on the background, a crisp highlight on the cap, soft reflections in the glass, and gentle shadows across the wood and moss. Keep the framing vertical, the bottle centered slightly low in the composition with generous negative space above, and the overall mood natural, luxurious, earthy, cinematic, and polished like a premium fragrance campaign shot.
```

### Case 149: [Editorial Perfume Bottle in Golden Fur](https://x.com/Salmaaboukarr/status/2048103506125463983) (by [@Salmaaboukarr](https://x.com/Salmaaboukarr))

| Output |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-prompts" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts/main/images/poster_case149/output.jpg" width="300" alt="Output image"></a> |

**Prompt:**

```
A luxurious editorial product photograph of a single perfume bottle nestled into dense, plush faux fur in rich golden caramel and honey-brown tones. Center the composition on one clear oval glass bottle filled with warm amber liquid, with a glossy rounded black cap and a clean white rectangular label. The label text should read {argument name="brand name" default="BYREDO"} at the top, {argument name="product name" default="BAL D’AFRIQUE"} large in the middle, and {argument name="product type" default="EAU DE PARFUM"} in small text near the bottom. Shoot it as a close-up still life with soft studio lighting, subtle highlights on the glass and cap, gentle shadows in the folds of the fur, and a warm cinematic color palette. The bottle should sit slightly embedded in the fur so the surrounding texture frames it from all sides, creating a premium fashion editorial mood, minimal composition, shallow depth of field, crisp focus on the label, and a high-end beauty campaign aesthetic.
```

### Case 150: [Luxury Miniature Dubai City Model](https://x.com/silentempiredev/status/2048086378383384773) (by [@silentempiredev](https://x.com/silentempiredev))

| Output |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-prompts" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts/main/images/poster_case150/output.jpg" width="300" alt="Output image"></a> |

**Prompt:**

```
A hyper-detailed cinematic isometric miniature city model of {argument name="landmark tower" default="Burj Khalifa"} rising dramatically from the center of a square architectural master-plan board, presented like a luxury urban planning maquette on a black background. The composition shows one dominant ultra-tall silver skyscraper in the exact center, surrounded by a dense ring of modern high-rise towers, illuminated roads, bridges, and glowing warm city lights. Curving turquoise-blue water features and artificial lakes wrap around the central district in multiple connected pools and canals, with one large circular fountain-like feature near the tower base and several small island shapes visible in the water. In the lower right quadrant, include a large low-rise complex with rounded geometric roofs and subtle green-lit sections, connected by multilane roads and looping interchanges. The entire city sits on one square beige map board engraved with faint street grids and planning lines, with the board edges clearly visible and slightly raised. Viewpoint is a high three-quarter isometric angle, centered and symmetrical, with the tower extending far upward into negative space. Lighting is dramatic and luxurious: warm golden edge lights on buildings and roads, cool reflections in the water, crisp metallic highlights on the central tower, and a deep black void surrounding the model. Style should feel like a photorealistic architectural visualization mixed with a premium collectible scale model, extremely intricate, sharp, polished, and elegant.
```

### Case 131: [Parody Luxury Product Advertisement](https://x.com/tonysimons_/status/2048057490940596595) (by [@tonysimons_](https://x.com/tonysimons_))

| Output |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-prompts" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts/main/images/poster_case131/output.jpg" width="300" alt="Output image"></a> |

**Prompt:**

```
High-impact parody e-commerce infographic for “{argument name="product" default="Four Loko"}” malt beverage. Foreground: An extreme close-up of a rough, weathered hand holding a tall, brightly colored can of {argument name="product" default="Four Loko"} toward the camera. The can is slightly cold with visible condensation droplets and a loud, chaotic flavor design. The hand and can have a slight macro-lens blur for depth, with the can still reading clearly as the hero product. Central Subject: In the mid-ground, a funny, disheveled {argument name="subject" default="homeless-looking man"} sitting casually on a milk crate in an urban alley. He has a scruffy beard, messy hair, layered worn clothing, and a huge unbothered grin. He should look chaotic but oddly charismatic, like the accidental king of bad decisions. He is posed like a confident lifestyle-ad model, proudly showing off the can. Background & Lighting: A ridiculously polished ad-style backdrop mixed with a grimy city alley setting. Soft-focus urban textures, dumpster shapes, graffiti hints, and scattered clutter in the distance. Add dramatic studio lighting, soft glow, rainbow prism flares, and subtle light leaks to make the whole thing look way too premium for the subject matter. A few blurred {argument name="product" default="Four Loko"} cans can float artistically in the background for extra absurdity. Typography & Layout (Bold sans-serif, white and neon accent styling): Top Center (Background): Massive, bold text reading “{argument name="brand name" default="FOUR LOKO"}” positioned behind the subject. Top Right: Bold text reading “The Champagne of Bad Ideas”. Mid-Left: “Premium chaos and zero self-control” Mid-Right: Large, bold “23” with the text “ounces of terrible decisions.” Bottom-Right: Large, bold “1" with the text “can to ruin tomorrow.” Optional small callout text near the bottom: “Now with more regret.” Style: Ultra-detailed, 8k parody commercial photography, sharp focus on the can, shallow depth of field, vibrant trashy color palette, clean advertising composition, exaggerated premium product-ad aesthetic, funny visual contrast between polished branding and the wrecked subject.
```

### Case 109: [VR Headset Exploded View Poster](https://x.com/wory37303852/status/2045925660401795478) (by [@wory37303852](https://x.com/wory37303852))

| Output |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-prompts" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts/main/images/poster_case109/output.jpg" width="300" alt="Output image"></a> |

**Prompt:**

```
{
  "type": "exploded view product diagram poster",
  "subject": "VR headset",
  "style": "clean high-tech 3D render, studio lighting, glowing accents",
  "background": "{argument name=\"background color\" default=\"soft purple and blue gradient\"}",
  "header": {
    "logo": "∞ {argument name=\"product name\" default=\"Meta Quest 3\"}",
    "subtitle": "{argument name=\"main catchphrase\" default=\"まったく新しい現実を、まったく新しい構造から。\"}"
  },
  "layout": {
    "centerpiece": "vertically stacked exploded view of a VR headset showing 9 distinct layers of internal components: outer shell, camera sensors, motherboard with chip, pancake lenses, internal frame, battery packs, side straps, top strap, and facial interface cushion.",
    "callout_labels": {
      "count": 8,
      "left_side": [
        "Snapdragon® XR2 Gen 2\n圧倒的な処理性能でリアルタイムな体験を。",
        "調整可能なIPD機構\n幅広いユーザーに快適なフィット感を。",
        "精密設計されたヘッドストラップ\n快適さと安定性を追求したエルゴノミクス。"
      ],
      "right_side": [
        "フェイスプレート\n洗練されたデザインと最適な重量バランス。",
        "トラッキングカメラ\n高精度な位置トラッキングと環境認識を実現。",
        "パンケーキレンズ\n薄型設計で広い視野角と鮮明な映像を提供。",
        "高性能バッテリー\n長時間駆動を支える最適化された電源設計。",
        "柔らかなフェイスインターフェース\n長時間でも快適な装着感を実現。"
      ]
    },
    "footer": {
      "left_text_block": {
        "headline": "{argument name=\"bottom headline\" default=\"体験は、構造から進化する。\"}",
        "body": "一つひとつのパーツに、没入体験を支える最先端テクノロジーとこだわりの設計。Meta Quest 3は、未来を感じさせる体験を内部から生み出しています。"
      },
      "right_logo": "∞ Meta"
    }
  }
}
```

### Case 168: [Luxury poster for fictional AI ad printer](https://x.com/nijisora_yuma/status/2049462065639858687) (by [@nijisora_yuma](https://x.com/nijisora_yuma))

| Output |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-prompts" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts/main/images/poster_case168/output.jpg" width="300" alt="Output image"></a> |

**Prompt:**

```
縦型3:4の、高級商業ポスターを制作してください。

テーマは、架空の新商品広告です。商品は「BRAND PRESS 01（ブランドプレス・ゼロワン）」という、Pollo AIを搭載した架空の広告ポスター生成プリンターです。

この商品は、まだ存在しないブランド名・商品ジャンル・世界観・ターゲット層を入力すると、Pollo AIがコピー、ビジュアル、レイアウトまで完成された商業広告ポスターを自動生成し、高精細な印刷物としてその場で出力する未来型プリンターです。単なるAIサービスの概念広告ではなく、実際に販売されていそうな架空商品の広告として成立させてください。

メインコンセプト: 「まだないブランドに、最初の一目惚れを。」

商品ビジュアル: 画面中央に実物の商品「BRAND PRESS 01」を大きく配置。未来型の高級プロ用印刷デバイスとして、黒い金属筐体、シルバーのエッジ、透明カバー、青白く発光するAIコア、精密な印刷ヘッド、ローラー、タッチパネル、排紙スロット、ポスター受けトレイを備える。排紙スロットから、架空の高級香水ブランド広告ポスターが紙として大きく出力されている構図。

構図: ややローアングル、斜め45度。背景は暗いネイビーから黒の高級広告制作スタジオ。映画的でドラマチックな高級プロダクト広告。

広告レイアウト: 上部に大きなキャッチコピー、中央にプリンター本体と排出中のポスター、右側に機能説明、左下に価格と発売日、下部にCTA。

入れる文字: 「まだないブランドに、最初の一目惚れを。」 / BRAND PRESS 01 / 「Pollo AI搭載・広告ポスター生成プリンター」 / 「名前だけのアイデアを、完成された商業ポスターとして出力。」 / 「構想、コピー、ビジュアル、印刷まで。1台で。」
```

<!-- Case 18: Luxury chocolate campaign system (by @SPEEDAI07) -->
### Case 18: [Luxury chocolate campaign system](https://x.com/SPEEDAI07/status/2049459155086500321) (by [@SPEEDAI07](https://x.com/SPEEDAI07))

| Output |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-prompts" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts/main/images/poster_case169/output.jpg" width="300" alt="Output image"></a> |

**Prompt:**

```
Create a premium, square (1:1) product advertisement for a fictional luxury chocolate brand called Noirvelle Chocolat, inspired by high-end chocolate brands. The ad should feel like a high-end editorial campaign, combining luxury food photography, refined packaging design, and cinematic lighting. Use matte black wrapper, subtle gold foil, elegant serif typography, and realistic product rendering. Generate flavor variants such as Blood Orange Noir, Salted Pistachio Muse, and Raspberry Ember with distinct mood, color palette, ingredients, headline, and supporting copy. Keep the chocolate bar as hero centerpiece with subtle reflections, shallow depth of field, luxury minimalism, and a small CTA: “Shop the drop.”
```

### Case 170: [Urban fruit juice ad poster](https://x.com/AIwithSarah_/status/2049452842931630202) (by [@AIwithSarah_](https://x.com/AIwithSarah_))

| Output |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-prompts" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts/main/images/poster_case170/output.jpg" width="300" alt="Output image"></a> |

**Prompt:**

```
Create a premium modern beverage advertisement poster in a vertical 3:4 format featuring a stylish young female model crouching confidently in a bright urban indoor hallway with colorful graffiti wall art on one side and clean minimal architecture on the other. In the foreground, a giant realistic fruit juice bottle is held toward the camera in forced perspective, with fictional branding like “VIVAJUICE”. Add brand logo, tagline, huge bold overlapping typography, four icon-based feature badges, and three smaller bottle variants at bottom right. Use soft natural lighting mixed with commercial studio polish, realistic shadows, shallow depth of field, glossy floor reflections, and a premium energetic eCommerce campaign aesthetic.
```



### Case 171: [Miniature City Diamond Necklace Ad](https://x.com/ChillaiKalan__/status/2053310109678535000) (by [@ChillaiKalan__](https://x.com/ChillaiKalan__/status/2053310109678535000))

| Output |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts/main/images/ad_case171/output.jpg" width="300" alt="Output image"></a> |

**Prompt:**

```
Create a hyper-detailed luxury advertising poster in a cinematic miniature-world style. A gigantic royal diamond necklace with intricate gold filigree and massive ruby gemstones stands in the center like an architectural monument. Surround the necklace with a futuristic miniature city built around and inside the jewelry piece, including skyscrapers, elevated highways, bridges, spiral staircases, tiny human figures, luxury billboards, drones, helicopters, and cinematic urban activity. Use a deep crimson red monochrome background with gold and ruby accents. Add premium fashion-ad aesthetics, ultra-realistic textures, glossy reflections, dramatic studio lighting, depth of field, tilt-shift miniature effect, and high-end commercial composition. Include bold elegant typography at the top saying: "EMBRACE THE EXTRAORDINARY". Style inspired by luxury jewelry campaigns, surreal city-building concepts, and premium 3D advertising renders. Ultra realistic, 8K, octane render, sharp focus, highly detailed, cinematic shadows, symmetrical composition.
```

### Case 172: [Watermelon Lime Beverage Ad Poster](https://x.com/ShamiWeb3/status/2053430685399232756) (by [@ShamiWeb3](https://x.com/ShamiWeb3/status/2053430685399232756))

| Output |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts/main/images/ad_case172/output.jpg" width="300" alt="Output image"></a> |

**Prompt:**

```
Create a premium modern beverage promotional poster for We Drink.

TOPIC:

Watermelon Pink + Lime Green Refresh Campaign

STYLE & ART DIRECTION:
Modern energetic beverage advertising
Youthful commercial branding
Split-color background composition
Bright refreshing summer aesthetic
Minimal dynamic layout
High-contrast drink advertisement style
Instagram-ready beverage promotion
Premium fast-moving commercial design

MAIN SUBJECT:

Two large ultra-realistic cold beverages positioned prominently in the center.

Drink 1:

A vibrant watermelon pink drink in a transparent plastic cup with visible ice cubes, condensation droplets, and a fresh watermelon garnish.

Drink 2:

A bright lime green drink in a matching transparent cup with visible ice cubes, condensation droplets, and a lime slice garnish.

Additional elements:

Floating ice cubes around the composition
Dynamic water splash effects
Soft realistic shadows beneath each cup
Premium glossy liquid textures
Tiny fruit slices suspended in motion

LAYOUT & COMPOSITION:
Diagonal split-color background
Left side: watermelon pink gradient
Right side: lime green gradient
Large bold headline at the top center: "SIP THE FRESHNESS"
Two hero drinks centered prominently
Product descriptions placed beside each cup
Promotional price section near the bottom-left
We Drink logo and small branding elements at the bottom
Floating ice cubes and splash effects around the drinks
Spacious modern commercial hierarchy

TEXT & TYPOGRAPHY:
Bold oversized sans-serif typography
Youthful rounded commercial fonts
White typography accents
Supporting text: "Watermelon Burst" and "Lime Rush"
Promotional price: Only $3.99
Tagline: "Freshness in Every Sip"

DEPTH & LIGHTING:
Soft glossy studio lighting
Bright refreshing reflections
Realistic beverage highlights
Floating commercial depth
Soft ambient shadows
Premium condensation texture lighting

EXTRA DESIGN DETAILS:
Floating ice cubes
Water splash particles
Glossy gradients
Modern promotional badges
Fruit slices and droplets
Minimal energetic decorative elements

COLOR PALETTE:
Watermelon Pink (#FF4F87)
Lime Green (#A8FF2A)
White typography
Soft transparent highlights

QUALITY:

Ultra-realistic beverage photography, premium advertising composition, Behance-quality commercial poster, high-resolution, sharp focus, photorealistic textures, professional brand campaign aesthetic.
```

### Case 173: [Berry Loud Acai Bowl Food Ad](https://x.com/Sairah_0/status/2053312926141005835) (by [@Sairah_0](https://x.com/Sairah_0/status/2053312926141005835))

| Output |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts/main/images/ad_case173/output.jpg" width="300" alt="Output image"></a> |

**Prompt:**

```
Prompt 1: Vibrant lifestyle food advertisement, smiling woman in a bright hot pink blazer sitting inside a colorful trendy café, holding a spoon and eating an acai berry bowl topped with strawberries, blueberries, banana slices, and granola, branded "Berry Loud" jar on wooden table, playful retro typography reading "BERRY LOUD" in large cream bubble letters, tropical café interior with hanging plants, warm natural sunlight, cheerful atmosphere, bold pink and teal color palette, shallow depth of field, cinematic food photography, ultra realistic, high detail, commercial ad campaign style, 4k

Prompt 2: Dynamic food product advertisement for "Berry Loud" mixed berry blend, acai smoothie bowl overflowing with strawberries, raspberries, blueberries, blackberries, banana slices, granola, dramatic berry juice splashes and floating fruits in mid air, branded jar beside bowl, vivid hot pink background, large retro cream typography saying "NEW DROP BERRY LOUD", glossy lighting, hyper realistic food photography, energetic composition, vibrant colors, commercial product shoot, ultra detailed textures, splash effect, studio lighting, 4k, advertising poster style
```

<!-- Case 20: Luxury Fragrance Campaign Portrait (by @amynys) -->

### Case 20: [Luxury Fragrance Campaign Portrait](https://x.com/amynys/status/2054340951678587051) (by [@amynys](https://x.com/amynys))

| Output |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts/main/images/ad-creative_case174/output.jpg" width="300" alt="GPT-Image-2 Prompt Example - Luxury Fragrance Campaign Portrait"></a> |

**Prompt:**

```
Transform the uploaded portrait into a luxurious cinematic fragrance poster inspired by the dark seductive elegance of a high-fashion perfume campaign. Preserve her exact facial features, warm skin tone, confident expression, wavy brunette hair, and recognizable identity. Style her as a mysterious femme fatale with soft glossy lips, luminous skin, subtle smoky eyes, and an intense captivating gaze.

Dress her in a black satin slip dress with delicate lace trim and a glamorous faux fur wrap slipping off her shoulders. Place her inside a moody Parisian-inspired luxury interior with black reflective walls, gold rim lighting, deep shadows, cinematic contrast, and sensual ambient lighting. Add elegant reflections and depth for a premium editorial look.

Include a sleek black perfume bottle inspired by a luxury noir fragrance aesthetic near the foreground. Use refined minimalist typography in a luxury fashion-ad style with dramatic spacing and premium composition. Add a tagline such as: “She doesn’t follow. She leaves a trace.”

The overall mood should feel seductive, mysterious, powerful, feminine, cinematic, timeless, and ultra-luxurious — like a Chanel Coco Noir campaign directed by a Hollywood cinematographer. High detail, photorealistic skin texture, glossy highlights, rich blacks, warm gold accents, magazine-quality fashion photography, 8K luxury editorial finish.
```

<!-- Case 21: Berry Splash Cafe Campaign (by @iamaiistudio) -->

### Case 21: [Berry Splash Cafe Campaign](https://x.com/iamaiistudio/status/2054248552294158350) (by [@iamaiistudio](https://x.com/iamaiistudio))

| Output |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts/main/images/ad-creative_case175/output.jpg" width="300" alt="GPT-Image-2 Prompt Example - Berry Splash Cafe Campaign"></a> |

**Prompt:**

```
Prompt 1:
Create a vibrant lifestyle food ad set inside a colorful, trendy cafe. Show a smiling woman in a bright hot pink blazer seated at a wooden table, lifting a spoon as she eats an acai berry bowl topped with strawberries, blueberries, banana slices, and granola. Keep a clearly branded "Berry Loud" jar on the table. Add playful retro cream bubble-letter typography that reads "BERRY LOUD". Use a tropical cafe interior with hanging plants, warm natural sunlight, a cheerful mood, a bold pink-and-teal palette, shallow depth of field, cinematic food-photography realism, high detail, and a polished commercial campaign finish. Format: vertical 9:16. Quality: ultra realistic, 4k.

Prompt 2:
Create a dynamic food product advertisement for "Berry Loud" mixed berry blend. Feature an acai smoothie bowl overflowing with strawberries, raspberries, blueberries, blackberries, banana slices, and granola. Surround it with dramatic berry juice splashes and floating fruit frozen midair. Place a branded jar next to the bowl. Use a vivid hot pink background and large retro cream typography that says "NEW DROP BERRY LOUD". Keep the lighting glossy, the composition energetic, the colors vibrant, the textures ultra detailed, and the overall look like a polished studio-shot commercial poster with hyper-realistic food photography and splash-effect motion. Format: vertical 9:16. Quality: 4k.
```

<!-- Case 22: Fast Food Hero Poster (by @ShamsAmin56) -->

### Case 22: [Fast Food Hero Poster](https://x.com/ShamsAmin56/status/2054238324198625780) (by [@ShamsAmin56](https://x.com/ShamsAmin56))

| Output |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts/main/images/ad-creative_case176/output.jpg" width="300" alt="GPT-Image-2 Prompt Example - Fast Food Hero Poster"></a> |

**Prompt:**

```
A cinematic 9:16 vertical composition featuring a gourmet "Smokey Obsidian" burger.
WHAT: A towering burger with a charcoal brioche bun, thick Wagyu beef patty with visible sear marks, melting aged gruyère dripping like lava, and crispy maple-glazed bacon.
FEEL: An atmosphere of "Urban Indulgence." Dark, moody lighting with a single warm amber spotlight. Wisps of real hickory smoke curl around the bun. The texture is hyper-realistic you can see the salt crystals on the crust and the moisture on the heirloom tomato.
SHOW: The burger is captured in a "deconstructed gravity" moment the top bun is slightly hovering, revealing the internal layers of house-made aioli and pickled red onions.
TYPOGRAPHY: Integration of ultra-bold, distressed sans-serif typeface overlapping the bottom third of the frame. The text reads "DEFY GRAVITY" in a raw, concrete-texture finish.
TECHNICAL: 4k resolution, macro photography style, shallow depth of field, neon-noir color grading (deep blacks, warm ambers, and subtle teal highlights).
```

<!-- Case 23: Matcha Granola Ad Poster (by @Sairah_0) -->

### Case 23: [Matcha Granola Ad Poster](https://x.com/Sairah_0/status/2054111354202779672) (by [@Sairah_0](https://x.com/Sairah_0))

| Output |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts/main/images/ad-creative_case177/output.jpg" width="300" alt="GPT-Image-2 Prompt Example - Matcha Granola Ad Poster"></a> |

**Prompt:**

```
(Matcha Granola Ad)

Ultra-realistic premium food advertisement poster for a healthy breakfast granola brand, centered matte pouch packaging labeled “Matcha Oat Granola”, green monochrome aesthetic, flat lay composition, soft studio lighting, vibrant matcha green background, surrounded by kiwi slices, almonds, oats, chia seeds, matcha powder bowl, granola bowls, scattered ingredients, clean modern typography headline “SUPERFOOD MORNING BOWL”, handwritten annotation arrows with wellness benefits, luxury organic branding, natural shadows, high-end commercial food photography, minimal yet detailed layout, symmetrical composition, sharp focus, Instagram ad style, 8k detail, healthy lifestyle marketing design.

Prompt : (Berry Yogurt Cereal Ad)

High-end commercial breakfast cereal advertisement, pastel pink aesthetic with centered standing pouch packaging labeled “Berry Yogurt Crunch Cereal”, surrounded by strawberries, blueberries, yogurt bowls, milk jug, crunchy granola, scattered berries and grains, soft natural lighting, vibrant fresh mood, modern bold typography headline “START FRESH EVERY MORNING”, handwritten callout arrows and benefit text, realistic food textures, luxury supermarket packaging design, clean flat lay composition, soft shadows, premium branding, glossy vibrant colors, ultra-detailed food photography, Instagram/Facebook ad campaign style, healthy breakfast concept, 8k realistic render.

Prompt : (Chocolate Protein Muesli Ad)

Premium protein breakfast food advertisement poster featuring centered pouch package labeled “Chocolate Protein Muesli”, rich brown monochrome theme, surrounded by dark chocolate chunks, almonds, oats, banana slices, milk jug, muesli bowls, scattered ingredients, dramatic warm studio lighting, bold modern headline typography “HIGH PROTEIN BREAKFAST FUEL”, handwritten annotation arrows highlighting benefits, luxury fitness breakfast branding, realistic textures, symmetrical flat lay composition, high-end commercial food photography, strong contrast, healthy energy concept, clean packaging mockup design, ultra-realistic 8k advertising render, cinematic food styling.
```

<!-- Case 24: Tropical Product Ad Poster (by @AIwithAliya) -->

### Case 24: [Tropical Product Ad Poster](https://x.com/AIwithAliya/status/2054553101236080714) (by [@AIwithAliya](https://x.com/AIwithAliya))

| Output |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts/main/images/ad-creative_case178/output.jpg" width="300" alt="GPT-Image-2 Prompt Example - Tropical Product Ad Poster"></a> |

**Prompt:**

```
GPT Image 2 Prompt Create a creative commercial advertising poster for [PRODUCT NAME], a [PRODUCT TYPE], inspired by vibrant tropical product campaigns. Place the product as a large hero object on the center-right with realistic glossy reflections, sharp label details, and premium lighting. Add a stylish model sitting beside or slightly in front of the product, naturally interacting with it by [MODEL ACTION]. The model should look [MOOD], wearing [OUTFIT STYLE], and should not cover the product label.
```

<!-- Case 25: Foam Clogs Ad Poster (by @Shinning1010) -->
### Case 25: [Foam Clogs Ad Poster](https://x.com/Shinning1010/status/2055688162333401470) (by [@Shinning1010](https://x.com/Shinning1010))

| Output |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts/main/images/ad-creative_case179/output.jpg" width="300" alt="Output image"></a> |

**Prompt:**

```
Create a premium vertical 4:5 commercial advertising poster for perforated foam clogs, making the shoes visually central, clean, and instantly legible. Use the uploaded portrait photo only for the woman’s appearance and hairstyle so the final result keeps a similar identity. Preserve face shape, facial features, hairstyle, skin tone, body proportion, and overall temperament only; do not copy the original expression, clothing, background, lighting, or pose. Style her in refined modern summer campaign wardrobe with effortless premium casual energy. Composition: a confident lifestyle fashion portrait with the woman seated or stepping forward in an airy sunlit architectural setting, the clogs clearly visible in the foreground and on-foot, showing their rounded shape, ventilation holes, heel strap, soft matte foam texture, and lightweight comfort. Atmosphere: elevated urban resort, fresh air, clean shadows, soft natural daylight, polished commercial photography, subtle water or glass reflections, crisp product detail, realistic skin texture, premium but approachable. Poster headline: “STEP INTO AIR”. Subtitle: “Lightweight comfort for every city moment.” Use clean modern typography with generous spacing, placed in reserved negative space without covering the face or shoes. No watermark.

Negative Prompt:
watermark, random text, misspelled headline, garbled letters, logo distortion, low quality, blurry, plastic skin, extra fingers, deformed hands, bad anatomy, overexposed highlights, unrealistic lighting, oversmoothed skin, cheap e-commerce look, AI-generated look, warped clog holes, incorrect shoe structure, melted foam texture, distorted heel strap, mismatched pair, hidden product, product cropped out, cluttered background
```

<!-- Case 26: Energy Drink Stadium Ad (by @Shorelyn_) -->
### Case 26: [Energy Drink Stadium Ad](https://x.com/Shorelyn_/status/2055570197973799376) (by [@Shorelyn_](https://x.com/Shorelyn_))

| Output |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts/main/images/ad-creative_case180/output.jpg" width="300" alt="Output image"></a> |

**Prompt:**

```
Ultra realistic premium product advertising shot of a sleek aluminum energy drink can standing upright on a wet reflective surface inside a futuristic football stadium at night. The can design features vivid swirling rainbow brushstroke patterns in red, orange, yellow, green, and blue wrapping around the entire can, with a large glossy black and white soccer ball graphic in the center. Bold white distressed typography on the front reads “GOAL” with smaller clean modern text below saying “ENERGY DRINK”. Tiny premium icon details for energy, focus, and endurance near the bottom, along with “250 ml”.

The can is covered in realistic cold water droplets and condensation, highly detailed metallic texture, cinematic reflections, ultra sharp focus, luxury beverage commercial aesthetic, professional studio lighting.

Background filled with explosive colorful powder smoke clouds in blue, red, orange, green, and yellow bursting dramatically behind the can, combined with glowing football stadium floodlights, floating particles, water splashes, sparks, mist, and bokeh light effects. Dark moody environment with intense contrast and neon glow atmosphere.

Composition centered and symmetrical, low angle hero shot, shallow depth of field, hyper realistic, cinematic color grading, ultra detailed advertising photography, sports branding campaign aesthetic, IMAX quality, 8k resolution, volumetric lighting, premium commercial product render, high energy dynamic mood.
```

### Case 181: [Sticker Reality Product Collage](https://x.com/oggii_0/status/2056061748806090940) (by [@oggii_0](https://x.com/oggii_0))

| Output |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-prompts" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts/main/images/ad-creative_case181/output.jpg" width="300" alt="Output image"></a> |

**Prompt:**

```
Edit this image while preserving the original subject, composition, and background.

Transform the scene into a “sticker reality” collage:

* Add elements that look like physical stickers, paper cutouts, and taped notes layered over the image
* Use slight misalignment and overlapping placement to create a natural scrapbook feel

Incorporate hand-drawn doodles mixed with sticker-like graphics such as icons, shapes, and labels.

Add subtle paper textures, torn edges, and tape details to enhance realism.

Ensure the product remains the main focal point while the collage elements build around it.

Balance the composition so it feels rich and layered but still visually pleasing, not cluttered.

The final result should feel like a real photo transformed into a creative scrapbook composition.
```

### Case 182: [Soft Serve Cozy Aesthetic](https://x.com/Sairah_0/status/2056060219361501319) (by [@Sairah_0](https://x.com/Sairah_0))

| Output |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-prompts" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts/main/images/ad-creative_case182/output.jpg" width="300" alt="Output image"></a> |

**Prompt:**

```
GPT Image 2 On ChatGPT

Prompt : (Soft Serve Ice Cream Aesthetic)

Close-up aesthetic photo of two hands holding vanilla soft serve ice cream cones, cozy warm cafe lighting, creamy texture, dreamy beige and brown color palette, shallow depth of field, soft bokeh background, kawaii doodle stickers and white hand-drawn illustrations around the image, cute cartoon kids and bunny characters, handwritten typography saying “Sweet Moments”, playful sparkles and hearts, cozy lifestyle photography, cinematic warm tones, Instagram story aesthetic, soft glow, realistic food photography, adorable scrapbook journal style, ultra detailed, high quality, vibrant yet soft editing, wholesome happy vibe.

Prompt : (Iced Coffee Cozy Aesthetic)

Close-up aesthetic shot of a hand holding iced coffee in a transparent branded cup, warm golden cafe ambience, creamy iced latte with ice cubes, cozy sunlight and soft bokeh background, cute white doodle overlays and handwritten text, kawaii cartoon boy and bunny stickers, scrapbook aesthetic, soft brown and green color palette, dreamy lifestyle photography, playful sparkles and hearts around the drink, “Good Vibes, Good Coffee” typography style, warm cinematic tones, ultra realistic beverage photography, cozy Instagram aesthetic, soft glow effect, highly detailed, cheerful and refreshing mood.
```


---
<!-- Case 27: Showroom Still Life Merch Drop (by @iamaiistudio) -->
### Case 27: [Showroom Still Life Merch Drop](https://x.com/iamaiistudio/status/2062279671618957656) (by [@iamaiistudio](https://x.com/iamaiistudio))

**Source**: [@iamaiistudio](https://x.com/iamaiistudio/status/2062279671618957656)

**Prompt**:
```
[BRAND NAME]. You are a Creative Director and Still Life Photographer for a high-fashion hypebeast magazine.

YOUR TASK:
Design a premium "Showroom Still Life" image to announce a limited merch drop for [BRAND NAME].

STEP 1: BRAND ANALYSIS
Study [BRAND NAME]: identify its industry and signature physical product (e.g., "Spalding" = basketballs, "McDonald's" = burger packaging, "Visa" = metal cards).
Choose the Color Palette:
- Background: a deep, rich, textured tone from the brand's secondary colors (Teal, Navy, Burgundy, or Slate Grey).
- Merch: a warm or neutral accent tone (Camel, Orange, or Cream) that pops against the backdrop.
- Apparel Piece: select something that fits the brand's energy (Varsity Letterman Jacket, Heavyweight Hoodie, Canvas Tote, or Wool Scarf).

STEP 2: SET DESIGN
Main Prop: a clean, modern White Powder-Coated Metal Rack or shelving unit.
Layout:
- The apparel piece hangs casually from the rack or a hanger, showing off its texture.
- On the rack shelves, stack several units of the brand's core product (e.g., basketballs, cans, boxes).
- Backdrop: hand-painted canvas in the chosen deep background color, with visible brushstrokes for that studio aesthetic.

STEP 3: BRANDING DETAILS
Apparel: feature premium physical branding via Chenille Patches, Embroidered Logos, or Screen Print on the sleeve or back. It should look like a genuinely expensive garment.
Products: ensure the [BRAND NAME] logo is clearly visible on all stacked items.

STEP 4: PHOTOGRAPHY
Lighting: soft, directional side window light with realistic soft shadows and rich texture highlights.
Focal length: 50mm or 85mm. Sharp focus on the merch, gentle background falloff.

STEP 5: GRAPHIC OVERLAY
Left-aligned composition:
- Large, clean white [BRAND NAME] logo placed in the negative space on the left.
- Beneath the logo, small white text with the brand's official tagline.
```

**Output**:

<img src="../images/ad-creative_case183/output.jpg" width="500">

---
<!-- Case 28: Adidas Futuristic Drop Ad Poster 9:16 (by @iamaiistudio) -->
### Case 28: [Adidas Futuristic Drop Ad Poster 9:16](https://x.com/iamaiistudio/status/2065133774413906004) (by [@iamaiistudio](https://x.com/iamaiistudio))

**Source**: [@iamaiistudio](https://x.com/iamaiistudio/status/2065133774413906004)

**Output:**

| Output |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="../images/ad-creative_case184/output.jpg" width="300" alt="GPT-Image-2 Prompt Example - Adidas Futuristic Drop Ad Poster 9:16"></a> |

**Prompt:**

```
Full prompt:

Design a striking premium vertical advertising poster (9:16 format) for a fictional ultra-limited Adidas sneaker called "ADIDAS AEROBLADE X - LIMITED DROP". The creative direction should feel like a world-class agency campaign — original, futuristic, visually explosive.

Main visual:
A single hero sneaker floating center-frame, captured at a dramatic low angle as if levitating above a dark obsidian running track split by glowing energy cracks. The shoe combines knit mesh, sculpted foam, translucent panels, reflective stripes, and a carbon-fiber sole plate. Neon light trails swirl around it like captured speed. Particles and mist add motion and intensity. Background features faint silhouettes of elite sprinters frozen mid-dash, blurred enough to keep focus on the shoe.

Color palette:
Matte black, electric red, silver, deep charcoal, with subtle neon blue highlights.

Typography and copy (sharp, clean, strong visual hierarchy):
Main headline: "OWN THE SPEED"
Product title: "ADIDAS AEROBLADE X"
Subheadline: "Built for the ones who never run ordinary."
Feature callouts in elegant boxed layout:
- "Featherlight Adaptive Knit Upper"
- "Carbon Energy Return Plate"
- "Precision Grip Traction"
- "Limited Collector Release"
Price: "$280"
Primary CTA: "DROP LIVE NOW"
Secondary CTA: "Only at
Footer text: "Performance innovation meets futuristic street identity."

Layout:
Bold oversized headline partially integrated into background. Product name near shoe in refined premium placement. Feature callouts stacked vertically along one side. Add a "LIMITED SERIES" badge. The composition blends luxury sports campaign with futuristic editorial design.

Style: Ultra-detailed hyper-realistic product photography, cinematic studio lighting, premium advertising aesthetics, sharp focus, rich textures, subtle atmosphere, dynamic motion energy, high-end commercial poster feel. Aspect ratio 9:16.

#AIart #GPTImage2
```

---
<!-- Case 29: Luxury Linen Texture Editorial Poster (by @ZephyraLeigh) -->
### Case 29: [Luxury Linen Texture Editorial Poster](https://x.com/ZephyraLeigh/status/2065123985713700925) (by [@ZephyraLeigh](https://x.com/ZephyraLeigh))

**Source**: [@ZephyraLeigh](https://x.com/ZephyraLeigh/status/2065123985713700925)

**Output:**

<table>
<tr><td width="50%"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="../images/ad-creative_case185/output.jpg" width="100%" alt="GPT-Image-2 Prompt Example - Luxury Linen Texture Editorial Poster"></a></td><td width="50%"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="../images/ad-creative_case185/output2.jpg" width="100%" alt="GPT-Image-2 Prompt Example - Luxury Linen Texture Editorial Poster"></a></td></tr>
</table>

**Prompt:**

```
GPT Image 2 on ChatGPT 🪄

PROMPT ⬇

A photorealistic luxury editorial poster, 3:4 portrait ratio. Full frame covered in premium off-white Italian linen paper wall texture — warm ivory tone, subtle grain, ultra-tactile surface. Center of wall features a large precision-carved football-shaped archway with deep architectural relief — visible carved edges, realistic inner shadow depth, sculptural beveled detailing, premium craftsmanship aesthetic.
Inside the carved football frame: cinematic stadium atmosphere — deep blue and white luxury smoke trails drifting elegantly, gold and silver championship confetti cascading, white orchid and rose floral arrangements with dark green foliage accents, premium celebration balloons in royal blue and pearl white, championship trophy silhouettes subtly embedded in background haze. Atmosphere: elite sports gala, UEFA Champions League victory night energy.

Subject: Cristiano Ronaldo, full figure, standing powerfully inside the carved frame. Wearing Portugal's premium crimson and green national kit — authentic jersey fabric with realistic textile folds, fitted athletic shorts, premium Adidas/Nike high-performance football boots. Iconic athletic build — broad shoulders, defined physique, elite footballer anatomy. Signature confident expression — sharp jaw, focused dark eyes, short textured dark hair, photorealistic skin texture with natural pore detail.

Championship celebration pose — chest slightly forward, chin raised, one hand slightly relaxed, football resting precisely at his right boot.

3D Breakout Effect: Face, right shoulder, right arm below elbow, and right football boot extend realistically beyond the carved frame boundary onto the wall surface — casting soft natural drop shadows onto the paper texture. Depth of field creates believable dimensional layering.
Lighting: Premium stadium tungsten lighting blended with warm golden-hour cinematic sunlight entering from the upper left. Soft white rim light wrapping around shoulders and jawline. Subtle fill light on the wall from the right. No harsh overexposure, no fake neon — only warm, editorial luxury light grading.

Wall Typography — Clean Minimalist Luxury Layout:

CRISTIANO RONALDO — large, bold, high-end serif font (Didot or Bodoni style), embossed gold foil effect, positioned above the carved frame

CHAPTER 41 — medium weight elegant tracking, warm bronze metallic tone, centered below the name

365 MORE DAYS OF GREATNESS — refined thin uppercase sans-serif, spaced wide, cream-gold color, placed below Chapter line
Technical: Ultra-photorealistic rendering, 8K detail sharpness, professional commercial sports photography quality, luxury magazine cover art direction, natural color grading — warm ivory + deep blue + gold palette, authentic shadow physics, zero AI artifacts, correct human anatomy, no extra limbs, no tree shadows, no distorted proportions, award-winning editorial masterpiece quality.
```

---
<!-- Case 30: Luxury Watch Dramatic Beam Product Shot (by @meng_dagg695) -->
### Case 30: [Luxury Watch Dramatic Beam Product Shot](https://x.com/meng_dagg695/status/2065078841765458040) (by [@meng_dagg695](https://x.com/meng_dagg695))

**Source**: [@meng_dagg695](https://x.com/meng_dagg695/status/2065078841765458040)

**Output:**

| Output |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="../images/ad-creative_case186/output.jpg" width="300" alt="GPT-Image-2 Prompt Example - Luxury Watch Dramatic Beam Product Shot"></a> |

**Prompt:**

```
A luxury watch emerges from darkness. Extreme macro shot of ticking gears and moving hands. Golden sparks and floating particles surround the watch. The camera circles the timepiece while dramatic light streaks reflect across the sapphire crystal. Slow-motion water splash freezes in midair around the watch. Mechanical components assemble themselves automatically. Cinematic black-and-gold environment, premium commercial lighting, ultra-realistic reflections, luxury lifestyle advertisement, powerful orchestral atmosphere, smooth camera motion, product hero shot, brand reveal, Hollywood-level commercial, 8K photorealism.
```

---
<!-- Case 31: 可口可乐百事雪碧品牌 KV 对比 (by @liyue_ai) -->
### Case 31: [可口可乐百事雪碧品牌 KV 对比](https://x.com/liyue_ai/status/2065039304175538382) (by [@liyue_ai](https://x.com/liyue_ai))

**Source**: [@liyue_ai](https://x.com/liyue_ai/status/2065039304175538382)

**Output:**

<table>
<tr><td width="50%"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="../images/ad-creative_case187/output.jpg" width="100%" alt="GPT-Image-2 Prompt Example - 可口可乐百事雪碧品牌 KV 对比"></a></td><td width="50%"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="../images/ad-creative_case187/output2.jpg" width="100%" alt="GPT-Image-2 Prompt Example - 可口可乐百事雪碧品牌 KV 对比"></a></td></tr>
<tr><td width="50%"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="../images/ad-creative_case187/output3.jpg" width="100%" alt="GPT-Image-2 Prompt Example - 可口可乐百事雪碧品牌 KV 对比"></a></td></tr>
</table>

**Prompt:**

```
品牌 KV 海报系列。使用统一提示词框架，针对不同饮料品牌调整视觉情绪色彩：可口可乐 → 热烈红色聚会感；百事可乐 → 年轻蓝色潮流感；雪碧 → 清爽绿色柠檬感。同一结构展现不同品牌 DNA。3 张对比输出。
```

---
<!-- Case 32: Luxury Sneaker Editorial Grid (by @iamaiistudio) -->
### Case 32: [Luxury Sneaker Editorial Grid](https://x.com/iamaiistudio/status/2065964253505585436) (by [@iamaiistudio](https://x.com/iamaiistudio))

**Source**: [@iamaiistudio](https://x.com/iamaiistudio/status/2065964253505585436)

**Output:**

| Output |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="../images/ad-creative_case188/output.jpg" width="300" alt="GPT-Image-2 Prompt Example"></a> |

**Prompt:**

```
Louis Vuitton luxury leather sneaker campaign. High-fashion editorial, avant-garde aesthetic. Aspect ratio 3:4.

Materials: Full-grain calf leather, Monogram Embossed Canvas, Polished Gold Hardware.
Color palette: Cognac Brown, Deep Obsidian, Champagne Gold.
Lighting: High-contrast Chiaroscuro with soft-box key lighting.

9-cell editorial grid:

Row 1, Heritage:
- Hero side-profile: sneaker resting on a vintage LV trunk, side-lit to reveal the leather grain texture.
- Extreme macro close-up: gold-tone "LV" lace aglets and precision stitching detail.
- Dynamic shot: gold dust particles swirling around the sole as the shoe steps into frame.

Row 2, Innovation:
- Minimalist: sneaker balanced on top of an abstract, floating glass "V" sculpture.
- Floating deconstructed view: sole and upper suspended in a void.
- Sensory: a gloved hand adjusting the tongue, highlighting the softness of the leather.

Row 3, Surrealism:
- Monochromatic scene in LV Havane brown with liquid silk drapes.
- Abstract: rubber sole pattern reimagined as a geometric desert landscape.
- Fusion: sneaker walking on a mirror-still lake reflecting a Parisian sunset skyline.
```

---
<!-- Case 33: Wireless Earbuds Lifestyle Ad (by @iamaiistudio) -->
### Case 33: [Wireless Earbuds Lifestyle Ad](https://x.com/iamaiistudio/status/2065753093283991651) (by [@iamaiistudio](https://x.com/iamaiistudio))

**Source**: [@iamaiistudio](https://x.com/iamaiistudio/status/2065753093283991651)

**Output:**

| Output |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="../images/ad-creative_case189/output.jpg" width="300" alt="GPT-Image-2 Prompt Example"></a> |

**Prompt:**

```
Design a 9:16 vertical product infographic for Bolt True Wireless Earbuds with a high-end lifestyle ad feel.
Composition & Framing
Full-body shot of a young woman whose face, skin tone, and hairstyle match the reference photo exactly
Slightly low camera angle close to the subject, fashion campaign style, for depth and visual presence
She's seated casually on the floor, one knee up, one leg stretched toward the camera
Foreground (Product)
She holds an open Bolt earbud charging case out toward the viewer
One earbud is visible inside the case, the other is in her ear
The case is glossy white with "BOLT" branding
Slight macro bokeh blur on the hand and case for cinematic depth
Outfit & Style
Modern athleisure streetwear: off-white or neutral lightweight jacket, crop top or sports bra, soft pink joggers, textured white sneakers
Expression: confident and relaxed, subtle smile
Pose feels natural and lifestyle-driven, not posed
Background
Soft gray gradient studio background
Rainbow prism lens flares and subtle light leaks
Floating blurred earbuds and case in background
Studio floor texture visible underfoot
Lighting
Diffused commercial studio lighting emphasizing skin texture, the glossy case, and fabric detail
Soft rim light to separate the subject from the background
Text Overlays (modern sans-serif, white)
Top Center: "BOLT" in large bold text, partially behind the subject
Top Right: Bolt Earbuds / True Wireless
Mid Left: Powerful sound. / Effortless vibes. / Engineered for every beat of your day.
Mid Right: 30 hours of playtime / IPX5 water resistant
Bottom Right: 1 year warranty
Quality
8K ultra-realistic commercial photography
Sharp on face and earbuds, gentle depth blur on foreground and background
Clean Apple/Nike premium ad aesthetic, strong negative space
```

<!-- Case 34: Kinder Joy Swing Chair Scene (by @iamaiistudio) -->
### Case 34: [Kinder Joy Swing Chair Scene](https://x.com/iamaiistudio/status/2066312771978092587) (by [@iamaiistudio](https://x.com/iamaiistudio))

| Output |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts/main/images/ad-creative_case190/output.jpg" width="300" alt="GPT-Image-2 Prompt Example - Kinder Joy Swing Chair Scene"></a> |

**Prompt:**

```
Hyper-realistic 8k medium shot photograph with shallow depth of field, surreal indoor scene with cinematic lighting. A normal-sized woman sits cross-legged inside a massive, highly detailed Kinder Joy egg that's been converted into a swing chair. The egg is split open, its white interior forming the seat and orange textured exterior visible, suspended by dark metal chains from a curved metal stand.

She wears a black t-shirt and blue-and-white plaid pajama pants, holding a small white teacup with both hands, gazing directly at the viewer with a calm, relaxed expression. Use uploaded face as reference.

On a polished wooden table to the left foreground: another gigantic fully wrapped Kinder Joy egg with intricate foil texture and branding details. To the right of the swing base: a vintage-style wooden radio with white dials, and a tiny bonsai tree in a small pot.

Soft warm directional lighting from the left casts subtle shadows, highlighting the detailed egg wrapper textures, clothing, and wooden surface. Background is a softly blurred warm-toned interior wall with pleasing bokeh. Standard lens, shot from mid-height.
```

<!-- Case 35: Invisible Shield Sunscreen Ad (by @iamrealsnow) -->
### Case 35: [Invisible Shield Sunscreen Ad](https://x.com/iamrealsnow/status/2066200217347854445) (by [@iamrealsnow](https://x.com/iamrealsnow))

<table>
<tr><td width="50%"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts/main/images/ad-creative_case191/output.jpg" width="100%" alt="GPT-Image-2 Prompt Example - Invisible Shield Sunscreen Ad"></a></td><td width="50%"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts/main/images/ad-creative_case191/output2.jpg" width="100%" alt="GPT-Image-2 Prompt Example - Invisible Shield Sunscreen Ad"></a></td></tr>
</table>

**Prompt:**

```
SUNSCREEN AD, “THE INVISIBLE SHIELD”

Luxury skincare advertising masterpiece, a colossal premium sunscreen bottle standing on a pristine tropical shoreline at golden hour, powerful beams of sunlight crashing down from the sky and splitting apart upon contact with a transparent protective energy dome radiating from the sunscreen, millions of sparkling UV particles dissolving into golden dust before reaching flawless skin, crystal clear ocean reflections, flowing water suspended in mid air around the product, microscopic droplets catching cinematic sunlight, ultra realistic textures revealing every detail of the bottle surface, luxury beauty campaign aesthetics, dramatic volumetric lighting, glowing atmospheric haze, premium white and gold color palette, futuristic protection technology visualized as elegant light waves, hyper detailed environment, commercial photography perfection, award winning advertising design, photorealistic rendering, 16K ultra resolution, global skincare brand campaign, masterpiece quality.

Text Overlay:
SUNSCREEN

Tagline:
“Protect Every Ray. Reveal Every Glow.
```

<!-- Case 36: Hidden Logo Landscape Illusion (by @iamaiistudio) -->
### Case 36: [Hidden Logo Landscape Illusion](https://x.com/iamaiistudio/status/2066191259354689714) (by [@iamaiistudio](https://x.com/iamaiistudio))

<table>
<tr><td width="50%"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts/main/images/ad-creative_case192/output.jpg" width="100%" alt="GPT-Image-2 Prompt Example - Hidden Logo Landscape Illusion"></a></td><td width="50%"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts/main/images/ad-creative_case192/output2.jpg" width="100%" alt="GPT-Image-2 Prompt Example - Hidden Logo Landscape Illusion"></a></td></tr>
</table>

**Prompt:**

```
Create a subliminal advertising landscape photograph where a recognizable brand logo (like the Apple logo, Nike swoosh, or Batman symbol) is secretly embedded into a breathtaking natural environment (like snowy mountains, dense jungle, sand dunes, or ocean coastline).

The logo must be formed entirely by the physical geography of the terrain — NOT overlaid digitally. The main body of the logo appears as a carved void (a deep valley, cliff edge, or sharp color contrast in the terrain), while any disconnected elements (like Apple's leaf) float as a suspended island of rock and earth in the misty sky above.

Camera: wide aerial drone shot, landscape stretching vast and majestic across the frame.

Atmosphere: dramatic and moody — heavy swirling clouds, rolling mist through valleys, crepuscular god rays bursting through gaps in the clouds, defining the hidden silhouette.

Visual rule: at first glance it must look like a 100% authentic nature photo. The brand logo only emerges as an optical illusion (pareidolia) on second look. Edges must be slightly jagged and organic, shaped by real geological features like cliff faces and treelines — never perfect vector shapes.

Lighting: high contrast between dark shadowed valleys (dense forests) and bright snow or sunlit highlights. Sun partially hidden behind clouds or the floating landmass, backlighting the entire scene.

Mood: cinematic, majestic, subtly surreal.

Output: 1:1 square, photorealistic, National Geographic aerial photography aesthetic.
```

<!-- Case 37: SPLASH Liquid Logo Fashion Poster (by @iamaiistudio) -->
### Case 37: [SPLASH Liquid Logo Fashion Poster](https://x.com/iamaiistudio/status/2065979523229975021) (by [@iamaiistudio](https://x.com/iamaiistudio))

| Output |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts/main/images/ad-creative_case193/output.jpg" width="300" alt="GPT-Image-2 Prompt Example - SPLASH Liquid Logo Fashion Poster"></a> |

**Prompt:**

```
Hyper-realistic fashion campaign poster for brand "SPLASH". A girl (matching the reference photo exactly, same face) seated confidently atop a gleaming, water-like 3D SPLASH logo surrounded by dynamic water splash effects. Editorial pose: one leg loose, one bent.

Enormous bold "SPLASH" typography fills the background, partially behind her. Small tagline reads: "Own Your Style."

Clothing: contemporary black streetwear (blazer, fitted top, trousers, sneakers).

Lighting: cinematic studio setup with soft key light and rim light, glossy reflections on the liquid logo.

Style: luxury fashion campaign aesthetic (Zara / H&M), polished clean environment.

Shot with an 85mm lens, shallow depth of field, 8K resolution, ultra-detailed, photorealistic.
```

<!-- Case 38: OBSIDIAN Coffee Brand Campaign (by @iamaiistudio) -->
### Case 38: [OBSIDIAN Coffee Brand Campaign](https://x.com/iamaiistudio/status/2066523210808484228) (by [@iamaiistudio](https://x.com/iamaiistudio))

| Output |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="../images/ad-creative_case194/output.jpg" width="300" alt="GPT-Image-2 Prompt Example - OBSIDIAN Coffee Brand Campaign"></a> |

**Prompt:**

```
Generate four cohesive high-end realistic editorial visuals for OBSIDIAN coffee brand. Cinematic, dark, mature aesthetic inspired by luxury sportswear and premium coffee advertising. Studio lighting that's dramatic yet controlled, photorealistic textures, clean compositional layout. Shot 1: Hero brand poster featuring 'OBSIDIAN' lettering with an artful coffee display — steam rising, beans scattered. Shot 2: Full product range — coffee bags, cans, and capsules arranged together. Shot 3: Tight packaging detail with tagline 'Coffee for grown-ups who chase flavor.' Shot 4: Lifestyle close-up of a steaming cup. Ultra-polished finish, crisp realistic materials, unified brand identity, no fantastical or surreal elements
```

<!-- Case 39: Coconut Paradise Skincare Ad (by @Strength04_X) -->
### Case 39: [Coconut Paradise Skincare Ad](https://x.com/Strength04_X/status/2067445760325734734) (by [@Strength04_X](https://x.com/Strength04_X))

| Output |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="../images/ad-creative_case195/output.jpg" width="300" alt="GPT-Image-2 Prompt Example - Coconut Paradise Skincare Ad"></a> |

**Prompt:**

```
Minimal white bottle with golden pump surrounded by cracked coconuts, coconut milk splash and foam clouds, tropical luxury spa atmosphere, creamy textures, realistic bubbles floating in background, premium skincare commercial, soft warm lighting, ultra detailed 8K.
```

<!-- Case 40: Reverse-Assembly Product VFX (by @iamaiistudio) -->
### Case 40: [Reverse-Assembly Product VFX](https://x.com/iamaiistudio/status/2067399156596175345) (by [@iamaiistudio](https://x.com/iamaiistudio))

<table>
<tr><td width="50%"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="../images/ad-creative_case196/output.jpg" width="100%" alt="GPT-Image-2 Prompt Example - Reverse-Assembly Product VFX"></a></td><td width="50%"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="../images/ad-creative_case196/output2.jpg" width="100%" alt="GPT-Image-2 Prompt Example - Reverse-Assembly Product VFX"></a></td></tr>
<tr><td width="50%"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="../images/ad-creative_case196/output3.jpg" width="100%" alt="GPT-Image-2 Prompt Example - Reverse-Assembly Product VFX"></a></td><td width="50%"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="../images/ad-creative_case196/output4.jpg" width="100%" alt="GPT-Image-2 Prompt Example - Reverse-Assembly Product VFX"></a></td></tr>
</table>

**Prompt:**

```
[PRODUCT] reassembling in midair from scattered pieces, reverse-disintegration effect, mechanical precision, each component suspended at a different depth, dark void background, high-concept product advertising, cinematic VFX.
```

<!-- Case 41: Grape Reveal Can Product Shot (by @iamaiistudio) -->
### Case 41: [Grape Reveal Can Product Shot](https://x.com/iamaiistudio/status/2067750180724855280) (by [@iamaiistudio](https://x.com/iamaiistudio))

| Output |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="../images/ad-creative_case197/output.jpg" width="300" alt="GPT-Image-2 Prompt Example - Grape Reveal Can Product Shot"></a> |

**Prompt:**

```
Product shot of a 330ml aluminum can called "VINE GLOW – Natural Extract" placed center-frame against a clean light grey studio background. The can is adorned with refined purple vine line illustrations. A dramatic horizontal torn paper reveal slices across the can and background, exposing glistening red and purple grapes inside, covered in water droplets with a glossy wet texture. Soft studio lighting, ultra-sharp focus, photorealistic commercial packaging photography, symmetrical layout, 8K resolution.
```

---
<!-- Case 42: Ray-Ban Giant Aviator Ad (by @MrDasOnX) -->
### Case 42: [Ray-Ban Giant Aviator Ad](https://x.com/MrDasOnX/status/2068024611074367579) (by [@MrDasOnX](https://x.com/MrDasOnX))

<table>
<tr><td width="50%"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="../images/ad-creative_case198/output.jpg" width="100%" alt="GPT-Image-2 Prompt Example - Ray-Ban Giant Aviator Ad"></a></td><td width="50%"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="../images/ad-creative_case198/output2.jpg" width="100%" alt="GPT-Image-2 Prompt Example - Ray-Ban Giant Aviator Ad"></a></td></tr>
</table>

**Prompt:**

```
Minimalist commercial ad featuring oversized Ray-Ban Aviator sunglasses, ultra-clean design. A young woman in all-white outfit leans casually against the giant sunglasses, relaxed confident pose, eyes closed, also holding a regular-sized pair in her hand. Soft gradient golden background with large bold white “RAY-BAN” text behind. Glossy reflective floor, soft studio lighting, modern high-end product photography. Small top-right text “Designed by Mr Das”. Bottom center tagline in small white font: “Iconic vision, every look.”
```

<!-- Case 43: Noir Elixir Perfume Ad (by @iamaiistudio) -->
### Case 43: [Noir Elixir Perfume Ad](https://x.com/iamaiistudio/status/2069238367792112016) (by [@iamaiistudio](https://x.com/iamaiistudio))

<table>
<tr><td width="50%"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="../images/ad-creative_case199/output.jpg" width="100%" alt="GPT-Image-2 Prompt Example - Noir Elixir Perfume Ad"></a></td><td width="50%"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="../images/ad-creative_case199/output2.jpg" width="100%" alt="GPT-Image-2 Prompt Example - Noir Elixir Perfume Ad"></a></td></tr>
</table>

**Prompt:**

```
Ultra-cinematic luxury fragrance advertising photography of "NOIR ÉLIXIR – Midnight Reserve" perfume bottle. Faceted geometric crystal bottle with sharp elegant edges, deep smoked black gradient glass, polished reflective surfaces with subtle matte facets. Magnetic brushed gold metal cap with engraved emblem. Minimal serif typography etched directly into glass with gold inlay. Dark amber liquid with golden undertones.

Bottle floats mid-air at a dramatic diagonal hero angle with slight forward tilt. Atomized perfume mist trails and fluid fragrance ribbons suspended in motion. Background: deep black velvet gradient fading into shadow. Surrounding elements: atomized perfume droplets suspended mid-air, shattered crystal glass fragments catching highlights, dark orchid petals drifting slowly, glossy black citrus peel curls, fine gold dust particles sparkling in light. Micro condensation beads and polished reflections enhancing realism.

Lighting: dramatic low-key studio with soft directional key light sculpting glass facets, strong rim lights outlining silhouette and edges, gold-toned specular highlights on cap and engraved details, deep cinematic shadows, high contrast with controlled reflections and luminous highlights.

Color palette: obsidian black, smoked charcoal, deep amber with metallic gold and warm champagne glow accents.

Macro cinema prime lens, shallow depth of field isolating product from background, smooth cinematic bokeh from reflective particles, extreme micro-detail clarity. 8K ultra high definition, hyper-realistic luxury commercial render, accurate glass refraction and internal reflections, physically accurate fluid dynamics, ultra-detailed crystal, metal, mist, and micro-droplet textures. Vertical 4:5 aspect ratio.
```
<!-- Case 44: Fluorescent Foam Logo Hero (by @iamaiistudio) -->
### Case 44: [Fluorescent Foam Logo Hero](https://x.com/iamaiistudio/status/2069135898265125326) (by [@iamaiistudio](https://x.com/iamaiistudio))

| Output |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="../images/ad-creative_case200/output.jpg" width="300" alt="GPT-Image-2 Prompt Example - Fluorescent Foam Logo Hero"></a> |

**Prompt:**

```
[BRAND NAME] | [COLOR]

CORE RULE: The fluid mass must take the exact shape of the [BRAND NAME] logo — not a circle, not a blob, not an oval. The outer silhouette of the fluid IS the logo outline, identical to the canonical trademark. If you cover the bubble texture and look only at the silhouette, you must immediately recognize [BRAND NAME]. This is the single most important rule and overrides everything else.

Create a hero image as a Macro Fluid Photographer and CGI Art Director: the brand logo formed entirely from living fluorescent foam and bubble liquid — as if poured into a logo-shaped mold on a black surface, captured at peak bubble activity. References: macro fluid photography, fluorescent paint foam art, soap bubble macro photography.

PHASE 0: LOGO GEOMETRY IS LAW
Use the 100% canonical [BRAND NAME] trademark silhouette — every curve, angle, and proportion exactly as trademarked. This silhouette is the rigid mold. The fluid fills its interior. The outer boundary of the fluid mass IS the logo outline — precise and hard. Gaps in the logo design show pure black background. No container (no circle, oval, badge, or frame). Correct canonical upright orientation — not rotated, flipped, or tilted. Zero fluid, bubbles, or droplets outside the logo boundary. When fluid physics conflict with logo geometry — geometry wins always. Apply [COLOR] as the fluid foam color throughout in maximum fluorescent saturation.

PHASE 1: FLUID MATERIAL
The logo is filled with a single viscous fluid in two physical states simultaneously. NOT water — thick, surface-tension-dominant, like fluorescent soap foam or colored slime. Base: [COLOR] at maximum fluorescent saturation, self-luminous, UV-reactive quality. Tonal variation within [COLOR] only: bubble membrane walls 35-45% lighter (near-transparent); mid-thickness zones pure saturated [COLOR]; deep liquid pools 25-35% darker. Liquid surface: high gloss, wet, shiny, broad specular reflection. Foam membranes: lower gloss, subtle soap film iridescence.

PHASE 2: BUBBLE ARCHITECTURE
Full size hierarchy across foam zone only. Large anchor bubbles 10-18mm, 4-8 count. Medium 4-9mm, 15-25 count. Small 1.5-3mm, 30-50 count. Micro 0.5-1mm, 50-100+ count. Each bubble: physically accurate air sphere in thin colored membrane 0.1-0.3mm thick, semi-transparent. Dome highlight: bright white crescent arc in upper-left, 15-20% of dome surface, soft-edged, white. Burst holes: 3-8 irregular dark voids in foam zone only, never at logo boundary edges.

PHASE 3: DUAL-STATE CONTRAST
Left zone — foam state: dense chaotic foam with full bubble hierarchy, strictly within logo silhouette, no bubbles at or beyond the edge. Right zone — liquid state: smooth continuous mass, bubbles absent (max 2-3 micro at transition edge), high gloss with broad soft specular highlight toward upper-left. Transition zone: 8-15mm wide gradual transition at vertical center. Both foam and liquid sides terminate exactly at the canonical logo outline — clean edge, no ragged silhouette. NO splatter, droplets, spray, or tendrils beyond the boundary.

PHASE 4: LIGHTING
Primary: large softbox upper-LEFT at 20-30 degrees from vertical, 5500K neutral white. Left and upper-left surfaces brighter, right relatively darker. All bubble dome highlights in upper-left. Liquid zone specular toward upper-left. Micro-shadows from bubbles fall lower-right, 0.5-1mm. Secondary: 8-10% cool ambient from above. No fill from right, no rim light, no colored light.

PHASE 5: COMPOSITION
Background: absolute black  zero texture, zero noise. Aspect ratio 1:1. Logo occupies 60-70% of frame, centered. Camera: directly overhead, perfectly perpendicular, zero perspective distortion, zero rotation. Pure top-down macro. Sharp depth of field across entire surface.

PHASE 6: TECH SPECS
Houdini FLIP fluid simulation + Redshift/Octane or equivalent photorealistic CGI. Fluid simulation domain bounded by logo silhouette — cannot escape boundary. Real FLIP geometry per bubble, not texture map. Bubble membranes: thin-shell geometry, IOR 1.33, transmission 0.7-0.85, thin-film iridescence. Liquid zone: smooth FLIP mesh, roughness 0.02-0.05. Foam: fluorescent shader, emissive 0.05-0.1, SSS 2-4mm. Area light 80x80cm upper-left 20-30 degrees, 5500K. HDRI ambient 8-10% neutral gray. Ray tracing 12+ bounces, caustics on, sampling 2048+, max anti-aliasing. No film grain, no post-process.

FINAL CHECK: (1) Does the fluid silhouette exactly match the [BRAND NAME] logo? (2) Is it inside a container? If yes, regenerate. (3) Any fluid outside the boundary? If yes, regenerate. (4) Both foam and liquid states visible? If no, regenerate.
```
<!-- Case 45: Glossier Brand World Collage (by @iamaiistudio) -->
### Case 45: [Glossier Brand World Collage](https://x.com/iamaiistudio/status/2069120574287392978) (by [@iamaiistudio](https://x.com/iamaiistudio))

| Output |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="../images/ad-creative_case201/output.jpg" width="300" alt="GPT-Image-2 Prompt Example - Glossier Brand World Collage"></a> |

**Prompt:**

```
Act as a world-class creative director, brand strategist, and editorial art director with deep expertise in high-impact campaign systems for global brands.

Create a bold, visually explosive, densely layered editorial moodboard collage that captures an entire brand identity system in a single frame. The result should feel raw, expressive, and intentionally chaotic, like a brand world exploding on the canvas.

BRAND INPUTS:

BRAND NAME: GLOSSIER
PRODUCT TYPE: beauty / skincare
PRIMARY COLOR: soft pink
SECONDARY COLOR: white
ACCENT: translucent gloss
PERSONALITY: fresh, minimal, youthful, clean
SLOGAN: SKIN FIRST

COMPOSITION:

Build a dense, overlapping collage that mixes:

• real product photography and lifestyle imagery
• packaging elements: bags, boxes, labels, stickers
• typography snippets and brand phrases
• hand-drawn doodles and illustrated graphics
• icons, symbols, and badge / stamp elements
• abstract blobs, squiggles, and starbursts
• UI-style cards, menus, and label panels
• editorial cutouts layered with depth

The layout should feel:

• asymmetrical, not grid-based
• intentionally messy but visually balanced
• like a Pinterest board crossed with a high-end campaign shoot
• expressive, youthful, and saturated with brand identity

VISUAL EXECUTION:

Include elements such as:

• product packaging mockups (bags, boxes, tags)
• a lifestyle shot of someone interacting with the brand
• bold headline typography blocks
• illustrated objects interacting with real photography
• merch items: t-shirt, tote bag, cap
• playful graphic overlays and brand-consistent texture

COLOR RULES:

• strictly adhere to the brand palette
• dominant use of soft pink throughout
• white for contrast and layering
• avoid introducing off-brand colors
• high contrast and visually commanding

TYPOGRAPHY:

• mix of editorial serif and clean sans-serif
• bold headlines paired with small UI-style text
• brand name and slogan integrated naturally into the layout

FINAL FEEL:

This must look like a creative direction board for a global campaign. Not a clean layout, not a grid, not minimal. It must feel alive, layered, and brand-heavy, a visual identity snapshot that is highly shareable and scroll-stopping.
```

<!-- Case 46: STARKIDZ Cosmic Telescope Ad (by @Strength04_X) -->
### Case 46: [STARKIDZ Cosmic Telescope Ad](https://x.com/Strength04_X/status/2069448983651787177) (by [@Strength04_X](https://x.com/Strength04_X))

| Output |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="../images/ad-creative_case202/output.jpg" width="300" alt="GPT-Image-2 Prompt Example - STARKIDZ Cosmic Telescope Ad"></a> |

**Prompt:**

```
A magical science advertisement poster. A curious young boy age 10 in a NASA tshirt gazes up in total wonder beside a giant shiny silver telescope 3x his height pointed toward a breathtaking galaxy view above, "STARKIDZ" written in glowing white font on the telescope body. Deep dark space background with milky way galaxy colorful nebula clouds and shooting stars. Glowing cosmic typography "STARKIDZ" in white and blue filling the background. Tagline bottom: "Explore the universe." Small text top-right corner reads "Designed with GPT Image 2" in grey. Photorealistic, magical kids science product commercial, dramatic deep space galaxy lighting.
```


<!-- Case 47: Monumental Timepiece Fashion Ad (by @iamaiistudio) -->
### Case 47: [Monumental Timepiece Fashion Ad](https://x.com/iamaiistudio/status/2069387162425205211) (by [@iamaiistudio](https://x.com/iamaiistudio))

| Output |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="../images/ad-creative_case203/output.jpg" width="300" alt="GPT-Image-2 Prompt Example - Monumental Timepiece Fashion Ad"></a> |

**Prompt:**

```
Oversized luxury wristwatch as a modern sculpture centerpiece, fashion model leaning against the dial face, monumental "TIME" typography looming in the background, deep emerald studio environment, reflective polished floor, Swiss high-end advertising aesthetic, cinematic editorial photography, ultra-clean minimalist composition, 1:1
```

---
<!-- Case 48: Doodle Escape Studio Sprint (by @john_my07) -->
### Case 48: [Doodle Escape Studio Sprint](https://x.com/john_my07/status/2071605998729740705) (by [@john_my07](https://x.com/john_my07))

<table>
<tr><td width="50%"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="../images/ad-creative_case204/output.jpg" width="100%" alt="GPT-Image-2 Prompt Example - Doodle Escape Studio Sprint"></a></td><td width="50%"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="../images/ad-creative_case204/output2.jpg" width="100%" alt="GPT-Image-2 Prompt Example - Doodle Escape Studio Sprint"></a></td></tr>
<tr><td width="50%"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="../images/ad-creative_case204/output3.jpg" width="100%" alt="GPT-Image-2 Prompt Example - Doodle Escape Studio Sprint"></a></td><td width="50%"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="../images/ad-creative_case204/output4.jpg" width="100%" alt="GPT-Image-2 Prompt Example - Doodle Escape Studio Sprint"></a></td></tr>
</table>

**Prompt:**

```
Create an ultra-realistic editorial studio photograph set against a smooth off-white seamless backdrop with a bright, airy minimalist aesthetic.

A fun-loving young woman with a pastel blue pixie cut is captured in a spontaneous moment of playful escape. She bursts into laughter while jogging forward, her smile wide and genuine, eyes nearly closed from amusement. Her posture shows energetic movement as she tries to continue running despite being gently held back, creating a humorous tug-of-war effect.

Pose & Movement

Natural mid-stride running motion.

One leg lifted slightly off the floor.

Arms moving freely with realistic running dynamics.

One hand confidently holding a vibrant rainbow spiral lollipop.

Subtle motion in the hair and clothing.

Strong sense of forward momentum with believable body mechanics.

Wardrobe

Loose oversized powder-blue sweatshirt.

Relaxed-fit beige trousers with wide legs.

Red checkerboard slip-on skate shoes.

Round eyeglasses casually resting atop her head rather than covering her eyes.

Doodle Character Interaction
A simple hand-drawn black doodle figure appears beside her, sketched in thick marker lines directly onto the photograph. The character features a round head, tiny dot eyes, and a straight neutral mouth.

The doodle extends an exaggerated arm that grips the back of the woman's sweatshirt, stretching the fabric noticeably as it attempts to stop her from getting away. The tension creates realistic folds and pull lines in the sweatshirt while subtly drawing her shoulders backward even as her body continues moving forward.

Small sketch-style motion marks around the doodle's arm suggest effort and resistance. Additional playful doodle accents around the woman's head emphasize her laughter, excitement, and movement.

Details

Anatomically accurate hands and fingers.

Clear visibility of both hands despite oversized sleeves.

Realistic grip and proportions on the lollipop.

Convincing fabric tension and clothing physics.

Bright high-key lighting with soft natural shadows.

Clean editorial lifestyle photography aesthetic.

Humorous visual storytelling.

Modern premium magazine-quality look.

Wholesome and playful mood.

Ultra-realistic textures, sharp focus, crisp detail, 8K resolution.

Vertical composition.
```

---
<!-- Case 49: Metro CCTV Thriller Frame (by @frametheory058) -->
### Case 49: [Metro CCTV Thriller Frame](https://x.com/frametheory058/status/2071605430858756121) (by [@frametheory058](https://x.com/frametheory058))

<table>
<tr><td width="50%"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="../images/ad-creative_case205/output.jpg" width="100%" alt="GPT-Image-2 Prompt Example - Metro CCTV Thriller Frame"></a></td><td width="50%"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="../images/ad-creative_case205/output2.jpg" width="100%" alt="GPT-Image-2 Prompt Example - Metro CCTV Thriller Frame"></a></td></tr>
<tr><td width="50%"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="../images/ad-creative_case205/output3.jpg" width="100%" alt="GPT-Image-2 Prompt Example - Metro CCTV Thriller Frame"></a></td><td width="50%"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=awesome-gpt-image-2-API-and-Prompts" target="_blank" rel="noopener noreferrer"><img src="../images/ad-creative_case205/output4.jpg" width="100%" alt="GPT-Image-2 Prompt Example - Metro CCTV Thriller Frame"></a></td></tr>
</table>

**Prompt:**

```
Create a cinematic surveillance-thriller image set inside a massive multi-level underground metro station. The camera should feel like a ceiling-mounted CCTV positioned high above at roughly a 40-degree angle, looking down over a long industrial escalator and the complex architecture of the station.
The composition should use a 4:5 vertical frame, with the escalator cutting diagonally through the image to create strong depth and scale. The station is crowded with hundreds of commuters moving in both directions, forming a chaotic flow of people with subtle motion blur.
At the center of the frame, a single person matching the uploaded reference image is descending the escalator. The subject appears to be moving quickly, slightly leaning forward. One hand holds the escalator handrail for balance, while the other carries a small glossy black mini bag with realistic reflections.
At a dramatic moment, the subject suddenly turns their head over their shoulder and looks directly into the camera, creating an intense fourth-wall-breaking moment, as if they know they are being watched.
Add a realistic CCTV interface overlay, including:
Live recording indicators
Timestamp and camera ID
A facial-tracking square locked onto the subject
A secondary zoomed-in facial recognition panel in one corner
Minimal technical HUD elements and surveillance graphics
Lighting should be cold and fluorescent, typical of a modern subway station, with realistic reflections on the metallic escalator surfaces and polished handrails. Keep the surrounding crowd slightly blurred while the subject remains sharp and in focus.
Overall mood: high-end documentary surveillance thriller, ultra-photorealistic, cinematic composition, realistic skin textures, natural crowd behavior, detailed environmental reflections, and professional movie-grade realism.
```
