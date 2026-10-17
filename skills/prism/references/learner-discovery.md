# Learner discovery

Use this reference when missing learner information would materially change the explanation. Apply the workflow in [SKILL.md](../SKILL.md). These are question patterns, not a checklist to ask in full.

## Choose the next useful question

Use the conversation and supplied material before asking. Find the uncertainty that most affects the explanation. Ask that question first. A few independent questions can share a round, but a question whose answer depends on an open question should wait.

Adapt each follow-up to what the answer establishes. Once you know enough to select prerequisites, depth, examples, progression, and a suitable explanation, proceed. Do not exhaust every possible branch or require a separate approval of the learner profile.

Use the host's question interface when available and appropriate, or ordinary conversation. Offer concrete choices when they reduce effort, while allowing another answer or “I don't know.” Do not recommend an answer about the learner's own knowledge or imply that one answer is preferred.

## Useful question patterns

| Missing information | Possible question | Design consequence |
| --- | --- | --- |
| Audience | “Is this for your own understanding or for a group you are teaching?” | Determines whose knowledge and goal to establish |
| Relevant prior knowledge | “Are arrays and loops familiar, or should I introduce them?” | Sets prerequisites and starting point |
| Learning goal | “Should learners describe the idea, trace an example, or apply it to a new problem?” | Sets depth and useful evidence of understanding |
| Current difficulty | “Which part stops making sense: the initial setup, the update, or why it works?” | Locates the gap in the explanation |
| Vague scope | “What would understanding AI help you do?” | Narrows the topic around a useful outcome |

For personal understanding, ask about the user's question and current mental model. For teaching materials, ask about the learners rather than assuming they share the requester's expertise. Ask about viewing conditions, duration, or other delivery constraints only when they affect the result.

## When the learner is unsure

Accept uncertainty without demanding a self-assessment. Offer a small concrete example, then ask what the learner expects or where the reasoning becomes unclear. For binary search: “In a sorted list, if the middle value is below the target, which half could still contain it?”

Use the reasoning in the answer to choose the next explanation. An incorrect prediction can suggest a misconception; one answer does not establish a general ability level. Explain enough setup for the question to be meaningful. Avoid trivia, scoring, or a diagnostic test unless requested.

If the learner cannot answer, introduce the relevant prerequisite through an example and adjust as feedback arrives. If they request an immediate explanation, proceed with a brief assumption about the starting point.

## Respond to unresolved confusion

Use the learner's response as evidence about the specific gap. Retain what they have already demonstrated. If they only say “I still don't get it,” ask which step became unclear or offer a small example to locate it. If their reasoning already identifies the gap, revise the explanation directly.

For example, a learner understands halving but asks: “Why is the cost logarithmic rather than n/2?” The gap is the distinction between candidates remaining after one step and the number of steps. Switch from tracing a search target to counting repeated halvings: 8 candidates become 4, then 2, then 1. Three halvings reduce the set to one candidate; 4 is the size after the first halving. Connect that count to logarithms. If useful, ask how many halvings reduce 16 candidates to one. Keep this count separate from the exact number of comparisons in a particular binary-search implementation.

If confusion persists, revise the diagnosis and approach using the new feedback. Do not restart the full audience interview, add unrelated detail, or keep quizzing after the learner asks to move on. Judge understanding from their reasoning or application when available; a correct artifact or no further questions does not establish mastery.

## Teaching groups

For mixed audiences, establish shared prerequisites and the intended outcome. Use a common starting example, brief prerequisite support, and optional depth when useful. Do not assume that all learners know a topic because some do.

If the requester does not know the audience's background, agree on a reasonable starting point or include a short prerequisite explanation. State material assumptions. Do not claim to have assessed learners who have not participated.

## Examples of when to ask and stop

- **Broad request:** “Explain transformers.” Clarify the intended meaning if context does not establish it, then ask about the learning goal. Ask about relevant prerequisites after the goal makes them clear.
- **Sufficient context:** “Explain why binary search takes logarithmic time to a learner who knows arrays, loops, and halving.” Proceed with a worked trace; no background interview is needed.
- **Requested medium:** “Animate gradient descent for my class.” Preserve animation. If the goal and prerequisites are unclear, ask what learners should understand and whether slopes or derivatives are familiar. Use those answers to choose the visual model.
- **Useful answer received:** A learner says they know derivatives but cannot see why subtracting the gradient moves downhill. Explain the sign of the slope with one update, then connect it to the general rule. Do not keep interviewing about unrelated mathematics.
- **Quick answer:** “Give me a quick intuitive explanation of attention.” Explain directly, using a brief assumption if needed. Do not turn it into a discovery session.

Clarification is complete when remaining uncertainty would not materially change the explanation. Check understanding through a useful prediction or application when appropriate; keep that separate from claiming the artifact itself has been verified.
