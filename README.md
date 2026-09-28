# Craft Essays

An open-source agent skill for writing that has to work on its reader: decks, websites, talks, stories, treatments, essays, emails and posts.

It starts from what the piece is for: who reads it, and what should change in them. Then it brings the tools of the craft to bear. Unpack the label. Cut the received phrase. Let the reader arrive first. Ride the same few horses. Plant the gun the ending fires. The tools come from Chuck Palahniuk's craft essays and the teachers he credits. The voice stays yours: the skill is tools, not a style, and nothing here asks the writing to sound like Palahniuk.

## Install

### Codex and other local agents

With [Node.js](https://nodejs.org/) and Git installed, run:

```sh
npx skills add bomkino/craft-essays --skill craft-essays --agent codex --global
```

This uses the open-source [Skills CLI](https://github.com/vercel-labs/skills). The command works on macOS, Linux and Windows. Omit `--agent codex` to choose another supported agent; omit `--global` for a project installation.

For a fixed release, use:

```sh
npx skills add https://github.com/bomkino/craft-essays/tree/v0.1.1/skills/craft-essays --agent codex --global
```

You can also ask Codex:

> Use skill-installer to install the skill at https://github.com/bomkino/craft-essays/tree/v0.1.1/skills/craft-essays.

The skill becomes available on the next turn. If your client keeps a cached skill list, start a fresh task.

### ChatGPT Cloud Work

1. Download **craft-essays.zip** from the [latest release](https://github.com/bomkino/craft-essays/releases/latest).
2. In ChatGPT, open **Plugins → Skills → Create → Upload from your computer**.
3. Upload the ZIP and finish the installation.

Upload the release asset named `craft-essays.zip`, which contains the skill and its references. GitHub's automatic "Source code" archives contain the entire repository.

Skills availability and labels can vary by account. Local installation and Cloud Work installation are separate.

### Manual installation

Extract the release ZIP. Place the resulting `craft-essays` folder in your agent's skills directory. Keep its `references` and `agents` folders beside `SKILL.md`.

For Codex's installer-managed location, that is `~/.codex/skills/craft-essays`, or `%USERPROFILE%\.codex\skills\craft-essays` on Windows, unless you use a custom `CODEX_HOME`. For Claude Code, it is `~/.claude/skills/craft-essays`. Use one installation method to avoid duplicate copies.

## Use

Invoke it with the piece and whatever you know about its reader:

```text
$craft-essays
Rewrite this ten-slide deck for a funding panel that has already read our report.
Keep every figure; the ask is £36,400.
[paste the slides]
```

```text
$craft-essays
Our homepage reads like every other agency's. Here are the facts and the current copy.
[paste]
```

```text
$craft-essays
Give me notes on this short story. Don't rewrite it.
[paste the story]
```

Other skills can call it too. A deck or voice skill can hand over a drafted passage for a **craft pass**: craft-essays keeps the caller's brief, voice and markers, runs its revision passes, and returns the draft in the same shape.

It keeps facts, commitments, quotations and meaningful uncertainty intact. Where a fact is missing, it writes `??????` rather than inventing one, and tells you what it needs.

## How it works

1. **Purpose.** Who reads it, what should change in them, what the writer wants, and what must survive untouched.
2. **Plan.** The shape the purpose needs, the two to four horses the piece rides, and one job for every paragraph, slide or scene.
3. **Write** with the tools the purpose calls for.
4. **Test against the plain version.** Every crafted choice has to do more for the reader than the plain version would; everything else stays plain.
5. **Revision passes.** Each of the essays' time-boxed bans becomes a pass: labels, explanations, received text, thought verbs, horses and guns, jobs, sound and truth.

The tools: received text, unpack, the reader arrives first, thumbnail, horses, buried gun, big voice and little voice, head and heart, submerge the I, textures, gradual reveal, and read it aloud.

## Inside

- [SKILL.md](skills/craft-essays/SKILL.md): purpose, steps, tools and revision passes.
- [Decks and talks](skills/craft-essays/references/decks-and-talks.md): decks, pitch documents, story decks, presenting work, talks.
- [Web and product](skills/craft-essays/references/web-and-product.md): websites, product and campaign copy, posts and newsletters.
- [Narrative](skills/craft-essays/references/narrative.md): shapes, scenes, dialogue, perception, time, true stories.
- [Sentences](skills/craft-essays/references/sentences.md): verbs, comparisons, rhythm, sound, labels.
- [Origins](skills/craft-essays/references/origins.md): attribution, a page map and the limits of the adaptation.
- [v0.2 design note](docs/v0.2-design.md) and [research foundation](docs/foundation.md): maintainer reading, outside the installed skill.
- [Evaluation](evals/v0.2.0/README.md): blind comparisons, with the earlier studies linked.

The package contains instructions only. It adds no scripts or service dependencies. A task loads the branch it needs.

## Maintain and package

Keep changes grounded in a real writing decision. Test a substantial change on fresh briefs, including a task that calls for restraint, and compare blind against the previous release and against no skill. Keep examples and evaluation outputs outside the installed skill unless they teach something the runtime instructions cannot.

Build the portable release ZIP with Python 3:

```sh
python3 scripts/package.py
```

The command writes `dist/craft-essays.zip` and `dist/SHA256SUMS`. Only the skill folder is packaged.

## Attribution and licence

Created by [pitch.dog](https://github.com/bomkino). Original instructions, adaptations and examples are available under the [Zero-Clause BSD licence](LICENSE).

The teaching source is Chuck Palahniuk's craft essays, with the lineage credited in [Origins](skills/craft-essays/references/origins.md). This project is independent and does not claim endorsement. The licence covers this repository's original work; it does not license the source essays.
