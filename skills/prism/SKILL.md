---
name: prism
description: >-
  Make concepts, ideas, and knowledge clear for personal understanding or for
  teaching others. Use when asked for a clearer explanation, causal account,
  diagram, interactive HTML page, teaching document or slides, or a custom
  concept-driven animation. Choose the form that reveals the idea and use
  concise, ASD-STE100-informed writing without hiding important reasoning.
---

# Prism

## Purpose

Help a person understand an idea, or help that person explain it to others. Use the same reasoning process for both tasks. Match the explanation to the learner, the depth needed, and the best output form. Do not convert a personal question into teaching content unless the user asks for it.

Include examples, steps, comparisons, or visuals when they help the learner understand or use the idea. Remove details that add no value. Use as much explanation, analysis, and visual detail as the task needs.

## 1. Identify the learner and objective

Use the supplied audience, sources, objective, and format. Preserve explicit constraints.

For personal understanding, address the user's question and confusion. Adapt to demonstrated knowledge. For teaching materials, identify prerequisites and likely misconceptions, then arrange the requested material in a useful progression. Add practice when it helps learners apply the idea.

State material assumptions briefly. Ask a focused question only if missing information changes the result. Otherwise, proceed. Keep internal planning brief unless requested. A quick question may need only a direct answer and an example.

## 2. Select the output form

Honor an explicitly requested format. Otherwise, select the form that reveals the difficult relationship most clearly.

First identify what the learner needs to understand and what makes it difficult: meaning, relationships, the effect of changing inputs, or a transformation over time. Choose the simplest form that makes that difficulty clear. The same concept can need different forms for different questions or learners.

| What helps the learner understand? | Likely form | What it reveals |
| --- | --- | --- |
| A definition, argument, short example, or comparison | Text | The idea and its consequence |
| Seeing structure or relationships | Text with a diagram, or diagram-based HTML slides | How parts relate |
| Changing inputs, comparing outcomes, or inspecting states | Interactive HTML | How choices affect the result |
| Watching geometry, state, or a process transform in a controlled sequence | Concept-driven animation | How a change produces its consequence |

Choose the explanatory approach before the delivery structure. Use slides for a requested presentation or when staged guidance helps; use a continuous page when exploration benefits from keeping information together. HTML can contain diagrams, interaction, or animation. A sequence alone does not require a video: prefer interaction when learners need to control the sequence or test alternatives, and timed animation when the planned visual progression explains the mechanism.

If text alone explains the concept adequately and no presentation format is requested, answer directly in text. When several treatments help, choose one primary format and add supporting elements where useful. Apply a 3Blue1Brown-inspired approach when requested or useful; it is not a requirement for every animation.

Make the format choice without asking the user to choose a medium unless missing audience information or constraints would materially change the result. Briefly explain the choice before producing a substantial artifact. Do not create every form by default. Read [visual-explanations.md](references/visual-explanations.md) when the task needs slides, a diagram, an interactive page, or an animation. Apply only the guidance relevant to the selected format.

Prism guides the explanation and learning design. Use the tools and artifact workflows available in the current host to create the requested file or visual. For a slide deck or document, let the available presentation or document workflow handle file construction. For exact algorithms, equations, charts, and state transitions, use exact data, code, or vector graphics instead of generated imagery.

## 3. Explain the mechanism

Adapt this sequence to the task. Do not force every step into a short answer.

1. Show a concrete situation and the question it raises.
2. Trace one example. Show the relevant state, action, and cause. Introduce terms when needed.
3. Change an input or show a boundary case or misconception. Explain what changes and why.
4. For a lesson, add a useful prediction or application question when appropriate.
5. State the reusable rule and any material limitation.

Keep names, colors, units, notation, and inputs consistent. Label simulations and simplifications. State where an analogy stops matching the real mechanism.

For slide decks, give each slide a clear purpose that advances the learning objective. Connect examples and activities across slides. Explain changes in context or assumptions before learners use the new information.

## 4. Write clearly

Use STE-informed writing by default: precise terms, direct verbs, clear actors, explicit conditions, gradual information, and consistent terminology. Aim for no more than 20 words in a procedural sentence and 25 words in a descriptive sentence. Keep each paragraph on one topic. Treat these lengths as revision targets; do not remove needed reasoning to meet them.

The full ASD-STE100 Issue 9 standard is an **optional, user-supplied local reference**, expected at `references/ASD-STE100_ISSUE9.pdf` inside this skill folder. It is not bundled with this skill. If present and a specific rule, example, or dictionary entry matters, read or search only the relevant pages with the available PDF tools. If necessary, extract searchable text locally; do not assume every host can search PDF directly. Read the dictionary introduction before checking approved words.

If the file is absent, continue ordinary explanations with the clear-writing principles above. For an exact STE-rule, controlled-vocabulary, or formal-compliance request, obtain the user's copy of the standard or direct the user to the official [ASD download page](https://www.asd-ste100.org/STE_downloads.html). Do not invent a rule or approve a word from memory. Do not claim formal compliance without checking the full rules, dictionary, terminology, and applicable exceptions.

Delete generic introductions, promotional adjectives, repeated summaries, and unrelated background. Keep the worked example and its reasoning. Let a visual show relationships; use nearby text or narration to explain their meaning.

## 5. Build and verify

For a creation request, produce the artifact. Follow [visual-explanations.md](references/visual-explanations.md) for visual design and format-specific checks. Use the current host's available tools. If a required production tool is unavailable, explain the limitation and provide the closest useful result in its actual format.

Handle required setup and execution within the user's authorization and the environment's permissions. Inspect existing tools before installing dependencies. Create or reuse an isolated environment when needed, and request approval for actions that require it. For a rebuild request, use the saved source and recorded dependencies to produce and verify the output. If blocked, identify the specific blocker, the work completed, and any user action needed to continue.

Before delivery:

- Check calculations, state transitions, causal claims, and a boundary case.
- Check that the explanation supports the learning objective and that the chosen medium reveals the difficult relationship. Simplify when added visuals, interaction, or motion provide no explanatory value, while preserving an explicitly requested format.
- Remove elements that provide no reasoning, orientation, accessibility, or useful practice.
- Inspect the rendered visual when possible. Test interactions, animation, and narration when present.
- Report content checks, rendered inspection, and interaction checks separately where applicable. State material checks that could not be completed.

Preserve editable source when it may need reuse. Follow the current host's file-saving process. Do not publish beyond the requested destination. For personal understanding, return the explanation directly. For artifact requests, return the artifact and a short account of its purpose and limitations.
