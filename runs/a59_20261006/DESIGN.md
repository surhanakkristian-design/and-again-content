# A58 design spec (from Figma 4evr-2.0, frames 402x874; screenshots in figma/)

Common (both themes): page bg #f5f5f5. Header: white circle 39x39 (radius 19.5) with "N." Roboto Medium 20 black,
14 px gap, title Roboto Medium 20 #070707/black. Header at y=11 (or 48 on frames 3/4 with status bar). Rail on the
right (heart, ⇄, share, flag), gap 50, right 23.
Picture card: radius 30, full width 402, from y=59 to bottom (frames 1,2) / y=101 h=646 (frame 3 carousel).

DARK theme (content reaches the edges: photos/videos):
1 Tap: picture card full width, radius 30, the clip covers it (cover). Phrase pill ON the picture, top centre
  (card padding 20): black bg, 1px rgba(255,255,255,.1) border, radius 45, padding 20/30, Roboto Medium 24 white.
  Rail icons white.
2 Nouns: same card; slots = rgba(255,255,255,.1) bg + 1px white border, radius 45, pad 10/15 (text transparent);
  chip bank ON the picture at the bottom: panel rgba(255,255,255,.3) + border rgba(255,255,255,.1), radius 25,
  w 380 (centred, ~11 from edges), pad 10/15, gap 10, wrap; chips white bg radius 45 pad 10/15 Roboto Medium 20 black.
3 Caption: card y=101 h=646 radius 30, picture covers; dots indicator 51x13 near bottom of the card (y=712), white;
  captions BELOW the card: centred wrap gap 8, chips white radius 45 pad 10/15 Medium 20 black.
4 Fill (no picture): mind map top (key word pill #AC3C72 white text Regular 20 centre; collocation partners as white
  pills around it, connected by thin black lines); divider line 320 wide (#d9d9d9-ish); phrase rows: "to" plain
  Regular 20 + white pills (radius 45, pad 10/15) for each part, gaps = empty white pills, gap 10, rows gap 15;
  divider; bank = panel rgba(20,138,234,.08) radius 25 w 354 pad 10/15 gap 10 wrap with white pills.
5 Story (no picture): a) b) c) rows (label Regular 20 + white pill radius 45 pad 10/20 Regular 20 black, rows gap 10)
  at y=121; field = white box radius 29 w 373 h 364 pad 19/23, mic icon (17x25) + placeholder "Tell your own
  sentence." #787878 Regular 20; tapped sentences sit in the field as #f5f5f5 pills (pad 10/20 radius 45, gap 20);
  arrow button #148AEA h 50 radius 45 full width (373), white arrow.

WHITE theme (plain light edges, illustration in the centre): same as dark except
1 Tap: picture card = WHITE panel radius 30 (full width, to bottom), the picture contained in the middle (radius 20),
  pill on the panel's top (same black pill). Rail icons BLACK.
2 Nouns: slots rgba(0,0,0,.2) + 1px black border; bank panel rgba(0,0,0,.2) radius 25 at the bottom of the panel.
3 Caption: white panel radius 30 with the picture contained; dots black; captions below as dark.
4, 5: identical to dark (no picture).

Frame texts are placeholders (laugh ABOUT is wrong; owner: laugh AT).
