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

Prism can choose the explanatory format for you. Give it the concept, your question, and any relevant audience or constraints. It identifies what is difficult to understand, then chooses text, diagrams, interactive HTML, or animation. Slides provide staged guidance when useful; animation provides a timed visual progression. An explicitly requested format takes precedence.

For example:

> Use Prism to explain binary search to a learner who knows arrays and loops. Choose the clearest format for understanding why the search takes logarithmic time.

The same concept can lead to different outputs. A short trace may explain binary search's logarithmic cost in text. Trying different targets benefits from interactive HTML. Watching the search interval contract may benefit from animation. Prism should choose the simplest form that explains the particular difficulty and briefly explain substantial artifact choices.

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

## Create narrated animations

Use this workflow when animation is selected or explicitly requested. Prism can guide animations for different subjects, courses, audiences, and durations. Choose the visual model and tools for the concept. The workflow below uses Manim for exact geometry, Kokoro for optional local narration, and FFmpeg for assembly. Other tools can be used when they better fit the requested output.

Your AI agent can perform the complete workflow: inspect existing tools, create an isolated environment, install required dependencies, generate animation and audio, combine them, verify the result, and rebuild from saved source. Ask the agent to do the work; the commands below are reproducibility references and can also be run manually. Installation and execution depend on the agent's available tools and permissions. The agent should request any required approval and explain specific blockers.

For example:

> Use Prism to create a narrated animation explaining this concept. Set up the required tools, generate the animation and audio separately, combine them, and verify the result.

For an existing animation:

> Rebuild this animation from its saved source and dependencies. Check the output and report any checks you could not complete.

### Plan the explanation

Identify the audience, prerequisites, learning objective, and target duration. Plan a sequence that introduces the visual model, shows a meaningful change, explains its cause, and applies the idea to another case. Match each spoken passage to the visual event it explains. Use an original visual treatment and a supplied or authorised voice.

For each animation, choose a working folder such as `demo/my-animation/`. Keep its source, script, environment, caches, and generated artifacts together. Use names and durations appropriate to that animation. Keep setup and rebuild documentation in this root README.

### Set up a local Python environment

