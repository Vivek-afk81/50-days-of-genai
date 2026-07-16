Day 33 of building a CoT robustness experiment from scratch.

Today had zero API calls. Zero code shipped. Just me, 35 wrong model answers, and a blank column asking one question: "where did the reasoning actually break?"

Quick context if you're just catching this series: I've been testing whether Llama can still solve grade-school math problems when you take its own correct reasoning steps and scramble the order. Short version — scrambling hurts accuracy, but I didn't want to just trust the model's word on *why*.

So for H2, I had the model self-report where its own reasoning first went off track. It clustered hard at "Step 3." Interesting pattern. But here's the catch I couldn't skip past: a model confidently explaining its own mistake isn't the same as the explanation being true. I already caught it citing a phrase as "the error" that was never actually used to compute anything.

The only real check for that is manual annotation — done blind, no shortcuts:

→ Strip the model's self-report and the ground-truth answer out entirely
→ Read the problem, the steps exactly as the model saw them, and its wrong final answer
→ Write down where I think it broke, before seeing what the model said
→ Only then compare

No LLM-assisted grading. No "let the model check itself" loop. Just sitting with each of the 35 cases and making a call.

It's slow. It's the least glamorous part of this whole project. It's also the only way to know if "Step 3" is a real signal or a confident-sounding hallucination about its own thinking.

Manual annotation isn't a chore standing between me and the results — for this question, it *is* the result.

#LLM #MachineLearning #AIResearch #ChainOfThought #ReasoningModels #BuildInPublic