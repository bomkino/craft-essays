# Writing evaluation — v0.2.0

Ten fresh briefs, written on 28 September 2026 by an agent that never saw the skill, cover the forms studios write most: a funding deck, a homepage, a spoken client presentation, a case study, an announcement, an About-page rewrite, a short-film treatment, a practical email, a talk opening and a personal-essay revision. Each brief supplies its facts and forbids inventing more; each carries objective checks the writers never saw.

The [briefs and checks](cases.json) and the [complete record](comparison.json) are public: snapshot hashes, every output, the exact texts each judge saw, the seeds, the sealed label mappings and every verdict.

## Method

Three writers in fresh Claude Opus 5.5 contexts completed every brief: one with no skill, one with v0.1.1, one with the v0.2.0 candidate. Each read only its frozen skill snapshot and the briefs.

Two judges on different models (Claude Opus 5.5 and Claude Fable 5.1) received the briefs, the checks and anonymous A/B/C responses, with labels shuffled independently per judge from recorded seeds. They checked every constraint, flagged mannerism (including any imitation of a recognisable author), ranked the three with ties allowed, and quoted the wording behind each judgment. Mappings were unsealed only after verdicts were saved.

After round one, the losses were diagnosed and repaired, and the affected briefs were rewritten by a fresh writer with the revised candidate and judged again against the same no-skill and v0.1.1 outputs.

## Round one: first candidate, ten briefs

| Brief | Opus 5.5 | Fable 5.1 |
| --- | --- | --- |
| Deck | v0.1.1 > none > v0.2 | v0.1.1 > none > v0.2 |
| Website | **v0.2** > v0.1.1 > none | **v0.2** > v0.1.1 > none |
| Client presentation | **v0.2** > none > v0.1.1 | **v0.2** > none > v0.1.1 |
| Case study | **v0.2** > v0.1.1 > none | **v0.2** > none > v0.1.1 |
| Announcement | v0.1.1 > v0.2 > none | **v0.2** > v0.1.1 > none |
| About rewrite | none > v0.1.1 > v0.2 | **v0.2** > none > v0.1.1 |
| Treatment | **v0.2** > v0.1.1 > none | **v0.2** > none > v0.1.1 |
| Practical email | **v0.2** > none > v0.1.1 | **v0.2** > v0.1.1 > none |
| Talk opening | **v0.2** > v0.1.1 > none | v0.1.1 > v0.2 > none |
| Essay revision | v0.1.1 > v0.2 > none | **v0.2** > v0.1.1 > none |

Across the twenty rankings, v0.2 beat unassisted writing 17 times and v0.1.1 14 times. Neither judge flagged any output as imitating Palahniuk or any other author.

Both judges put v0.2 last on the deck for one reason: a `??????` placeholder left in a speaker note. The other losses were a rewrite that read "like the fact sheet" instead of like its author, an announcement that dropped one unchanged detail, and every essay revision falling under its length floor.

## Repairs

- Placeholders belong to drafts; finished work narrows the claim and names the gap after the work.
- A new **Harvest** tool: use the author's own asides and phrases, which carry the voice as well as the facts.
- The truth pass became **truth and completeness**: calculated figures count, every fact the reader needs is present, and a required length is restored from the material.
- Weaknesses are owned once, where they matter most; one-line paragraphs are saved for the beat that most needs one.
- The plain-version test keeps whichever version does more for the reader, including more memorable and more pleasure to read.

## Round two: revised candidate, the five affected briefs

| Brief | Opus 5.5 | Fable 5.1 |
| --- | --- | --- |
| Deck | **v0.2** > v0.1.1 > none | **v0.2** > none > v0.1.1 |
| About rewrite | **v0.2** > v0.1.1 > none | **v0.2** > none > v0.1.1 |
| Talk opening | **v0.2** > v0.1.1 > none | **v0.2** > v0.1.1 > none |
| Announcement | v0.1.1 > v0.2 > none | v0.1.1 > v0.2 > none |
| Essay revision | v0.1.1 > v0.2 > none | v0.1.1 > v0.2 > none |

The essay row is a separate third judging that used every writer's final text (see Integrity notes). The revised v0.2 announcement again omitted swaps from the list of what stays the same, and its essay revision, which both judges called the cleanest and truest to the writer and free of mannerism, came in more than 20 words under the floor, with a note explaining why. Both points were then written into the skill: list what stays the same as completely as what changes, and when a cut meets a required length, the length wins. These two final wording changes have not been re-evaluated.

## What this establishes

Taking each brief's latest judging, the v0.2 candidate ranked first on eight of ten briefs with both judges and second on the other two, and it placed above unassisted writing on all ten. The five briefs not rerun were judged with the first candidate; the revisions add to it and were not separately tested on those briefs.

This is one generation per condition per brief, two model judges from one model family, English only. It is not a human taste study or a statistical estimate. Packaging, installation and cross-host behaviour are checked separately.

## Integrity notes

Two writers kept revising files after reaching a full set, and two packets were built before they finished. Round one judged interim versions of two v0.1.1 outputs (deck and essay), and round two judged an interim v0.2 essay. The record keeps the texts each judge actually saw. Round two used the final v0.1.1 texts, and the third judging reran the essay with every final text. Future runs pack only after each writer reports completion.
