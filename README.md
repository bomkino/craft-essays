# Craft Essays

An open-source agent skill for developing better writing in your own voice.

Use it to draft, revise or critique practical and expressive writing: explanations, essays, notes, speeches, criticism, product copy, poetry and more. It helps the agent choose what the piece needs—better material, a developed thought, clearer order, sharper observation, stronger cadence or restraint.

The instructions adapt lessons from Chuck Palahniuk’s craft essays for general writing. They preserve the writer’s voice and the purpose of the piece. The original essays are not included.

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

Upload the release asset named `craft-essays.zip`, which contains the skill and its references. GitHub’s automatic “Source code” archives contain the entire repository.

Skills availability and labels can vary by account. Local installation and Cloud Work installation are separate.

### Manual installation

Extract the release ZIP. Place the resulting `craft-essays` folder in your agent’s skills directory. Keep its `references` and `agents` folders beside `SKILL.md`.

For Codex’s installer-managed location, that is `~/.codex/skills/craft-essays`, or `%USERPROFILE%\.codex\skills\craft-essays` on Windows, unless you use a custom `CODEX_HOME`. Use one installation method to avoid duplicate copies.

## Use

Invoke it with a writing task:

```text
$craft-essays
Revise this explanation for a reader who is new to the subject.
Keep the technical terms and the uncertainty.
[paste your draft]
```

```text
$craft-essays
Help me develop this essay. Keep its prickly humour.
Find the thought I have stopped short of exploring.
[paste your draft]
```

```text
$craft-essays
Give me editorial notes on this poem. Preserve its ambiguity.
[paste your poem]
```

In Cloud Work, select **Craft Essays** if the skills picker is available, or ask to use the **craft-essays** skill with your brief.

Give it the audience, purpose, constraints and source material you have. It can draft from a brief, revise an existing piece, critique without rewriting, or make a narrow edit. It may expand a thin passage or leave a successful one alone.

It keeps facts, commitments and meaningful uncertainty intact. It can invent when the brief calls for invention. It has no fixed sentence length, house voice, joke quota or requirement to make every piece a story.

## Inside

- [SKILL.md](skills/craft-essays/SKILL.md): the compact entry point and reference routing.
- [Structure](skills/craft-essays/references/structure.md): disclosure, development, inference and endings.
- [Substance](skills/craft-essays/references/substance.md): evidence, observation, particulars and comparison.
- [Expression](skills/craft-essays/references/expression.md): voice, cadence, texture, feeling and play.
- [Origins](skills/craft-essays/references/origins.md): attribution and the limits of the adaptation.
- [Research foundation](docs/foundation.md): the deeper study behind the instructions; maintainer reading, outside the installed skill.
- [Evaluation](evals/v0.1.1/README.md): longer writing comparisons, constraints and limitations, with the initial study linked.

The package contains instructions only. It adds no scripts or service dependencies. Only the relevant reference needs to load for a writing task.

## Maintain and package

Keep changes grounded in a real writing decision. Test a substantial change on fresh briefs, including a task that calls for restraint. Keep examples and evaluation outputs outside the installed skill unless they teach something the runtime instructions cannot.

Build the portable release ZIP with Python 3:

```sh
python3 scripts/package.py
```

The command writes `dist/craft-essays.zip` and `dist/SHA256SUMS`. Only the skill folder is packaged.

## Attribution and licence

Created by [pitch.dog](https://github.com/bomkino). Original instructions, adaptations and examples are available under the [Zero-Clause BSD licence](LICENSE).

The teaching source is Chuck Palahniuk’s craft essays, with the lineage credited in [Origins](skills/craft-essays/references/origins.md). This project is independent and does not claim endorsement. The licence covers this repository’s original work; it does not license the source essays.
