# 1. Prompt Engineering

### What goes in to a good prompt:

1. Define a persona
2. Provide context to the AI
3. Be specific
4. Provide examples
5. Define a response structure

## 1.Define a persona

Defining the AI's role or persona helps define the entire interaction and sets expectations for the type of response you want. When you assign a specific role to the AI, you're effectively providing it with context-specific knowledge and a specific communication style. This helps unlock specific areas of the LLM to ensure it effectively utilises the knowledge it has in that area.

For example, when you specify "You are a senior software engineer helping a junior developer debug a code issue," you're not just giving the AI a title – you're instructing it to:

- Draw upon expert-level software engineering knowledge
- Explain concepts at an appropriate level for a junior developer
- Focus on practical, implementable solutions
- Include explanations of why certain approaches are recommended
- Use appropriate technical terminology while remaining accessible

Compare these two prompts:

```markdown
Bad: "Fix this code: [code snippet]"
Good: "You are a senior software engineer doing a code review. Review this code focusing on best practices and maintainability: [insert code snippet]"
```

**The second prompt will typically result in more thorough, professionally-oriented feedback that includes both technical corrections and architectural considerations.**

<aside>
💡

Review the output of the [bad prompt](https://chatgpt.com/share/677c68d3-bc04-8001-9681-b78f6b339826) vs the [good prompt](https://chatgpt.com/share/677c6911-b41c-8001-9728-7aee642f4dc3) and notice how the output of the prompt with a *persona* is much more detailed!

</aside>

## 2. Context

Context is crucial because it helps the LLM understand the broader situation and constraints it should consider when generating a response. Good context includes:

- Background information about the problem
- Relevant constraints or requirements
- Current state or environment
- Target audience
- Expected outcome

For example, consider these two prompts about code optimisation:

```
Bad: "Make this code faster: [code]"

Good: "You are a software architect reviewing code for a high-traffic financial trading platform where millisecond performance is crucial. The following function runs thousands of times per second during market hours. Current average execution time is 100ms, and we need to get it under 50ms. Here's the function to optimise: [code]"

```

The second prompt provides crucial context that helps the LLM understand:

- The performance requirements (under 50ms)
- The execution environment (high-traffic financial platform)
- Current performance metrics (100ms)
- Usage patterns (thousands of times per second)
- Time sensitivity (during market hours)

**This context helps the LLM prioritise certain optimisation strategies over others and provide more relevant suggestions.**

<aside>
💡

Review the output of the [bad prompt](https://chatgpt.com/share/677c6dee-b2d0-8001-999e-e7d79e52ac25) vs the [good prompt](https://chatgpt.com/share/677c6acb-ad90-8001-9a1d-ba641a02b64c) and notice how the output of the prompt with *context* is much more aligned to the objective and detailed in its explanation!

</aside>

## 3. Specificity

Specificity in prompts helps eliminate ambiguity and ensures you get precisely the type of response you need. This involves Clear Task Definition:

- What exactly needs to be done
- What format the output should take
- What aspects to focus on or ignore

Compare these prompts:

```
Bad: "Review this code: [code]"

Good: "Review this Python function for:
1. Memory leaks and resource management
2. Error handling for network timeouts
3. SQL injection vulnerabilities
4. Compliance with PEP 8 style guidelines
Provide specific code examples for any suggested improvements.
Format your response with separate sections for each category."

```

<aside>
💡

Review this [bad prompt](https://chatgpt.com/share/677c8935-8e9c-800d-a440-2a52b5c1b62d) vs the [good prompt](https://chatgpt.com/share/677c89ab-2a60-800d-9c6a-f38cee69b9a2), to see how even though the LLM points out security flaws in the ‘bad’ example, it also points out a lot of other things we are not concerned about

</aside>

The specific prompt helps the LLM understand:

- Exactly what aspects of the code to analyse
- What types of issues to look for
- How to structure the response
- What to include in the feedback

## 4. Examples

Including examples in your prompts serves multiple purposes:

1. Sets Clear Expectations:
    - Shows the desired format
    - Demonstrates the level of detail needed
    - Illustrates the style of response
2. Provides a Reference Point:
    - Helps the LLM understand patterns
    - Demonstrates the transformation you want
    - Shows edge cases or special considerations

Here's an expanded example:

```
"Transform these function names to follow Python naming conventions.

Examples:
Input: calculateTotalAmount() -> Output: calculate_total_amount()
Input: GetUserData() -> Output: get_user_data()
Input: processXMLfile() -> Output: process_xml_file()

Now transform these functions:
1. validateUserInput()
2. fetchAPIresponse()
3. parseJSONdata()"
```

<aside>
💡

Review the output of [this prompt](https://chatgpt.com/share/677c8a04-3894-800d-9776-4dace2949cd2), noticing how the LLM follows exactly the structure we would want it from the examples provided

</aside>

This approach:

- Shows the exact transformation pattern
- Demonstrates handling of acronyms (XML, API, JSON)
- Illustrates consistent formatting rules
- Provides multiple examples to establish patterns

## 5. Response Structure

Specifying the desired response structure helps ensure the output from the LLM is immediately usable and consistent. This involves defining:

1. Format Specifications:
    - Data structure (JSON, XML, YAML)
    - Required fields or components
2. Detail Level:
    - Depth of explanation needed
    - Number of examples to include
    - Supporting information requirements

Example of a well-structured prompt:

```
"Analyse this code for security vulnerabilities. Provide your response in JSON format with the following structure:

{
  "vulnerabilities": [
    {
      "severity": "HIGH|MEDIUM|LOW",
      "type": "vulnerability category",
      "location": "file name or line numbers",
      "description": "detailed description",
      "impact": "potential impact",
      "remediation": "suggested fix with code example"
    }
  ],
  "summary": {
    "total_issues": number,
    "critical_count": number,
    "recommended_priority": "immediate|high|medium|low"
  }
}

Code to analyse: [insert code]"
```

<aside>
💡

In [this prompt](https://chatgpt.com/share/677c8a53-8d1c-800d-9a0d-81a30521f4bc), notice how we used the exact same code as above, however by defining the output structure we get exactly what we asked for. 

</aside>

This structure:

- Defines exact fields needed
- Specifies data types and formats
- Creates a hierarchical response
- Makes the output programmatically parse able - to then be used in the next part of your program
- Ensures consistent reporting across multiple analyses