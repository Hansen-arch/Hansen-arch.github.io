# Design direction

**Read:** a working portfolio for forestry, GIS and remote sensing reviewers, in a quiet
instrument panel language. Dial **ENERGY 2 / RHYTHM 2 / MOTION 1**.

## What it should feel like

A survey instrument, not a startup page. The people reading this are lecturers, forest
managers and GIS leads. They are checking whether the numbers hold up, so the page should
look like something that measures things: flat ground, hairlines, precise type, one signal
colour, and the imagery given the brightest surface on the screen.

## Palette

Two neutrals plus one accent, nothing else. No gradient, no glow, no shadow anywhere.

| Token | Dark | Light | Why |
|---|---|---|---|
| Ground | `#0d0f10` | `#f3f3f0` | Graphite holds the aerial plates as the brightest surface, the way a console presents imagery. Light mode is the paper plot sheet for printing and daylight. |
| Ink | `#e8eae9` | `#161817` | Neutral, slightly cool, so the amber stays the only warm thing. |
| Ink secondary | `#a2a7a4` | `#4b4f4c` | Body copy at 7:1 or better on the ground. |
| Rule | 14% ink | 14% ink | Structure comes from 1 px rules, not from boxes. |
| Accent | `#e3a15c` | `#8f5310` | Sodium amber, the backlight of a field instrument. It marks the active tab, focus, the plate index and the primary action, and nothing else. |

Amber is chosen over the blue or cyan that technical sites default to: it keeps the cool
orthophoto plates and the warm signal apart, so the accent still reads as a signal.

## Type

IBM Plex Sans and IBM Plex Mono.

Plex was drawn for technical documentation, and its mono is the same voice, so a CRS code,
a coordinate or a tree count sits in the page without a terminal costume. Headings run in
Plex Sans 600 at a tight track; the mono is reserved for data: readouts, plate captions,
table figures, and the section indices. No uppercase tracking anywhere.

## Layout

- **Masthead:** asymmetric. The name is the focal point on the left, a four-line readout on
  the right holding facts a reviewer actually checks (location, study, focus, availability).
- **Sections** are introduced by a hairline with a small mono index, the way a plot sheet
  numbers its panels.
- **Capabilities** are a datasheet: category in the left column, evidence in the right. Not
  four identical cards.
- **Projects** are rows with an index, a summary, a stack line and one small plate. Rows
  scale where a card grid does not, and the hierarchy comes from the plate size.
- **Project pages** keep prose and data tables; their hero image becomes a plate with a
  mono caption naming the block and ground resolution, because that caption is provenance.

## Motion

Hover and focus only. Links take a fuller underline, plates lift their desaturation, rows
mark themselves with the accent on the index. Nothing animates on load.

## Honesty

The readout only carries facts that can be checked: the city and its coordinates, the
university and year, the stated availability. No counters, no "10+ projects", no logos of
employers that have not hired him.
