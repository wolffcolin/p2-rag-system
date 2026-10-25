# Ingest report

Written by `uv run p2 ingest`.
It lists every document in this corpus that ingest added, with what the cleaning pass did and anything that looks wrong.
Running ingest again adds to the table and replaces the "last run" section, and `uv run p2 ingest --report` rewrites it for the documents in docs/ now, after you removed some.

## Summary

- Documents: 264 (the final check needs at least 200)
- Words: 279,709
- Estimated tokens (words times 1.4): 391,592 (`p2 check` warns above 800,000 and fails above 1,000,000)
- Flagged documents: 0

## Documents

| docid | words | characters per page | flags | cleaning |
|---|---:|---:|---|---|
| `mcs2023-abrasives` | 1,043 | 3528 | - | - |
| `mcs2023-aluminum` | 1,138 | 3849 | - | - |
| `mcs2023-antimony` | 872 | 2909 | - | - |
| `mcs2023-arsenic` | 1,123 | 3910 | - | - |
| `mcs2023-asbestos` | 1,385 | 4660 | - | - |
| `mcs2023-barite` | 1,086 | 3558 | - | - |
| `mcs2023-bauxite-alumina` | 1,054 | 3556 | - | - |
| `mcs2023-beryllium` | 1,153 | 3820 | - | - |
| `mcs2023-bismuth` | 1,041 | 3465 | - | - |
| `mcs2023-boron` | 1,083 | 3610 | - | - |
| `mcs2023-bromine` | 1,032 | 3528 | - | - |
| `mcs2023-cadmium` | 1,114 | 3736 | - | - |
| `mcs2023-cement` | 1,161 | 4042 | - | - |
| `mcs2023-cesium` | 1,433 | 4837 | - | - |
| `mcs2023-chromium` | 978 | 3399 | - | - |
| `mcs2023-clays` | 973 | 3072 | - | - |
| `mcs2023-cobalt` | 1,079 | 3784 | - | - |
| `mcs2023-copper` | 1,276 | 4159 | - | - |
| `mcs2023-diamond` | 1,097 | 3610 | - | - |
| `mcs2023-diatomite` | 821 | 2694 | - | - |
| `mcs2023-feldspar` | 839 | 2803 | - | - |
| `mcs2023-fluorspar` | 1,140 | 3768 | - | - |
| `mcs2023-gallium` | 1,278 | 4472 | - | - |
| `mcs2023-garnet` | 1,048 | 3528 | - | - |
| `mcs2023-gemstones` | 995 | 3424 | - | - |
| `mcs2023-germanium` | 998 | 3384 | - | - |
| `mcs2023-gold` | 1,129 | 3623 | - | - |
| `mcs2023-graphite` | 1,021 | 3502 | - | - |
| `mcs2023-gypsum` | 945 | 3212 | - | - |
| `mcs2023-helium` | 1,216 | 3899 | - | - |
| `mcs2023-indium` | 1,015 | 3302 | - | - |
| `mcs2023-iodine` | 740 | 2432 | - | - |
| `mcs2023-iron-ore` | 1,158 | 3742 | - | - |
| `mcs2023-iron-oxide-pigments` | 878 | 2904 | - | - |
| `mcs2023-iron-steel` | 961 | 3079 | - | - |
| `mcs2023-iron-steel-scrap` | 1,266 | 4001 | - | - |
| `mcs2023-iron-steel-slag` | 1,227 | 3830 | - | - |
| `mcs2023-kyanite` | 1,062 | 3574 | - | - |
| `mcs2023-lead` | 908 | 2918 | - | - |
| `mcs2023-lime` | 800 | 2713 | - | - |
| `mcs2023-lithium` | 1,198 | 4230 | - | - |
| `mcs2023-magnesium-compounds` | 1,027 | 3585 | - | - |
| `mcs2023-magnesium-metal` | 1,182 | 3864 | - | - |
| `mcs2023-manganese` | 936 | 3202 | - | - |
| `mcs2023-mercury` | 1,137 | 2607 | - | - |
| `mcs2023-mica` | 988 | 3268 | - | - |
| `mcs2023-molybdenum` | 1,023 | 3558 | - | - |
| `mcs2023-nickel` | 1,057 | 3688 | - | - |
| `mcs2023-niobium` | 943 | 3208 | - | - |
| `mcs2023-nitrogen` | 880 | 2936 | - | - |
| `mcs2023-peat` | 934 | 3052 | - | - |
| `mcs2023-perlite` | 767 | 2540 | - | - |
| `mcs2023-phosphate` | 865 | 2981 | - | - |
| `mcs2023-platinum-group` | 904 | 3252 | - | - |
| `mcs2023-potash` | 1,251 | 4052 | - | - |
| `mcs2023-pumice` | 773 | 2538 | - | - |
| `mcs2023-quartz` | 868 | 2996 | - | - |
| `mcs2023-rare-earths` | 910 | 3040 | - | - |
| `mcs2023-rhenium` | 1,169 | 4100 | - | - |
| `mcs2023-rubidium` | 1,066 | 3752 | - | - |
| `mcs2023-salt` | 995 | 3258 | - | - |
| `mcs2023-sand-gravel` | 939 | 3220 | - | - |
| `mcs2023-sand-industrial` | 1,113 | 3763 | - | - |
| `mcs2023-scandium` | 1,114 | 3846 | - | - |
| `mcs2023-selenium` | 1,125 | 3776 | - | - |
| `mcs2023-silicon` | 926 | 3112 | - | - |
| `mcs2023-silver` | 1,092 | 3640 | - | - |
| `mcs2023-soda-ash` | 1,031 | 3346 | - | - |
| `mcs2023-stone-crushed` | 1,001 | 3422 | - | - |
| `mcs2023-stone-dimension` | 882 | 2912 | - | - |
| `mcs2023-strontium` | 1,013 | 3460 | - | - |
| `mcs2023-sulfur` | 1,015 | 3313 | - | - |
| `mcs2023-talc` | 914 | 3038 | - | - |
| `mcs2023-tantalum` | 1,038 | 3524 | - | - |
| `mcs2023-tellurium` | 1,305 | 4329 | - | - |
| `mcs2023-thallium` | 987 | 3376 | - | - |
| `mcs2023-thorium` | 1,026 | 3604 | - | - |
| `mcs2023-tin` | 1,077 | 3484 | - | - |
| `mcs2023-titanium` | 1,097 | 3732 | - | - |
| `mcs2023-titanium-minerals` | 932 | 3147 | - | - |
| `mcs2023-tungsten` | 1,044 | 3658 | - | - |
| `mcs2023-vanadium` | 1,122 | 3865 | - | - |
| `mcs2023-vermiculite` | 795 | 2674 | - | - |
| `mcs2023-wollastonite` | 1,075 | 3798 | - | - |
| `mcs2023-yttrium` | 1,122 | 4002 | - | - |
| `mcs2023-zeolites` | 1,066 | 3690 | - | - |
| `mcs2023-zinc` | 1,120 | 3612 | - | - |
| `mcs2023-zirconium-hafnium` | 1,062 | 3734 | - | - |
| `mcs2024-abrasives` | 1,043 | 3519 | - | - |
| `mcs2024-aluminum` | 1,094 | 3709 | - | - |
| `mcs2024-antimony` | 833 | 2814 | - | - |
| `mcs2024-arsenic` | 1,170 | 4076 | - | - |
| `mcs2024-asbestos` | 1,318 | 4470 | - | - |
| `mcs2024-barite` | 948 | 3162 | - | - |
| `mcs2024-bauxite-alumina` | 1,054 | 3523 | - | - |
| `mcs2024-beryllium` | 1,154 | 3864 | - | - |
| `mcs2024-bismuth` | 1,022 | 3406 | - | - |
| `mcs2024-boron` | 1,184 | 3904 | - | - |
| `mcs2024-bromine` | 1,050 | 3515 | - | - |
| `mcs2024-cadmium` | 1,125 | 3782 | - | - |
| `mcs2024-cement` | 1,237 | 4303 | - | - |
| `mcs2024-cesium` | 1,457 | 4932 | - | - |
| `mcs2024-chromium` | 915 | 3152 | - | - |
| `mcs2024-clays` | 969 | 3002 | - | - |
| `mcs2024-cobalt` | 1,063 | 3741 | - | - |
| `mcs2024-copper` | 1,243 | 4074 | - | - |
| `mcs2024-diamond` | 1,094 | 3598 | - | - |
| `mcs2024-diatomite` | 863 | 2854 | - | - |
| `mcs2024-feldspar` | 814 | 2742 | - | - |
| `mcs2024-fluorspar` | 1,003 | 3380 | - | - |
| `mcs2024-gallium` | 1,236 | 4292 | - | - |
| `mcs2024-garnet` | 1,062 | 3578 | - | - |
| `mcs2024-gemstones` | 1,036 | 3579 | - | - |
| `mcs2024-germanium` | 1,122 | 3874 | - | - |
| `mcs2024-gold` | 1,136 | 3684 | - | - |
| `mcs2024-graphite` | 1,145 | 3838 | - | - |
| `mcs2024-gypsum` | 961 | 3262 | - | - |
| `mcs2024-helium` | 1,406 | 4490 | - | - |
| `mcs2024-indium` | 1,186 | 3901 | - | - |
| `mcs2024-iodine` | 719 | 2359 | - | - |
| `mcs2024-iron-ore` | 1,200 | 3904 | - | - |
| `mcs2024-iron-oxide-pigments` | 869 | 2878 | - | - |
| `mcs2024-iron-steel` | 1,105 | 3538 | - | - |
| `mcs2024-iron-steel-scrap` | 1,268 | 4034 | - | - |
| `mcs2024-iron-steel-slag` | 1,306 | 4086 | - | - |
| `mcs2024-kyanite` | 1,085 | 3664 | - | - |
| `mcs2024-lead` | 918 | 2918 | - | - |
| `mcs2024-lime` | 775 | 2649 | - | - |
| `mcs2024-lithium` | 1,209 | 4265 | - | - |
| `mcs2024-magnesium-compounds` | 1,128 | 3918 | - | - |
| `mcs2024-magnesium-metal` | 1,281 | 4156 | - | - |
| `mcs2024-manganese` | 930 | 3200 | - | - |
| `mcs2024-mercury` | 1,064 | 3686 | - | - |
| `mcs2024-mica` | 1,028 | 3384 | - | - |
| `mcs2024-molybdenum` | 1,056 | 3662 | - | - |
| `mcs2024-nickel` | 1,101 | 3866 | - | - |
| `mcs2024-niobium` | 1,018 | 3494 | - | - |
| `mcs2024-nitrogen` | 896 | 2982 | - | - |
| `mcs2024-peat` | 1,054 | 3456 | - | - |
| `mcs2024-perlite` | 802 | 2642 | - | - |
| `mcs2024-phosphate` | 968 | 3302 | - | - |
| `mcs2024-platinum-group` | 935 | 3322 | - | - |
| `mcs2024-potash` | 1,097 | 3568 | - | - |
| `mcs2024-pumice` | 775 | 2544 | - | - |
| `mcs2024-quartz` | 1,184 | 4050 | - | - |
| `mcs2024-rare-earths` | 904 | 3050 | - | - |
| `mcs2024-rhenium` | 1,085 | 3854 | - | - |
| `mcs2024-rubidium` | 1,097 | 3858 | - | - |
| `mcs2024-salt` | 948 | 3126 | - | - |
| `mcs2024-sand-gravel` | 977 | 3332 | - | - |
| `mcs2024-sand-industrial` | 989 | 3324 | - | - |
| `mcs2024-scandium` | 1,061 | 3636 | - | - |
| `mcs2024-selenium` | 1,079 | 3658 | - | - |
| `mcs2024-silicon` | 1,016 | 3308 | - | - |
| `mcs2024-silver` | 1,136 | 3839 | - | - |
| `mcs2024-soda-ash` | 972 | 3174 | - | - |
| `mcs2024-stone-crushed` | 1,038 | 3553 | - | - |
| `mcs2024-stone-dimension` | 934 | 3092 | - | - |
| `mcs2024-strontium` | 1,098 | 3784 | - | - |
| `mcs2024-sulfur` | 1,003 | 3291 | - | - |
| `mcs2024-talc` | 1,007 | 3275 | - | - |
| `mcs2024-tantalum` | 1,057 | 3652 | - | - |
| `mcs2024-tellurium` | 1,173 | 3918 | - | - |
| `mcs2024-thallium` | 1,065 | 3638 | - | - |
| `mcs2024-thorium` | 937 | 3290 | - | - |
| `mcs2024-tin` | 1,038 | 3390 | - | - |
| `mcs2024-titanium` | 1,047 | 3549 | - | - |
| `mcs2024-titanium-minerals` | 894 | 3006 | - | - |
| `mcs2024-tungsten` | 1,008 | 3524 | - | - |
| `mcs2024-vanadium` | 1,174 | 4016 | - | - |
| `mcs2024-vermiculite` | 795 | 2640 | - | - |
| `mcs2024-wollastonite` | 1,048 | 3728 | - | - |
| `mcs2024-yttrium` | 1,100 | 3945 | - | - |
| `mcs2024-zeolites` | 1,097 | 3792 | - | - |
| `mcs2024-zinc` | 1,099 | 3593 | - | - |
| `mcs2024-zirconium-hafnium` | 1,073 | 3774 | - | - |
| `mcs2025-abrasives` | 985 | 3330 | - | - |
| `mcs2025-aluminum` | 1,083 | 3642 | - | - |
| `mcs2025-antimony` | 880 | 2972 | - | - |
| `mcs2025-arsenic` | 1,200 | 4235 | - | - |
| `mcs2025-asbestos` | 1,285 | 4380 | - | - |
| `mcs2025-barite` | 1,003 | 3320 | - | - |
| `mcs2025-bauxite-alumina` | 1,048 | 3522 | - | - |
| `mcs2025-beryllium` | 1,166 | 3910 | - | - |
| `mcs2025-bismuth` | 1,033 | 3414 | - | - |
| `mcs2025-boron` | 1,151 | 3802 | - | - |
| `mcs2025-bromine` | 1,171 | 3944 | - | - |
| `mcs2025-cadmium` | 1,103 | 3660 | - | - |
| `mcs2025-cement` | 1,281 | 4394 | - | - |
| `mcs2025-cesium` | 1,490 | 5080 | - | - |
| `mcs2025-chromium` | 960 | 3334 | - | - |
| `mcs2025-clays` | 963 | 2997 | - | - |
| `mcs2025-cobalt` | 1,010 | 3580 | - | - |
| `mcs2025-copper` | 1,274 | 4160 | - | - |
| `mcs2025-diamond` | 1,094 | 3587 | - | - |
| `mcs2025-diatomite` | 905 | 2968 | - | - |
| `mcs2025-feldspar` | 799 | 2667 | - | - |
| `mcs2025-fluorspar` | 1,127 | 3698 | - | - |
| `mcs2025-gallium` | 1,202 | 4160 | - | - |
| `mcs2025-garnet` | 1,064 | 3592 | - | - |
| `mcs2025-gemstones` | 1,067 | 3645 | - | - |
| `mcs2025-germanium` | 1,265 | 4331 | - | - |
| `mcs2025-gold` | 1,146 | 3702 | - | - |
| `mcs2025-graphite` | 1,189 | 3926 | - | - |
| `mcs2025-gypsum` | 965 | 3274 | - | - |
| `mcs2025-helium` | 1,373 | 4340 | - | - |
| `mcs2025-indium` | 1,234 | 4008 | - | - |
| `mcs2025-iodine` | 738 | 2410 | - | - |
| `mcs2025-iron-ore` | 1,211 | 4009 | - | - |
| `mcs2025-iron-oxide-pigments` | 817 | 2724 | - | - |
| `mcs2025-iron-steel` | 1,017 | 3268 | - | - |
| `mcs2025-iron-steel-scrap` | 1,302 | 4186 | - | - |
| `mcs2025-iron-steel-slag` | 1,466 | 4574 | - | - |
| `mcs2025-kyanite` | 1,159 | 3944 | - | - |
| `mcs2025-lead` | 843 | 2670 | - | - |
| `mcs2025-lime` | 760 | 2602 | - | - |
| `mcs2025-lithium` | 1,242 | 4388 | - | - |
| `mcs2025-magnesium-compounds` | 990 | 3440 | - | - |
| `mcs2025-magnesium-metal` | 1,104 | 3569 | - | - |
| `mcs2025-manganese` | 1,002 | 3437 | - | - |
| `mcs2025-mercury` | 1,074 | 3692 | - | - |
| `mcs2025-mica` | 1,099 | 3634 | - | - |
| `mcs2025-molybdenum` | 1,083 | 3746 | - | - |
| `mcs2025-nickel` | 989 | 3475 | - | - |
| `mcs2025-niobium` | 958 | 3330 | - | - |
| `mcs2025-nitrogen` | 875 | 2914 | - | - |
| `mcs2025-peat` | 1,115 | 3666 | - | - |
| `mcs2025-perlite` | 912 | 2964 | - | - |
| `mcs2025-phosphate` | 952 | 3258 | - | - |
| `mcs2025-platinum-group` | 947 | 3352 | - | - |
| `mcs2025-potash` | 1,050 | 3473 | - | - |
| `mcs2025-pumice` | 764 | 2506 | - | - |
| `mcs2025-quartz` | 1,256 | 4270 | - | - |
| `mcs2025-rare-earths` | 940 | 3210 | - | - |
| `mcs2025-rhenium` | 1,055 | 3764 | - | - |
| `mcs2025-rubidium` | 1,209 | 4280 | - | - |
| `mcs2025-salt` | 959 | 3173 | - | - |
| `mcs2025-sand-gravel` | 1,059 | 3582 | - | - |
| `mcs2025-sand-industrial` | 1,125 | 3780 | - | - |
| `mcs2025-scandium` | 989 | 3434 | - | - |
| `mcs2025-selenium` | 1,237 | 4170 | - | - |
| `mcs2025-silicon` | 1,074 | 3447 | - | - |
| `mcs2025-silver` | 1,074 | 3614 | - | - |
| `mcs2025-soda-ash` | 1,035 | 3355 | - | - |
| `mcs2025-stone-crushed` | 1,091 | 3680 | - | - |
| `mcs2025-stone-dimension` | 1,040 | 3447 | - | - |
| `mcs2025-strontium` | 1,032 | 3572 | - | - |
| `mcs2025-sulfur` | 1,005 | 3283 | - | - |
| `mcs2025-talc` | 984 | 3228 | - | - |
| `mcs2025-tantalum` | 1,087 | 3697 | - | - |
| `mcs2025-tellurium` | 1,253 | 4186 | - | - |
| `mcs2025-thallium` | 974 | 3356 | - | - |
| `mcs2025-thorium` | 907 | 3171 | - | - |
| `mcs2025-tin` | 1,016 | 3360 | - | - |
| `mcs2025-titanium` | 1,017 | 3399 | - | - |
| `mcs2025-titanium-minerals` | 879 | 2971 | - | - |
| `mcs2025-tungsten` | 1,010 | 3548 | - | - |
| `mcs2025-vanadium` | 1,159 | 3989 | - | - |
| `mcs2025-vermiculite` | 746 | 2514 | - | - |
| `mcs2025-wollastonite` | 1,138 | 4064 | - | - |
| `mcs2025-yttrium` | 1,097 | 3944 | - | - |
| `mcs2025-zeolites` | 1,071 | 3700 | - | - |
| `mcs2025-zinc` | 1,047 | 3474 | - | - |
| `mcs2025-zirconium-hafnium` | 1,079 | 3797 | - | - |

