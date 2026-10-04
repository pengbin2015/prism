# Visual explanations

Apply the writing guidance in [SKILL.md](../SKILL.md) to labels, narration, captions, and instructions. When the user supplies ASD-STE100 Issue 9 and exact wording matters, use the local PDF as described there.

Choose layout, color, and visual language for the concept, learner, and viewing setting. Follow any supplied style or template. Do not impose one palette or panel layout on every explanation.

## Diagrams and images

Use a diagram when the main difficulty is structure or relationship. Use an image when the main difficulty is recognition, spatial form, or a concrete situation.

Start with the relationship that the learner must see. Remove objects that do not support that relationship. Use exact labels and consistent colors. Use arrows only when they show direction, dependency, movement, or sequence. Add a short caption that states what the learner should notice.

Do not use a decorative image as a substitute for a missing explanation. Do not use generated images for exact values, equations, algorithms, data, or state transitions. Use code or an exact diagram for those cases.

## Interactive HTML pages

Use an HTML page when a learner should change a variable, step through a process, compare alternatives, or inspect hidden state. The page must teach through the interaction. It must not be a static slide deck with buttons added.

Define the model before designing the interface:

- State
- Inputs
- Update rules
- Initial conditions
- Units
- Invariants

Separate the model from the rendering. Provide a reproducible baseline. Provide Reset. When a sequence matters, provide Previous, Next, Play, and Pause as appropriate. Show the input value and the resulting state. Make the effect of each control visible.

Start paused when learners need to inspect a state. Keep prediction questions separate from answer reveals. Ensure every control change produces a consistent display. Support keyboard use, visible focus, clear labels, sufficient contrast, and reduced motion. Provide a static or stepped path when motion is disabled.

For distributed systems, concurrency, ML, or probability, label a simulation as a simulation. Do not present browser behavior as measured production latency, distributed correctness, or model quality. Distinguish illustrative values from measured results.

For an interactive artifact in the conversation, use the host's available visual tools. For a standalone HTML file, keep assets embedded when practical and avoid unnecessary external dependencies. Use hosting only when the user requests it.

## 3Blue1Brown-style animations

Use this form when the idea depends on a transformation, geometric relationship, sequence, invisible process, or change of viewpoint. The goal is not to add motion to slides. The goal is to make the reasoning visible.

Start with one question and one visual model. Build that model gradually. Label objects before using them. Animate one meaningful change at a time. Hold important states long enough for inspection. Use camera movement only to guide attention or reveal a relationship.

Prefer this sequence:

1. Show the concrete question.
2. Build the initial objects or state.
3. Transform one object or relationship.
4. Connect the visual change to the rule.
5. Test the rule with a changed example.
6. End with the reusable insight.

Use code-driven geometry, SVG, canvas, Manim, or another exact animation method. Use MP4, GIF, or an interactive HTML canvas according to the requested output. Keep the source editable.

Narration is optional. If narration is requested, write it as a spoken explanation that follows the visual reasoning. Generate captions from the final narration. Do not let narration describe motion without explaining why the motion matters.

Use a 3Blue1Brown-inspired conceptual approach when requested. Do not imitate a person's voice. Do not copy proprietary artwork or branding.

## Validation

Check the underlying example without relying on the visual output. Check the initial state, each important transition, the changed example, and the final rule. Inspect the rendered result. Check readability when paused. Check interaction and Reset for HTML pages. Check timing and synchronization when narration is present.

If a required renderer, encoder, browser, or speech tool is unavailable, state the limitation. Deliver the closest useful artifact with its actual format clearly labeled.
