---
name: prism
description: >-
  Make concepts, ideas, and knowledge clear for personal understanding or for
  teaching others. Use when asked for a clearer explanation, causal account,
  diagram, interactive HTML page, teaching document or slides, or a custom
  concept-driven animation. Clarify the learner and goal when needed, identify
  the learning difficulty, and choose a suitable form. Use
  concise, ASD-STE100-informed writing without hiding important reasoning.
---

# Prism

## Purpose

Help a person understand an idea, or help that person explain it to others. Use the same reasoning process for both tasks. Match the explanation to the learner, the depth needed, and the best output form. Do not convert a personal question into teaching content unless the user asks for it.

Include examples, steps, comparisons, or visuals when they help the learner understand or use the idea. Remove details that add no value. Use as much explanation, analysis, and visual detail as the task needs.

## 1. Identify the learner and objective

Use the conversation and supplied material first. Preserve the requested audience, sources, objective, format, and constraints. Distinguish the requester's knowledge from the audience's knowledge when creating teaching materials.

Establish who the learner is, what relevant knowledge they already have, where they are confused, and what they should understand or do afterward. Ask focused questions when missing information would materially change prerequisites, depth, examples, progression, or explanation design. Do not ask for information already available or require a questionnaire for every request.

Start with the highest-value question. Group a few independent questions when useful; defer questions that depend on unanswered ones. Ask about concrete knowledge rather than relying on labels such as “beginner.” Accept “I don't know.” A small example or prediction question can help reveal the learner's current mental model without making clarification an exam.

Wait for answers before making design choices that depend on them. Adapt follow-up questions to the answers. Stop asking once remaining uncertainty would not materially change the explanation. If the user requests an immediate answer, proceed with brief, explicit assumptions. A quick question may need only a direct answer and an example. Keep internal planning brief unless requested.

Read [learner-discovery.md](references/learner-discovery.md) when meaningful clarification is needed. It provides question patterns and examples, not a mandatory interview. Prism does not require a separate interview skill.

## 2. Identify the learning difficulty

Identify the gap between what the learner knows and what the learning goal requires. Look for missing prerequisites, unfamiliar terms, misconceptions, abstractions, hidden state, difficult relationships, or transformations. Treat an inferred misconception as a hypothesis until the learner's answers or work support it.

Use this diagnosis to choose the starting point, worked example, depth, and progression. Introduce needed prerequisites where they become useful. For teaching materials, arrange the requested content so learners can build on established knowledge. Add practice when it helps them apply the idea.

## 3. Select the output form

Honor an explicitly requested format. Otherwise, select the form that reveals the difficult relationship most clearly.

Use the identified learning difficulty to choose the simplest form that makes it clear. Adapt the explanation within an explicitly requested format; do not reopen that choice unnecessarily. The same concept can need different forms for different questions or learners.

| Learning difficulty | Likely form | What it reveals |
| --- | --- | --- |
| Meaning, reasoning, or comparison | Clear writing with a worked example | The idea and its consequence |
| Structure, dependency, or spatial relationships | Text with a diagram, or diagram-based HTML slides | How parts relate |
| Effects of changing inputs, comparing alternatives, or inspecting hidden state | Interactive HTML | How choices affect the result |
| A transformation or mechanism best understood through motion | Concept-driven animation | How a change produces its consequence |

Choose the explanatory approach before the delivery structure. Use slides for a requested presentation or when staged guidance helps; use a continuous page when exploration benefits from keeping information together. HTML can contain diagrams, interaction, or animation. A sequence alone does not require a video: prefer interaction when learners need to control the sequence or test alternatives, and timed animation when the planned visual progression explains the mechanism.

If text alone explains the concept adequately and no presentation format is requested, answer directly in text. When several treatments help, choose one primary format and add supporting elements where useful. Apply a 3Blue1Brown-inspired approach when requested or useful; it is not a requirement for every animation.

Make the format choice without asking the user to choose a medium unless missing audience information or constraints would materially change the result. Briefly explain the choice before producing a substantial artifact. Do not create every form by default. Read [visual-explanations.md](references/visual-explanations.md) when the task needs slides, a diagram, an interactive page, or an animation. Apply only the guidance relevant to the selected format.

