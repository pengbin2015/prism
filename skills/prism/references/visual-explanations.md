# Visual explanations

Apply the writing guidance in [SKILL.md](../SKILL.md) to labels, narration, captions, and instructions. When the user supplies ASD-STE100 Issue 9 and exact wording matters, use the local PDF as described there.

Choose layout, color, and visual language for the concept, learner, and viewing setting. Follow any supplied style or template. Do not impose one palette or panel layout on every explanation.

Use the learner knowledge, goal, and learning difficulty established in [SKILL.md](../SKILL.md). Introduce unfamiliar notation and visual conventions before relying on them.

Choose each visual or interaction for the relationship it helps learners understand. When the user requests feature coverage, map the requested features to useful learning activities. Place supplementary demonstrations where they do not interrupt the main explanation.

Select the explanatory approach using SKILL.md before choosing a renderer or installing tools. Use only the production guidance needed for that approach. A topic or the presence of a sequence does not by itself establish a need for slides, interaction, or animation.

## Slides

Arrange slides around a learning progression appropriate to the audience and subject. Keep each slide focused on a clear question, explanation, example, or activity. Honor the requested length without crowding content to fit.

Check text size, content density, and layout for the intended viewing conditions. Make labels, units, scales, and series identification visible when learners need them to interpret a visual. Explain changes of scale or clipped values when they affect the conclusion.

Maintain consistent terminology, notation, and visual meanings across the deck. Make transitions between examples or activities explicit. For interactive decks, define which selections persist across slides and which activities start independently.

Use the requested presentation format and choose libraries according to the capabilities needed. For HTML slides, plan viewport fit at the intended presentation sizes and an accessible overflow strategy for smaller screens. Apply the interactive HTML guidance below when the deck includes controls or simulations.

## Diagrams and images

Use a diagram when the main difficulty is structure or relationship. Use an image when the main difficulty is recognition, spatial form, or a concrete situation.

Start with the relationship the learner struggles to see. Connect it to a familiar example or representation when useful. Remove objects that do not support that relationship. Use exact labels and consistent colors. Use arrows only when they show direction, dependency, movement, or sequence. Add a short caption that states what the learner should notice.

Do not use a decorative image as a substitute for a missing explanation. Do not use generated images for exact values, equations, algorithms, data, or state transitions. Use code or an exact diagram for those cases.

## Interactive HTML pages

Use an HTML page when a learner should change a variable, step through a process, compare alternatives, or inspect hidden state. The page must teach through the interaction. It must not be a static slide deck with buttons added.

Prefer learner-controlled exploration when testing alternatives or choosing the pace helps understanding. Use slide navigation when staged guidance helps; use a continuous layout when learners need to compare information together. A play button or an animated transition alone does not justify an interactive explanation.

Give each control a learning purpose, such as testing a prediction, comparing cases, or exposing hidden state. Start with inputs and examples the learner can interpret, then introduce useful variations.

Define the model before designing the interface:

- State
- Inputs
- Update rules
- Initial conditions
- Units
- Invariants

Separate the model from the rendering. Provide a reproducible baseline. Provide Reset. When a sequence matters, provide Previous, Next, Play, and Pause as appropriate. Show the input value and the resulting state. Make the effect of each control visible.

Define the scope of Reset, including relevant selections, revealed answers, expanded panels, and playback. Preserve keyboard focus during updates or move it to a meaningful location when the focused element is replaced. Make information needed for the activity accessible without hover.

Start paused when learners need to inspect a state. Keep prediction questions separate from answer reveals. Ensure every control change produces a consistent display. Support keyboard use, visible focus, clear labels, sufficient contrast, and reduced motion. Provide a static or stepped path when motion is disabled.

For distributed systems, concurrency, ML, or probability, label a simulation as a simulation. Do not present browser behavior as measured production latency, distributed correctness, or model quality. Distinguish illustrative values from measured results.

For an interactive artifact in the conversation, use the host's available visual tools. For a standalone HTML file, keep assets embedded when practical and avoid unnecessary external dependencies. Use hosting only when the user requests it.

## Concept-driven animations

Use this form when a deliberately timed visual progression makes a transformation, geometric relationship, invisible process, or change of viewpoint easier to understand. Choose interaction instead when learners need to test alternatives or inspect states at their own pace. Animation may be embedded in HTML or delivered as a video according to the task.

Start with one question and one visual model. Build that model gradually. Label objects before using them. Animate one meaningful change at a time. Hold important states long enough for inspection. Allow more time for unfamiliar transitions and explain their causes before building on them. Use camera movement only to guide attention or reveal a relationship.

Prefer this sequence:

1. Show the concrete question.
2. Build the initial objects or state.
3. Transform one object or relationship.
4. Connect the visual change to the rule.
5. Test the rule with a changed example.
6. End with the reusable insight.

Use code-driven geometry, SVG, canvas, Manim, or another exact animation method. Use MP4, GIF, or an interactive HTML canvas according to the requested output. Keep the source editable.

Carry out the animation workflow with the available tools, including required setup, rendering, and assembly. Create or reuse an isolated environment when dependencies are needed. Record working dependencies and preserve editable source and rebuild instructions so the agent can reproduce the output later. Reuse the recorded environment for rebuilds where compatible; explain necessary changes. Apply the authorization and permission guidance in SKILL.md to setup and execution.

Narration is optional. If narration is requested, write it as a spoken explanation that follows the visual reasoning. Generate captions from the final narration. Do not let narration describe motion without explaining why the motion matters.

Generate narration and animation as separate assets when useful for timing or reuse, then combine them into the requested deliverable. Check that spoken passages align with the visual events they explain.

Use a 3Blue1Brown-inspired conceptual approach when requested or when useful for the explanation. Other visual treatments may better fit the audience and concept. Do not imitate a person's voice. Do not copy proprietary artwork or branding.

## Validation

Check the underlying example without relying on the visual output. Check the initial state, each important transition, the changed example, and the final rule.

Check that learners can interpret the labels, notation, controls, and transitions using established prerequisites or explanations provided in the artifact. Check whether the selected medium helps learners understand the identified difficulty and reach the learning goal. Simplify elements that add production complexity without explanatory value, while preserving the requested format and useful accessibility support.

Inspect rendered output at the intended viewing sizes. For slides, check navigation, content fit, and readability, including expanded or revealed content. For interactive formats, check control effects, shared state, keyboard focus, answer reveals, and Reset against its defined scope. Check readability when paused and timing and synchronization when narration is present.

Report which content, visual, and interaction checks were completed. Syntax or calculation checks alone do not establish rendered usability.

If a required renderer, encoder, browser, or speech tool is unavailable, state the limitation. Deliver the closest useful artifact with its actual format clearly labeled.