Install [uv](https://docs.astral.sh/uv/) if it is unavailable. Python 3.12 is the verified baseline for the Manim and Kokoro combination used here. Check compatibility before changing dependency versions.

For macOS with Homebrew, install the native rendering, text, speech, and media dependencies:

```sh
brew install cairo pkg-config pango ffmpeg espeak-ng
```

Other operating systems need equivalent native dependencies; follow the [Manim installation guide](https://docs.manim.community/en/stable/installation/uv.html) and [Kokoro instructions](https://github.com/hexgrad/kokoro).

From the repository root, choose the animation folder and create its environment:

```sh
animation_dir="demo/my-animation"
mkdir -p "$animation_dir"
uv venv --python 3.12 --seed "$animation_dir/.venv"
UV_CACHE_DIR="$animation_dir/.cache/uv" uv pip install --python "$animation_dir/.venv/bin/python" 'manim[typst]' 'kokoro==0.9.4' soundfile
```

The folder name is an example. Set `animation_dir` to the actual destination when running these commands. Omit Kokoro and SoundFile for animations without narration. Manim's Typst support can render mathematical text without LaTeX; sources that use `MathTex` or `Tex` need a suitable LaTeX installation.

Record the working environment for reproducible rebuilds:

```sh
"$animation_dir/.venv/bin/python" -m pip freeze > "$animation_dir/requirements.txt"
```

Recreate a recorded environment by installing its requirements file instead of selecting fresh package versions:

```sh
UV_CACHE_DIR="$animation_dir/.cache/uv" uv pip install --python "$animation_dir/.venv/bin/python" -r "$animation_dir/requirements.txt"
```

Ignore `.venv/`, `.cache/`, and `__pycache__/` in each animation folder. The Python runtime and native dependencies may be managed outside that folder; the virtual environment is local.

### Generate animation and narration separately

Create editable Manim source and, when narration is requested, a script with timed passages. Use exact calculations for algorithms, equations, and state transitions. Label illustrative simulations and state their limitations.

Configure generated media under the chosen animation folder. For local speech generation, set `HF_HOME`, `TORCH_HOME`, and `XDG_CACHE_HOME` beneath its `.cache/` directory before importing model libraries. Kokoro's first run downloads model weights, a voice, and language assets. Select a voice that matches the narration language and save its audio as a separate WAV file. Kokoro's standard output sample rate is 24 kHz.

Render a short preview and synthesise a short speech sample before producing the complete animation. Measure speech duration, then align narration and visual events. Allow time to inspect important states. Derive caption timing from the final audio. If sentence audio is cached, include text, voice, and speech settings in the cache key.

A typical Manim render command, run from the animation folder, is:

```sh
.venv/bin/manim -qh --fps 60 animation.py SceneName
```

Replace `animation.py` and `SceneName` with the actual source and scene class. Resolution and frame rate are choices for the intended use. Any narration or assembly scripts must be created for that project; Prism does not supply universal scripts with those names.

### Combine and verify

After aligning the separate video and audio to the intended timeline, combine them with FFmpeg. For example, from the animation folder:

```sh
ffmpeg -i animation-silent.mp4 -i narration.wav -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -b:a 128k -movflags +faststart animation-narrated.mp4
```

Use the actual filenames. Check durations before assembly so the result has no unintended silent tail or truncated explanation. Add subtitles and chapters when useful. Keep the separate silent animation and narration available for reuse.

Check the underlying calculations and important transitions independently of the visuals. Inspect rendered frames and playback for readability, synchronisation, and pacing. Listen for pronunciation and audio quality. Verify final duration, resolution, audio presence, and decoding. Report completed checks and any remaining limitations separately.

### Worked example: gradient descent

The existing example in `demo/animation/` uses the workflow above for a three-minute explanation. It includes:

- [Final narrated video](demo/animation/gradient-descent-narrated.mp4), [silent animation](demo/animation/animation-silent.mp4), and [separate narration](demo/animation/narration.wav).
- [Storyboard](demo/animation/storyboard.md), [Manim source](demo/animation/gradient_descent.py), and [narration script](demo/animation/narration.json).
- Project-specific [audio generation](demo/animation/generate_audio.py), [assembly](demo/animation/assemble.py), and [verification](demo/animation/verify.py) scripts.
- A local `.venv/`, recorded `requirements.txt`, captions, timing records, and review frames.

To rebuild this example, run from `demo/animation/`:

```sh
.venv/bin/python generate_audio.py
.venv/bin/manim -qh --fps 60 gradient_descent.py GradientDescent
.venv/bin/python assemble.py
.venv/bin/python verify.py
```

These scripts encode this example's six scenes, 180-second timeline, selected voice, and mathematical checks. Adapt those decisions for a different animation. After the initial model downloads, this example supports `HF_HUB_OFFLINE=1` for audio regeneration. Its narration generator checks that speech fits each scene's time slot.

### Tools and licences

See [Manim Community](https://github.com/ManimCommunity/manim), [Kokoro](https://github.com/hexgrad/kokoro), the [Kokoro model card](https://huggingface.co/hexgrad/Kokoro-82M), and [FFmpeg](https://ffmpeg.org/) for their documentation and licences. Keep virtual environments and model caches out of Git.

## Maintain and publish

Edit the one source copy under `skills/prism/`. Keep host-specific tool names and permissions out of `SKILL.md`. Review links and run `gh skill publish --dry-run` from this repository to validate before a GitHub release. Publish only your original files. Do not add the ASD PDF or a full text extraction to a commit or release.

The original Prism files are licensed under [MIT](LICENSE). ASD-STE100 belongs to ASD and is not covered by that license. The 3Blue1Brown name describes an animation approach; this project is independent of 3Blue1Brown.