Prism guides the explanation and learning design. Use the tools and artifact workflows available in the current host to create the requested file or visual. For a slide deck or document, let the available presentation or document workflow handle file construction. For exact algorithms, equations, charts, and state transitions, use exact data, code, or vector graphics instead of generated imagery.

## 4. Explain the mechanism

Adapt this sequence to the task. Do not force every step into a short answer.

1. Show a concrete situation and the question it raises.
2. Trace one example. Show the relevant state, action, and cause. Introduce terms when needed.
3. Change an input or show a boundary case or misconception. Explain what changes and why.
4. For a lesson, add a useful prediction or application question when appropriate.
5. State the reusable rule and any material limitation.

Keep names, colors, units, notation, and inputs consistent. Label simulations and simplifications. State where an analogy stops matching the real mechanism.

When a learner remains confused or gives reasoning that reveals a gap, revisit the diagnosis. Use their feedback to locate the unresolved step; ask a focused question only if the gap is unclear. Change the example, representation, or prerequisite support to address that gap, rather than merely repeating or lengthening the explanation. Preserve confirmed knowledge, the learning goal, and any requested format. Check the revised idea with a small prediction or application when useful. See [learner-discovery.md](references/learner-discovery.md#respond-to-unresolved-confusion) for an example. Do not claim understanding from silence or artifact checks alone.

For slide decks, give each slide a clear purpose that advances the learning objective. Connect examples and activities across slides. Explain changes in context or assumptions before learners use the new information.

## 5. Write clearly

Use STE-informed writing by default: precise terms, direct verbs, clear actors, explicit conditions, gradual information, and consistent terminology. Aim for no more than 20 words in a procedural sentence and 25 words in a descriptive sentence. Keep each paragraph on one topic. Treat these lengths as revision targets; do not remove needed reasoning to meet them.

The full ASD-STE100 Issue 9 standard is an **optional, user-supplied local reference**, expected at `references/ASD-STE100_ISSUE9.pdf` inside this skill folder. It is not bundled with this skill. If present and a specific rule, example, or dictionary entry matters, read or search only the relevant pages with the available PDF tools. If necessary, extract searchable text locally; do not assume every host can search PDF directly. Read the dictionary introduction before checking approved words.

If the file is absent, continue ordinary explanations with the clear-writing principles above. For an exact STE-rule, controlled-vocabulary, or formal-compliance request, obtain the user's copy of the standard or direct the user to the official [ASD download page](https://www.asd-ste100.org/STE_downloads.html). Do not invent a rule or approve a word from memory. Do not claim formal compliance without checking the full rules, dictionary, terminology, and applicable exceptions.

Delete generic introductions, promotional adjectives, repeated summaries, and unrelated background. Keep the worked example and its reasoning. Let a visual show relationships; use nearby text or narration to explain their meaning.

## 6. Build and verify

For a creation request, produce the artifact. Follow [visual-explanations.md](references/visual-explanations.md) for visual design and format-specific checks. Use the current host's available tools. If a required production tool is unavailable, explain the limitation and provide the closest useful result in its actual format.

Handle required setup and execution within the user's authorization and the environment's permissions. Inspect existing tools before installing dependencies. Create or reuse an isolated environment when needed, and request approval for actions that require it. For a rebuild request, use the saved source and recorded dependencies to produce and verify the output. If blocked, identify the specific blocker, the work completed, and any user action needed to continue.

Before delivery:

- Check calculations, state transitions, causal claims, and a boundary case.
- Check that the explanation starts from established knowledge, introduces needed terms and prerequisites, and addresses the identified learning difficulty. Use a short prediction or application question when it helps assess understanding; do not make every answer a quiz.
- Check that the explanation supports the learning objective and that the chosen medium reveals the difficult relationship. Simplify when added visuals, interaction, or motion provide no explanatory value, while preserving an explicitly requested format.
- Remove elements that provide no reasoning, orientation, accessibility, or useful practice.
- Inspect the rendered visual when possible. Test interactions, animation, and narration when present.
- Report content checks, rendered inspection, and interaction checks separately where applicable. State material checks that could not be completed.

Preserve editable source when it may need reuse. Follow the current host's file-saving process. Do not publish beyond the requested destination. For personal understanding, return the explanation directly. For artifact requests, return the artifact and a short account of its purpose and limitations.
