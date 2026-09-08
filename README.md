# eval-awareness
Measuring evaluation awareness in LLMs; a matched pair method for testing whether open weight models exhibit situational awareness and behave differently when they understand they are being evaluated.  Built on Petri/Inspect framework.

# Introduction
Although frontier models are being guarded well from malicious inputs or generating harmful outputs, the constraints are less on open weight models. They are not guarded by constitutional classifiers to filter out harmful inputs/outputs or might not have been trained through techniques like deliberative alignment techniques. Hence, they have less guardrails and are more prone to exhibition of traits like eval-awareness,sycophancy and deceptive behavior. However that is subject to experimentation and testing. 
In this project we evaluate such behaviors using an open-source framework called Petri from Anthropic based on Inspect from Meridian Labs.  

