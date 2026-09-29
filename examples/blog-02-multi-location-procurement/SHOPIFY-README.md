# Shopify install — Multi-Location Cleaning Supply Procurement: How to Run One Wipe Program Across Every Site

## Install
1. Themes > Edit code > `sections/` > Add a new section > name `Wipex Multi-Location` > paste
   `sections/wipex-section-multi-location-procurement-2026.liquid`. Save.
2. `snippets/wipex-blog-schema.liquid` > Add a new snippet with that exact name > paste. Save.
3. `theme.liquid` > before `</head>` add:
   {%- if article and article.handle == 'multi-location-cleaning-supply-procurement' -%}{{ render 'wipex-blog-schema' }}{%- endif -%}
4. `templates/` > Add a new template > article > name it `multi-location-cleaning-supply-procurement` > paste
   `templates/article.multi-location-procurement.json`. Save.
5. Assign the template to the post, or add the section to the post's template in the theme editor.
6. Leave the blog post BODY empty — the section renders the whole article. Anything in the body
   renders twice.

## In the theme editor
Hero (eyebrow/H1/intro/two CTAs) · three editorial stills with alt, caption and focal point · one
native video band with fallback + optional overlay · sticky mobile CTA. Everything else in the
article is generated prose and is read-only by design.

## Pre-publish verification
- [ ] section saves without a validation error (schema name <= 25 chars, <= 40 settings)
- [ ] no JSON-LD inside the section file (`wipex-section-multi-location-procurement-2026`): @type keys count as settings
- [ ] page renders once (body empty), no duplicate H1
- [ ] checklist ticks persist after a reload
- [ ] calculator updates on input, on mobile too
- [ ] sticky CTA appears after the hero and hides over the final CTA
- [ ] images carry the supplied alt text; empty slots render nothing
- [ ] Rich Results test: BlogPosting + FAQPage + Product + BreadcrumbList, no duplicates
- [ ] `SECTION-VALIDATION.txt` in this folder reports "none"

## Troubleshooting
| Symptom | Cause | Fix |
|---|---|---|
| "too many settings" on save | JSON-LD left inside the section | keep it in the snippet only |
| section name rejected | name > 25 chars | shorten the name |
| article renders twice | body not empty | clear the post body |
| no styles | theme strips section styles | add the CSS to theme CSS, keep the markup |
| checklist does not persist | browser blocks localStorage | expected in private mode |
