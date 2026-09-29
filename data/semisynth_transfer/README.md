# Semi-Synthetic Transfer Track

This directory contains benchmark-only 22-method semi-synthetic transfer checks under real low-frequency backgrounds. These files support the living benchmark and are not camera-ready paper tables.

Large downloaded source files are excluded from this Hugging Face release. The included files are:

- canonical small background CSV files under `data/track_c/`;
- method defaults and benchmark manifest under `configs/`;
- merged and summarized metric outputs under `results/`.

The extension ranking source is `results/summary/ranking_paper_5metric_overall.csv`, which ranks methods by mean within-setting rank over the five paper recovery metrics.

The headline interpretation is that the mechanism-level picture transfers, while method-level conclusions become more conservative. In the aligned 22-method track, STL ranks first, followed by AMD block, MA baseline, Times2D block, and a tie among Autoformer, DLinear, and the moving-average decomposition block; CEEMDAN ranks sixth. CEEMDAN preserves strong seasonal agreement under real backgrounds, but its trend recovery remains sensitive to mode mixing against low-frequency real structure.
