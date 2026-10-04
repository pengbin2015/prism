# Prism

Prism helps an AI agent explain an idea so a person can understand it. It is especially useful for explaining technical ideas clearly or teaching them to others. It also guides the explanation and learning design of teaching materials. It chooses between clear writing, diagrams, interactive HTML, and concept-driven animation. It does not create every format for every question.

Prism was inspired by Andrej Karpathy's idea of using language models to make ideas easier to understand through clear writing, diagrams, interactive web pages, and custom explainer videos.

This repository contains one portable [Agent Skill](https://agentskills.io/specification) for Claude Code, Codex, and GitHub Copilot. The skill designs the explanation; each agent uses the document, presentation, browser, or media tools available in its environment to produce the artifact.

## Install

Use [GitHub CLI 2.90.0 or later](https://cli.github.com/manual/gh_skill_install) to install Prism for your user account, across projects. Run the command for your agent:

```bash
gh skill install pengbin2015/prism prism --agent claude-code --scope user
gh skill install pengbin2015/prism prism --agent codex --scope user
gh skill install pengbin2015/prism prism --agent github-copilot --scope user
```

Run only the command for the agent you use, or run all three. To install for one project instead, omit `--scope user` and run the command inside that project's Git repository. GitHub CLI places the skill in the host's expected directory. You can also download `skills/prism/` and copy that **whole folder**, including `references/`, into a supported skills directory.

| Agent | User installation directory | Project installation directory |
| --- | --- | --- |
| Claude Code | `~/.claude/skills/prism/` | `.claude/skills/prism/` |
| Codex | `~/.agents/skills/prism/` | `.agents/skills/prism/` |
| GitHub Copilot | `~/.copilot/skills/prism/` | `.agents/skills/prism/` |

The project paths above describe GitHub CLI's agent targets. GitHub Copilot also recognizes `.github/skills/prism/`. Start a new agent session if Prism does not appear after installation. Use `gh skill list` to find the installed copy and `gh skill update prism` to check for updates.

## Optional: add ASD-STE100 Issue 9

The full standard is **not included** in this repository. [Request a free official copy from ASD](https://www.asd-ste100.org/STE_downloads.html). Save the downloaded PDF inside your **installed** Prism skill folder at:

```text
references/ASD-STE100_ISSUE9.pdf
```

For example, a user-level Codex installation expects `~/.agents/skills/prism/references/ASD-STE100_ISSUE9.pdf`. If ASD gives the file another name, rename your local copy to the name above. Repeat this step for each agent installation that should read the standard. Keep the PDF and any extracted text on your machine. The skill's `.gitignore` excludes local files beginning with `ASD-STE100` from Git; check the files you stage before publishing.

Prism works without the PDF for ordinary explanations. It uses original clear-writing guidance as a default. For an exact rule, dictionary entry, or formal compliance check, it needs the official standard and should not guess. Some agents need a PDF reader or a local text extraction tool to search it.

## Use Prism

Ask normally, or invoke the skill by name if your agent supports it:

- “Use Prism to explain why a distributed rate limiter needs shared state. Show one request sequence.”
- “Use Prism to make an interactive HTML explanation of token-bucket refill. Let me change capacity and refill rate.”
- “Use Prism to design three teaching slides on prompt injection for learners who know basic web APIs.”
- “Use Prism to create a 3Blue1Brown-style animation that shows how a hash table collision is resolved.”

The result depends on the agent's available tools. For example, an agent without a video renderer may provide editable animation source and explain what it could not render.

## Repository files

```text
skills/prism/
├── SKILL.md                        Explanation workflow and writing guidance
├── references/visual-explanations.md  Diagram, HTML, and animation guidance
└── .gitignore                      Keeps locally supplied ASD files out of Git
```

## Maintain and publish

Edit the one source copy under `skills/prism/`. Keep host-specific tool names and permissions out of `SKILL.md`. Review links and run `gh skill publish --dry-run` from this repository to validate before a GitHub release. Publish only your original files. Do not add the ASD PDF or a full text extraction to a commit or release.

The original Prism files are licensed under [MIT](LICENSE). ASD-STE100 belongs to ASD and is not covered by that license. The 3Blue1Brown name describes an animation approach; this project is independent of 3Blue1Brown.
