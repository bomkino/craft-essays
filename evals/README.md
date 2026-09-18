# Writing evaluation — v0.1.0

Eight fresh synthetic briefs were tested on 18 September 2026. They cover a practical explanation, personal essay opening, argument, informal note, speech, poem critique, spelling-only edit and exhibition review.

The [briefs](cases.json) and [complete responses, judgments and checks](comparison.json) are public so the evidence can be inspected.

## Method

Two fresh-context agents independently completed the same eight briefs. One received only the briefs. The other received the candidate skill and could read its linked references; it read structure, substance and expression during the eight-case run. Neither received the research foundation, worked foundation examples, intended answers or the other agent’s responses.

A third fresh-context agent saw the original briefs and anonymous A/B responses, with labels shuffled independently for each case using a recorded seed of 18092026. It judged fulfilment of the request, factual and constraint integrity, substance, voice, rhythm and overall quality. It was permitted to prefer either output, call a tie or reject both. It did not see the skill or the condition labels. Conditions were revealed only after its judgments were saved.

The parent agent separately inspected the outputs and mechanically checked the five word limits and the exact spelling-only result. Word counts use whitespace splitting.

## Results

| Brief | Blind preference | Main observation |
| --- | --- | --- |
| Explanation | Tie | Both preserve all four privacy distinctions in plain language. |
| Personal essay opening | Baseline | The baseline develops the inherited physical habit; the skill-assisted ending names the feeling and closes with a tidier callback. |
| Argument | Skill | The proposal and a way to assess quiet use develop the argument beyond its premise. |
| Informal note | Tie | Both preserve the awkwardness and all of the writer’s words. |
| Speech | Skill | The humour fits the welcome, and the newcomer gets a useful way to begin. |
| Poem critique | Tie | Both leave the addressee unresolved and make text-specific observations. |
| Spelling-only edit | Tie | Both are exactly correct, including punctuation and line breaks. |
| Exhibition review | Skill | The review develops how measurement directs attention and keeps the supplied reservation about repetition. |

The skill-assisted outputs were preferred in three cases, the baseline in one, with four ties. Both conditions passed all five word limits and the exact spelling-only check. No material constraint violation was identified in the skill-assisted set.

The personal-essay loss matters. Plainly naming an emotion can work, but here the reviewer preferred a conclusion developed through the object’s physical behaviour. The instructions were left unchanged after this comparison: a single preference does not justify banning direct feeling or requiring an object-based ending. The tradeoff remains visible for future evaluation.

## What this establishes

The candidate could be used to complete these eight tasks while preserving their explicit constraints. In this small comparison, some skill-assisted outputs developed their material more fully; others were equivalent or less effective.

This is one agent-generated response per condition per brief, with one agent reviewer. It is not a human taste study, a statistically reliable estimate of improvement, a cross-model benchmark or proof across languages and every writing form. The cases were written after the runtime candidate and before either response run; they were not drawn from the foundation’s worked examples. No test response was used as an example in the installed skill.

Packaging, public download, host discovery and Cloud Work installation are checked separately from writing quality.
