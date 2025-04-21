# Annotation Guidelines for CMV Dataset

## 1. Introduction

These guidelines provide instructions for annotating relations between utterances in the CMV (ChangeMyView) dataset. The goal is to classify the relationship between a given text and its parent comment as either:

* **Attack:** The text disagrees with or challenges the parent comment.
* **Support:** The text agrees with or provides evidence for the parent comment.
* **Neutral:** The text is related to the parent comment but neither attacks nor supports it.

## 2. General Principles

* **Context is crucial:** Always consider the text in the context of its parent comment.
* **Subjectivity is expected:** Annotation can be subjective. Aim for consistency and refer to examples when in doubt.
* **Softening:** Pay attention to language that softens a disagreement.

## 3. Annotation Categories

### 3.1 Attack

* The text directly contradicts the parent comment.
* The text questions the validity of the parent comment's claims.
* The text presents counter-arguments or evidence against the parent comment.
* **Disagree also means attack.**

### 3.2 Support

* The text provides evidence or reasoning in favor of the parent comment.
* The text agrees with the parent comment's claims.
* The text elaborates on or clarifies the parent comment.

### 3.3 Neutral

* The text is a follow-up question to the parent comment.
* The text provides additional information without expressing agreement or disagreement.
* The text seeks clarification from the parent comment.
* Delta awarded comments are considered neutral.
* Follow-up questions and answers are neutral, unless they contain additional statements that attack or support.
* When the author changes their view, their reply to their own post is considered neutral.
* Text is irrelevant to the conversation.

## 4. Specific Cases and Examples

### 4.1 Follow-up Questions

* Follow-up questions, in isolation, are generally annotated as **Neutral**.
    * Example:
        * Parent Comment: "Almost all mass shootings occur in areas where concealed carry is not permitted."
        * Text: "Got some stats on this?"
        * Relation: Neutral

### 4.2 Knowledge-Seeking

* Follow-up questions and answers to those questions are **Neutral** as they are knowledge-seeking, not opinionated.
    * Example:
        * Parent Comment: "And also the harder to defend against them. I think the sweet spot lies somewhere when more people have guns."
        * Text: "Why?"
        * Relation: Neutral
        * Text: "Because guns are generally the most viable tool..."
        * Relation: Neutral

### 4.3 Agreement with Reservations

* A reply that initially agrees with the parent text, and then provides a soft counter-argument is also classified as an **Attack**. The reasoning is that, generally, we as humans tend to disagree with someone in the general structure of 'I see your point, but hear me out <>', or similar forms. 
    * Example:
        * Parent Comment: "Mass shootings are incredibly rare in Europe and incredibly common in the US"
        * Text: "I see your point, but surely you can admit this is a bit of a stretch. 486 people have been killed in the US in the last 13 years. I don't know that I'd call this 'incredibly common.'"
        * Relation: Attack

### 4.4 Irrelevant Utterances

* Utterances that are irrelevant to the parent comment's topic should be annotated as **Neutral**.
    * Example 1:
        * Parent Comment: "I am a lawyer... This is one of the most lucid explorations I've seen..."
        * Text: "If you're a lawyer, barring the likely tens of thousands of dollars of law school debt, you can probably afford to buy him reddit gold."
        * Relation: Neutral
    * Example 2:
        * Parent Comment:"This is your position since you seem to have forgotten: >Cause has to do with agency, choice, and effort"
        * Text: Well, you win this round amigo
        * Relation: Neutral

### 4.5 Unclear Cases

* If the relationship is unclear, annotate it as the category that seems most fitting

### 4.6 Delta Awarded Comments

* Comments that have been awarded a delta (indicating a change in view) should be annotated as **Neutral**.

## 5. Annotation Procedure

1.  Read the parent comment carefully.
2.  Read the text to be annotated.
3.  Determine the relationship between the text and the parent comment.
4.  Select the appropriate category (Attack, Support, or Neutral).
5.  Record your annotation.


## 6. Contact

* For questions or clarifications, contact \[karthik.sairam@colorado.edu].