## Not added in the last run

Nothing was left out.

## What to check by eye

Ingest cleans text by rules, and rules miss things.
Take five minutes to open the shortest, a middle one and the longest document next to its original and read one page of each.

- Search the documents for `þ`, `¼`, `(cid:` and the replacement character.
  A hit usually means the PDF's font map is wrong, which no tool can repair, so treat it as a defect and leave that document out.
- Look at the end of a few papers.
  Ingest drops a trailing reference list when it finds a References heading or a run of numbered entries.
  A paper whose list has neither can keep it, and then every author and journal name matches queries it should not.
- Open the first lines of a few documents.
  Author lists, copyright pages and tables of contents are not removed automatically, and you may want to cut them.
- Compare one table with the PDF.
  A PDF prints footnote marks as small raised digits, and the converter glues them onto the word or number next to them: `ALUMINUM1` is the heading ALUMINUM with footnote 1, and `11210,000` can be 210,000 with footnote 11.
  Quotes still match the stored text, but a number read from it can be wrong, so check before you trust a figure in a query, a judgment or an answer.
- Fix the `license` column in the manifest for every document, then run `uv run p2 license`.
  It is `unknown` until you do, and `unknown` does not pass.

## If a document is flagged as scanned

A scan is a picture of a page, so there is no text for ingest to read.
This template does not install an OCR tool, because it is large and most students never need it.
If you do need one, the opt-in route is pymupdf4llm with rapidocr, run on its own outside the template's environment:

```
uv run --no-project --with pymupdf4llm --with rapidocr python -c "import pymupdf4llm, sys, pathlib; pathlib.Path(sys.argv[2]).write_text(pymupdf4llm.to_markdown(sys.argv[1], use_ocr=True, force_ocr=True), encoding='utf-8')" scan.pdf scan.md
```

Put the resulting `.md` file in your folder and ingest the folder again.
It costs about 2 seconds a page, and OCR text needs a second look: it misreads ligatures, hyphens and numbers.
pymupdf4llm is AGPL-3.0 software, so use it only as a tool on your own machine, and do not add it to this repo's dependencies or copy its code into the repo.
